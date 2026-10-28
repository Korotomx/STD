![](https://www.youtube.com/watch?v=55AoWKZZtww)

MIT 18.06SC Linear Algebra, Fall 2011  
View the complete course: https://ocw.mit.edu/18-06SCF11  
Instructor: Ana Rita Pires  
  
A teaching assistant works through a problem on properties of determinants.  
  
License: Creative Commons BY-NC-SA  
More information at https://ocw.mit.edu/terms  
More courses at https://ocw.mit.edu

## Transcript

### Introduction

**0:06** · ANA RITA PIRES: Hi.

**0:07** · Welcome back to recitation.

**0:09** · In lecture, you've been learning about the properties of determinants.

**0:12** · To remember, there were three main properties, and then seven more that fall out of those three.

**0:17** · I'll tell you what these three were.

**0:19** · The first one was the determinant of the identity matrix is always equal to 1.

**0:23** · If you switch two rows in a matrix, the determinant switches sign.

**0:27** · And the determinant is a function of each-- it's a linear function of each row separately.

**0:34** · And there's seven more.

**0:36** · We'll use them here.

**0:38** · Today's problem is about finding the determinants of matrices by using these properties.

**0:43** · So here you have four matrices.

**0:46** · A has lots of 100's, 200's, and 300's numbers.

**0:50** · B is called a Vandermonde matrix.

**0:54** · It has a very nice structure with 1's, and then a, b, c; a squared, b squared, c squared.

**0:59** · It can be bigger, and you'll just have cubes and more letters down here.

**1:04** · C is given by the product of these two, and D is this matrix.

**1:11** · Good luck.

**1:12** · Hit pause, work on them, and when you're ready, come back and I'll show you how I did it.

**1:25** · Did you get some?

**1:26** · OK, let's do it.

**1:28** · Starting with matrix A. I have lots of big numbers.

**1:41** · I suggest that we do a little bit of elimination, because as you know, doing elimination steps, except for permuting rows, doesn't change the determinant of the matrix.

**1:52** · So let's do determinant of A is equal to-- 101, 201, 301.

**2:04** · Then if I subtract off the first row from the second one, I'll get 1, 1, 1, which is very convenient.

**2:12** · And actually, if you subtract the second row from the third one, you'll get 1, 1, 1.

**2:21** · Here's the property of the determinant: if you have two equal rows on your matrix, the determinant is automatically equal to zero.

**2:30** · All right.

**2:31** · All done with one of them.

**2:32** · Let's work on the second one.

**2:35** · The determinant of B. Well, let's try elimination again.

**2:42** · 1, a, a squared.

**2:47** · 1 minus 1 is 0, b minus a, and b squared minus a squared.

**2:53** · b squared minus a squared-- let me factor that into b minus a, b plus a, which will be very convenient in the next step.

**3:03** · And then I'm going to subtract the first row again from the third one.

**3:07** · I'll get 0, c minus a.

**3:10** · And again, I'll get c squared minus a squared, c minus a, c plus a.

### Linear Determinants

**3:23** · Let's use that third property that was the determinant is linear on each row separately.

**3:34** · So what I'm going to do is, see this factor of b minus a?

**3:38** · It shows up in every entry of this row.

**3:41** · Well it's a 0, so it's the zero multiple of b minus a.

**3:45** · So I'm going to pull out this factor of b minus a, and this row is going to become 0, 1, b plus a.

**3:53** · I will also, in the same step, do the same thing with the third row.

**3:58** · I'll pull out a factor of c minus a, and it will become 0, 1, c plus a.

**4:08** · Here's one factor from the second row.

**4:11** · Another factor from the third row.

**4:14** · And 1, a, a squared.

**4:18** · 0, 1, b plus a.

**4:22** · 0, 1, c plus a.

**4:28** · Now what?

**4:29** · Well remember, you know how to do the determinant of upper triangular matrices because all that you do is multiply the pivots.

**4:37** · This is almost upper triangular, except there's a 1 over here.

**4:40** · So let's do another elimination step.

**4:45** · b minus a, c minus a.

**4:50** · 1, a, a squared; 0, 1, b plus a; 0, 0, c plus a minus b plus a is c minus b.

**5:06** · So the determinant of this matrix is now 1 times 1 times c minus b.

**5:12** · So we get b minus a, c minus a, c minus b, which has a really nice formula.

**5:23** · This is called the Vandermonde determinant.

**5:25** · It's always like this, even if your matrix is bigger than 3 by 3, if it's 4 by 4, or 5 by 5 and so on, you just have more differences of all the letters that show up in your matrix.

**5:37** · On to matrix number 3.

**5:41** · C equals \[1, 2, 3\] \[1, -4, 5\].

**5:53** · How did you get the determinant for this one?

**5:58** · Well remember, this is a rank one matrix because it's a column vector times a row vector.

**6:05** · So if you write out what the matrix is it'll be a 3 by 3 matrix where we can think about it this way.

**6:13** · The first row will be 1 times \[1, -4, 5\].

**6:17** · The second row will be 2 times those numbers.

**6:20** · And the third row will be three times those numbers.

**6:23** · So all the rows are going to be linearly dependent, or another way of saying the matrix is singular.

### Skew Determinants

**6:34** · When the matrix is singular, the determinant is always equal to 0.

**6:37** · That's also one of the properties.

**6:40** · C is 0.

**6:45** · Onto the next matrix.

**6:48** · Last one.

**6:49** · D is equal to 0, 0, 0.

**6:56** · 1, -1, 3, -3, 4, -4.

**7:06** · Maybe you didn't get that from just looking at the matrix the first time, but did you see how I wrote it down?

**7:13** · It has 0's down the diagonal.

**7:15** · And then for each entry, I have minus that entry.

**7:20** · That means that this matrix is skew symmetric.

**7:22** · What that means is if you do D transpose, it will not be equal to D, but it will be equal to minus D. D transpose is equal to minus D.

**7:37** · Now, what does this give us for a determinant?

**7:39** · Well if these two matrices are the same matrix, this determinant is equal to that determinant.

**7:46** · One of the properties is that the determinant of a transpose of the matrix is equal to the determinant of the original matrix.

**7:56** · How about this side?

**7:57** · Well, first temptation would be to just write that.

**8:07** · Is that always true?

**8:09** · No.

**8:09** · The determinant is linear on each row separately.

**8:14** · That means that you can't pull out the factor that is multiplying the matrix.

**8:18** · You have to pull it out once for each row of the matrix.

**8:21** · So what I should have written was -1, that's my factor, minus.

**8:34** · How many rows do I have?

**8:35** · One, two, three.

**8:37** · Pull it out once for each row.

**8:39** · Times the determinant of D. Well fortunately, -1 to the third is simply equal to -1.

**8:48** · So here we go.

**8:50** · It was correct, in fact.

**8:54** · We have determinant of D is equal to minus determinant of D. What is the only number that is equal to minus that number?

**9:01** · 0.

**9:03** · Determinant of D is equal to 0 again.

**9:08** · Let me ask you one last question.

**9:11** · Is it true that all skew symmetric matrices have the determinant equal to 0?

**9:16** · It was true for this one.

**9:18** · Is it true in every case?

**9:21** · Well, the key factor here was that I had -1 to the third power and I got a minus sign here, determinant of D is equal to minus determinant of D.

**9:32** · What if this number had been an even number?

**9:34** · Then I would just have the determinant of D is equal minus 1 to an even number, D. That's 1.

**9:42** · So I would have determinant of D is equal to determinant of D.

**9:46** · There's nothing I can say about that number.

**9:48** · It can be your favorite number, not necessarily 0.

**9:51** · All right.

**9:52** · We're done for today.

**9:53** · Thank you.