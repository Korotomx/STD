![](https://www.youtube.com/watch?v=t-n4a18AW08)

MIT 18.06SC Linear Algebra, Fall 2011  
View the complete course: https://ocw.mit.edu/18-06SCF11  
Instructor: Nikola Kamburov  
  
A teaching assistant works through a problem on projection into subspaces.  
  
License: Creative Commons BY-NC-SA  
More information at https://ocw.mit.edu/terms  
More courses at https://ocw.mit.edu

## Transcript

**0:05** · PROFESSOR: Hi, guys.

**0:08** · My name is Nikola, and in this video, we're going to work out an example of an orthogonal projection matrix.

**0:14** · Specifically, we are gonna compute the projection matrix onto the plane given by the equation x plus y minus z equals 0.

**0:23** · So before we start, let me just recall what a projection matrix is.

### What a Projection Matrix Is

**0:29** · So you've seen this sketch here a million times already.

**0:35** · A projection matrix takes any vector in three-space-- well, just in this case, we are dealing with a three-space-- and projects it down onto the plane, a two-dimensional subspace of R^3.

**0:52** · So I'll give you a few moments to consider the problem for yourselves.

**0:58** · And then you'll see my take on it.

**1:10** · Hi again.

**1:12** · So in lecture, Professor Strang derived, in meticulous detail, the formula for the projection matrix.

### The Formula for the Projection Matrix

**1:21** · So it was given by the following slightly complicated expression.

**1:28** · It's A times A transpose A inverse A transpose where A is a matrix that somehow encodes the subspace we're projecting on.

**1:45** · In particular, A has, as its columns, a\_1, a\_2, I'm going to denote them-- a basis for the plane we're projecting on.

**2:00** · So essentially, what we need to do is find two such vectors that span the plane and start computing with a matrix.

**2:12** · This is fairly straightforward.

**2:18** · One choice that works, for example, is \[1, -1, 0\] for the first column, and \[1, 0, 1\] for the second column.

**2:35** · And let me write out the matrix A. So in the formula, the slightly more complicated combination is A transpose A inverse, so let me compute that first for you.

**3:00** · So A transpose A is a 2 by 2 matrix.

**3:08** · And it's not so hard to figure out that it's 2 and 1; 1, 2.

**3:18** · Now we shall invert it using the familiar formula.

**3:29** · 1 over the determinant.

**3:31** · 2 times 2 minus 1 is 3.

**3:34** · And so we switch the diagonal entries, and we flip the signs of the off-diagonal ones.

**3:45** · Right.

**3:46** · And therefore, projection matrix is given by the following product of matrices: ...1/3, \[2, -1; -1, 2\] and then transpose of A, which is \[1, -1, 0; 1, 0, 1\].

### Projection Matrix

**4:25** · I'm gonna carry out this multiplication in inhumanly fast fashion.

**4:31** · So I'm just gonna write down the answer, which is 1/3 \[2, -1, 1; -1, 2, 2; 1, 1, 1\].

**4:48** · So what you can do now is-- well, you can check whether this answer actually makes sense.

**4:56** · One thing you can do is just-- well, a projection matrix is supposed to take the normal to the plane down to 0.

**5:06** · So you can just multiply P and the normal vector \[1, 1, -1\].

**5:14** · And if you get 0, maybe you've done a good job.

**5:18** · Another curious thing that I would like to point out here is: so you see we had lots of freedom choosing the matrix A. We could have chosen any two columns that span the subspace, that spans the plane.

**5:36** · The beautiful thing about it is that in the end, we'll get the same answer.

**5:44** · So I hope there will be many of you who would say, hey, there is an easier way to do the problem.

**5:51** · And I'll agree with these people.

**5:53** · So let's see what would be an easier approach.

**6:01** · Well, let's go back to the sketch here.

**6:08** · And let's make the following observation, that any vector is a sum of two components.

**6:16** · The first component is its projection onto the plane.

**6:22** · And the other component is its projection onto the orthogonal complement of the plane, in this case, onto the normal vector through the plane.

**6:31** · So in the language of linear algebra, this is just b equals to its projection onto the plane plus its projection-- I'm gonna call it P\_N-- onto the orthogonal complement of the plane.

**6:52** · I'm gonna suggestively write here the identity matrix so that you can immediately read off a matrix equality.

**7:01** · Associated with this equality here, it's the identity equals P plus P\_N.

**7:10** · And therefore, the projection matrix is just the identity minus the projection matrix onto the normal vector.

**7:20** · Now, this object here, P\_N, is much easier to compute, well, for two reasons.

**7:28** · First one is that projecting onto a one-dimensional subspace is infinitely easier than projecting onto a higher-dimensional subspace.

**7:38** · And second, we already have-- well, immediately we can read off from the equation of the plane what the normal vector is.

**7:47** · So we don't have derive these guys.

**7:52** · We don't have to do what we did here.

**7:56** · So essentially, P\_N will be N N transpose N inverse N transpose.

**8:16** · And that's equal to \[1, 1, -1\]-- N transpose N inverse, this is just a number.

**8:33** · It's 1 over the magnitude of the normal vector, so that's-- then, the magnitude squared, so that's 3.

**8:41** · And 1, 1, -1.

**8:48** · I'm gonna write the answer here.

**8:55** · It's 1/3, 1, 1, -1; 1, 1, -1; and -1, 1, 1.

**9:25** · And in order to get the projection matrix-- yes?

**9:28** · AUDIENCE: \[INAUDIBLE\].

**9:30** · PROFESSOR: Oh.

**9:32** · Thank you.

**9:33** · Thank you.

**9:34** · And in order to get the projection matrix, we just subtract from the identity this expression.

**9:41** · And you can confirm that it's-- we get the same answer as here.

**9:48** · I think we're done here.