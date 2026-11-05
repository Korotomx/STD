![](https://www.youtube.com/watch?v=pz3zyUO2gpM)

MIT 18.06SC Linear Algebra, Fall 2011  
View the complete course: https://ocw.mit.edu/18-06SCF11  
Instructor: Linan Chen  
  
A teaching assistant works through problems found on the second exam.  
  
Watch this video in Chinese: https://youtu.be/ThxvK9t7DNo  
License: Creative Commons BY-NC-SA  
More information at https://ocw.mit.edu/terms  
More courses at https://ocw.mit.edu

## Transcript

### Introduction and Strategy

**0:06** · PROFESSOR: Hi.

**0:07** · Welcome to the second special recitation on exam problem solving.

**0:12** · As you may have experienced, when you do homework problems, you can give every problem or even every step a careful thought.

**0:20** · You may even try different methods in solving one problem, just to check your answers and also to find the optimal way.

**0:27** · But in the real exam, these may not be available to you anymore, because time is the main issue.

**0:35** · So you want to do things fast but accurately at the same time.

**0:40** · Today's recitation is going to focus on that.

**0:43** · So we're going to look at a real exam problem.

**0:46** · So this is the problem from a 15-minute linear algebra exam.

**0:54** · OK.

**0:56** · By now, you've developed enough background to completely solve this problem.

**1:01** · So because this is a 15-minute exam, a good suggestion on time spending on this problem would be no more than 15 minutes, which means within 15 minutes, you have to read through the questions, understand what they're asking for, and completely solve all three parts.

**1:22** · Why don't you hit Pause now, and try to complete this problem as if you were in an exam.

**1:28** · And time yourself for 15 minutes.

**1:31** · If you finish early, don't forget to check your answer.

**1:34** · You want to get all the credits you deserve in an exam.

**1:38** · OK.

**1:39** · I'll come back later and show you how I would speed up in the exam.

### Calculating the Determinant

**1:52** · OK.

**1:53** · Have you finished?

**1:55** · Well, let's solve this problem together.

**1:58** · We are looking at a 4 by 4 matrix A here.

**2:02** · As you can see, this matrix is made up by the examiner in a rather casual way, because you have numbers from 1 to 12 as the entries of this matrix.

**2:14** · And in the first part, we want to find all the nonzero terms in this big formula to compute determinant of A.

**2:22** · So the determinant of A-- so that's Part 1-- that's equal to a big summation of plus or minus a\_(1,alpha), a\_(2,beta), a\_(3,gamma), and a\_(4,delta).

**2:45** · So what I'm doing here is I choose one entry from each row with the columns being all different.

**2:52** · So in other words, if I take this column numbers down-- let me write it here-- alpha, beta, gamma, and delta, I want this to be a permutation of numbers 1, 2, 3, 4.

**3:09** · OK.

**3:10** · So how would you do it?

**3:12** · Well, if you follow this order, you may want to start with the first row.

**3:17** · And you go through all the possibilities of this alpha, beta, gamma, and delta, and at the end, you drop the terms which are 0.

**3:26** · But if you do it in that way, how many terms do you have to compute?

**3:32** · This is a 4 by 4 matrix.

**3:35** · So in general, this sum will contain 4 factorial, which is 24, terms.

**3:41** · That sounds time consuming.

**3:43** · So can you do it in a faster way?

**3:46** · Well, since we only care about nonzero terms in this sum, let's look at where 0 occurs in matrix A.

**3:55** · They're here.

**3:57** · You have zero entries in these four spots.

**4:01** · OK.

**4:01** · So they all occur in the third row and the fourth row, which means when you make your choice of the last two entries, in order not to get zero, you can only choose within this red box.

**4:22** · Because you want to avoid these 0's.

**4:24** · Which means the choice of the last two entries can only be either 9, 12 or 10, 11.

**4:34** · OK.

**4:35** · Now, if that's the case, what will happen to the first two entries?

**4:40** · Since they all have to come from different columns, which means when you choose the first two entries, they can only be from this red box.

**4:54** · Which means the choice of the first two entries can only be either 1, 6 or 2, 5.

**5:04** · So how many terms am I talking about?

**5:07** · Two possibilities here and two possibilities here, which comes to four.

**5:14** · So in other words, instead of computing 24 terms, you only need four terms here.

**5:21** · Let's put them down.

**5:24** · OK.

**5:24** · So we start with this choice: 1, 6, 9, 12.

**5:31** · So that's 1 times 6 times 9 times 12.

**5:37** · Well, these are from diagonal, right?

**5:40** · So of course, this coordinate numbers would just be a\_(1,1), a\_(2,2), a\_(3,3), a\_(4,4).

**5:50** · This is the perfect alignment of 1 2, 3, 4, so the sign of this term is just a plus sign.

**5:57** · Let's continue.

**5:58** · Now I'm going to look at 1, 6 but 10, 11.

**6:04** · So 1 times 6 times 10 times 11.

**6:11** · What is the coordinate number-- what are the coordinate numbers of this choice?

**6:17** · a\_(1,1), a\_(2,2), 10 comes from a\_(3,4).

**6:23** · So here I have 4 in the front.

**6:26** · The last one is a\_(4,3), so right here.

**6:31** · This is the permutation of 1, 2, 3, 4.

**6:34** · In order to get back to this, I have to exchange 3 and 4.

**6:39** · Just do it once.

**6:40** · OK.

**6:41** · Which means I need a negative sign in front.

**6:48** · A negative sign in front of the entire product.

**6:51** · Well, let's continue.

**6:55** · I'm going to write it down here.

**6:56** · As you can see the blue part indicate the signature of columns.

**7:01** · So next term, I'm going to put-- I've exhausted the first possibility of choosing 1, 6, right?

**7:10** · So let's look at 2, 5.

**7:12** · 2 times 5 times 9 times 12.

**7:20** · What is the column?

**7:22** · What are the column numbers?

**7:24** · 2 comes from (1, 2) entry, so I have a 2 in the front.

**7:28** · 5 is (2, 1) entry, so 2, 1, and then 3, 4.

**7:34** · 3, 4.

**7:37** · Again, I need one exchange to get back to 1, 2, 3, 4, which means I have a negative sign in the front.

**7:48** · The last one would be 2, 5.

**7:52** · 2 times 5 times 10, 11, so times 10 times 11.

**8:01** · Columns are a\_(1,2), a\_(2,1), a\_(3,4), a\_(4,3).

**8:09** · So you exchange the first two spots, and the last two spots.

**8:14** · You get back to 1, 2, 3, 4.

**8:16** · But you have to do twice, two exchanges, which means you need a plus sign in front.

**8:22** · That's it.

**8:24** · This big summation formula comes down to the sum of four terms.

**8:28** · And you can compute it.

**8:30** · If you don't make any algebra mistake, the result should be 8.

**8:38** · Did you get the right answer?

**8:40** · All right, time is really precious.

### Finding Matrix Cofactors

**8:42** · Let's move on to the second part.

**8:44** · In the second part, we need to find cofactors c\_(1,1), c\_(1,2), c\_(1,3), and c\_(1,4).

**8:54** · Let me put the second part here.

**9:02** · So we're looking for the cofactors of the first row of matrix A. Let's just write everything down.

**9:10** · c\_(1,1).

**9:11** · c\_(1,1) is the cofactor of this entry here.

**9:16** · So you're looking at the determinant of this left over 3 by 3 matrix.

**9:22** · So that's the determinant of-- copy it down-- \[6, 7, 8; 0, 9, 10; 0, 11, 12\].

**9:37** · How would you compute this?

**9:38** · This is a 3 by 3 matrix.

**9:41** · Of course, you can use the big summation formula again.

**9:45** · In other words, you can write down this determinant-- this formula, but for the specific 3 by 3 matrix.

**9:54** · But that will involve three factorial terms, right?

**9:58** · Which is six terms.

**10:00** · All right.

**10:01** · Is there a way that you can do it faster?

**10:05** · Just notice that the first column of this matrix has only one nonzero entry, which is this (1, 1) entry 6.

**10:14** · So why do we just expand this along the first column and use cofactors?

**10:20** · Let's do it.

**10:22** · This determinant is equal to 6 times its cofactor.

**10:27** · And its cofactor comes to the determinant of this 2 by 2 matrix, which is easy.

**10:33** · That becomes 9 times 12 minus 10 times 11.

**10:40** · And if you compute this correctly, that should be -12.

**10:47** · That's not too bad.

**10:48** · Let's look at the second one, c\_(1,2).

**10:53** · c\_(1,2) is the determinant of this 3 by 3 matrix.

**10:59** · So I have to delete the first row and the second column.

**11:03** · And I read what is left over and I put it here.

**11:07** · So that's \[5, 7, 8; 0, 9, 10; 0, 11, 12\].

**11:19** · Same thing.

**11:21** · The first column has only one nonzero entry.

**11:24** · You expand it along the first column, use cofactors, the result will be 10.

**11:33** · There's one thing that I've forgotten here.

**11:35** · Because we are looking at (1, 2) entry.

**11:38** · So for the cofactor, I have to put an extra negative sign here.

**11:43** · So this is actually -1 times the determinant of this 3 by 3 matrix.

**11:50** · And the result will be 10.

**11:52** · OK, let's continue.

**11:56** · c\_(1,3).

**11:58** · Let's hope the computation is going to get easier and easier.

**12:01** · So c\_(1,3) is the determinant of the leftover 3 by 3 matrix.

**12:06** · So I'll directly read from that.

**12:09** · That's going to be 5, 6, 8; 0, 0, 10; and 0, 0, 12.

**12:20** · What is the determinant of this matrix?

**12:24** · Again, you can use the same method as we did for the first two, because the first column has only one nonzero entry.

**12:32** · And if you do that, the result should be 0.

**12:36** · But you should be able to tell it without any direct computation.

**12:41** · Why is that?

**12:43** · Well, clearly the first two columns are linearly dependent, because the second column is 6 over 5 times the first column.

**12:54** · So this is a singular matrix.

**12:56** · Right away, the determinant is 0.

**13:00** · So what is c\_(1,4)?

**13:04** · c\_(1,4) is the determinant of the matrix of \[5, 6, 7; 0, 0, 9; 0, 0, 11\].

**13:16** · Same thing.

**13:17** · It's singular, so its determinant is 0.

**13:21** · All right.

**13:21** · So that completes the second part.

### Verification of Answers

**13:25** · You can move on to the third part now, but before you do that, just notice this may be a good point to check your answer from the first part.

**13:35** · Because you have all the cofactors of the first row of A, and if you use the other formula to compute the determinant of A, you can see the determinant of A is equal to the dot product of the first row with its cofactors.

**13:56** · So because the last two cofactors is 0, so I only have two terms in the sum.

**14:02** · So determinant A is equal to a\_(1,1) entry, which is 1, times c\_(1,1), which is -12, plus a\_(1,2) entry, which is 2, times c\_(1,2), which is 10.

**14:25** · What is that?

**14:27** · -12 plus 20, that give you 8.

**14:33** · OK, at least the answers from the first two parts are consistent.

**14:38** · So by now, you should be more confident to move on to the third part.

### Deriving the Inverse

**14:45** · I have a problem of space.

**14:47** · So please allow me to put the third part here.

**14:50** · I'm going to come all the way back here.

**14:53** · So that's my third part.

**14:55** · What is the third part?

**14:57** · Third part asks you to find the first column of A inverse.

**15:03** · Well, it seems that involves more computation of cofactors, but as many well designed exam problems, the answer from third part can be directly derived from the first part and the second part.

**15:19** · That's how you should do it.

**15:21** · So what is A inverse?

**15:25** · The formula for A inverse is equal to 1 over determinant of A times the transpose of a matrix C. This matrix C is composed by cofactors of matrix A.

**15:43** · We want to find the first column of A inverse.

**15:47** · So the first column of A inverse should be one of our determinants of A, this constant, times the first row of C, but transpose, right?

**16:07** · So I have to put here, first row of C, but transpose.

**16:17** · Determinant of A comes from the first part, and the first row of C comes from the second part.

**16:25** · So I just copy what I have from the first two parts down.

**16:29** · That's 1 over 8.

**16:31** · This column vector will become \[-12; 10; 0; 0\].

**16:41** · That's it.

**16:42** · That completes this problem.

**16:45** · Have you got your answer right?

**16:49** · OK, before I finish, there are two things that I like to remind you.

### Final Review and Tips

**16:54** · First, as you can see, this is an exercise on the big summation formula to compute determinant of A.

**17:03** · In previous recitation, we practice using the combination of elimination and the method by cofactors to compute determinants.

**17:12** · But we should never forget this formula.

**17:16** · Because it always works.

**17:17** · And in a lot of cases, this will turn out to be an easy way to compute determinant.

**17:23** · For example, for this matrix A here.

**17:27** · And second, in your real exam, it would be really helpful if you can put down your work like this, because it helps you to check your work.

**17:39** · And also, even if you don't get your final answer correct, this may get you some partial credits.

**17:47** · OK, I'm going to stop here, and thank you for watching.