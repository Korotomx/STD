![](https://www.youtube.com/watch?v=rMv2rDiOTsI)

MIT 18.06SC Linear Algebra, Fall 2011  
View the complete course: https://ocw.mit.edu/18-06SCF11  
Instructor: Martina Balagovic  
  
A teaching assistant works through a problem on change of basis.  
  
License: Creative Commons BY-NC-SA  
More information at https://ocw.mit.edu/terms  
More courses at https://ocw.mit.edu

## Transcript

### Introduction to problem

**0:05** · MARTINA BALAGOVIC: Hi.

**0:06** · Welcome to recitation.

**0:08** · Today's problem is about change of basis.

**0:10** · It says the vector space of polynomials in x of degree up to 2 has a basis 1, x, and x squared.

**0:18** · That's the obvious basis that you would write for that vector space.

**0:22** · But today we're going to consider another basis, w\_1, w\_2, and w\_3.

**0:26** · And we don't know what w\_1, w\_2, and w\_3 are explicitly.

**0:30** · What we know is that their values at x equals minus 1, 0, and 1 are given by this table here.

**0:38** · So they are 1, 0, 0; 0, 1, 0; and 0, 0, 1.

**0:43** · We're asked to do the following.

**0:45** · We're asked to express this polynomial-- so y of x is minus x plus 5-- in this basis, w\_1, w\_2, w\_3.

**0:54** · We're asked to find the change of basis matrices between these two bases, 1, x, x squared, and w\_1, w\_2, w\_3.

**1:02** · And finally, we're asked to find the matrix of taking derivatives, which is a linear map on this space, in both of these basis.

**1:10** · And let me give you an extra level of challenge, which is to try to do as much of this as possible without explicitly finding w\_1, w\_2, and w\_3.

**1:21** · I'll let you think about the problem and then you can come back and compare your solution with mine.

### Expressing polynomials

**1:33** · Hi.

**1:34** · Welcome back.

**1:35** · So to start with the problem a, we need to find coefficients alpha, beta, and gamma so that y of x

**2:02** · is expressed through, with this coefficient, in this new basis, w\_1, w\_2, and w\_3.

**2:08** · now, one way to do that would be to look at this table of values, explicitly find w\_1, w\_2, and w\_3, so a quadratic polynomial is-- all the information we need about it is in values at three points.

**2:26** · So say w\_1 is a\*1 plus b times x plus c times x squared.

**2:34** · Find a, b, and c.

**2:35** · Find w\_1, w\_2, w\_3 explicitly, and then go back to this system and try to find alpha, beta and gamma.

**2:43** · However, there's a trick.

**2:45** · Let's try to see if we can do it without finding w\_1, w\_2, and w\_3 explicitly.

**2:50** · So let me try to see what are the values of y at these points.

**2:56** · So y is minus x plus 5.

**2:58** · So the values are 6, 5, and 4.

**3:05** · And let me, instead of considering this equation, let me evaluate it at x is minus 1, x is 0, and x is 1.

**3:18** · What I get through this is that w at minus 1-- actually, let me write this.

**3:30** · I get w at minus 1, which is a number, equals alpha times w\_1 at minus 1, which is a number, plus beta times w\_2 at minus 1, plus gamma times w\_3 at minus 1.

**3:51** · And similarly at 0, and similarly at 1.

**3:58** · And now, let me think of this as a linear system that has unknowns alpha, beta, and gamma coefficients, these values here at minus 1, 0, and 1.

**4:11** · And the right-hand side, well, what's written here on the left-hand side. y at minus 1, y at 0, and y at 1.

**4:18** · If you write this in a matrix and read off coefficients from there, you get the following system.

**4:33** · So this is the matrix of the system read off from here.

**4:38** · These are the unknowns.

**4:42** · And these are the values of the right-hand side.

**4:48** · And I hope you'll agree that this is a very easy system to solve.

**4:51** · We just get alpha is 6, beta is 5, and gamma is 4.

**4:55** · So the solution to the first part is y equals 6\*w\_1 plus 5\*w\_2 plus 4\*w\_3.

**5:08** · And let's notice another thing.

**5:10** · No matter what values we put here, this matrix is always going to stay the same.

**5:16** · It's only the right-hand side that's going to change.

**5:18** · So if we're given any other polynomial now to express in a basis w\_1, w\_2, and w\_3, we don't have to do any thinking.

**5:26** · We don't have to do any computations.

**5:28** · What we do is go back to our table at the beginning and just read off-- let's go back to the table, and just read these values.

**5:35** · So in this case, y is 6 times w\_1, 5 times w\_2, and 3 times w\_3.

**5:43** · And that's already a hint to solving the b part, which is find the change of basis matrices between 1, x, x squared and w\_1, w\_2, w\_3.

**5:53** · Change of basis matrices means expressing one basis in terms of another.

**5:58** · So as a part of the problem, we will have to express 1, x, and x squared in terms of w\_1, w\_2, w\_3.

### Change of basis matrices

**6:06** · So let's just find their values at these three points.

**6:10** · One is a constant, it just takes value 1 everywhere.

**6:14** · x takes value minus 1 at minus 1, 0 at 0, and 1 at 1.

**6:19** · And x squared takes values 1, 0, and 1 at minus 1, 0, and 1.

**6:26** · And from this we can already conclude the part b here, we can conclude that 1 equals w\_1 plus w\_2 plus w\_3.

**6:39** · That x equals minus w\_1 plus w\_3.

**6:46** · And that x squared equals w\_1 plus w\_3.

**6:53** · And from this, we can immediately write one change of basis matrix.

**6:59** · Namely, since we know how to express 1, x, and x squared in terms of w\_1, w\_2, and w\_3, we can just copy this information over to this matrix, getting 1, 1, 1; minus 1, 0, 1; and 1, 0, 1.

**7:24** · So which matrix is this?

**7:26** · This is a matrix-- so we have 1, x, and x squared expressed in terms of w\_1, w\_2, and w\_3.

**7:34** · So if we feed this matrix something expressed in the basis 1, x, and x squared, say a, b, and c, what it's going to throw out is the same polynomial expressed in this basis here, w\_1, w\_2, and w\_3.

**7:50** · So I'm going to just write that this is a matrix of this basis change.

**8:02** · How do we get the other one?

**8:04** · Well, very easy.

**8:08** · We know it's just the inverse of A.

**8:11** · So this is going to be the matrix that takes something written in this basis and transfers it to this basis.

**8:27** · I'm not going to calculate the inverse of a matrix in front of you.

**8:30** · Instead I'm going to consult my oracle.

**8:32** · Sorry about that.

**8:34** · And my oracle says that the inverse should be 0, 1, 0; minus 1/2, 0, 1/2; and 1/2, minus 1, 1/2.

**8:52** · And that solves the b part.

### Derivative matrix mapping

**8:56** · Let's go into the c part.

**8:57** · The c part required us to find a matrix of taking derivatives, which is a linear map in the space of polynomials, in both of these basis.

**9:06** · So let's first do the 1, x, x squared basis because that one's easier.

**9:12** · I'm going to call it D\_x.

**9:18** · So I'm going to work in basis 1, x, x squared.

**9:22** · And what I want to express is the transformation of taking derivatives.

**9:27** · So here I'm going to write the vector to which taking derivatives maps the polynomial 1, which is 0.

**9:38** · And that's this expressed in the basis 1, x, x squared.

**9:41** · In the second column I'm going to write x prime, the vector to which D\_x sends to vector x, and that's equal to 1, which expressed in this basis is 1, 0, 0.

**9:58** · And here I'm going to write x squared prime, which is 2x, which, expressed in this basis, is just this.

**10:10** · That one was easy.

**10:12** · For the other one, well we could calculate w\_1, w\_2, w\_3 explicitly, take the derivatives, go back to the table and repeat the procedure that we did already.

**10:24** · So expressing these derivatives in terms of w\_1, w\_2, w\_3, and that's a lot of work.

**10:28** · But we pretty much already did most of this work.

**10:32** · So we know how to take derivatives in this basis, and we know how to go between these two basis.

**10:38** · So if we want to take a derivative of something written in the basis w\_1, w\_2, w\_3, well, let's first write this something in basis 1, x, x squared.

**10:53** · Then let's take a derivative of it.

**10:57** · And then let's write it back in the original basis that we want.

**11:02** · So it's multiplication of three matrices.

**11:05** · We have all three-- matrix multiplication is easy.

**11:07** · And my oracle, again, says that this should be minus 3 over 2, 2, minus 1 over 2; minus 1 over 2, 0, 1 over 2; and 1 over 2, minus 2, 3 over 2.

**11:28** · And that solves the problem.

**11:29** · Now, one thing that I would want to discuss in the end is how did you do with respect to my challenge, which was let's try to do as much of it as possible without finding w\_1, w\_2, and w\_3 explicitly.

**11:39** · And it seems like we did really well.

**11:41** · There's nowhere on the board written w\_1 equals, w\_2 equals, w\_3 equals.

**11:46** · But is it really so?

**11:47** · It's not.

**11:48** · We calculated the matrix of A inverse here.

**11:51** · And what this really means is that w\_1, w\_2, and w\_3, written in the basis 1, x, and x squared, are as follows.

**12:03** · w\_1 is minus 1/2 x plus 1/2 x squared.

**12:08** · w\_2 is 1 minus x squared.

**12:12** · And w\_3 is 1/2 x plus 1/2 x squared.

**12:16** · So you can check your work with the help of this matrix in case you did find w\_1, w\_2, and w\_3 explicitly.

**12:22** · And that's all I wanted to say today.