![](https://www.youtube.com/watch?v=VYS9EYZ3gCo)

MIT 18.06SC Linear Algebra, Fall 2011  
View the complete course: https://ocw.mit.edu/18-06SCF11  
Instructor: David Shirokoff  
  
A teaching assistant works through a problem on complex matrices.  
  
License: Creative Commons BY-NC-SA  
More information at https://ocw.mit.edu/terms  
More courses at https://ocw.mit.edu

## Transcript

### Introduction to matrix A

**0:04** · DAVID SHIROKOFF: Hi everyone.

**0:06** · Welcome back.

**0:07** · So today we're going to tackle a problem in complex matrices.

**0:10** · And specifically, we're going to look at diagonalizing a complex matrix.

**0:15** · So given this matrix A, we're asked to find its eigenvalue matrix lambda, and its eigenvector matrix S.

**0:23** · And one thing to note about this matrix A is that if we take its conjugate transpose, it's actually equal to itself.

**0:30** · So in Professor Strang's book, he combines this notation to be superscript H to mean conjugate transpose.

**0:38** · So if you were to take the transpose of this matrix and then conjugate all the elements, you would find that A equals its conjugate transpose, and we call this property Hermitian.

**0:48** · So I'll let you think about this for a moment and I'll be back in a second.

### Finding the eigenvalues

**1:03** · OK, welcome back.

**1:05** · So what's the first step in computing the eigenvectors and eigenvalues of the matrix?

**1:09** · It's to take a look at the characteristic equation.

**1:13** · So specifically, we take det of A minus lambda i.

**1:21** · And quite possibly, the only thing new with this problem is that the entries of the matrix A are complex.

**1:29** · Now, you may have already seen that lambda's being complex, but we're going to work this out explicitly.

**1:36** · So if I take the determinant, we get det of 2 minus lambda, 3 minus lambda, we have 1 minus i, 1 plus i.

**1:49** · We want to set this to 0.

**1:53** · This then gives us a polynomial for lambda.

**2:02** · 1 plus i, 1 minus i, set it equal to 0.

**2:09** · We can expand out this term.

**2:11** · You get 6 minus 5 lambda plus lambda squared.

**2:19** · These two terms you'll note are complex conjugates of each other.

**2:22** · This tends to make things simple.

**2:24** · So we have minus 1 minus i squared is going to give us 2.

**2:30** · Because they're differences of squares, the cross terms involving i cancel, and we get the characteristic equation.

**2:43** · Lambda squared minus 5 lambda plus 4 equals 0.

**2:49** · And specifically, we can factorize this equation.

**2:54** · We see that there's roots of minus 1-- or factorizes into factors of lambda minus 1 and lambda minus 4, which then give us roots of lambda is 1 and lambda is 4.

**3:10** · So when one curious point to note is that the eigenvalues are real in this case.

**3:15** · 1 and 4 are real, whereas the matrix that we started with was complex.

**3:19** · And this is a general property of Hermitian matrices.

**3:22** · So even though they might be complex matrices, Hermitian matrices always have real eigenvalues.

### Finding the eigenvectors

**3:29** · So this is the first step when asked to diagonalize a matrix.

**3:33** · The second step is to find the eigenvectors.

**3:45** · And to do that what we have to do is we have to look at the cases for lambda equals 1 and lambda is equal 4 separately.

**3:52** · So let's first look at the case of lambda is equal to 1.

**3:59** · And specifically, we're going to be looking for a vector such that A minus lambda\*I times the vector v is 0.

**4:13** · And if we've done things properly, this matrix A minus lambda\*I should be singular.

**4:20** · So if we take A minus lambda\*I, we're going to get 1, 1 minus i; 1 plus i, 3 minus 1 is 2.

**4:32** · And I'll write out components of v, which are v\_1 and v\_2.

**4:37** · And we want this to be 0.

**4:40** · And you'll note that it's almost always the case that when we work out A minus lambda\*I, the second row is going to be a constant multiple of the first row.

**4:52** · And this must be the case because these two rows must be linearly dependent on each other for the matrix A minus lambda\*I to be singular.

**5:00** · So if you look at this you might think that these two rows aren't necessarily linearly independent.

**5:06** · But the point is that there's complex numbers involved.

**5:09** · And indeed, actually if we were to multiply this first row by 1 plus lambda, we would get 1 plus lambda and 2.

**5:16** · And you note that that's exactly the second row.

**5:19** · So this second row is actually 1 plus lambda times the first row.

**5:23** · So these rows are actually linearly dependent on each other.

**5:28** · So what values of v\_1 and v\_2 can we take?

**5:30** · Well, we just need to make this top row multiplied by v\_1 and v\_2 equal to 0.

**5:36** · And then because the second row is a constant multiple of the first row, we're automatically guaranteed that the second equation holds.

**5:44** · So just by looking at it, I'm going to take v\_1 is equal to 1 minus i, and v\_2 is negative 1.

**5:57** · So we see that 1 times 1 minus i minus 1 times 1 minus i is going to give us 0.

**6:03** · So this is one solution.

**6:05** · And of course, we can take any constant multiple times this eigenvector, and that's also going to be an eigenvector.

**6:14** · So I'll just write this out.

**6:16** · 1 minus i, minus 1 is the eigenvector for lambda is equal to 1.

**6:24** · For lambda is equal to 4, again, A minus lambda\*I is going to give us negative 2, 1 minus i; 1 plus i, 3 minus lambda's going to be minus 1.

**6:41** · And I'll call this vector u\_1 and u\_2.

**6:47** · And again, we want u\_1 and u\_2 equal to 0-- or sorry, the matrix multiplied by \[u 1, u 2\] is equal to 0.

**6:54** · And just by looking at this again, we see that the second row is actually a constant multiple of the first row.

**7:01** · For example, if we were to multiply this row by negative 2, and this row by 1 plus i, we would see that they're constant multiples of each other.

**7:11** · So I can take u to be, for example, 1, and 1 plus i.

**7:22** · How did I get this?

**7:23** · Well I just looked at the second equation because it's a little simpler, and I said, well, if I have 1 plus I here, I can just say multiply it by 1.

**7:32** · And then minus 1 times 1 plus i, when I add them up, is going to vanish.

**7:37** · So this is how I get the second one.

**7:40** · Now there's something curious going on, and this is going to be another property of Hermitian matrices.

**7:45** · But if you actually take a look at this eigenvector, it will be orthogonal to this eigenvector when we conjugate the elements and dot the two vectors together.

**7:54** · So this is another very special property of complex Hermitian matrices.

### Diagonalizing the matrix

**8:02** · OK, so the last step now is to construct these matrices lambda and S. Now we already know what lambda is because it's the diagonal matrix with the eigenvalues 1 and 4.

**8:13** · So we have 1, 0; 0 and 4.

**8:21** · Now I'm going to do something special for S.

**8:24** · I've noted that these two vectors u and v are orthogonal to each other.

**8:30** · So what do I mean by orthogonal?

**8:32** · Specifically, if I were to take v conjugate transpose and multiply it by u, we would end up getting 1 plus i minus 1.

**8:45** · This would be v conjugate transpose.

**8:48** · 1, 1 plus i, and we see that when we multiply these out we get 0.

**8:59** · So when we have orthogonal eigenvectors, there's a trick that we can do to build up this matrix S and S inverse.

**9:06** · What we can do is we can normalize u and v.

**9:09** · So specifically, we can take any constant multiple of u and v, and it's still going to be an eigenvector.

**9:16** · So what I'm going to do is I'm going to take u and v and multiply them by their length.

**9:22** · So for example u, the amplitude of its top component is 1.

**9:27** · The amplitude of its bottom component is 2.

**9:30** · So notice that the modulus of the complex number 1 plus I is 2.

**9:34** · So we have-- sorry, it's root 2, the complex modulus is root 2.

**9:44** · So the amplitude of the entire vector is root 3.

**9:48** · It's 1 plus 2 squared quantity square rooted, so it's root 3.

**9:52** · So what we can do is we can build up this matrix S using a normalization factor of 1 over root 3.

**10:05** · And I'm going to take the-- the first column is the first eigenvector that corresponds to eigenvalue 1.

**10:13** · And then the second column is the second eigenvector which corresponds to eigenvalue 4.

**10:20** · And the reason I put in this root 3 here is to make this column unit length 1, and this column unit length 1.

**10:29** · And the reason I do this is because now this matrix S, it's possible to check that this matrix S is actually unitary, which means that its inverse is actually just equal to it's conjugate transpose.

**10:53** · So this is a very special property of the eigenvectors of a Hermitian matrix.

**11:00** · And then lastly, I'm just going to write down the diagonalization of A. So if I have A, because I have its eigenvector matrix S, and its eigenvalue matrix lambda, it's possible to decompose A into a product of S lambda S inverse.

**11:17** · And because S is unitary, its inverse is actually its conjugate transpose.

**11:29** · So just to put the pieces together, we have A is equal to S-- which is 1 over root 3 1 minus i, minus 1; 1, 1 plus i-- times the diagonal matrix \[1, 0; 0, 4\] times S inverse, which is going to be its conjugate transpose.

**11:56** · So what I do is I conjugate each element, so 1 minus i becomes 1 plus i and vice versa.

**12:02** · And then I take the transpose.

**12:04** · So I get 1 plus i.

**12:06** · Transposing swaps the minus 1 and 1.

**12:12** · And at the end of the day, I get S inverse is just this matrix here.

**12:19** · And if you were to multiply these matrices out, you would see it you actually do recover A.

**12:26** · So just to summarize quickly, even though we were given a complex matrix A, the process to diagonalize A is the same as what we've seen before.

**12:35** · The first step is to find the characteristic equation and the eigenvalues.

**12:39** · And then the second step is to find the eigenvectors, and you do this in the same procedure.

**12:44** · But in general, the eigenvectors can be complex.

**12:48** · And for this very special case, when A is Hermitian, the eigenvalues are real, and the eigenvectors are orthogonal to each other.

**12:56** · So I think I'll conclude here, and I'll see you next time.