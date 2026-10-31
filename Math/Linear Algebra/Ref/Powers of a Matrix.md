![](https://www.youtube.com/watch?v=5IGTFgPqlkw)

MIT 18.06SC Linear Algebra, Fall 2011  
View the complete course: https://ocw.mit.edu/18-06SCF11  
Instructor: Ben Harris  
  
A teaching assistant worksthrough a problem on powers of a matrix.  
  
License: Creative Commons BY-NC-SA  
More information at https://ocw.mit.edu/terms  
More courses at https://ocw.mit.edu

## Transcript

### Problem introduction

**0:08** · PROFESSOR: Hi, and welcome.

**0:10** · Today, we're going to do a problem about powers of a matrix.

**0:15** · Our problem is first to find a formula for the k-th power of this matrix C. This is a two by two matrix that depends on variables a and b.

**0:27** · And the second part of our problem is to calculate C to the 100th in the special case where a and b are -1.

**0:38** · You can hit pause now, and I'll give you a minute to do the problem yourself.

**0:42** · And then, I'll come back and we can do it together.

### Finding eigenvalues

**0:57** · OK.

**0:58** · We're back.

**1:00** · Now, what's the first step in finding powers of a matrix?

**1:05** · Well, we need to find the eigenvalues and eigenvectors of this matrix.

**1:10** · So how do we do that?

**1:13** · We compute the determinant of C minus lambda I, which is just the determinant of this matrix: 2b minus a minus lambda, 2b minus 2a; a minus b, and 2a minus b minus lambda.

**1:47** · OK.

**1:48** · If you compute this, well, we have a lambda squared term.

**1:54** · OK.

**1:56** · Our lambda term, if you look at it, you'll see we get 2b minus a plus 2a minus b, which is just a plus b.

**2:08** · And we have a negative sign.

**2:10** · And it's negative a plus b times lambda.

**2:15** · And our last term is a little tougher to compute.

**2:18** · So I'll let you do it yourself.

**2:21** · But you're just going to get plus a\*b.

**2:25** · And this will factor as lambda minus a times lambda minus b.

### Finding eigenvectors

**2:32** · So our eigenvalues are just a and b.

**2:38** · Now we need to find our eigenvectors.

**2:41** · So how do we do that?

**2:43** · Well, what we need to do is we need to look at C minus a times the identity.

**2:51** · And we need to find the null space of this matrix.

**2:54** · So what do we get here?

**2:58** · We get 2b minus 2a.

**3:07** · And then our next entry here, we get 2a minus b minus a.

**3:13** · So this is a minus b.

**3:15** · Good.

**3:16** · So you can see that this matrix has the same columns and the same rows.

**3:30** · And so you can see that a vector in the null space, since this column is -2 times this column, we can see that our first eigenvector is just-- or 1, 2, I should say.

**3:51** · It's just \[1, 2\].

**3:54** · Good.

**3:58** · Well, I guess we have space to do the second one too.

**4:02** · Why not?

**4:04** · So let's write out the second one also.

**4:08** · Here, we're subtracting b instead of a.

**4:11** · You get b minus a.

**4:14** · You get 2b minus 2a.

**4:17** · We get a minus b.

**4:20** · And what do we have here?

**4:22** · We have 2a minus 2b.

**4:28** · So now, what's in the null space of this matrix?

**4:33** · Well, what you can see is that this column is -1 times that column.

**4:43** · So our second eigenvector is just going to be \[1, 1\].

**4:50** · And I should remind you that if you have a harder example, you can just find these null spaces by elimination like we always do.

**4:59** · Great.

**5:00** · Now we have our eigenvalues and our eigenvectors.

### Matrix diagonalization

**5:02** · So now we can write C in a nice easy way that allows us to take powers of it.

**5:09** · So what's that way?

**5:11** · So that's C equals S lambda S inverse.

**5:21** · So this is just, what is S?

**5:24** · Remember, S is our matrix of eigenvectors.

**5:29** · So S is the matrix 1, 2; 1, 1.

**5:36** · Good.

**5:37** · Now what is lambda?

**5:39** · Lambda is the matrix of eigenvalues.

**5:40** · Right?

**5:41** · So it's just a and b.

**5:44** · Those are the diagonal entries of my lambda matrix.

**5:49** · And then, we just find S inverse.

**5:53** · So we just take negative signs here and recall that we have to divide by the determinant.

**6:05** · And the determinant of this matrix is just -1.

**6:10** · So we just change the signs there.

**6:13** · Good.

**6:13** · So this is our nice decomposition of C.

**6:18** · Now how do we take powers of C?

**6:20** · Well, C to the k is just S lambda to the k S inverse.

**6:28** · \[1, 1; 2, 1\]; a to the k, b to the k; \[-1, 1; 2, -1\].

**6:39** · Good.

**6:40** · And multiplying these matrices together, just do a little arithmetic here.

**6:54** · Got a bunch of powers of a and b.

**6:56** · Because we take powers of the eigenvalues.

**7:02** · We have here, we have 2 b to the k minus a to the k.

**7:09** · Have a to the k minus b to the k.

**7:15** · 2 b to the k minus 2 a to the k.

**7:20** · And finally, we get 2 a to the k minus b to the k.

**7:27** · And this is our k-th power matrix.

**7:33** · Good.

### Verification of formula

**7:36** · A quick check.

**7:37** · It's always good to check your work here.

**7:39** · Let's plug in k equals 1.

**7:42** · And what do we get?

**7:43** · We get 2b minus a, a minus b, 2b minus 2a, and 2a minus b.

**7:51** · And if we can go all the way back to our matrix at the very beginning, all the way back here, that agrees perfectly with what we started with.

**8:00** · So that's good.

**8:02** · That means that we did this decomposition right.

**8:05** · Good.

**8:05** · So now, we've computed the k-th power of this matrix.

**8:09** · Let's do a particular example.

### Calculating a specific case

**8:13** · So let's plug in a and b are -1.

**8:18** · So a equals b equals -1.

**8:22** · And k equals 100.

**8:25** · Then what do we get?

**8:27** · Well, -1 to the 100th is just 1.

**8:31** · So we're just plugging in 1 for b to the k and a to the k everywhere.

**8:35** · And we just get, in this case, C to the 100th is just \[1, 0; 0, 1\].

**8:45** · It's just the identity matrix.

**8:49** · Great.

**8:51** · Great.

### Summary of technique

**8:52** · OK.

**8:52** · Now to summarize, how do we take powers of a matrix?

**8:57** · Well, first we diagonalize.

**8:59** · We write our matrix as S lambda S inverse.

**9:02** · And then, we just take powers of the diagonal matrix.