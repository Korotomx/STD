![](https://www.youtube.com/watch?v=mVeuZzJdd1w)

MIT 18.06SC Linear Algebra, Fall 2011  
View the complete course: https://ocw.mit.edu/18-06SCF11  
Instructor: Nikola Kamburov  
  
A teaching assistant works through a problem on eigenvalues and eigenvectors.  
  
License: Creative Commons BY-NC-SA  
More information at https://ocw.mit.edu/terms  
More courses at https://ocw.mit.edu

## Transcript

**0:07** · PROFESSOR: Hi guys.

**0:08** · Today, we are going to play around with the basics of eigenvalues and eigenvectors.

**0:14** · We're going to do the following problem, we're given this invertible matrix A, and we'll find the eigenvalues and eigenvectors not of A, but of A squared and A inverse minus the identity.

**0:33** · So, this problem might seem daunting at first, squaring a 3 by 3 matrix, or taking an inverse of a 3 by 3 matrix is a fairly computationally intensive task, but if you've seen Professor Strang's lecture on eigenvalues and eigenvectors you shouldn't be all too worried.

**0:55** · So I'll give you a few moments to think of your own line of attack and then you'll see mine.

**1:11** · Hi again, OK, so the observation that makes our life really easy is the following one.

**1:20** · So say v is an eigenvector with associated eigenvalue lambda to the matrix A. Then, if we hit v with A squared, well, this we can write it as A times A\*v, but A\*v is lambda\*v, right?

**1:46** · So we have A\*lambda\*v.

**1:50** · Lambda is a scalar, so we can move it in front and get lambda\*A\*v, and lambda\*A\*v is, when we plug in A\*v, lambda\*v, is just lambda squared v. So, what we've find out is that if v is an eigenvector for A then it's also an eigenvector for A squared.

**2:15** · Just that the eigenvalue is the eigenvalue squared.

**2:19** · Similarly, if we hit A inverse-- if you hit v with A inverse.

**2:28** · So in this case we can write v as A\*v over lambda, given that of course, lambda is non-zero.

**2:41** · But the eigenvalues of an invertible matrix are always non-zero, which is an exercise you should do yourselves.

**2:52** · So if we just, then, take out the A and combine it with A inverse, this is the identity, and so we get 1 over lambda v. So v is also an eigenvector for a inverse, with eigenvalue the reciprocal of lambda.

**3:19** · OK, and from here, of course, A inverse minus the identity is lambda inverse minus 1 v, so the eigenvalue of A inverse minus the identity is 1 over lambda minus 1.

**3:44** · OK, so, what we've figured out is: we just need to find the eigenvalues and eigenvectors of A and then we have a way of finding what the eigenvalues and eigenvectors of A squared and A inverse minus the identity will be.

**4:05** · OK so, how do we find the eigenvalues?

**4:11** · Well, what does it mean for lambda to be an eigenvalue of A?

**4:19** · It means that the matrix A minus lambda the identity is singular, which is precisely the case when its determinant is 0, OK?

**4:35** · So we need to solve the following equation: 1 minus lambda, 2, 3; 0, 1 minus lambda, -2; and 0, 1, 4 minus lambda.

**5:08** · OK, it's fairly obvious which column we should use to expand this determinant.

**5:20** · We should use the first column, because we have only one non-zero entry, and so this is equal to 1 minus lambda times the determinant of the two by two matrix 1 minus lambda, -2; 1, 4 minus lambda, which is, I'm going to do the computation up here.

**5:57** · 1 minus lambda, lambda squared minus 5 lambda plus 6.

**6:08** · Which is a fairly familiar quadratic, and we can write it as the product of linear factors, as lambda minus 2, lambda minus three.

**6:23** · So the three eigenvalues of A are 1, 2, and 3.

**6:33** · OK so, first half of our problem is done, now we just need to find what the eigenvectors associated with each of these eigenvalues are.

**6:44** · How we do that?

**6:46** · Well, let's see.

**6:51** · Let's figure out what the eigenvector associated with lambda equals 1 is.

**6:59** · So, we know that the eigenvector needs to be in the null space of A minus lambda the identity, so A minus the identity, v, so-- write this out-- it's, 0, 0, 3, 2, 3, 0, -2, 0, 1.

**7:37** · And we see that the first column is 0, so the first variable will be our free variable if we want to solve this linear system of equations.

**7:57** · And you can just set it to 1 and it's not hard to see that the other two entries should be 0.

**8:09** · So we can do the same procedure with the other two eigenvalues and we'll get an eigenvector for each eigenvalue.

**8:24** · And in the end-- let me go back here.

**8:30** · So I'm going to put our results in a little table.

**8:36** · So A squared, inverse minus the identity, so the first row will be eigenvalues.

**8:54** · So it's going to be: if lambda is an eigenvalue for A, then we saw that lambda squared will be the eigenvalue for A squared and lambda inverse minus 1 will be the eigenvalue for A inverse minus the identity.

**9:11** · And the eigenvectors will be the same.

**9:19** · OK, we're done.