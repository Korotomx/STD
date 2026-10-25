![](https://www.youtube.com/watch?v=BaBoztM9Q1w)

MIT 18.06SC Linear Algebra, Fall 2011  
View the complete course: https://ocw.mit.edu/18-06SCF11  
Instructor: Ana Rita Pires  
  
A teaching assistant works through a problem on matrix spaces.  
  
License: Creative Commons BY-NC-SA  
More information at https://ocw.mit.edu/terms  
More courses at https://ocw.mit.edu

## Transcript

### Introduction to problem

**0:05** · ANA RITA PIRES: Hi there.

**0:06** · Welcome to recitation.

**0:08** · In lecture, you've been learning about vector spaces whose vectors are actually matrices or functions, and this is what our problem today is about.

**0:17** · We have a set of 2 by 3 matrices whose null space contains the vector \[2, 1, 1\].

**0:24** · And I want you to show that this set is actually a vector subspace of the space of all 2 by 3 matrices.

**0:32** · And then, I want you to find a basis for it.

**0:36** · When you're done, here is an additional question.

**0:39** · What about the set of those 2 by 3 matrices whose column space contains the vector \[2, 1\]?

**0:47** · All right.

**0:48** · Hit pause and work on it yourself, and when you're ready, I'll come back and show you how I did it.

### Proving a vector subspace

**1:01** · Hi.

**1:01** · I hope you managed to solve it.

**1:05** · Let's do it.

**1:07** · So, how do we show that something is a vector subspace?

**1:11** · Well, there are only two things that we need to check.

**1:13** · One is that if two vectors, in this case two matrices, are in that space, then their sum is in that space.

**1:21** · And if you take a vector, in this case a matrix, and you multiply by a scalar you'll still be in the space.

**1:28** · So, suppose that the matrices A and B are in this set that we want to prove is a subspace.

**1:39** · So that means that A times the vector \[2, 1, 1\] is equal to the vector \[0, 0\].

**1:48** · Notice that the dimensions are right: A is 2 by 3, so this 3 by 1.

**1:53** · I should get a 2 by 1.

**1:55** · Suppose that \[2, 1, 1\] is in the null space of A, and that \[2, 1, 1\] is also in the null space of B. Then what is A plus B times \[2, 1, 1\]?

**2:15** · Is \[2, 1, 1\] in the null space of A plus B?

**2:18** · Well, if you think about what this means, you're just adding entry by entry.

**2:23** · And you can do it slowly on your own and just check that this is what happens.

**2:35** · But by now you are familiar enough with matrices that this should not be a surprise.

**2:40** · Well, this is \[0, 0\], and this is \[0, 0\], so their sum is \[0, 0\].

**2:46** · So, indeed, \[2, 1, 1\] is in the null space of A plus B.

**2:50** · So if A and B are in the set, A plus B is in the set, as well.

**2:56** · Let's check the other thing.

**2:58** · The other thing is A times \[2, 1, 1\] is \[0, 0\].

**3:03** · So A is in the set, because \[2, 1, 1\] is in the null space of A. And also, let's let c be a scalar.

**3:13** · That just means that c is a number.

**3:16** · Then we want to check that \[2, 1, 1\] is in the null space of the matrix c\*A.

**3:24** · That matrix is just the matrix A except every entry is multiplied by the number c.

**3:30** · Well, again, this is how matrices work.

**3:35** · You can just pull out the constant and do A times \[2, 1, 1\] first.

**3:40** · Now this is the vector \[0, 0\].

**3:43** · So, this will simply be c times \[0, 0\], which is \[0, 0\].

**3:48** · So the matrix c\*A is also contained in this set.

**3:53** · So the set is closed under addition and under multiplication by scalar, so the set is, indeed, a vector subspace.

**4:01** · Well that takes care of the first part of the question.

### Finding a basis

**4:05** · The second part was: find a basis for the subspace.

**4:08** · So let's work on that now.

**4:12** · So the condition for a matrix to be in this subspace is that the vector \[2, 1, 1\] is in the null space.

**4:20** · So I must have A times \[2, 1, 1\] is equal to \[0, 0\].

**4:27** · So what is happening?

**4:28** · Well A is a 2 by 3 matrix.

**4:31** · So you can actually think about what happens in each row separately.

**4:35** · You'll have the first row of A times \[2, 1, 1\] is equal to 0.

**4:40** · And the second row of A times \[2, 1, 1\] is equal to 0.

**4:44** · So let's see what that means.

**4:49** · Each row of the matrix A in this vector subspace must be \[a, b, c\] \[2; 1; 1\] equal to 0.

**5:06** · This is not really a good sentence, but you understand.

**5:10** · Which means that-- well let's see-- 2a plus b plus c is equal to 0.

**5:19** · So I can actually write it in this format.

**5:25** · It must be of the form a, b, and then c must be equal to -2a minus b.

**5:42** · Right?

**5:43** · So, furthermore, we can say that it-- well, one thing that you can do-- let me write this here to help you.

**5:54** · It will be \[a, 0, -2a\] plus \[0, b, -bl.

**6:02** · See?

**6:03** · So what I'm doing is I'm splitting this into the linear combination of two vectors.

**6:09** · I can pull out the a out of this one, and pull the b out of this one, and it must be a linear combination-- that's what this means, linear combination-- of the following: \[1, 0, -2\] and \[0, 1, -1\].

**6:31** · Does that make sense?

**6:33** · So this is what each row of a must satisfy.

**6:36** · So we can now put everything together into what a basis for the vector space has to be.

**6:43** · The basis will be, well it's 2 by 3 matrix, and each row must be a linear combination of these two vectors.

**6:54** · So let's write that-- 1, 0, -2.

**6:59** · I'll keep the second row with zeros-- 0, 1, -1, and I'll keep the second row of zeros.

**7:06** · And now the same, but keeping the first row with zeros, I'm taking these vectors on the second row.

**7:19** · So this is a basis for my vector space.

**7:23** · One, two, three, four; that also means that the dimension of the subspace is 4.

### Analyzing column space

**7:30** · There was one further question, which was what can you say about the set of those matrices that contain the vector \[2, 1\] in their column space?

**7:44** · What about the set of those 2 by 3 matrices whose column space contains the vector \[2, 1\].

**7:50** · Is that a vector subspace?

**7:54** · Well one quick check that you can always do is check that the zero vector, in this case the zero matrix, belongs to the set.

**8:05** · Does the zero 2 by 3 matrix-- \[0, 0, 0; 0, 0, 0\].

**8:13** · Does this matrix belong to this set?

**8:15** · Does this matrix contain the vector \[2, 1\] in its column space?

**8:20** · It does not, so this set cannot be a vector subspace.

**8:25** · If you want to think about how this 0 belonging in the set has anything to do with the two conditions being closed under sum and closed under multiplication by scalar, simply think that you should always be able to multiply a matrix by the scalar 0 and have it still be in the set.

**8:44** · That will be your zero matrix.

**8:46** · Well the zero matrix is not in the set, so the set is not a vector subspace.

**8:51** · All right?

**8:52** · We're done.

**8:53** · Thank you.