![](https://www.youtube.com/watch?v=vVL6NFzr0Rg)

## Transcript

### Array

**0:00** · This video is sponsored by Inforge, the back end built for AI coding agents.

**0:06** · Arrays.

**0:07** · At a low level, much of what a computer does comes down to storing data in memory, laid out in a precise, ordered way.

**0:16** · One of the simplest and most powerful ways to organize that data is something called an array.

**0:21** · And from this simple idea, almost everything else in programming begins.

**0:26** · An array is a fixed-size, ordered collection of items where every item sits at a numbered position.

**0:32** · Think of seats in a movie theater. Seat one, seat two, seat three, and so on.

**0:37** · Each seat has a precise label.

**0:39** · If someone asks for seat 47, you don't check every seat before it. You go straight to seat 47 and you're there.

**0:46** · That's the essence of an array.

**0:49** · Every element has a fixed position, and that position lets you access it instantly.

**0:54** · So, the way this works is that every item in an array is stored right next to each other in memory. And because of that neat, predictable layout, the computer always knows exactly where any item lives.

**1:05** · Finding item number 40,000 takes the exact same time as finding item number four, and it's O of one.

**1:12** · That's remarkable.

**1:13** · But arrays come with an important constraint.

**1:17** · Their size is fixed at the moment of creation, and this size does not change.

**1:22** · Expanding an array is not a simple extension. It requires allocating a completely new block of memory and copying every existing element into it.

**1:32** · Insertion into an array introduces a similar limitation.

**1:36** · Placing an element in the middle is not just a local operation. It requires shifting every subsequent element one position forward to make space.

**1:45** · As a result, while accessing elements is immediate and efficient, modifying the structure can become costly, especially as the array grows larger.

**1:54** · This is the trade-off that sits quietly beneath the simplicity of arrays.

**1:58** · So, arrays are blazing fast for reading, but slow and rigid when the data keeps changing.

**2:05** · Still, arrays appear everywhere.

**2:08** · They underlie pixels in an image, frames in a video stream, situations where position is fixed and known in advance.

**2:15** · But the moment you need something more flexible, that's where the next data structure comes in. And it solves the exact problem arrays can't.

### Linked List

**2:24** · Linked lists.

**2:26** · Imagine a treasure hunt where each clue only tells you where the next clue is.

**2:31** · You don't know where clue number four is until you found clue number three.

**2:35** · You follow the chain one step at a time, never skipping ahead. That's a linked list. And it was invented specifically to fix the rigidity that arrays suffer from.

**2:45** · A linked list is a chain of nodes where each node stores its value and a pointer to the next node. The nodes don't sit next to each other in memory.

**2:53** · They're scattered everywhere.

**2:55** · But they stay connected through those pointers, like clues in a chain.

**2:59** · Here's where it gets interesting.

**3:01** · Remember how inserting into an array meant shifting thousands of items? With a linked list, you insert by updating two pointers. That's it. Two pointer changes and the new item is in. Doesn't matter if there are 10 nodes or 10 million.

**3:15** · Inserting is instant. Removal follows naturally from the structure itself.

**3:20** · Each element exists only through its connection to the next, so removing one does not require shifting anything around. Instead, the link is simply redirected, bypassing the element entirely.

**3:32** · The chain closes in on itself, as if that node was never there. A small, local adjustment with no effect on the rest of the structure.

**3:40** · But, and this is the part that trips people up, what you gain in flexibility, you give up in speed of access. To find a specific item in a linked list, you always start at the beginning and follow the chain.

**3:52** · Access is no longer direct. There is no index to jump to, no fixed position to compute. Instead, each element must be reached by following the chain from the beginning, one step at a time.

**4:06** · Finding an element near the end of a long list means traversing everything that comes before it.

**4:12** · A list of 10,000 nodes may require 10,000 steps.

**4:16** · There are no shortcuts.

**4:18** · Only a path defined by the links themselves.

**4:22** · So, arrays are fast to read, slow to change. Linked lists are slow to read, fast to change. Two different data structures for two different jobs.

### Stack

**4:32** · Stacks.

**4:33** · You know that satisfying feeling when you hit control plus C and your last mistake just disappears?

**4:40** · That's a stack. Silently running every undo feature in every app you've ever used.

**4:45** · A stack is a data structure where the last item in is always the first item out.

**4:50** · Picture a stack of plates. You add plates to the top, you take plates from the top, nobody pulls from the bottom.

**4:56** · The last plate placed is the first one grabbed. Stack has two main operations.

**5:01** · That's all. Push and pop. Push adds to the top, pop removes from the top. You can't touch the middle. You can't reach the bottom. Top only, every time.

**5:09** · And this limitation is actually brilliant. Because of it, both push and pop are instant. Stacks are everywhere, quietly shaping how we interact with the world. Your browser's back button is a perfect example. Each page you visit gets placed on top, and when you go back, the most recent page peels away first, revealing what came before.

**5:30** · The call stack running your code works the same way. Functions layer on top of each other, and the most recent call is always the one to finish next. Even undo in a document editor is just a stack at work. Each step removed in reverse order, one by one.

**5:46** · A stack isn't just a data structure, it's the rhythm of last in, first out, appearing everywhere once you start looking.

**5:54** · But here's the thing.

**5:55** · A stack only cares about what happened most recently. What if you need the opposite? What if the oldest thing waiting is the one that should go first?

**6:03** · For that, you flip the logic entirely.

### Queue

**6:08** · Queues.

**6:09** · A stack serves the newest item first. A queue does the exact opposite. It serves the oldest. A queue is first in, first out.

**6:18** · Simple as a line at a coffee shop. The person who arrived first gets served first. No cutting, no skipping. You join at the back, you wait your turn.

**6:27** · Queue has two main operations, such as enqueue and dequeue. Enqueue adds to the back. Dequeue removes from the front.

**6:34** · Just like a stack, you don't touch the middle.

**6:37** · And just like a stack, both operations are instant.

**6:40** · But the behavior is completely different. A stack is like a to-do list where you always work on the newest task. A queue is like a to-do list where you always finish what you started first. When you hit print in an office with a shared printer, your document joins a queue. The printer works through them in order. When a web server gets slammed with thousands of requests at once, it lines them up and processes them one by one. Keyboard inputs, game loading screens, customer support tickets.

**7:08** · All are the example use cases of queues.

**7:11** · Stacks and queues each limit you to a single end. One serves the most recent, the other serves the earliest. But real-world data isn't always so predictable.

**7:21** · Sometimes you need to reach both ends, grabbing the newest or the oldest, depending on the situation.

**7:27** · Meeting that challenge requires a structure that can flex at both sides, introducing a layer of versatility that makes the behavior of your data far more dynamic. That's where the deque comes in. Deque.

### Deque

**7:40** · It is a double-ended queue data structure. In the deque, you can add or remove from the front, as well as add or remove from the back. Both ends are live all the time.

**7:51** · Think of a train where passengers can board and exit from either side. More flexible than a regular queue, more flexible than a stack.

**8:00** · In fact, a deque is both at once. If you only use the back end, it behaves exactly like a stack. If you add to the back and remove from the front, it behaves exactly like a queue. It's the shape-shifting version of both.

**8:14** · Sliding windows in data processing illustrate a scenario where data flows continuously. New values are added at one end, while old ones are removed from the other. This is the domain of a deque, a double-ended queue. It powers browser history that allows both back and forward navigation, undo and redo systems that move in either direction, and scheduling systems that handle priority tasks at the front, while still accepting regular additions at the back.

**8:42** · Deque is a specialist data structure.

**8:44** · Most problems don't need them, but when a problem does need both ends, nothing else fits. Hash maps.

### Hash Map

**8:51** · You search mom in your phone contacts.

**8:53** · Her number appears instantly. You didn't scroll, you didn't wait, you just got the answer.

**8:58** · That's a hash map, and understanding how it actually works will change the way you think about software. A hash map stores data as key-value pairs and retrieves any value instantly using its key. The key is mom. The value is her phone number.

**9:13** · Give the map the key, get the value back, every time, instantly.

**9:18** · Here's the clever part. When you store something in a hash map, it runs the key through a hash function, a mathematical formula that converts any key into a number. That number points to a specific fixed slot in memory.

**9:31** · So, mom might become slot 4,827.

**9:35** · Her number gets stored there. Later, when you search for mom, the same formula runs again, gets the same number, and goes directly to slot 4,827.

**9:44** · No searching through every contact, direct jump.

**9:48** · This is what makes hash maps almost magical. It doesn't matter if you have 10 contacts or 10 million. Finding one is always instant. Without a hash map, finding something by name in a large list means scanning every item one by one until you hit a match. That gets slower and slower as the list grows.

**10:05** · With a hash map, the size of the collection basically stops mattering.

**10:09** · Python dictionaries are hash maps, JavaScript objects are also hash maps.

**10:14** · All the modern database indexes are built on hash map principles. It's arguably the most important data structure in everyday programming.

**10:22** · But, there's always a but.

**10:25** · Hash maps use more memory than plain lists, and very occasionally, two different keys produce the same slot number.

**10:32** · That's called a collision, and hash maps can also handle it. They're not flawless, they're just incredibly fast.

**10:38** · Now, suppose the value no longer matters. You only want to check whether something exists or not.

**10:44** · That's when the extra information fades away, leaving just the keys.

**10:49** · What remains is a simpler idea, a data structure built purely for checking membership.

### Hash Set

**10:54** · Hash sets.

**10:55** · A hash set is a hash map with no values, just keys. Its entire purpose is to answer one thing as fast as possible. Is this item in the collection or not?

**11:05** · Think of this scenario for better understanding.

**11:08** · A nightclub guest list. The bouncer doesn't care about your table number or your reservation details. He only needs to know, are you on the list or not? If yes, come in.

**11:19** · If you are not in the list, step aside.

**11:21** · That is the essence of hash set data structure.

**11:24** · Checking membership in a hash set is instant. Adding and removing is also instant. And when the question is whether there are any duplicates in the list, the answer is no, because hash set design is such a way that every item appears exactly once.

**11:38** · Without a hash set, checking if something exists in a large list means scanning through every item. But if we use a hash set, the answer is instant every time, regardless of how large the collection grows.

**11:51** · Tracking which users have seen a notification, filtering duplicates from a set, checking if a username is already taken.

**11:58** · Again and again, the same idea appears.

**12:01** · Not storing more, just knowing whether it's there.

**12:05** · These are all hash sets. It's smaller and simpler than a hash map.

**12:09** · But for this one job, it's perfect.

**12:11** · Hey, up to this point, everything has been flat, a direct mapping from key to results.

**12:16** · But not all data fits into that shape.

**12:19** · Some of it naturally forms layers, branching into deeper structure.

**12:23** · And to represent that, you need a different kind of data structure, like trees.

### Tree

**12:29** · Trees.

**12:30** · Open your file explorer. At the very top, a single starting point. From there, it splits into folders. Each of those splits again, into more folders, and eventually, into files.

**12:41** · A structure that keeps branching outward, step by step.

**12:45** · Every path flows in one direction, from the root down to the leaves. A quiet hierarchy, organizing everything you store.

**12:54** · This is the tree data structure.

**12:56** · A tree is a hierarchical data structure with one root at the top, nodes branching below it, and leaf nodes at the very bottom that have no children.

**13:05** · File systems, web pages.

**13:08** · Every HTML tag is a node, nested inside parent tags, branching into children.

**13:14** · Comment threads, where replies branch off replies.

**13:17** · Decision trees in machine learning.

**13:20** · All of these are tree data structures in works.

**13:23** · Trees are natural for anything with a parent-child relationship, but a plain tree has no rules about where values go.

**13:30** · Items aren't sorted.

**13:32** · Means potentially checking every single node.

**13:35** · Which raises a question.

**13:37** · What if you could take a tree, impose one simple rule on it, and suddenly make searching dramatically faster?

**13:43** · That's where the binary search tree comes in.

**13:45** · And speaking of smarter structures that just work, that's actually a perfect way to describe today's sponsor, Insforge.

### Ad

**13:52** · Because just like a BST removes the guesswork from searching, Insforge removes the guesswork from building your backend.

**13:58** · Here's the thing. If you're using tools like Cursor, Cloid Code, or GitHub Copilot to build apps, your agent is great at writing front-end code.

**14:08** · But the moment it has to set up a database, handle authentication, or deploy backend logic, things slow down fast.

**14:15** · Insforge fixes that by giving your coding agent a fully featured backend.

**14:19** · Postgres database, authentication, file storage, edge functions, real-time updates, and even AI model access.

**14:27** · All ready to go from the moment you connect it.

**14:30** · Here is the best part. You don't need to configure dashboards. You don't wrestle with infrastructure.

**14:35** · You just describe what you want to build, and your agent ships it. Insforge quietly handles everything your agent needs behind the scenes.

**14:44** · In fact, benchmarks show that AI agents that are using Insforge are 1.6 times faster, use 30% fewer tokens, and hit nearly 1.7 times higher accuracy compared to other backends. It works with Next.js, React, Svelte, Vue, and more.

**15:02** · So, check it out at insforge.dev.

**15:04** · Link is in the description. Now, back to binary search trees.

### Binary Search Tree

**15:08** · Do you know the number guessing game?

**15:10** · Someone picks a number between 1 and 1,000. You guess 500. Too high. Now, you only think about 1 to 499.

**15:18** · This time, you guess 250, and it's said, "Too low." Likewise, every guess cuts the remaining possibilities That one rule changes everything.

**15:28** · Now, when you search for a value, you start at the root. Is it smaller? Go left. Is it larger? Go right.

**15:34** · Each step eliminates an entire half of the remaining tree. In a well-balanced BST with a million nodes, you might need only 20 steps to find any item. 20.

**15:44** · Compared to a regular tree where searching can mean checking every node, a BST is on another level. The structure of the data does the work for you.

**15:53** · But here's the hidden weakness. If you add items in already sorted order, 1, then 2, then 3, then 4, the tree just grows in a straight line. No branching, no having. It looks like a tree, but behaves like a linked list. Slow again.

**16:09** · That's why self-balancing BST exist. But the core idea is left must be smaller than the right is the foundation of sorted tree data structures everywhere.

**16:19** · Binary search trees are powerful when searching through ordered data.

**16:23** · But in some cases, searching isn't the goal at all. What matters is always having immediate access to a single most important element available instantly every time.

**16:34** · And for that job, we have heap data structure. Heap.

**16:38** · Imagine this, an emergency room. A patient walks in with a minor headache.

**16:43** · Two minutes later, someone arrives with a heart attack. Who gets seen first? Not the headache. Urgency beats arrival time. The most critical case always jumps to the front automatically. No manual resorting required.

### Heap

**16:57** · That's a heap data structure.

**16:59** · A heap is a tree-based structure that always keeps the highest priority item at the very top, and reorganizes itself automatically every time something is added or removed.

**17:10** · In a max heap, the largest value rises to the top. In a min heap, it's the smallest.

**17:15** · Either way, the most important element is always immediately accessible.

**17:20** · And when it's removed, the structure quietly reorganizes itself, allowing the next in priority to take its place, efficiently.

**17:28** · Without a heap, finding the highest priority item from a constantly changing list would mean sorting the whole list every time something new arrives.

**17:36** · Imagine having millions of tasks, and every time a new one comes in, you have to sort the entire list again, just to find the most important one.

**17:45** · That quickly becomes too slow to be practical.

**17:48** · A heap avoids this completely by keeping things almost sorted at all times. So, the most important task is always right at the top, ready to be accessed instantly.

**17:58** · Here are some real-world events where the heap shows its magic, like the task schedulers inside your operating system, deciding which process deserves the CPU right now. And your GPS app constantly recalculating the fastest route as traffic shifts. Anywhere that involves repeatedly pulling the most important item from a live, evolving data set.

**18:18** · Heap is at work.

**18:20** · Remember that, the word heap and stack also refers to a region of memory in programming. Completely different thing.

**18:27** · Same word, two totally unrelated concepts. Don't let that confuse you.

**18:32** · So far, every data structure we've covered works well for collections with clear individual items. But the real world isn't always like that. Sometimes data isn't a list or a tree.

**18:42** · It's a web. It's connections. It's relationships going in every direction. And for that, you need something completely different.

**18:50** · Graphs.

**18:52** · Okay, this is where data structures get really interesting.

**18:55** · Forget the nice, clean hierarchies of trees.

**18:58** · Graphs are messy, chaotic, and honestly, that's what makes them powerful.

**19:03** · Here's the simplest way to think about it. Graphs are just dots and lines. Dots are called vertices or nodes, and lines connecting them are called edges. That's literally it.

### Graph

**19:14** · But here's where it clicks.

**19:16** · Facebook is a giant graph. You're a node, your friends are nodes, and every friendship is an edge connecting you.

**19:22** · Photos, groups, pages, comments, all are nodes, and every like, share, and connection is the edges of that graph.

**19:31** · The entire social network is just one massive graph.

**19:35** · Or, think about Google Maps. Cities are nodes, roads are edges. When you ask for directions, it's searching through that graph to find the shortest path.

**19:44** · Now, there are different types of graphs. Undirected graphs, where connections go both ways, like Facebook friendships. Directed graphs, where edges have direction like Twitter follows. You following someone doesn't mean they follow you back.

**19:59** · And here's a fun term, adjacency. If two nodes are connected by an edge, they're adjacent, basically neighbors.

**20:05** · So, how do you actually store a graph?

**20:08** · We can store graph in two main ways. One is adjacency matrix, where a giant grid with rows and columns are nodes, and you mark a one if there's an edge.

**20:17** · Best for fast lookups, but uses a lot of space if the graph has few connections.

**20:22** · The second way is an adjacency list, where each node keeps a list of its neighbors. Adjacency list is more memory efficient for most use cases.

**20:32** · The cool operation is to traversing the graph where you visit every node, usually with depth-first search or breadth-first search.

**20:39** · There are also some other operations, too, like finding paths between nodes, checking if a cycle exists, or detecting connected components. Each operation has its own use cases.

**20:49** · Real-world uses of graph are everywhere.

**20:52** · Social networks, maps, web page links, recommendation systems, network routing.

**20:56** · Basically, if things are connected in any way, you're dealing with a graph.

**21:01** · Trie.

**21:03** · All right, tries.

**21:04** · And before you say tree, it's pronounced try.

**21:07** · Yeah, I know, it's confusing.

**21:09** · But here's why this data structure is legitimately genius.

**21:13** · Type app into Google. Before you finish the word, you already see apple, application, appointment, App Store, etc.

### Trie

**21:22** · That didn't come from Google guessing what you meant. It came from a structure that already has every word mapped out, one letter at a time.

**21:30** · And the moment you typed app, it already knew exactly which branch you were heading down.

**21:36** · That structure is a trie.

**21:38** · A trie is a variation of tree data structure, where each level represents one character in a word. From the root, the first letter takes you down one branch.

**21:47** · Second letter, next branch. Third letter, next. By the time you've typed a few characters, you've already narrowed the entire structure down to only the words that start with those exact letters.

**21:58** · Here's why this beats a hash map for this job. A hash map is great for exact lookups. You give it the full key, it gives you the value. But searching by prefix, give me everything that starts with app, would mean checking every single entry in the map. A trie does that prefix search in exactly as many steps as the number of letters you typed.

**22:18** · Three letters typed, three steps taken.

**22:19** · You're already at the right branch. The rest of the matching words are right there.

**22:23** · This is the quiet magic behind autocomplete, spell checkers, dictionary lookups.

**22:29** · If I give you a simple example, it would be phone contact search. If you type J, then O, your phone instantly showed John, Jordan, Joseph. That branching through shared letter paths is a trie doing its job quietly in the background.

**22:42** · Disjoint set.

**22:44** · Disjoint set or union find sounds boring, but stick with me because this is actually brilliant data structure.

**22:50** · Imagine you're at a party with 100 people, and you need to figure out who knows who, even indirectly. Like, does Peter know Bob? Well, Peter knows Carol, Carol knows Dave, and Dave knows Bob.

### Disjoint Set (Union-Find)

**23:00** · So, yeah, they're connected.

**23:02** · Without a smart structure, answering that means tracing every connection in the chain, step by step. In a social network with millions of users, that's not fast enough. That's where the disjoint set comes in.

**23:13** · A disjoint set, also called union find, tracks group membership efficiently, even as groups keep merging and growing over time.

**23:22** · Every element starts as its own group.

**23:25** · When you connect two elements, their groups merge into one. Every group has a representative. We can also call them leaders. To check if two elements are in the same group, you check if they share the same leader. That check is nearly instant, even after millions of merges.

**23:40** · And the structure keeps getting smarter over time. Every time you trace a path to find a leader, it compresses that path, making the next lookup even faster. It literally gets more efficient as it's used.

**23:52** · When we do network connectivity checks, like is computer A on the same network as computer B, even in the image processing, where we need to to find out if those pixels form the same object.

**24:03** · And lastly, in the game world design, where we need to find is these two areas reachable from each other. These are the problems disjoint sets were made for.

**24:11** · It's a specialist data structure, but for this specific class of problem, tracking connected groups that keep evolving nothing is cleaner or faster than union find.

**24:20** · Bloom filter.

**24:22** · Let me tell you about the weirdest data structure I've ever learned.

**24:26** · And trust me, once you get it, you'll see it everywhere.

**24:29** · So, what if I told you there's a data structure that's super fast, uses almost no memory, but occasionally lies to you?

### Bloom Filter

**24:36** · That's a bloom filter. And yes, it literally lies.

**24:40** · Here's how the lie works.

**24:42** · A bloom filter gives you one of two answers when you search for something.

**24:46** · Yes or no.

**24:48** · If it says no, that's a guaranteed answer. The item is absolutely 100% not in the set. You can completely trust it.

**24:56** · If it says yes, that's where it gets interesting. It's probably right, but there's a small chance it made a mistake and said yes when the answer should actually be no.

**25:05** · We call these mistakes false positives.

**25:08** · But here's the one thing it never does.

**25:10** · It will never say no to something that's actually there. It only makes mistakes in one direction, and that direction is always a wrong yes, never a wrong no.

**25:20** · So, to put it simply, a no is always the truth, but a yes is mostly the truth.

**25:26** · Now the question arises, why would anyone use this weird data structure?

**25:31** · It's for speed and space, my friend.

**25:33** · Let's say you're building a password checker. You want to reject passwords that have been leaked in data breaches.

**25:38** · There are billions of those.

**25:40** · Storing all of them is gigabytes of data.

**25:43** · By using bloom filter, we can manage it to few megabytes.

**25:47** · Chrome uses it to flag sketchy websites without storing a massive list of every malicious URL.

**25:53** · Ethereum nodes use it to check data without loading the entire blockchain.

**25:57** · Spell checkers use it to quickly rule out obvious typos before doing expensive dictionary lookups.

**26:03** · And when a system instantly tells you a username is probably taken without checking every record, that's a bloom filter at work in the background.

**26:11** · Quietly filtering so that the heavy work doesn't have to happen.

**26:15** · And speaking of keeping things fast by being smart about what you store and what you throw away, the last data structure on this list does exactly that.

**26:24** · LRU cache. LRU stands for least recently used, and it's basically how your computer decides what to forget.

**26:31** · Here's the setup. You've got limited space.

**26:35** · Could be browser cache, could be RAM, doesn't matter.

### LRU Cache

**26:38** · Stuff you use all the time stays.

**26:40** · But stuff you haven't touched forever gets kicked out when space runs low.

**26:44** · Think about your CPU cache.

**26:47** · Your processor is constantly pulling data from memory, instructions, variables, intermediate results.

**26:53** · The ones it uses again and again stay close, right there in the cache for instant access.

**26:59** · But space is limited. So, when new data needs to come in, something has to go.

**27:04** · So, which one should go from the memory?

**27:06** · It must not be randomly, but based on the recency.

**27:10** · The data that hasn't been used for the longest time gets evicted first, because if it hasn't been needed for a while, it's probably not needed right now.

**27:18** · That's LRU cache, quietly deciding what stays fast and what gets forgotten.

**27:24** · The beauty is in how it's built. It is a combination of hash map and doubly linked list.

**27:29** · The hash map gives you O of one lookups, and the linked list tracks order so that most recently used stays at the front.

**27:36** · Least recently used goes to the back.

**27:39** · When you access something, move it to the front. When you're out of space, chop off the back. Simple and brutally efficient.

**27:46** · Both get and put operations are O of one time. That's why every interview loves asking about LRU cache.

**27:54** · It tests if you can combine data structures creatively.

**27:57** · Browsers use it. Databases use it.

**27:59** · Operating systems also use it.

**28:02** · Any system that needs to remember things, but can't afford to remember everything, almost always relies on LRU.

**28:09** · Because memory is limited, so your computer is constantly making decisions, quietly letting go of what you haven't used in a while. And that's not a flaw, that's exactly what keeps it fast.