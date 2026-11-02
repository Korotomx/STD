![](https://www.youtube.com/watch?v=FzncDO1eSNI)

MIT 18.06SC Linear Algebra, Fall 2011  
View the complete course: https://ocw.mit.edu/18-06SCF11  
Instructor: Linan Chen  
  
A teaching assistant works through a problem on differential equations.  
  
Watch this video in Chinese: https://www.youtube.com/watch?v=fiSp3Ss-Yo8  
License: Creative Commons BY-NC-SA  
More information at https://ocw.mit.edu/terms  
More courses at https://ocw.mit.edu

## Transcript

### Introduction to application

**0:07** · LINAN CHEN: Hi.

**0:07** · Welcome back to recitation.

**0:09** · In the lecture, you've learned eigenvalues and eigenvectors of a matrix.

**0:14** · One of the many important applications of them is solving a higher-order linear differential equation with constant coefficients.

**0:22** · A typical example is like what I've written on the board here.

**0:27** · y is a function of t, and y and its derivatives satisfy this equation.

**0:34** · As you can see, it involves y, y prime, and all the way to its third derivative.

**0:41** · So our first goal is to solve this differential equation for its general solution using the method of matrix.

**0:50** · So the very first thing that we should do is to find out which matrix we should be working with.

**0:56** · So after that, we also want to say something about the explanation of this matrix A\*t.

**1:05** · We want to find out the first column of this matrix exponential.

**1:10** · Why don't you hit the pause now, and try to write down this matrix A by yourself.

**1:16** · But before you continue, make sure you come back to this video and check with me you've got the correct A. I'll see you in a while.

### Transforming the equation

**1:33** · OK, let's work together to transform this problem into linear algebra.

**1:40** · The idea is to put y double prime, y prime, and y together as a vector.

**1:55** · And let me call this vector u.

**1:58** · So of course, vector u is also a function in t.

**2:07** · So this is vector u.

**2:09** · If this is u, what's going to be u prime?

**2:12** · OK, u prime is going to be-- so I take derivative of every coordinate here that's going to be y triple prime, y double prime, and y prime.

**2:27** · So this is our u prime t.

**2:34** · And my goal is to write u prime as a matrix, call it A, times vector u itself.

**2:46** · So I want to put a matrix here.

**2:52** · And I want to create this matrix by incorporating this differential equation.

**2:59** · If you move everything except y triple prime to the right-hand side of the equation, you can read y triple prime is equal to negative 2 times y double prime-- so y triple prime is negative 2 times y double prime-- plus y prime-- that's plus 1 times y prime-- plus 2y.

**3:24** · That's 2y, right?

**3:28** · That gives you the first row.

**3:30** · Then look at the second coordinate, this y double prime.

**3:34** · y double prime is simply itself.

**3:37** · So you read y double prime is equal to 1 y double prime, then 0, 0.

**3:45** · That's the second row.

**3:46** · Well, same thing happens to the last row.

**3:49** · y prime is again itself.

**3:52** · So that's 0, 1, and 0.

**3:58** · That is our matrix A. Did you get the right answer?

**4:03** · So we have transformed this equation, this third-order ordinary differential equation of y into a first-order differential equation of u(t).

**4:16** · Although u(t) is a vector, but if we can solve this equation for u, we have all the information we need for y.

**4:25** · So let's plan on solving this equation.

**4:30** · In order to solve this equation, we will need the eigenvalues and eigenvectors of this matrix A.

**4:38** · Again, this is a good practice for you.

**4:40** · Why don't you pause the video again, and try to complete this problem on your own.

**4:46** · When you're ready, I'm going to come back and show you how I did it.

### Finding eigenvalues

**5:01** · Let's finish up everything together.

**5:03** · So as we said, we need the eigenvalues and eigenvectors of matrix A, and that involves computing the determinant of the following matrix.

**5:15** · So I want to compute the determinant of A minus lambda times the identity matrix I.

**5:23** · Let's write it out.

**5:25** · That's the determinant of -2 minus lambda, 1 2; 1, negative lambda, 0; and 0, 1, negative lambda.

**5:45** · So we need the determinant of this three by three matrix.

**5:50** · Do it in your favorite way.

**5:52** · You can either use the big summation formula, or you can do by cofactor along any row or any column.

**6:00** · The correct answer should be this is equal to 1 minus lambda times 1 plus lambda times 2 plus lambda.

**6:14** · And this polynomial has three roots: 1, -1, and -2.

**6:21** · These are the eigenvalues we're looking for.

**6:24** · So let me write it here.

**6:26** · Lambda\_1 is equal to 1.

**6:30** · Lambda\_2 is equal to -1.

**6:34** · And lambda\_3 is equal to -2.

**6:42** · So now what we need is the eigenvector corresponding to each eigenvalue.

**6:49** · Let's take lambda\_1 for example.

**6:52** · The eigenvector of A corresponding to lambda\_1 is in the null space of the matrix A minus lambda\_1\*I, so in this case it's A minus I. So it's in the null space of this matrix.

**7:08** · In other words, we are looking for a vector, let's call it \[a, b, c\], a column vector a, b, and c, such that this matrix multiplying \[a, b, c\] gives me 0.

**7:23** · So if you write it out, that's going to be A minus I is \[-3, 1, 2; 1, -1, 0; 0, 1, -1\] times \[a; b; c\] is equal to 0.

**7:46** · OK.

**7:47** · Could we choose constants a, b, c such that this is always true?

**7:53** · Well if you read the last row, so the last dot product, it says that b has to be equal to c.

**8:04** · And if you read the second row it says that a has to be equal to b.

**8:12** · Which means a is equal to b is equal to c.

**8:16** · And if this relation is true, the first product is always going to be 0.

**8:23** · So that simply means we can choose the first eigenvector, the eigenvector corresponding to lambda\_1, to be x\_1 is equal to \[1, 1, 1\] transpose.

**8:41** · So we choose the first eigenvector to be the column vector with all the coordinates being 1.

**8:50** · And you can do the same thing to lambda\_2 and lambda\_3.

**8:55** · But please allow me to skip the computation here.

**8:58** · I'm going to write out the answer for you.

**9:00** · So x\_2 the eigenvector corresponding to the second eigenvalue, is going to be equal to 1, -1, and 1.

**9:13** · And x\_3 is going to be 4, -2, and 1.

**9:23** · Now we've got everything we need in order to create the general solutions for u(t) So we have eigenvalues, we have the corresponding eigenvectors.

**9:34** · What should be u(t)?

**9:36** · The general solution for u(t) is equal to some constant C\_1 times e to the power lambda\_1\*t-- so in this case, e to the power t.

**9:50** · Then times the first eigenvector, x\_1.

**9:56** · Plus some other constant C\_2 times e to the power lambda\_2\*t-- so e to the power negative t-- times x\_2.

**10:07** · That's the second eigenvector.

**10:09** · Then plus some other constant, C\_3 times e to the power lambda\_3t-- so negative 2t-- times x\_3.

**10:22** · That gives you the general solution for u.

**10:25** · As we just said, if you know what u is, you have all the information you need for y.

**10:33** · Just in case you're curious about what y is, you can just read the last coordinate of x\_1, x\_2, and x\_3.

**10:43** · And you can see that all of them are 1.

**10:46** · So y(t) is simply equal to C\_1 e to the power lambda t plus C\_2 e to the power negative t plus C\_3 e to the power negative 2t.

**11:06** · And the choice of C\_1, C\_2, and C\_3 is completely arbitrary.

**11:12** · So that completes the first part of this question.

### Computing matrix exponential

**11:16** · In the second part, we want to say something about the exponential of A\*t.

**11:21** · So let me first give you the recipe to cook up the exponential of A\*t.

**11:28** · The exponential of A\*t is equal to the product of three matrices.

**11:38** · So you usually we denote them by S times e to the power capital lambda t times S inverse.

**11:49** · And you may ask what S is, and what this matrix is.

**11:53** · So S is the matrix that has x\_1, x\_2, and x\_3 being its column vectors.

**12:01** · So S is x\_1, x\_2, and x\_3.

**12:09** · Let me copy it down here.

**12:11** · So that's 1, 1, 1; 1 -1, 1; 4, -2, 1.

**12:22** · And the matrix in the middle, e to the power lambda\*t is a diagonal matrix.

**12:28** · So e to the power lambda\*t, it's a diagonal matrix, and its diagonal entries are given by e to the power lambda\_1\*t-- so that's e to the power t-- then e to the power lambda\_2\*t-- negative t-- and e to the power lambda\_3\*t-- negative 2t.

**12:51** · 0 everywhere else.

**12:53** · So that's e to the power lambda\*t.

**12:55** · Then the exponential of this At is given by the product of these three matrices.

**13:02** · It looks a bit complicated because it involves the inverse of S. But luckily, we only want the first column of the result.

**13:12** · So if we consider this product, we can see: the product of the first two matrices is relatively easy, because this is a diagonal matrix, and we know that S is given by these columns.

**13:33** · So the result of the product of these two is simply multiplying the columns of S by these coefficients respectively.

**13:44** · So you expect to get e to the power lambda\_t x\_1 times e to the power-- sorry.

**13:52** · The second column should be e to the power negative t, x\_2.

**13:56** · The third column should be e to the power negative 2t, x\_3.

**14:02** · And here, what we should put is S inverse.

**14:07** · But we don't need everything from S inverse, because as we just said, we only need the first column of this result. And the first column of this product is going to be given by linear combinations of these columns, and the coefficients are going to be given by the first column S inverse.

**14:29** · So our goal should be just to get the first column of S inverse.

**14:37** · Then what is the first column of S inverse?

**14:40** · Well, the formula for S inverse is S inverse is going to be the reciprocal of the determinant of S, so 1 over determinant of S, times the transpose of a matrix C. This matrix C, the entries of this matrix C are given by cofactors of matrix S.

**15:02** · And then you take transpose, you divide everything by the determinant of S. The result will be S inverse.

**15:11** · And we only need the first column of this matrix.

**15:15** · Let's try to write the first column out.

**15:18** · Well again, do it in your favorite way to compute the determinant of S. The result should be 1 over 6.

**15:25** · So the determinant of S is 6.

**15:28** · Then what is the first column of C transpose?

**15:32** · Well we can read it from here.

**15:37** · This spot, the (1, 1) spot, should be the cofactor of this spot here.

**15:44** · That negative 1 minus negative 2, which is 1, so we put 1 here.

**15:55** · Now this spot will be the cofactor of this entry here.

**16:03** · so that's 1 minus negative 2, that's 3.

**16:08** · But this is (1, 2) entry, so you should put a negative sign in the front.

**16:16** · Then the last spot should be the cofactor of this entry here, which is 1 minus negative 1, that's 2.

**16:29** · Something else here.

**16:34** · Two warnings.

**16:35** · First, don't forget this transpose sign.

**16:39** · Second, don't forget this negative sign.

**16:44** · We've got the first column of S inverse, and that's all we need.

**16:49** · So we put it here.

**16:50** · That's 1 over 6, -1/2, and 1/3.

**17:02** · That's good enough for me.

**17:04** · Now I can read out the first column of exponential of A\*t.

**17:08** · So the first column of the exponential of A\*t, I'm going to write it here.

**17:16** · That's going to be equal to the linear combination of these columns.

**17:21** · So that's 1/6 of the first column, that's e to the power t over 6 times x\_1.

**17:30** · Plus this times this, so that's going to be minus 1/2 of e to the power negative t times x\_2.

**17:42** · Then plus 1/3 of e to the power negative 2t times x\_3.

**17:50** · That's the first column of the exponential A\*t.

**17:53** · And then with the other two columns.

**18:00** · That's the answer.

**18:02** · If you want more practice, you can certainly complete this S inverse, and then you can also complete the exponential of A\*t.

**18:13** · But I will leave the rest to you.

**18:16** · OK, I hope this example shows you that linear algebra can be a powerful tool in solving higher-order ordinary differential equations with constant coefficients.

**18:27** · And we have demonstrated the standard procedure to do it, and we also practiced how to calculate the exponential of a matrix.

**18:37** · Thanks for watching, and see you next time.