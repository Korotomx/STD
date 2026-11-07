![](https://www.youtube.com/watch?v=KUuxdk_V7To)

MIT 18.06SC Linear Algebra, Fall 2011  
View the complete course: https://ocw.mit.edu/18-06SCF11  
Instructor: Ben Harris  
  
A teaching assistant works through a problem on similar matrices.  
  
License: Creative Commons BY-NC-SA  
More information at https://ocw.mit.edu/terms  
More courses at https://ocw.mit.edu

## Transcript

**0:05** · BEN HARRIS: Hi.

**0:07** · Today we're going to do a problem about similar matrices.

**0:10** · The problem is right here.

**0:12** · So the question asks, which of the following statements are true, and it asks you to explain why.

**0:19** · The first statement is: if A and B are similar matrices, then 2 A cubed plus A minus 3 times the identity is similar to 2 times B cubed plus B minus 3 times the identity.

**0:34** · The second question asks: if A and B are 3 by 3 matrices with eigenvalues 1, 0, and -1, then they're similar.

**0:43** · And the third part asks you whether these two J matrices are similar.

**0:50** · OK.

**0:51** · I'll give you a moment to hit pause and try it on your own.

**0:55** · I'll be back in just a moment, and we can do it together.

**1:09** · And we're back.

**1:15** · Let's start with part A. Part A is true.

**1:25** · Why?

**1:26** · Well, what does it mean for A and B to be similar?

**1:31** · Right, we know there's some matrix M, such that-- that's what "st" means-- when I multiply A on the left by M and the right by M inverse, I get B.

**1:48** · OK.

**1:49** · So let's take that same matrix M and multiply it on the left and the right of 2 A cubed plus A minus 3 times the identity.

**2:05** · OK.

**2:06** · What do we get here?

**2:08** · Well, the point is what M times A cubed times M inverse, we can just write that as three M A M inverses.

**2:24** · Similarly, we have an M\*A M inverse and an M times the identity times M inverse.

**2:35** · Good.

**2:38** · Remember that M times A times M inverse is B.

**2:41** · So we just get 2 B cubed-- three B's-- plus B minus-- well, M times the identity is just M. So we just get the identity back, and we have 3 times the identity.

**2:57** · Good.

**2:58** · And this is a general remark, that if you have matrices A and B that are similar, then any polynomials in these matrices A and B will be similar.

**3:09** · It's the exact same justification.

**3:13** · OK.

**3:15** · Now let's go on to part B. So now A and B are 3 by 3 similar matrices with the same eigenvalues.

**3:24** · And their eigenvalues are distinct.

**3:28** · So it turns out that b is true as well.

**3:35** · And why is that?

**3:38** · A matrix with distinct eigenvalues is diagonalizable.

**3:43** · So we can write A as S lambda S inverse, where lambda is just this eigenvalue matrix.

**4:00** · We can also write B as T lambda T inverse, where lambda is the same in both cases because they have the same eigenvalues.

**4:12** · Good.

**4:13** · Now I'll let you-- so before we check it, let's just say the point.

**4:20** · The point is if two matrices are similar to the same matrix, then they're similar to each other.

**4:26** · Similarity is a transitive relation.

**4:30** · And I'll just let you check that you can take T S inverse A times T S inverse inverse, and you'll get B. This follows directly from these two relations.

**4:52** · Good.

**4:53** · Now let's take on part C. Part C is false.

**5:01** · Let's come back over here and look at these two matrices, J\_1 and J\_2.

**5:06** · The first thing you should see is that these two are Jordan blocks-- sorry, not Jordan blocks, they're matrices in Jordan normal form.

**5:17** · They're different matrices in Jordan normal form, so they will not be similar.

**5:23** · But let's actually see why.

**5:27** · Let's look at-- remember, one of the things that similarity preserves are eigenvectors and eigenvalues.

**5:34** · So let's look at the eigenspace with eigenvalue minus one with these two matrices.

**5:41** · So J\_1 plus the identity-- let's look at the nullspace of this matrix.

**5:50** · So this is just 0's on the diagonal and 1's right above the diagonal.

**6:01** · And J\_2 plus the identity.

**6:05** · this is just 0, 1, 0, 0.

**6:12** · So the point is that the nullspace of this matrix is just one-dimensional.

**6:22** · So there's only one independent eigenvector of J\_1 with eigenvalue minus 1.

**6:27** · Whereas the nullspace of this matrix is two-dimensional.

**6:36** · There are two independent eigenvectors with eigenvalue minus 1.

**6:41** · So the dimension-- the nullspace of J\_1 plus the identity, this is 1, and this is 2.

**6:54** · So they cannot possibly be similar.

**7:02** · Good.

**7:03** · So that completes the problem.

**7:04** · It's a nice exercise to do this more generally.

**7:08** · And you can use these techniques not just looking at the number of independent eigenvectors and the nullspace of your J minus lambda\*I matrix, but also powers of J minus lambda I and their nullspaces.

**7:24** · You can use this to show that any two matrices in Jordan normal form that are different are not similar.

**7:33** · This same method works.

**7:34** · And that's a nice exercise if you want to go a little further with similar matrices.

**7:41** · Let's just recap the properties we saw here.

**7:45** · We saw that if we had two similar matrices, then any polynomials in those matrices were similar.

**7:51** · And we saw that if we have two matrices that have the same distinct eigenvalues, then they're similar.

**8:02** · And we saw that, in a special case, we saw that two matrices in Jordan normal form that are different are not similar.

**8:10** · Thanks.