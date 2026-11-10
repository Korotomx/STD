![](https://www.youtube.com/watch?v=2uDvRUowBzg)

MIT 18.06SC Linear Algebra, Fall 2011  
View the complete course: https://ocw.mit.edu/18-06SCF11  
Instructor: Nikola Kamburov  
  
A teaching assistant works through a problem on linear transformations.  
  
License: Creative Commons BY-NC-SA  
More information at https://ocw.mit.edu/terms  
More courses at https://ocw.mit.edu

## Transcript

**0:06** · PROFESSOR: Hi, everyone.

**0:07** · Today, we're going to talk about linear transformations.

**0:10** · So, we've seen linear transformations incognito all the time until now.

**0:17** · We've played around with matrices.

**0:19** · Matrices multiplying vectors, say, in R^n and producing vectors in R^m.

**0:28** · So really, the language of linear transformations only provides a nicer framework when we want to analyze linear operations on more abstract vector spaces, like the one we have in this problem here.

**0:44** · We're going to work with the space of two by two matrices.

**0:51** · And we're going to analyze the operation, have the matrix A, and we produce its transpose.

**0:59** · OK.

**1:00** · So please take a few minutes to try the problem on your own and come back.

**1:15** · Hi, again.

**1:16** · OK.

**1:18** · So the first question we need to ask ourselves is, indeed, why is T a linear operator?

**1:24** · So what are the abstract properties that a linear operator satisfies?

**1:30** · Well, what happens when T acts on the sum of two matrices, A and B?

**1:41** · So it produces the matrix the transpose of A plus B.

**1:48** · But we know that this is A transpose, B transpose.

**1:53** · And so, this is exactly T(A) plus T(B).

**2:01** · So the transformation that we're analyzing takes the sum of two matrices into the sum of their transformations.

**2:15** · OK.

**2:16** · Similarly, it takes a multiple of a transformation into the multiple of the transformations.

**2:33** · So it takes the matrix c times A to c times A transpose, which is c T of A.

**2:43** · OK.

**2:43** · So it is a linear operator.

**2:47** · Now, can we figure out what its inverse is?

**2:52** · Well, what does the transpose do?

**2:57** · It takes a column and flips it into a row.

**3:03** · So what happens if we apply the operation once again?

**3:06** · Well, it's going to take the row and turn it back down to the column.

**3:11** · So applying the transformation twice, we come back to the original situation.

**3:21** · So therefore, T squared is the identity.

**3:28** · And from this, we infer that the inverse is the transformation itself.

**3:36** · Now, this was part one.

**3:40** · Part two, we'll compute the matrix of the linear transformation in the following two bases.

**3:51** · So the first basis is, in fact-- it is the standard basis for the space of two by two matrices.

**4:01** · And the way we compute the matrix, we first compute what T does to each of the basis elements.

**4:12** · So T of v\_1.

**4:15** · Let's go back.

**4:17** · So here.

**4:21** · So T takes the transpose of this matrix.

**4:25** · And we see that the transpose of \[1, 0; 0, 0\] is \[1, 0; 0, 0\].

**4:29** · So it's a symmetric matrix.

**4:31** · So T of v\_1 is v\_1.

**4:36** · What about T of v\_2?

**4:38** · Come back here.

**4:41** · So this 1 comes here.

**4:44** · 0 comes here.

**4:45** · And so we actually get v\_3.

**4:49** · So T of v\_2 is v\_3.

**4:54** · Similarly, T of v\_3 is v\_2.

**5:00** · And finally, T of v\_4.

**5:03** · Well, v\_4 is a symmetric matrix as well.

**5:08** · So the transpose doesn't change it.

**5:12** · OK.

**5:17** · Now, we encode this into a matrix in the following way.

**5:32** · Essentially, the first column will tell us how T of v\_1 is expressed as a linear combination of the basis elements.

**5:49** · Well, in this case, it's just v\_1.

**5:51** · So it's going to be 1 times v\_1 plus 0\*v\_2 plus 0\*v\_3 plus 0\*v\_4.

**5:58** · T of v\_2 is v\_3.

**6:00** · So we have 0, 0, 1, 0.

**6:08** · T of v\_3 is 0\*v\_1, 1\*v\_2, 0\*v\_3, 0\*v\_4.

**6:19** · And T of v4 is 0\*v\_1, 0\*v\_2, 0\*v\_3, plus 1\*v\_4.

**6:27** · OK.

**6:28** · So we've written down the matrix of the linear transformation T in the standard basis.

**6:35** · And you can check that this is exactly what we want.

**6:50** · The representation of some matrix, say, \[1, 2; 3, 4\] in this standard basis is, it's the vector \[1, 2, 3, 4\].

**7:07** · T takes this to its transpose, \[1, 3; 2, 4\].

**7:15** · So this in the basis is represented as \[1, 3, 2, 4\].

**7:24** · Right?

**7:26** · And it's not hard to see that when M\_T multiplies this vector, we get exactly this vector.

**7:41** · So we'll pause for a bit, so that I erase the board.

**7:45** · And we're going to return with the representation of T in the basis w\_1, w\_2, w\_3, and w\_4.

**7:57** · OK.

**7:57** · So let's now compute the matrix T in the basis w\_1, w\_2, w\_3, and w\_4.

**8:06** · We played the same game.

**8:08** · We look at how T acts on each of the basis vectors.

**8:14** · So T of w\_1-- well, w\_1 is a symmetric matrix.

**8:19** · So T of w\_1 is w\_1.

**8:23** · Similarly, with w\_2 and w\_3.

**8:27** · They're all symmetric.

**8:29** · What about w\_4?

**8:30** · Well, we see that the 1 comes down here, the negative one comes up here, and in the end, we just get the negative of w\_4.

**8:40** · So, let me just write this out.

**8:43** · We had T of w\_1 equal to w\_1, T of w\_2 equal to w\_2, T of w\_3 equal to w\_3, and T of w\_4, was negative of w\_4.

**9:00** · So therefore, the matrix of the linear transformation T, in this basis-- I'm going to call the matrix M prime T-- has a fairly simple expression.

**9:19** · The only non-zero entries are on a diagonal.

**9:21** · And they're precisely 1, 1, 1, and negative 1.

**9:32** · And finally, let's tackle the eigenvalues slash eigenvectors issue.

**9:38** · Well, you've seen what an eigenvector for a matrix is.

**9:46** · And the idea for an eigenvalue, eigenvector for a linear transformation is virtually the same.

**9:53** · And we are looking for the vectors v and scalars lambda such that T of v is lambda\*v. But if you guys look back to what we just did with w\_1, w\_2, w\_3, and w\_4, you'll see precisely that w\_1, w\_2, and w\_3 are eigenvectors for T with eigenvalue 1.

**10:22** · And w\_4 is an eigenvector for T with eigenvalue negative 1.

**10:27** · So yeah, we essentially have solved the problem knowing a very, very nice basis in which we computed the linear transformation T.

**10:43** · So I'll leave it at that.