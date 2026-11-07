![](https://www.youtube.com/watch?v=IePrsH3gU_A)

The Lowest Common Ancestor problem: a seemingly impossible problem with a surprisingly beautiful solution.  
  
00:00 Prologue  
01:34 The Easy Solution  
04:36 The Range Minimum Query Problem  
08:55 A Clever Reduction  
13:11 Sparse Tables  
18:07 Indirection  
25:29 Epilogue  
  
Animations created with Manim  
Music: Fantasia on El-C-A by SithDev  
  
Sources:  
Dov Harel and Robert Tarjan: Fast Algorithms for Finding Nearest Common Ancestors  
Eric Demaine: Advanced Data Structures (Lecture Notes)

## Transcript

### Prologue

**0:00** · Imagine you're in a coding interview, and the interviewer asks you the following question.

**0:06** · You're given a tree and two nodes within that tree.

**0:09** · Find their lowest common ancestor.

**0:12** · Of course, you did your homework. So, you come up with an algorithm, which for any pair of nodes finds their lowest common ancestor. And your algorithm is also quite fast, only needing linear time in the worst case.

**0:25** · But then, the interviewer asks you a follow-up question.

**0:28** · Now, do the same thing, but in the constant time.

**0:32** · At first glance, this seems totally impossible.

**0:35** · But then, the interviewer gives you a way out.

**0:37** · You are given linear time once at the start to look at the tree and gather as much information about it as possible.

**0:45** · But after this preprocessing phase, you should be able to answer any given lowest common ancestor query in constant time.

**0:53** · This problem is known as the lowest common ancestor problem, or LCA for short.

**0:59** · When it was first introduced in the '70s, the LCA problem sparked a surprising amount of research, and it took over 10 years until a first solution was found.

**1:09** · In this video, I want to show you a particularly beautiful way to solve this problem.

**1:14** · It involves three really interesting algorithmic techniques, which I think not enough people know about.

**1:21** · An important notion from theoretical computer science, a useful data structure to answer range queries, and one of the most counterintuitive concepts in the whole field of algorithms.

### The Easy Solution

**1:34** · To begin our journey, let's take a look at how we might answer an LCA query without any preprocessing.

**1:41** · We start at one of the two nodes and write down all its ancestors from bottom to top.

**1:48** · We do the same with the other node.

**1:52** · The paths we get form a list of all the ancestors of the two nodes.

**1:57** · Starting from the root, we compare the paths node by node until we find the point where they diverge.

**2:04** · The last node to appear on both paths is the lowest common ancestor.

**2:09** · This simple method works for every pair of vertices, even if one of the nodes is an ancestor \[music\] of the other.

**2:19** · The lengths of the paths decide how much time the algorithm needs.

**2:24** · Depending on the shape of the tree, these paths can be quite long.

**2:28** · But, they definitely don't contain more nodes than the entire tree.

**2:33** · So, in the worst case, the algorithm needs linear time.

**2:38** · If we want to improve this running time, \[music\] we need to store some information about the tree during the pre-processing phase.

**2:46** · But, which kind of information would allow us to find the lowest common ancestor faster?

**2:52** · One really simple method is to just pre-compute the lowest common ancestor for every pair of nodes, and store the results in a lookup table.

**3:02** · With this kind of table, we can obviously answer any possible LCA query in constant time, simply by looking up the answer.

**3:10** · But, how long would it take to create such a table?

**3:14** · There are n squared results we need to store, one for each pair of nodes.

**3:19** · However, there is some redundant information in our table.

**3:23** · First of all, the table is symmetric because the lowest common ancestor operation itself is symmetric.

**3:29** · So, we can get rid of roughly one half of the entries, n \* n - 1 / 2 to be exact.

**3:37** · The entries on the diagonal are also not very interesting.

**3:41** · The LCA of node B and node B is, well, node B.

**3:45** · But, even with all these queries removed, we're still left with order n squared results we need to compute.

**3:52** · As we've just seen, computing just one answer already takes linear time in the worst case.

**3:58** · So, the time for computing all the answers is n squared \* n, or order n cubed, which is really slow.

**4:07** · And even if we could somehow find a faster way to build up this lookup table, just writing down all the results already takes order n squared time, which is still much slower than the linear time we want.

**4:18** · What we need is a new perspective.

**4:21** · In a situation like this, where the solution seems completely out of reach, it's often a good idea to look out for simpler, related problems, and see how they might give us insights into solving our original problem.

### The Range Minimum Query Problem

**4:36** · The problem, which ends up being exactly the right kind of perspective shift, is known as the range minimum query problem, or RMQ \[music\] for short.

**4:47** · Here, we're given an array of numbers and a range within this array.

**4:52** · What we want is to find the minimum number within that range.

**4:57** · Just like with LCA, there is a simple linear time algorithm to do this.

**5:02** · Namely, iterate over the range and find the minimum.

**5:05** · But again, also like LCA, the real challenge is finding the minimum in constant time \[music\] after some pre-processing of the array.

**5:15** · There is one more way in which RMQ is very similar to LCA.

**5:20** · For LCA, each query is a pair of nodes, and the result is another node.

**5:26** · For RMQ, each query can be viewed as two array elements, \[music\] namely, the first and the last element of the range.

**5:33** · And the result is some other array element within that range.

**5:38** · In fact, these two problems aren't just related.

**5:42** · In some sense, they are one and the same problem.

**5:45** · What do I mean by this?

**5:47** · It turns out that we can convert every array for the RMQ problem into an equivalent tree for the LCA problem.

**5:56** · We do this \[music\] by taking the minimum of the array and using it as the root of our tree.

**6:03** · We then take the minimum of each of the two halves and again use it as the root of the two subtrees and so on until we have a complete tree.

**6:13** · If we now pick any range of the array, we can see that the minimum in that range is just the lowest common ancestor of the two end points.

**6:22** · What we just did is called a reduction.

**6:26** · We reduced the RMQ problem to the LCA problem.

**6:30** · This means that if we find a solution to LCA, this also immediately gives us a solution for RMQ.

**6:38** · Why?

**6:39** · Well, to solve RMQ, we simply transform the array into a tree as we've just seen and then use the LCA algorithm on this tree.

**6:49** · But how exactly does this help us to solve LCA?

**6:53** · It doesn't.

**6:54** · What we want is a reduction in the other direction.

**6:57** · If we can reduce LCA to RMQ, we only need to focus on how we can solve RMQ quickly.

**7:04** · This is exactly the kind of perspective shift we might need to make progress.

**7:09** · To reduce LCA to RMQ, we need to convert the tree into an array.

**7:15** · It makes sense to place the nodes of the tree into the array somehow.

**7:19** · But since RMQ is about finding minimums, we need a way to compare two nodes in the array.

**7:26** · If you recall the reduction from RMQ to LCA, intuitively, nodes closer to the root should get a lower value.

**7:34** · So, we will assign each node its depth.

**7:37** · In other words, which layer of the tree it lies in.

**7:41** · Then, we traverse the tree from left to right and place the nodes into the array.

**7:47** · This is called an in-order traversal.

**7:52** · It's not hard to see that what we just did is essentially the same reduction as before, just backwards.

**7:58** · \[music\] So, the minimum for every range indeed corresponds to the lowest common ancestor of the two range end points. However, there's one big problem with this reduction. It only works for binary trees. Once we have nodes with three or more children, there is no obvious way to traverse the tree from left to right. Take this tree, for example. The lowest common ancestor of B and C is A.

**8:23** · So, in the RMQ array, A should lie between B and C. But A is also the lowest common ancestor of C and D. So, it should lie between C and D as well. No matter how we order the array, there's always a range which should contain A, but doesn't. The only way to solve this is by including A twice. Now, A is actually contained in every relevant range, and the reduction works.

**8:51** · Let's see how we can apply this idea in general. An in-order traversal, like before, only makes sense for binary trees. So, instead, we start at the root \[music\] and perform a so-called Euler tour, where we always try to go as deep into the tree as possible and only return once we have explored all the paths. Every time we visit a node, we add it to our array.

### A Clever Reduction

**9:16** · Then, we check if there's a child node we have not visited yet. If there is, we move down to it and add it to the array as well, and so on. If at any point we have hit a dead end, we move up to the parent node and add it to the array one more time. The same thing happens if at any point we've visited all the children of some node already.

**9:41** · The algorithm finishes after we have visited all the root's children and have added the root to the array one last time. You might be wondering how this could possibly \[music\] work. As nodes now appear multiple times, making range queries ambiguous.

**9:57** · If we want to know the lowest common ancestor of say B and D, which range do we look at?

**10:02** · \[music\] It turns out that it doesn't matter. We will get the correct answer regardless of which range we choose. So apparently, this reduction actually works.

**10:14** · But why?

**10:15** · First, \[music\] for every range, the lowest common ancestor of the two end points must be contained in that range. This is because we build up the array during a tree traversal.

**10:26** · \[music\] So, every range between two nodes in the array corresponds to a path in the tree from one node to the other. And every path from one node to the other has to cross the lowest common ancestor at some point. But could we perhaps overshoot? So, the range contains a node higher up in the tree than the lowest common ancestor.

**10:48** · No, we cannot.

**10:50** · Consider node B and where it appears in the array. If a pair of nodes has B as its lowest common ancestor, then both nodes of the pair must lie in the subtree below B. But because of the way we constructed the array, all nodes in that subtree lie in the range given by the first and the last occurrence of B in the array.

**11:11** · If we pick any two nodes within that range, we'll stay in that range and there is no way the minimum node will be outside the subtree. So, the reduction does work. But one thing we should check is if it is fast enough. The run time of the reduction directly corresponds to the size of the array. Each node is added to the array once when we first encounter it, but some nodes are visited more than once.

**11:37** · In fact, every time we move up in the tree, we add a node to the array we have already visited. Since every edge is traversed upwards exactly once, the number of additional entries in the array is always equal to the number of edges in the tree. And the number of edges in a tree is always one less than the number of nodes, since every node has one edge upwards except the root.

**12:00** · Therefore, the size of the array is linear in the size of the tree. So, the reduction takes linear time. Let's look at how we can use our reduction to solve the LCA problem. Our approach will look something like this. In the preprocessing phase, we will first perform the reduction to RMQ, which we can do in linear time as we've just seen.

**12:24** · Then, we will do the preprocessing phase for RMQ, which we haven't figured out yet, but which we can hopefully do quite efficiently. Now, to answer an LCA query, we must first find the correct range for the given pair of nodes. To do this in constant time, we can use something like a hash table, which maps nodes to their position in the array. We can create the lookup table in linear time during the preprocessing phase.

**12:51** · Finally, once we know the correct range, we only need to answer the RMQ query for this range to find the lowest common ancestor. With this approach, we can focus entirely on the preprocessing of RMQ now. The faster we can do this, the better our LCA solution will be. The main advantage of RMQ is that it's much simpler than LCA.

### Sparse Tables

**13:16** · For RMQ, it's actually really easy to come up with a way of precomputing all queries in quadratic time. First, we compute the minimums for all ranges starting at the first element. Each element is compared with the current minimum, so this only takes linear time. And similarly, we can compute the minimums for all ranges starting at the second element, the third, and so on. This way, every query only takes constant time to compute.

**13:46** · And because the number of possible queries is quadratic, we only need quadratic time. This is already a massive improvement compared to our previous solution, but still a lot slower than our desired linear running time.

**13:59** · So, what can we do to improve this?

**14:03** · One natural idea is to ask ourselves if we actually need to precompute every possible minimum, or if we can get rid of some minimums while still being able to answer every query in constant time. Let's imagine we want to find the minimum of this range, but the corresponding entry in the table is missing. What we can do instead is split the range into parts and find the minimum for each part.

**14:28** · The minimum of the total range is then simply the smaller of the two elements. Sure, this makes queries a bit slower. Instead of a single table lookup, we now need two lookups plus one comparison. But all three steps can be performed in constant time. So, the total query time stays constant. This means that we don't need to precompute queries for large ranges if we can combine the results of two smaller ranges instead.

**14:54** · This even works if the two ranges overlap. Since we are only interested in the minimum, it makes no difference if we cover some elements more than once. To show how we can further reduce the number of precomputed queries, I will reorder this table slightly. Now, each column contains the ranges that start at the same position, and each row contains the results for ranges with the same length.

**15:18** · For example, our blue range starts at seven and contains six numbers. Our array has eight elements in total. Every range with at least five elements can be covered by two ranges of length four. Therefore, we can get rid of the last four rows. We need to keep row four for the larger ranges, but ranges with size three can again be covered by two ranges of size two. This means we can also remove row three.

**15:47** · With the remaining results, we can cover all possible ranges using at most two results in our table. If we stop for a moment, we see that the rows you're left with are all powers of two. If our array contains more than eight elements, we also precompute ranges for size eight to cover ranges of size nine or higher. If the array contains more than 16 elements, we also need the ranges for size 16 and so on.

**16:14** · While each row still contains up to n results, we now only need logarithmically many rows, namely the powers of two. This means our table size is now n log n, which is much better than n squared.

**16:28** · But do we also need n log n time to create the table?

**16:34** · Well, ranges of size one are straightforward. Just copy the numbers from the array. And size two is still easy. We simply take the minimum of every pair of adjacent elements. For size four, we can also reuse our previous results. We just take the minimum of two size two ranges, which we have already precomputed.

**17:00** · \[music\] The same goes for sizes eight, 16, and so on. By precomputing the range queries in this way, every query only needs constant time to precompute. Since there are n log n queries, we can indeed create this table in n log n time. The data structure we've just created is called a sparse table.

**17:22** · Sparse tables are really useful in general and not just for finding minimums, but also for all sorts of other operations like addition, bitwise and, or the greatest common divisor. So, we have found an n log n preprocessing solution. Since the logarithm grows extremely slowly, in practice, this is essentially just as good as a linear time solution. So, you could stop watching this video here. But, we are so close to the theoretical optimum, which is linear time.

**17:55** · We just need to get rid of this extra log factor. To achieve this, we can use a technique which is so cool, but also so counterintuitive, I simply cannot resist showing it to you. The concept we will need is known as indirection. The idea is so simple that at first, it's not clear at all how it could possibly help us. We split our data into multiple chunks of the same size.

### Indirection

**18:21** · For each chunk, we store its minimum in the parent array. We can create this parent array easily in linear time simply by iterating once over all values. Let's say we need to respond to a range query. There are now two possibilities. Either the range is contained in one of the chunks, then we only need to answer the query locally for that chunk. Or, the query covers multiple chunks.

**18:47** · \[music\] Then, we can think of the query as consisting of three sections. The minimum of the first section can again be found locally for that chunk. And the same goes for the third section. The minimum of the middle section is the result of a range query for the parent array. Because remember, the parent array stores chunk minimums. So, the result of the entire range query is simply the minimum of these three values.

**19:14** · This means that if we can answer range queries for the parent array in constant time and range queries for each chunk in constant time, then we can answer range queries for the original array in constant time. The reason that splitting the problem into two layers helps us is that it introduces a lot of flexibility, since we can freely choose how we tackle each layer and also how large our chunks should be.

**19:40** · Let's say we divide the array into chunks of size C. Then P, the size of the parent array, is simply N divided by C. Recall that with the sparse table method, we were just off by a factor of log N compared to a linear time solution. If we choose the chunk size C to be log N, then the parent array will be smaller than the original array exactly by a factor of log N.

**20:06** · If we now use the sparse table method on the parent array, the preprocessing time for it will be P log P. To simplify this, we can plug in N over log N for the first P, and since big O notation describes only an upper bound, we can be a bit sloppy for the second P, plugging \[music\] in N instead of N over log N. With this simplification, we can see that the log factors cancel out.

**20:31** · So, we indeed need at most linear time for preprocessing the parent array. But of course, we still need a solution for the individual chunks that needs at most linear preprocessing in total. Your first instinct may be to also use sparse tables for the individual chunks. This would require log N times log log N preprocessing for each chunk. Since there are N over log N different chunks, we get this combined running time for all the chunks.

**21:01** · Again, we can cancel the log N, and we see that this runtime is N times log log n. Log log n grows even slower than the single logarithm. So, this is an improvement compared to the running time without indirection. But, at the same time, it is also painfully close to linear time. Off by a factor of only log log n. There is one last insight we are missing to finally reach our goal. Consider these two chunks.

**21:30** · Even though they contain completely different numbers, their minimum is at the same position. And in fact, no matter which range query we look at, they behave completely identically. So, instead of creating separate tables for each chunk, we could just create one single table which stores the index of each minimum. For example, the minimum of the first two elements is at position zero.

**21:55** · This way, we can reuse the table for both chunks. \[music\] Since the chunks are quite small compared to the entire array, chances are that there are many more of these chunk twins that share the same minimum table. In fact, remember that we're still trying to solve the lowest common ancestor problem. So, the numbers in the array are not random. Instead, they come from a reduction from lowest \[music\] common ancestor to range minimum query.

**22:22** · In each step during the reduction, we either went down or up one layer. This means that every number is either exactly one smaller or exactly one larger than the previous one. In terms of range minimums, each chunk can therefore be uniquely identified by the plus and minus ones. For example, chunks one and three both have a plus and then a minus one. So, they can share the same table. The idea will therefore be the following.

**22:52** · Create all possible minimum tables, one for each chunk class. Then, loop over the chunks. For each chunk, find out its class and add a pointer to the correct minimum table.

**23:05** · How much time does this take?

**23:07** · Iterating over the chunks just takes linear time. We need to look at each number just once. Let's say that we again use a sparse table for the minimum table of each chunk class. Then, each table takes C log C time to create. Remember that C was the size of our chunks.

**23:27** · And how many tables are there?

**23:29** · Well, if C is our chunk size, then each chunk class is identified by C minus one plus ones and minus ones. So, there are exactly two to the C minus one possible classes. This means that this is the total time for creating the tables, which in big O notation we can simplify to two to the C times C log C. Now, we only need to plug in our chunk size of log n.

**23:59** · Two to the log n is just n, so after simplifying we well, still do not achieve linear time. There is one final step we need to achieve linear preprocessing, one final trick.

**24:13** · Can you figure it out?

**24:15** · I will give you a hint. Everything you need is on your screen right now. Well, we selected a chunk size of log n to cancel out the logarithmic overhead of the sparse table for the parent. But for this to work, \[music\] the chunk size does not have to be exactly log n. It just has to scale like log n. So, what if we make the chunk size a bit smaller? Let's say by a factor of two.

**24:46** · When plugging this in for C, we now get 1/2 \* log n in the exponent instead of log n, which equals the square root of n. And even if we multiply square root of n by some log factors, it still clearly grows slower than linear time. So, we're actually sublinear now for the chunks.

**25:06** · This factor of 1/2 makes all the difference for the chunks, while it only increases the size of the parent array by a factor of two. So, the running time stays linear. I don't know about you, but getting a better running time in big O notation just by splitting the data and cleverly choosing the chunk size almost feels like magic to me. And with that last puzzle piece, we reach our final solution.

### Epilogue

**25:34** · First, we perform the reduction from LCA to RMQ to convert the tree into an array where we can answer minimum queries. Then, we split the array into chunks of size 1/2 \* log n and compute the minimum for each chunk. We create sparse table to store these minimums. And finally, we precompute lookup tables for each chunk class and store reference to its table for each chunk.

**25:58** · Every step takes linear time, and the final data structure only uses linear space.

**26:05** · Now, probably at least some of you are asking, "Isn't this overkill?"

**26:10** · Yes, of course it's overkill. Lowest common ancestor has some practical applications, but there are far more important and challenging problems in computer science. And a more simple approach for the LCA problem would probably be more than enough in practice. But I think our journey was still worth it in the end.

**26:28** · A perspective shift from a hard problem to an easier one, a clever data structure to answer range queries, and a technique of combining two data structures into one. Each part is clever on its own, yes, but each is also a tried and true building block used in many algorithms and data structures. The magic only happens if if combine them all together. When solving your own problems, you don't have to reinvent the wheel.

**26:57** · But having a large toolbox of established techniques and ideas can make the difference between getting stuck and building something beautiful.