![](https://www.youtube.com/watch?v=D8u1LV9CnCk)

MIT 18.06SC Linear Algebra, Fall 2011  
View the complete course: https://ocw.mit.edu/18-06SCF11  
Instructor: Ben Harris  
  
A teaching assistant works through a problem on the four fundamental subspaces.  
  
License: Creative Commons BY-NC-SA  
More information at https://ocw.mit.edu/terms  
More courses at https://ocw.mit.edu

## Transcript

**0:08** · BEN HARRIS: Hi, and welcome back.

**0:10** · Today we're going to do a problem about the four fundamental subspaces.

**0:15** · So here we have a matrix B. B is written as the product of a lower triangular matrix and an upper triangular matrix.

**0:24** · And we're going to find a basis for, and compute the dimension of, each of the four fundamental subspaces of B.

**0:33** · I'll give you a minute to try that on your own, to hit pause, and then I'll be right back in just a minute and we can do it together.

**0:52** · OK.

**0:52** · We're back.

**0:54** · Now, the first thing to notice is that this is an LU decomposition of B.

**1:04** · So we have L here and U here.

**1:08** · Now let's go one space at a time.

### start with the column space

**1:11** · Let's start with the column space.

**1:16** · And first, let's just say what the dimension of the column space is.

**1:21** · OK, so let's look at our U matrix.

**1:24** · How many pivots do we have?

**1:26** · We have two pivots, so the column space has dimension 2.

**1:31** · This is the number of pivots.

**1:35** · Good.

### find a basis for the column space

**1:36** · Now, how do we find a basis for the column space?

**1:50** · How do we find that basis?

**1:52** · Well, in lecture, Professor Strang had started with a matrix B. He did elimination on it, and then he took the pivot columns in the original matrix.

**2:03** · And that's great.

**2:04** · That works.

**2:05** · You can also take the pivot columns in the L matrix.

**2:09** · You can see by multiplying this out that it will amount to essentially the same thing.

**2:15** · So a basis for this column space, I can just take these two pivot columns of my L matrix, \[1, 2, -1\] and \[0, 1, 0\].

**2:29** · Good.

**2:31** · OK.

**2:32** · So there's the dimension of and the basis for the column space of B.

**2:41** · Next, let's do the null space together.

**2:45** · OK.

**2:46** · What's the dimension of the null space?

**2:53** · Well, the dimension of the null space is always the number of columns minus the number of pivots.

**3:06** · Right?

**3:06** · It's the number of free variables.

**3:11** · So here, that's just one.

**3:15** · Good.

### find this one vector in the null space

**3:16** · And how do we find this one vector in the null space?

**3:34** · Well, what we do is we can just plug in 1 for our free variable, and we can backsolve to get the other two.

**3:47** · So this equation tells me that my second number is -1, and this equation tells me that that third variable -3/5, if I can fit it in here.

**4:04** · That's a -3/5, if it's difficult to see that on the tape.

**4:10** · Now, let's move on, next, to the row space.

**4:17** · Next is the row space.

### find the dimension of the row space

**4:19** · So how do we find the dimension of the row space?

**4:23** · I'm going to write row space as column space of B transpose.

**4:27** · How do we find that?

**4:29** · Well, remember that one of our big facts in this class is that the dimension of the row space is the same as the dimension of the column space.

**4:37** · It's just the number of pivots.

**4:40** · So that's good.

**4:41** · It's 2.

### find a basis for the row space

**4:43** · And how do we find a basis for the row space?

**4:49** · There are a couple ways of thinking about this.

**4:53** · One way to think about it is: we got this upper triangular matrix from B by doing elimination.

**5:00** · And elimination doesn't change the row space.

**5:04** · So I can just use the two pivot rows of the matrix U.

**5:12** · Basis for my row space here is: I just put these two pivot rows together, and I get a basis for this row space.

**5:38** · The last one is always the toughest and the trickiest.

**5:42** · We have to do the left null space or the null space of B transpose.

**5:51** · First, let's compute its dimension.

**5:54** · What's the dimension of this left null space?

**5:59** · Well, there's a similar formula to the one we used when we were computing the dimension of the null space.

**6:07** · It's just the number of rows minus the number of pivots.

**6:12** · So there are three rows.

**6:13** · Our matrix is 3 by 3.

**6:15** · And there are two pivots.

**6:17** · So this is just one-dimensional, again.

**6:23** · We need to compute, now, this left null space.

**6:33** · Let me go back to our original matrix.

**6:36** · The way to do this is to take B equals L\*U, and invert L, and get E\*B equals U. So we need to move L over to the left-hand side.

**6:51** · If we do that-- I'm just going to write that down here.

**6:59** · So what's the inverse of the L matrix?

**7:03** · We just get 1, -2, 1, 0, 1, 1, times B, is our U matrix, this upper triangular matrix.

**7:25** · Now that I moved L over to the other side, I can read off the vectors in my left null space.

**7:35** · Now, I'm looking at not my pivot variables but my free variables, because it's some sort of null space.

**7:42** · but I want to look at this E matrix.

**7:45** · So the third row of this E matrix, the third row corresponds to the three row here and when I multiply this by B, I just get zeros, so this is in the left null space.

**8:03** · A basis for this left null space is-- see if I can fit it here-- just this \[1, 0, 1\].

**8:17** · Good.

**8:21** · So we've found the dimension of and basis for all of the four fundamental subspaces.

**8:32** · Before I move on, I just want to recall which of the L matrix or the U matrix we used for each of these subspaces.

**8:43** · So for the column space, we used the pivot columns of the L matrix.

**8:51** · For the null space, we looked at the U matrix.

**8:56** · For the row space, we also looked at the U matrix.

**9:02** · And for the left null space, we needed to invert the L matrix and look at the free row.

**9:14** · We're done with the problem.

**9:16** · But the last thing that's useful is to draw a picture, which I have right here.

**9:22** · I know in lecture Professor Strang has drawn you some sort of cartoon pictures of what these subspaces look like.

**9:30** · But here I want to try to actually draw them in a special case.

**9:35** · So if you can read my drawing here, what do we have?

**9:41** · We have the row space here, and the null space here.

**9:53** · Right?

**9:54** · And so B maps this picture into this picture.

**10:02** · The null space here-- all the scalar multiples of this vector-- all go to 0, because they're in the null space.

**10:11** · That's exactly what B takes to 0.

**10:16** · B takes everything else, including the row space, into this column space.

**10:23** · And what does B transpose do?

**10:25** · Well, B transpose kills this left null space, kills this vector, and it take everything else into the row space, into the column space of B transpose.

**10:37** · OK.

**10:38** · Thanks for doing this exercise together.

**10:40** · I hope this picture is helpful.