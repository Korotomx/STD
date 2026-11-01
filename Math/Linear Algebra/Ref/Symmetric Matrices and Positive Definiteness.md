![](https://www.youtube.com/watch?v=lpnY5QVjU5w)

MIT 18.06SC Linear Algebra, Fall 2011  
View the complete course: https://ocw.mit.edu/18-06SCF11  
Instructor: David Shirokoff  
  
A teaching assistant works through a problem on symmetric matrices and positive definiteness.  
  
License: Creative Commons BY-NC-SA  
More information at https://ocw.mit.edu/terms  
More courses at https://ocw.mit.edu

## Transcript

### Introduction to tasks

**0:08** · PROFESSOR: Hi, everyone.

**0:09** · Welcome back.

**0:10** · So today, I'd like to talk about positive definite matrices.

**0:14** · And specifically, we're going to analyze several properties of positive definite matrices.

**0:19** · And specifically, we're going to look at why each one of these following statements is true.

**0:24** · So first off, why every positive definite matrix is invertible.

**0:29** · Why the only positive definite projection matrix is the identity matrix.

**0:34** · If D is a diagonal matrix with positive entries, show that it must also be positive definite.

**0:41** · And then lastly, if S is a symmetric matrix where the determinant S is bigger than 0, show why this might not necessarily imply that it's positive definite.

**0:50** · So I'll let you think about these for a moment.

**0:53** · And I'll come back in a second.

### Positive definite invertibility

**1:08** · Hi, everyone.

**1:09** · Welcome back.

**1:10** · OK.

**1:11** · So let's take a look at part A. So part A is asking why every positive definite matrix is invertible.

**1:21** · Well, let's just recall that if A is a matrix and if A is invertible, then this necessarily implies that the determinant of A is non-zero.

**1:40** · And I'm going to just write out det A as the product of the eigenvalues of A. So lambda\_1 to lambda\_n are the eigenvalues of A.

**2:06** · OK.

**2:07** · In addition, if A is positive definite, what does this say about the eigenvalues of A?

**2:21** · Well, it says that each eigenvalue of A, lambda\_1, lambda\_2, dot, dot, dot, to lambda\_n, each one of them must be bigger than 0.

**2:33** · So this statement that each eigenvalue of A is bigger than 0 is completely equivalent to A being positive definite for symmetric matrices A.

**2:46** · So if I have a whole bunch of eigenvalues and each of them are bigger than 0, what does this say about det A?

**2:56** · Well, I can take the product of all these eigenvalues.

**3:03** · And of course, the product of a whole bunch of positive numbers must also be positive.

**3:10** · So if the quantity is positive, then it certainly cannot equal 0.

**3:15** · So this proves that det A is not equal to 0.

**3:18** · Hence, A must be invertible.

### Projection matrix properties

**3:22** · OK.

**3:23** · So for part B, we're asked to show that the only positive definite projection matrix is the identity matrix.

**3:35** · So again, how do we tackle this problem?

**3:37** · We're going to look at the eigenvalues.

**3:39** · So remember, if P is a projection, what does it say about the eigenvalues of P?

**3:52** · Well, it says that the eigenvalues of P are either 0 or 1.

**4:09** · So this is point one.

**4:11** · Point two, if P is a positive definite, what does that say about the eigenvalues of P?

**4:27** · Well, as I've noted before, it means that the eigenvalues are bigger than 0.

**4:47** · So if P is a projection and it's positive definite, the only possible eigenvalues that are both 0 and 1 and bigger than 0 are 1.

**4:59** · So the conclusion is that the eigenvalues of P must all equal 1.

**5:12** · So which matrix has eigenvalues 1 and is also symmetric?

**5:17** · Well, the only matrix that satisfies this property is the identity matrix.

**5:28** · Now you might ask, how do you actually show that?

**5:31** · Well, you could argue as follows.

**5:35** · If P is diagonalizable-- and every symmetric matrix is diagonalizable, so I'm not making this up.

**5:50** · So if P is diagonalizable, then you can always write P as some matrix, U, times a diagonal matrix-- and we know in this case, the diagonal matrix has eigenvalues 1, so it's actually the identity matrix-- times the inverse of the eigenvector matrix.

**6:12** · But of course, this is just U times U inverse, which then gives me the identity at the end.

**6:21** · So U times the identity times U inverse.

**6:23** · This is just U times U inverse.

**6:25** · And of course, U and U inverse collapse back down to the identity.

**6:29** · So this shows you that the only matrix that has eigenvalues of 1 is the identity matrix.

**6:35** · So that's just to cross all the T's and dot all the I's.

### Diagonal matrix positivity

**6:39** · OK.

**6:40** · For part C, we're given D as a diagonal matrix with positive entries on the diagonal.

**6:47** · Now we have to show that it's positive definite.

**6:50** · OK.

**6:50** · So let me write D as follows.

**6:53** · I'll just write it like this.

**6:54** · I'm going to use a compact notation, which is sometimes seen: diagonal d\_1, d\_2, d\_n.

**7:05** · So D is a diagonal matrix whose elements along the diagonal are d\_1, d\_2, dot, dot, dot, to d\_n.

**7:13** · Now what does it mean for a matrix to be positive definite?

**7:16** · Well, it means that for any x, for any vector x, I have to look at the product x transpose D\*x.

**7:34** · And I have to show that it's bigger than 0.

**7:38** · And I should qualify this and say that the vector we're looking at is x not equal to 0.

**7:43** · So we're now looking at the zero vector.

**7:46** · But for D to be positive definite, we have to show that x transpose D\*x is bigger than 0.

**7:51** · This is just one way to show that it's positive definite.

**7:53** · It's not the only way.

**8:00** · So if I write x out using components, x\_1, x\_2, dot, dot, dot, to x\_n-- I'll write it like this-- then you can work out the quantity x transpose D\*x.

**8:19** · And we see that we get a sum of squares.

**8:21** · We get d\_1 times x\_1 squared plus d\_2 x\_2 squared plus dot, dot, dot plus d\_n x\_n squared.

**8:36** · Now by definition, each coefficient is positive.

**8:41** · A sum of a square is positive.

**8:44** · so-- sorry.

**8:45** · A product of a positive number with a square is positive.

**8:49** · And then of course, a sum of positive numbers is going to be positive.

**8:54** · So this means the whole thing is positive.

**8:57** · Now there's other more efficient ways of getting at this using other tricks we know.

**9:01** · For example, if we're given a diagonal matrix, we know its eigenvalues are already d\_1, d\_2, dot, dot, dot, to d\_n.

**9:09** · And we know that a matrix with positive eigenvalues is already positive definite.

**9:16** · But this is kind of starting from the base to show that it's positive definite.

**9:23** · And now lastly, let's look at part D.

### Symmetric matrix counterexample

**9:27** · So S is a symmetric matrix with det S bigger than 0.

**9:32** · Show that S might not necessarily be positive definite.

**9:36** · So there's lots of counterexamples.

**9:38** · I only need to construct one.

**9:42** · So I'm looking at S, which is a symmetric matrix.

**9:44** · So I'm just going to throw in some numbers on some off diagonals.

**9:47** · So I'll just pick one.

**9:50** · And now I need to pick some numbers along the diagonal.

**9:55** · And the easiest way to do it is just to pick two negative numbers on the diagonal.

**9:59** · Because if there's a negative number on a diagonal, then we know S can't be positive definite.

**10:06** · And I'll say more about that in a second.

**10:12** · So I can just pick negative 2 and negative 3.

**10:14** · So let's quickly check what det S is.

**10:21** · Well, it's negative 2 times negative 3 minus 1.

**10:25** · So this gives me 6 minus 1, which is 5.

**10:29** · So by construction, det S is positive, which is good.

**10:33** · And then, as I mentioned before, if there's negative elements along the diagonal of the matrix, that matrix can't be positive definite.

**10:41** · Well, why is that?

**10:43** · Well, suppose I wanted to take a look at this upper left component, negative 3, and it's negative, how do I show that that implies S is not positive definite?

**10:58** · Well, what I can do is I can look at the product x transpose S\*x.

**11:06** · And what I do is I look at it.

**11:08** · I just take one value of x.

**11:12** · So we know that this has to be positive for every value of x.

**11:15** · So I can pick any value I want.

**11:17** · So I can take x, say, \[1, 0\] transpose.

**11:25** · And when I do this, we end up getting that x transpose S\*x is equal to negative 3.

**11:37** · So notice how by taking 1 in the first entry and 0 on the second entry, that picks out the upper left corner, negative 3.

**11:44** · If I were to take 0 here and 1 here, it would pick out the negative 2 entry in S.

**11:52** · So by picking 1 in entry i of a vector x, and then computing this product x transpose S\*x, I pick out the i-th element along the diagonal.

**12:05** · And since that element is negative, this shows me that along the direction \[1, 0\], the product x transpose S\*x is also negative.

**12:15** · And hence, S can't possibly be positive definite.

**12:19** · OK.

**12:19** · So just to summarize, we've taken a look at a couple matrices and a couple different properties of positive definite matrices.

**12:27** · And notably, we've used the eigenvalues to get a handle of the positive definite matrices.

**12:33** · And I hope these provide some useful tricks.

**12:36** · And I'll see you next time.