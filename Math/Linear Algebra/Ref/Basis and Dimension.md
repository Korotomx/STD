![](https://www.youtube.com/watch?v=MMWqGD4Urso)

MIT 18.06SC Linear Algebra, Fall 2011  
View the complete course: https://ocw.mit.edu/18-06SCF11  
Instructor: Ana Rita Pires  
  
A teaching assistant works through a problem on basis and dimension.  
  
License: Creative Commons BY-NC-SA  
More information at https://ocw.mit.edu/terms  
More courses at https://ocw.mit.edu

## Transcript

**0:07** · PROFESSOR: Hi there.

**0:07** · Welcome back to recitation.

**0:09** · In lecture, you've been learning about when vectors are linearly independent, when they span the space, what a basis is, what a dimension of a vector space is.

**0:19** · And the problem for today is exactly about that.

**0:23** · We have a vector space that is given.

**0:26** · It's spanned by these four vectors.

**0:28** · And we're asked to find the dimension of that vector space and the basis for it.

**0:35** · Well, why don't you hit pause on the video, and work on it for a while.

**0:39** · And I'll come back in a little bit to help you out with it.

**0:51** · We're back.

**0:51** · Let's work on it.

**0:54** · So we need to find the dimension and the basis.

**1:00** · Remember what the dimension is?

**1:01** · It's simply the number of vectors in a basis for the vector space.

**1:05** · So actually, the problem is backwards.

**1:07** · We want to find the basis for the space first, and then find the dimension.

**1:11** · I'll write "first" here and "second" here.

### Basis for the Vector Space

**1:19** · So we want to find a basis for the vector space spanned by these four vectors.

**1:24** · So you might be tempted to just say that a basis for this vector space is those four vectors, because they span the vector space.

**1:31** · But there's another thing that a basis has to satisfy.

**1:34** · And it is the elements of the basis have to be linearly independent.

**1:38** · We don't know that these are.

**1:40** · So we have to check.

**1:42** · How do we check that four vectors are linearly independent?

**1:45** · Well, there's a couple of different ways.

**1:47** · But here's what we're going to do.

**1:50** · We're going to put these vectors as rows of a matrix.

**1:54** · And then we'll do elimination.

**1:57** · And when we get to the end, the rows that have pivots are the independent ones.

**2:02** · So let's do that.

**2:06** · 1, 1, -2, 0, -1; 1, 2, 0, -4, 1; 0, 1, 3, -3, 2; 2, 3, 0, -2, 0.

**2:30** · By now you must have done elimination a million times, so I'll go a little bit faster.

**2:36** · 1, 1, -2, 0, -1; 0, 1, 0, +2, -4, 2-- this one's already done-- 1, 3, -3, 2; 2 minus 2, 3 minus 2, 0 plus 4, -2, and 2.

**3:05** · One more step.

**3:08** · 1, 1, -2, 0, -1-- all these are done-- 0, 1, 2, -4, 2; 0, 1 minus 1 is 0, 3 minus 2 is 1, -3 plus 4 is 1, 2 minus 2 is 0, 1 minus 1 is 0, 2, 2 again, and 0.

**3:37** · Well, you can see where this is going.

**3:39** · In the next step, this row is going to disappear.

**3:44** · 1, 1, -2, 0 -1; 0, 1, 2, -4, 2; 0, 0, 1, 1, 0; 0, 0, 0, 0, 0.

**3:59** · All right.

**3:59** · We're done with elimination.

**4:03** · So let's circle our pivots.

**4:08** · All right, here are our pivots.

**4:10** · We have three pivots.

**4:14** · And so these three rows are linearly independent.

**4:19** · And in fact, these rows still span the same space that the initial four rows did.

**4:25** · Because when you do elimination, all that you're doing is recombining your rows by doing linear combinations of them.

**4:32** · So, for example, your first row stayed the same throughout.

**4:36** · Your second row was replaced by row 2 minus row 1.

**4:41** · But it's really still spanning the same space.

**4:45** · And it goes on.

**4:46** · And then the fourth row, it turns out, was useless.

**4:48** · You only needed the first three.

### The Elements for a Basis

**4:50** · So the elements for a basis-- well, it will be these three.

**4:57** · So let me write that.

**5:01** · Basis \[1, 1, -2, 0, -1\], 2, 2, and \[0, 0, 1, 1, 0\].

**5:18** · Could you have used the first three rows?

**5:22** · Yes, you could.

**5:24** · You can't always do that.

**5:25** · Sometimes in elimination, you have to switch rows, because there's a 0 where a pivot should be.

**5:30** · When that happens, you have to use these three, or you have to keep track of which row you switched to go back and use the initial ones.

**5:39** · But it's really safe to use these ones.

**5:41** · And also they're simpler than the ones that you started with, so why not?

**5:45** · The other question that we had was: what is the dimension of the vector space?

### What Is the Dimension of the Vector Space

**5:49** · Well, this is the easy part.

**5:52** · The dimension of the vector space is 1, 2, 3.

**5:58** · And that solves the problem.

**5:59** · But there's one more thing that I want to tell you.

**6:03** · I told you that there's a couple of ways to find out which of those four vectors are linearly independent.

**6:10** · And the one that I used was I put them into rows and performed elimination and picked out the rows that have pivots on them.

**6:19** · Another way to do it is to write the initial vectors as columns of the matrix and then perform elimination.

**6:26** · That also works and, as you know, because you're only working with the transpose of this matrix, you get the same number of pivots.

**6:34** · Let's go over here where I have the same-- well, the transpose of that matrix-- I have the same vectors, but now written as columns.

**6:44** · My four initial vectors written as columns.

**6:46** · And here I have performed elimination.

**6:49** · And this is the final result. Let me circle the pivots again.

**6:55** · Here they are, three, which is going to give me three linearly independent vectors and hence, three elements of the basis, and hence, dimension 3 for the vector space.

**7:06** · But I could no longer use these three columns as elements of the basis, because when I did elimination, I changed the column space.

**7:17** · So the column space of this matrix is not the same as the column space of the eliminated version.

**7:24** · So I cannot use these.

**7:27** · In fact, if you look at them, you can probably understand that they're not going to span the same space as these.

**7:34** · Because all that I have down here are 0's, and I get a lot more than just 0's in the last two entries of the vectors.

**7:41** · So what I need to do is-- the pivots are in the first, second, and third columns.

**7:48** · I need to use these three columns as my basis.

**7:53** · I'll just write basis down here.

**7:57** · And that will work too.

**7:58** · So see, I have produced two different bases for the same vector space, which is totally fine.

**8:04** · You can pick the basis that you prefer.

**8:06** · All right.

**8:07** · We're done.

**8:08** · Thank you.