> 对应主课笔记：[[L12 图与网络 · 习题课]]

![](https://www.youtube.com/watch?v=h0m2tsmSPTI)

MIT 18.06SC Linear Algebra, Fall 2011  
View the complete course: https://ocw.mit.edu/18-06SCF11  
Instructor: Nikola Kamburov  
  
A teaching assistant works through a problem on graphs and networks.  
  
License: Creative Commons BY-NC-SA  
More information at https://ocw.mit.edu/terms  
More courses at https://ocw.mit.edu

## Transcript

**0:06** · NIKOLA KAMBUROV: Hi, guys.

**0:07** · Today we're going to see how one can use linear algebra to describe graphs and networks.

**0:14** · In particular, we'll do the following problem.

**0:17** · We're given this very simple graph here with five nodes and six edges.

**0:23** · We've already labeled them, and we've put directions on the edges.

**0:27** · And we are asked to write down the incidence matrix A, and then to compute its kernel and the kernel of A transpose.

**0:36** · And finally, we're asked to compute the trace of A transpose A.

**0:39** · I'll give you a few moments to try the problem on your own.

**0:44** · And then you'll see my take on it.

**0:53** · Hello again.

**0:55** · OK, so let's first recall what an incidence matrix is.

### Incidence Matrix

**0:59** · So an incidence matrix is supposed to encode how the nodes connect to the edges.

**1:05** · In particular, it has as many rows as there are edges and as many columns as there are nodes.

**1:13** · And we're going to fill in the rows.

**1:19** · And we'll fill them out as follows.

**1:22** · So we're going to use only negative 1, 1, and 0.

**1:27** · And we're going to put a negative 1 in entry i and 1 in entry j if the corresponding edge connects node i to node j.

**1:42** · OK, let me just do it concretely.

**1:44** · So let's look at edge number 1.

**1:48** · So it corresponds to the first row.

**1:50** · It connects 1 to 2.

**1:52** · So we have a negative 1 and a 1.

**1:58** · Then edge number 2, it connects node 2 to 3, so negative 1, 1.

**2:06** · Edge number 3 connects node 1 to 3, so negative 1, 1.

**2:13** · And I believe you get the picture, right?

**2:15** · So I'm just going to fill out the rest of the entries.

**2:19** · All right, 4 is: negative 1, to 1.

**2:27** · 5 is: well, 4, well, negative 1, 1 here.

**2:35** · And 6 is: negative 1 and 1.

**2:45** · OK.

**2:46** · So we've constructed the matrix A. Now, we'll compute its null space.

**2:53** · And we're going to do it without performing any row operations whatsoever.

**2:59** · So in order to do this, it's helpful to look at the graph as an electric circuit and to assign to each of the nodes an electric potential.

**3:14** · If we collect all the electric potentials in a vector x, then A times x is a vector with as many entries as there are edges and gives precisely the potential differences across the edges of the graph.

**3:39** · OK, so then if A\*x is to be 0, this means that across the graph, across all the edges of the graph, all potential differences are 0.

**3:53** · Therefore, all the potentials at all the nodes need to be equal to a constant number.

**4:05** · So therefore, we conclude that the null space of A is spanned by constant 1.

**4:22** · OK?

**4:24** · There are five 1's here, corresponding to the five nodes.

**4:29** · Now what about the null space of A transpose?

### The Null Space of a Transpose

**4:36** · Adopt this analogy with electric circuits.

**4:40** · But this time, we're going to look at currents flowing across the edges of the graph.

**4:49** · Oh, and we are going to adopt the following convention for the currents.

**4:53** · So a current is going to be positive if it flows in the direction of the edge and negative if it flows in the opposite direction.

**5:05** · Right.

**5:06** · So then, what is A transpose y, where y is a vector, each of whose entries is a current on the edge?

**5:25** · Well, the entries of A transpose y are precisely equal to the total current flowing through each of the nodes of the graph.

**5:38** · So A transpose y being equal to 0 means that there is a balance in the circuit, that the currents that flow into each node equal the currents that flow out of it.

**5:54** · Right.

**5:56** · And it's fairly easy to find such a configuration of currents that satisfies this balance equation.

**6:08** · We do it by flowing around loops of the graph.

**6:12** · So you see, this graph has three loops.

**6:19** · The first one is this triangle up there.

**6:26** · The second one is this square.

**6:29** · And I'm just, by this curled direction, I'm signifying in which way I'm going to trace the loop.

**6:42** · And there is third loop, is along the outer contour of the graph.

**6:49** · But in fact, the third one can be thought of as a superposition of these two, and I'll explain why in a second.

**7:02** · So let's figure out the configuration of currents that balances these loops.

**7:10** · So if we flow a current 1 from 1 to 2 and then flow a current of 1 along edge 2, from 2 to 3, and then we flow a current of negative 1, mind that the direction is opposite to the direction of the loop, then we're going to have a balanced configuration of currents.

### Balanced Configuration of Currents

**7:36** · So let me write this down.

**7:42** · The following configuration, so 1 along edge 1, 1 along edge 2, and negative 1 along edge 3, and the rest 0, is a solution to A transpose y.

**8:03** · Let's see what solution we get by flowing around the loop in the square.

**8:13** · Well, we flow a current of 1 along edge 4, current of 1 along edge 5, current of 1 along edge 6, and current of negative 1 along edge 2.

**8:30** · So let's be careful.

**8:33** · So it was 0, then along edge 2 was negative 1.

**8:40** · Along 3: 0; along 4: 1; along 5: 1; along 6: 1.

**8:49** · Now we can do the same thing with the big loop and produce a vector corresponding to it.

**8:58** · And I prompt you to do it.

**9:01** · But what you'll see is that the vector that you get is precisely a sum of these two vectors.

**9:10** · In a way, the big loop is a superposition of the small loops.

**9:15** · OK, so we figured out what the null space of A transpose is.

**9:21** · And now, let's concentrate our attention on finding the trace of A transpose A. We're going to do it right here.

### Finding the Trace of a Transpose

**9:32** · So the trace of a matrix is the sum of its diagonal entries.

**9:38** · And we've seen this many times already, that the diagonal entries of A transpose A are precisely the magnitudes squared of the columns of A.

**9:56** · OK?

**9:59** · So the (1, 1) entry is the magnitude squared of the first column.

**10:05** · The (2, 2) entry is the magnitude squared of the second column, and so on.

**10:10** · Now what is the magnitude squared of a column of an incidence matrix?

**10:17** · Well, each entry in a column of an incidence matrix is either 1, negative 1, or 0.

**10:30** · So when we square these entries, we get 1's or 0's.

**10:35** · And when we add them up, we get precisely a number which is the nontrivial entries in that column.

**10:44** · OK?

**10:45** · So the magnitude squared of the column is the number of nontrivial entries in it.

**10:49** · But if we go back to the matrix A, and we count the number of non-zero entries, this is precisely the number of edges that connect with a node.

**11:07** · OK, so the number of edges that connects with each node is called the degree of the node.

**11:14** · In this way, trace of A transpose A will be just the sum of the degrees of the graph in the picture.

**11:28** · So we have there are 2 edges connecting to 1, so 2, plus 3 edges connecting to 2, 3 edges connecting to 3.

**11:48** · And we've got a 2 for the number of edges connecting to 4, and 2 for the number of edges connecting to 5.

**11:57** · So altogether, we get 12.

**12:04** · So you see, in this problem, we computed certain linear algebra objects without performing the usual algebraic operations, but just by looking at the graph and seeing how the linear algebra is encoded in it.

**12:25** · I hope it was most illuminating.

**12:28** · I'll see you next time.