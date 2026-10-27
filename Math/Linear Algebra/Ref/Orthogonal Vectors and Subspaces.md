![](https://www.youtube.com/watch?v=h9aDgvW59TU)

MIT 18.06SC Linear Algebra, Fall 2011  
View the complete course: https://ocw.mit.edu/18-06SCF11  
Instructor: David Shirokoff  
  
A teaching assistant works through a problem on orthogonal vectors and subspaces.  
  
License: Creative Commons BY-NC-SA  
More information at https://ocw.mit.edu/terms  
More courses at https://ocw.mit.edu

## Transcript

### Intro

**0:07** · DAVID SHIROKOFF: Hi everyone.

**0:08** · I'm Dave.

**0:10** · Now today, I'd like to tackle a problem in orthogonal subspaces.

**0:13** · So the problem we'd like to tackle: given a subspace S, and suppose S is spanned by two vectors, \[1, 2, 2, 3\] and \[1, 3, 3, 2\].

**0:24** · We have a question here which is to find a basis for S perp-- S perp is another subspace which is orthogonal to S.

**0:32** · And then secondly, can every vector in R^4 be uniquely written in terms of S and S perp.

**0:39** · So I'll let you think about this for now, and I'll come back in a minute.

### Problem Statement

**0:53** · Hi everyone.

**0:54** · Welcome back.

**0:56** · OK, so why don't we tackle this problem?

**1:02** · OK, so first off, what does it mean for a vector to be in S perp?

**1:06** · Well, if I have a vector x, and S perp, and x is in S perp, what this means is x is going to be orthogonal to every vector in S. Now specifically, S is spanned by these two vectors.

**1:27** · So it's sufficient that x be perpendicular to the two basis vectors in S.

**1:33** · So specifically, I can take \[1, 2, 2, 3\] and dot it with x, and it's going to be 0.

**1:47** · So I'm treating x as a column vector here.

**1:52** · In addition, x must also be orthogonal to \[1, 3, 2, 2\].

**2:03** · So any vector x that's an S perp must be orthogonal to both of these vectors.

### Solution

**2:08** · So what we can do is we can write this as a matrix equation.

**2:16** · And we do this by combining these two vectors as rows of the matrix.

**2:31** · So if we step back and take a look at this equation, we see that what we're really asking is to find all x that are in the null space of this matrix.

**2:40** · So how do we find x in the null space of a matrix?

**2:42** · Well what we can do is we can row reduce this matrix and try and find a basis for the null space.

**2:49** · So I'm going to just row reduce this matrix.

**2:51** · And notice that by row reduction, we don't actually change the null space of a matrix.

**2:56** · So if I'm only interested in the null space, this system is going to be equivalent to-- I can keep the top row the same.

**3:09** · And then just to simplify our lives, we can take the second row and subtract one copy of the first row.

**3:18** · Now, if I do that, I obtain 0, 1, 1, -1.

**3:29** · Now, to parameterize the null space, what I'm going to do is I'm going to write x out as components.

**3:36** · So if I write x with components x\_1, x\_2, x\_3 and x\_4, we see here that this matrix has a rank of 2.

**3:52** · Now, we're looking at vectors which live in R^4, so we know that the null space is going to have a dimension which is 4 minus 2.

**4:02** · So that means there should be two vectors in the null space of this matrix.

**4:07** · To parameterize these two-dimensional vectors, what I'm going to do is I'm going to let x\_4 equal some constant, and x\_3 equal another constant.

**4:17** · So specifically, I'm going to let x\_4 equal b, and x\_3 equal a.

**4:29** · Now what we do is we take a look at these two equations, and this bottom equation will say that x\_2 is equal to negative x\_3 plus x\_4, which is going to equal negative a-- x\_4-- plus b.

**4:55** · And then the top equation says that x\_1 is equal to negative 2\*x\_2 minus 2\*x\_3 minus 3\*x\_4.

**5:12** · And if I substitute in, x\_2 is -a plus b.

**5:22** · x\_3 is a.

**5:25** · And x\_4 is b.

**5:30** · So when the dust settles, the a's cancel and I'm left with minus 5b.

**5:38** · So we can combine everything together and we end up obtaining \[x\_1, x\_2, x\_3, x\_4\] equals -5b, x\_2 is minus a plus b, x\_3 is a, and x\_4 is b.

**6:09** · And now what we can do is we can take this vector and we can decompose it into pieces which are a multiplied by a vector, and b multiplied by a vector.

**6:19** · So you'll note that this is actually a times \[0, -1, 1, 0\] plus b times \[-5, 1, 0, 1\].

**6:40** · OK?

**6:42** · So we have successfully achieved a parameterization of the null space of this matrix as some constant a times a vector \[0, -1, 1, 0\] plus b times a vector \[-5, 1, 0, 1\].

**6:56** · And now we claim that this is the entire space, S perp.

**7:04** · So S perp is going to be spanned by this vector and this vector.

**7:10** · Now notice how, if I were to take either of these two vectors in S and dot it with any vector in the null space, by construction, it automatically vanishes.

**7:25** · So this concludes part one.

### Part II

**7:28** · Now for part two.

**7:30** · Can every vector v in R^4 be written uniquely in terms of S and S perp?

**7:35** · The answer is yes.

**7:42** · So how do we see this?

**7:44** · Well, if I have a vector v, what I can do is I can try and write it as some constant c\_1 times the vector \[1, 2, 2, 3\] plus c\_2 times the vector \[1, 3, 3, 2\] plus the vector c\_3 \[0, -1, 1, 0\] plus c4 \[-5, 1, 0, 1\].

**8:25** · OK?

**8:26** · So c\_1 and c\_2 are multiplying the vectors in S, and c\_3 and c\_4 are multiplying the vectors in S perp.

**8:35** · So the question is, given any v, can I find constants c\_1, c\_2, c\_3, c\_4, such that this equation holds?

**8:44** · And the answer is yes.

**8:48** · Just to see why it's yes, what we can do is we can rewrite this in matrix notation, and there's kind of a handy trick.

**9:13** · What I can do is I can take these columns and write them as columns of the matrix.

**9:22** · And this whole expression is actually equivalent to this matrix multiplied by the constant, c\_1, c\_2, c\_3, c\_4.

**9:32** · And on the right-hand side, we have the vector v.

**9:36** · Now, by construction, these vectors are linearly independent.

**9:41** · And we know from linear algebra that if we have a matrix with linearly independent columns, the matrix is invertible.

**9:48** · What this means is, for any v on the right-hand side, we can invert this matrix and obtain unique coefficients, c\_1, c\_2, c\_3, c\_4.

**9:57** · This then gives us a unique decomposition for v in terms of a piece which is in S and a piece which is in S perp.

**10:10** · And in general this can be done for any vector space.

**10:14** · Well I'd like to conclude this problem now and I hope you had a good time.

关联：[[Linear Algebra/主页|线性代数]]
