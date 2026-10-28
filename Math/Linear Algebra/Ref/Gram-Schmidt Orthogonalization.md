![](https://www.youtube.com/watch?v=HEQuN0QELSQ)

MIT 18.06SC Linear Algebra, Fall 2011  
View the complete course: https://ocw.mit.edu/18-06SCF11  
Instructor: Ana Rita Pires  
  
A teaching assistant works through a problem on Gram-Schmidt orthogonalization.  
  
License: Creative Commons BY-NC-SA  
More information at https://ocw.mit.edu/terms  
More courses at https://ocw.mit.edu

## Transcript

### Introduction to QR

**0:06** · ANA RITA PIRES: In lecture, you've learned about Gram-Schmidt orthogonalization, and that's what today's problem is about.

**0:12** · We have a matrix A, and its columns are a, b, and c.

**0:17** · And I want you to find orthonormal vectors q\_1, q\_2, and q\_3 from those three columns.

**0:24** · Then I want you to write A as a-- it's QR decomposition where Q is an orthogonal matrix, and R is an upper triangular matrix.

**0:33** · Remember, an orthogonal matrix is a matrix whose columns are orthonormal vectors.

**0:39** · Work on it for a little while, hit pause, and when you're ready I'll come back and we'll do it together.

**0:52** · Did you manage to solve that all right?

**0:55** · Well let's start solving it together.

### Gram-Schmidt process

**0:58** · So Gram-Schmidt orthogonalization, as you should remember from lecture, consists of the following.

**1:06** · At each step, you find your orthonormal vector by taking the vector that you started with, a, b, or c in this case, and making it orthonormal to the previous ones.

**1:22** · Let's actually do it.

**1:25** · We want to find q\_1.

**1:27** · Well, to find q\_1, start with a, and make it orthonormal to the previous one.

**1:32** · There's no previous one, so that's very easy.

**1:35** · The direction of a is fine and you just need to ensure that your vector has length 1.

**1:40** · Well, a is the vector \[1, 0, 0\].

**1:44** · So you should divide it by its length, but its length is 1, so this is simply \[1, 0, 0\].

**1:54** · q\_1 is done.

**1:55** · Now let's do q\_2.

**1:59** · So with q\_2, I will start with my vector b.

**2:03** · And then I want to make it, well first of all, orthogonal to what I already have, which is q\_1.

**2:09** · For that, I'm going to subtract off from b the projection of b onto q\_1.

**2:16** · Minus b dot q\_1 times q\_1.

**2:21** · Usually, when you're doing the projection of a vector onto another vector, you have to divide it by the length of, in this case, q1\_.

**2:29** · But because q\_1 has length 1, you don't need to do that.

**2:34** · So what will it be here?

**2:36** · Well b dot q\_1 is going to be-- b is \[2, 0, 3\], minus, b dot q\_1 will be 2, and \[1, 0, 0\].

**2:53** · So this will be \[0, 0, 3\].

**2:59** · This vector is orthogonal to this one, and you can check by doing your dot product.

**3:04** · It should be 0, and it is.

**3:07** · We need it also to be length 1, because we want these two vectors to be orthonormal.

**3:13** · So this is not actually q\_2.

**3:15** · Let's call this one q\_2 prime, and set q\_2 equals to q\_2 prime divided by its length, which in this case is 3.

**3:29** · \[0, 0, 1\].

**3:32** · That's my vector q\_2.

**3:35** · Let's go on to the third one, q\_3.

**3:40** · Well again, I start with my third vector, c.

**3:45** · And then I want to subtract the projection of c onto q\_1 and onto q\_2, and that will give me a q\_3 that is orthogonal to both q\_1 and q\_2.

**3:56** · c minus c dot q\_1 times q\_1 minus c dot q\_2 dot q\_2.

**4:09** · This will be c, \[4, 5, 6\] minus, q\_1 was \[1 0 0\], so 4, times \[1, 0, 0\], minus-- q2-- 6 \[0, 0, 1\].

**4:28** · So this vector will be \[0, 5, 0\].

**4:34** · And once again, this one is orthogonal to q\_1 and q\_2, but it is not norm 1 yet.

**4:42** · So q\_3-- I'll call that one q\_3 prime, and I'll set q\_3 equal to q\_3 prime divided by its length which is 5.

**4:55** · q\_3 is the vector \[0, 1, 0\].

**5:04** · One thing that I want you to note is that my vectors q\_1, q\_2, q\_3 are very nice in this case.

**5:10** · Usually, when you perform Gram-Schmidt orthogonalization, you end up with lots of square roots because you're dividing by the length.

**5:17** · In this case, we have everything is integers, which is, well, very lucky.

**5:25** · Next part of the problem is we want to write the QR decomposition of the matrix A. A equals Q\*R. Well, the matrix A, you already know what it is.

### Constructing matrix Q and R

**5:38** · It is the matrix \[1, 2, 4; 0, 0, 5; 0, 3, 6\].

**5:50** · And Q you want to be an orthogonal matrix.

**5:54** · Like I said before, an orthogonal matrix has orthonormal vectors for its columns.

**6:00** · And we already have such a matrix.

**6:02** · It's the matrix that has q\_1, q\_2, and q\_3 as its column vectors.

**6:07** · 1, 0, 0; 0, 0, 1; and 0, 1, 0.

**6:15** · Now, we need an upper triangular matrix that makes this equality true.

**6:21** · Take a moment to look at your matrix Q. It is simply a permutation matrix, so it's very easy to come up with a matrix that should fit here.

**6:30** · What this permutation matrix does is it exchanges rows two and three from my matrix R to give you A.

**6:39** · So you know what R must be.

**6:40** · It must be 1, 2, 4; 0, 3, 6-- that's the third row of A-- and then 0, 0, 5, which is the second row of A.

**6:52** · And indeed, R is upper triangular.

**6:56** · This is your QR decomposition of the matrix A. Q is orthogonal, R is upper triangular.

### Verification of decomposition

**7:04** · But let's see where these numbers in the matrix R are coming from.

**7:08** · Let me label these columns for you, a, b, c and q\_1, q\_2, q\_3.

**7:15** · And then I have my matrix R.

**7:18** · You know from the way that matrix multiplication works that A is going to be this matrix Q times the first column of R. So you can regard that as these numbers in the first column of R are giving you the linear coefficients in which you need to take these vectors to add up to A. Let me write that down.

**7:43** · A is going to be 1 times q\_1 plus 0 times q\_2 plus 0 times q\_3.

**7:51** · Let's do it for b.

**7:53** · The second column of this matrix will be Q times this column.

**7:57** · So it will be 2 times q\_1 plus 3 times q\_2 plus 0 times q\_3.

**8:08** · And finally, for c I will have c is equal to this matrix times this vector, 4\*q\_1 plus 6\*q\_2 plus 5\*q\_3.

**8:23** · Now let's go back and see where these numbers are showing up.

**8:30** · I wanted to have A equals 1 times q\_1.

**8:34** · Well that's very easy.

**8:35** · It comes from here, a equals 1 times q\_1.

**8:42** · Let's try the second one.

**8:44** · b equals 2\*q\_1 plus 3\*q\_2.

**8:49** · Well q\_2, let's see.

**8:52** · q\_2 prime is equal to 3 times q\_2, so let me write this here to help.

**8:57** · 3\*q\_2.

**8:59** · Now let me remind you that b dot q\_1 was equal to 2.

**9:05** · Now look at this equation.

**9:06** · You we have b is equal to 2\*q\_1 plus 3\*q\_2, which is what we wanted.

**9:14** · Let's check q\_3.

**9:18** · q\_3 prime is equal to 5\*q\_3 so let me write that here, 5\*q\_3.

**9:25** · And now I have c is equal to-- this number was 4, and this number was 6-- c is equal to 4\*q\_1 plus 6\*q\_2 plus 5\*q\_3, which indeed, is what we wanted.

**9:45** · So this is where these numbers from the matrix R are coming from.

**9:49** · And that finishes this problem.

**9:52** · I hope you have a better grasp of the QR decomposition now.

**9:56** · Bye.

**9:57** · See you next time.