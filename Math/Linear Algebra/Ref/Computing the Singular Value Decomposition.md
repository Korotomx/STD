![](https://www.youtube.com/watch?v=pSbafxDHdgE)

MIT 18.06SC Linear Algebra, Fall 2011  
View the complete course: https://ocw.mit.edu/18-06SCF11  
Instructor: Ben Harris  
  
A teaching assistant works through a problem on computing the singular value decomposition.  
  
License: Creative Commons BY-NC-SA  
More information at https://ocw.mit.edu/terms  
More courses at https://ocw.mit.edu

## Transcript

### Introduction to the problem

**0:06** · PROFESSOR: Hey, we're back.

**0:09** · Today we're going to do a singular value decomposition question.

**0:13** · The problem is really simple to state: find the singular value decomposition of this matrix C equals \[5, 5; -1, 7\].

**0:25** · Hit pause, try it yourself, I'll be back in a minute and we can do it together.

### SVD definition and formulas

**0:40** · All right, we're back, now let's do it together.

**0:44** · Now, I know Professor Strang has done a couple of these in lecture, but as he pointed out there, it's really easy to make a mistake, so you can never do enough examples of finding the SVD.

**0:59** · So, what does the SVD look like?

**1:02** · What do we want to end up with?

**1:05** · Well, we want a decomposition C equals U sigma V transpose.

**1:16** · U and V are going to be orthogonal matrices, that is, their columns are orthonormal sets.

**1:25** · Sigma is going to be a diagonal matrix with non-negative entries.

**1:31** · OK, good.

**1:32** · So now, how do we find this decomposition?

**1:34** · Well, we need two equations, OK?

**1:39** · One is C transpose C is equal to V, sigma transpose, sigma, V transpose.

**1:54** · And you get this just by plugging in C transpose C here and noticing that U transpose U is 1, since U is an orthogonal matrix.

**2:02** · Okay.

**2:04** · And the second equation is just noticing that V transpose is V inverse, and moving it to the other side of the equation, which is C\*V equals U\*sigma.

**2:15** · OK, so these are the two equations we need to use to find V, sigma, and U. OK, so let's start with the first one.

### Calculating eigenvalues

**2:28** · Let's compute C transpose C. So C transpose C is that-- Well, if you compute, we'll get a 26, an 18, an 18, and a 74, great.

**3:00** · Now, what you notice about this equation is this is just a diagonalization of C transpose C. So we need to find the eigenvalues-- those will be the entries of sigma transpose sigma-- and the eigenvectors which will be the columns of a V. Okay, good.

**3:22** · So how do we find those?

**3:24** · Well, we look at the determinant of C transpose C minus lambda times the identity, which is the determinant of 26 minus lambda, 18, 18, and 74-- 74 minus lambda, thank you.

**3:55** · Good, OK, and what is that polynomial?

**3:59** · Well, we get a lambda squared, now the 26 plus 74 is 100, so minus 100\*lambda.

**4:09** · And I'll let you do 26 times 74 minus 18 squared on your own, but you'll see you get 1,600, and this easily factors as lambda minus 20 times lambda minus 80.

**4:27** · So the eigenvalues are 20 and 80.

**4:31** · Now what are the eigenvectors?

**4:33** · Well, you take C transpose C minus 20 times the identity, and you get 6, 18, 18 and 54.

**4:50** · To find the eigenvector with eigenvalue 20, we need to find a vector in the null space of this matrix.

**4:58** · Note that the second column is three times the first column, so our first vector, v\_1, we can just take that to be, well, we could take it to be \[-3, 1\], but we'd like it to be a unit vector, right?

**5:21** · Remember the columns of v should be unit vectors because they're orthonormal.

**5:25** · So 3 squared plus 1 squared is 10, we have to divide by the square root of 10.

**5:34** · OK, similarly, we do C transpose C minus 80 times the identity, we'll get -54, 18; 18, and -6, and similarly we can find that v\_2 will be 1 over square root of 10, 3 over the square root of 10.

**6:08** · Great, OK, so what information do we have now?

### Assembling V and Sigma

**6:11** · we have our V matrix, which is just made up of these two columns, and we actually have our sigma matrix too, because the squares of the diagonal entries of sigma are 20 and 80.

**6:26** · Good, so let's write those down, write down what we have.

**6:33** · So we have V-- I just add these vectors and make them the columns of my matrix.

**6:43** · Square root of 10, 1 over square root of 10; 1 over square root of 10, 3 over square root of 10.

**6:55** · And sigma, this is just the square roots of 20 and 80, which is just 2 root 5 and 4 root 5 along the diagonal.

**7:11** · Squeezing it in here, I hope you all can see these two.

**7:17** · Good, so these are two of the three parts of my singular value decomposition.

### Finding the U matrix

**7:24** · The last thing I need to find is u, and for that I need to use this second equation right here.

**7:31** · So you need to multiply C times V, okay so So c is \[5, 5; -1, 7\], let's multiply it by V, 1 over root 10, 3 over square root of 10.

**7:54** · What do we get?

**7:56** · Well, I'll let you work out the details, but it's not hard here.

**8:05** · You get -10 over root 10, which is just negative square root of 10 here.

**8:12** · Then I just get 2 square root of 10, and then I get--

**8:32** · 1 is 2 square root of 10 and-- I think I made an error here.

**8:49** · Give me a second to look through my computation again.

**8:55** · AUDIENCE: \[INAUDIBLE\] PROFESSOR: The (2, 1) entry should be-- oh, yes, thank you.

**9:03** · The (2, 1) entry should be the square root of 10.

**9:05** · Good, yes, that's what I was hoping, yes, because we get-- Yes, I did it in the wrong order, right, so your recitation instructor should know how to multiply matrices, great, yes, thank you.

**9:33** · You multiply this first, then this, then this, and then this, and if you do it correctly you will get this matrix here.

**9:44** · Good, great.

**9:45** · So now I'd like this to be my U matrix, but it's actually U times sigma, so I need to make these entries unit length.

**9:57** · OK, so I get -1 over root 2, 1 over root 2, 1 over root 2, 1 over root 2, times my sigma matrix here, which is, remember, 2 square root of 5, 4 square root of 5, and these constants are just what I needed to divide these columns by in order to make them unit vectors.

**10:27** · So now, here's my U matrix, 1 over square root of 2, -1 over square root of 2; 1 over square root of 2, 1 over square root of 2, good.

**10:41** · So now I have all three matrices, U, V, and sigma and despite some little errors here and there, I think this is actually right.

### Final review and summary

**10:51** · You should go check it yourself, because if you're at all like me, you've screwed up several times by now.

**10:59** · But anyway, this is a good illustration of how to find the singular value decomposition.

**11:05** · Recall that you're looking for U sigma V transpose where u and v are orthogonal matrices, and sigma is diagonal with non-negative entries.

**11:16** · And you find it using these two equations, you compute C transpose C, that's V sigma transpose sigma times V transpose, and you also have C\*V is U\*sigma.

**11:32** · I hope this was a helpful illustration.