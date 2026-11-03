![](https://www.youtube.com/watch?v=wuyAeWE3iIM)

MIT 18.06SC Linear Algebra, Fall 2011  
View the complete course: https://ocw.mit.edu/18-06SCF11  
Instructor: David Shirokoff  
  
A teaching assistant works through a problem on Markov matrices.  
  
License: Creative Commons BY-NC-SA  
More information at https://ocw.mit.edu/terms  
More courses at https://ocw.mit.edu

## Transcript

**0:06** · PROFESSOR: Hi, everyone.

**0:07** · Welcome back.

**0:08** · So today, I'd like to tackle a problem in Markov matrices.

**0:12** · Specifically, we're going to start with this problem which almost has a physics origin.

**0:17** · If we have a particle that jumps between positions A and B with the following probabilities-- I'll just state it-- if it starts at A and jumps to B with probability 0.4 or starts at A and stays at A with probability 0.6, or if it starts at B then it goes to A with probability 0.2 or stays at B with probability 0.8, we'd like to know the evolution of the probability of this particle over a long period of time.

**0:45** · So specifically the problem we're interested today is: if we have a particle and we know that it starts at position A, what is the probability that it is at position A and the probability that it's at position B after one step, after n steps, and then finally after an infinite number of steps?

**1:04** · So I'll let you think about this problem for a moment and I'll be back.

**1:17** · Hi everyone.

**1:18** · Welcome back.

**1:20** · So the main difficulty with this problem is that it's phrased as a physics problem.

**1:25** · And we need to convert it into some mathematical language to get a handle on it.

**1:29** · So specifically, what we'd like to do is to convert this into a matrix formalism.

**1:35** · So what we can do is we can write this little graph down and describe everything in this graph using a matrix.

**1:44** · So I'm going to call this matrix A, and I'm going to associate the first row of A with particle position A and particle position B.

**1:58** · And I'll associate the first and second columns with particles positions A and B.

**2:08** · And then what I'm going to do is I'm going to fill in this matrix with the probability distributions.

**2:15** · So, specifically what's going to go in this top left corner?

**2:18** · Well, the number 0.6, which represents the probability that I stay at position A, given that I start at position A. What's going to go here in the bottom left-hand corner?

**2:33** · Well, we're going to put 0.4, because this is the probability that I wind up at B, given that I start at A. And then lastly, we'll fill in these other two columns or the second column with 0.8 and 0.2.

**2:56** · So I'll just state briefly this is what's called a Markov matrix.

### A Markov Matrix

**3:00** · And it's called Markov, because first off, every element is positive or 0.

**3:06** · And secondly, the sum of the elements in each column is 1.

**3:11** · So if we note 0.4 plus 0.6 is 1, 0.8 plus 0.2 is 1.

**3:16** · And these matrices come up all the time when we're talking about probabilities and the evolution of probability distributions.

**3:23** · OK.

**3:24** · So now, once we've encoded this graph using this matrix A, we now want to tackle this problem.

**3:30** · So I'm going to introduce the vector p, and I'm going to use a subscript 0 is to denote the probability that the particle is at time 0.

**3:41** · So we're told that the particle starts at position A.

**3:50** · So at time 0, I'm going to use the vector \[1, 0\].

**3:55** · Again, I'm going to match the top component of this vector with the top component of this matrix and the first column of this matrix.

**4:09** · And then likewise, the second component of this vector with the second row and second column of this matrix.

**4:17** · And we're interested in: how does this probability evolve as the particle takes many steps?

**4:26** · So for one step, what's the probability of the particle going to be?

**4:36** · Well, this is the beauty of introducing matrix notation.

**4:41** · I'm going to denote p\_1 to be the probability of the particle after one step.

**4:48** · And we see that we can write this as the matrix A multiplied by p\_0.

**4:58** · So the answer is 0.6 and 0.4.

**5:07** · And I achieve this just by multiplying this matrix by this vector.

**5:11** · OK?

**5:11** · So this concludes part one.

**5:16** · Now part two is a little trickier.

**5:19** · So part two is n steps.

**5:26** · And to tackle this problem, we need to use a little more machinery.

**5:30** · So first off, I'm going to note that p\_1 is A times p\_0.

**5:38** · Likewise, p\_2-- so this is the position of the-- the probability distribution of the particle after two steps.

**5:45** · This is A times p\_0, which is A squared times p\_0.

**5:52** · And we note that there's a general trend.

**5:55** · After n steps-- so P\_n-- the general trend is, it's going to be this matrix A raised to the n-th power, multiply the vector P0.

### The Nth Power of a Matrix

**6:09** · So how do we take the n-th power of a matrix?

**6:11** · Well, this is where we use eigenvectors and eigenvalues.

**6:16** · So recall, that we can take any matrix A that's diagonalizable and write it as U D U inverse, where D is a diagonal matrix and this matrix U is a matrix whose columns correspond to the eigenvectors of A.

**6:41** · So for this problem, I'm just going to state what the eigenvalues and eigenvectors are.

**6:44** · And I'll let you work them out.

**6:48** · So because it's a Markov matrix, we always have an eigenvalue which is 1.

**6:55** · And in this case, we have an eigenvector u which is 1 and 2.

**7:04** · In addition, the second eigenvalue is 0.4.

**7:11** · And the eigenvector corresponding to this one is \[1, -1\].

**7:17** · And I'll just call these u\_1 and u\_2, like that.

**7:30** · OK, we can now write this big matrix U as 1, 2; 1, -1.

**7:41** · D is going to be-- now I have to match things up.

**7:44** · If I'm going to put the first eigenvector in the first column, we have to stick 1 in the first column as well and then 0.4 like this.

**7:57** · And then lastly, we also have U inverse which I can just work out to be minus 1/3, one over the determinant, times -1, -1; -2, and 1, which simplifies to this.

**8:29** · OK, so now if we take A and raise it to the power of n, we have this nice identity that all the U and U inverses collapse in the middle.

**8:46** · And we're left with U, D to the n, U inverse, p\_0.

### Raising the Diagonal Matrix to the Power of N

**8:54** · Now raising the a diagonal matrix to the power of n is a relatively simple thing to do.

**8:59** · We just take the eigenvalues and raise them to the power of n.

**9:03** · So when we compute this product, there's a question of what order do we do things?

**9:07** · Now these are 2 by 2 matrices, so in theory we could just multiply out, 2 by 2 matrix, 2 by 2 matrix, 2 by 2 matrix, and then on a vector which is a 2 by 1 matrix.

**9:16** · But if you're in a test and you're cramped for time, you want to do as little computations as possible.

**9:21** · So what you want to do is you want to start on the right-hand side and then work backwards.

**9:28** · So if we do this, we end up obtaining 1, 2, this is going to be to the power of n, 1/3, \[1, 2\].

**9:51** · OK, so for this last part, I'm just going to write down the final answer.

**9:55** · And I'll let you work out the multiplication of matrices.

**9:59** · So we have for p\_n: 1/3, 2 times 0.4 to the n plus 1, -2 0.4 to the n plus 2.

**10:21** · And this is the final vector for p of n.

**10:26** · So this finishes up Part 2.

**10:27** · And then lastly, for Part 3, what happens when n goes to infinity?

### Part Three What Happens When N Goes to Infinity

**10:33** · Well, we have the answer for any n.

**10:36** · So we can just take the limit as n goes to infinity.

**10:39** · Now, specifically as n goes to infinity, 0.4 raised to some very large power vanishes.

**10:46** · So these two terms drop off.

**10:48** · And at the end of the day, we're left with p\_infinity is 1/3 \[1, 2\].

**10:58** · OK?

### Recap

**10:59** · So just to recap, we started off with a particle starting at A, and then after a very long time, the particle winds up with a probability distribution which is 1/3, 1 and 2.

**11:16** · And this is quite characteristic of Markov matrix chains.

**11:20** · Specifically, we note that 1/3 \* \[1, 2\] is a multiple of the eigenvector corresponding to eigenvalue 1.

**11:31** · So even though the particle started at position A, after a long period of time, it tended to forget where it started and approached, diffused into this uniform distribution.

**11:43** · OK.

**11:43** · I'd like to finish up here.

**11:45** · And I'll see you next time.