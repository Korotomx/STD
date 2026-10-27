![](https://www.youtube.com/watch?v=AMLekTJR5_U)

MIT 18.06SC Linear Algebra, Fall 2011  
View the complete course: https://ocw.mit.edu/18-06SCF11  
Instructor: Nikola Kamburov  
  
A teaching assistant introduces problems found in the first exam.  
  
License: Creative Commons BY-NC-SA  
More information at https://ocw.mit.edu/terms  
More courses at https://ocw.mit.edu

## Transcript

### Introduction

**0:10** · PROFESSOR: Hi, everyone.

**0:13** · So for the first part of this course, we've learned basically the ins and outs of solving linear systems of equations.

**0:24** · Today we're going to do a little review of the basic concepts.

**0:29** · Hopefully we'll see a few of them in the following problem.

**0:35** · We're given a square matrix A-- a three by three square matrix A-- where the last entry is a parameter k.

**0:43** · And this parameter will vary.

**0:46** · And we'll see what happens to the system of equations A\*x equal to \[2, 3, 7\], for which k it has a unique solution, for which k it has infinitely many solutions.

**1:04** · Then we'll find the LU decomposition.

**1:06** · And finally, we'll write down the complete solution, the system.

**1:11** · So I'll give you a few minutes to work this problem on your own.

**1:14** · And then please come back and see how I do it.

### Part a

**1:24** · All right, welcome back.

**1:26** · So let's start with part A. For which k does this system, A\*x equal \[2, 3, 7\], have a unique solution?

**1:37** · So what do we know about square systems of linear equations?

**1:46** · They have a unique solution when the matrix A is invertible.

**1:51** · So now, when is A invertible?

**1:55** · It is invertible when it is of full rank.

**1:58** · And how do we figure this out?

**2:01** · We do it by performing row operations.

**2:04** · We do it by doing eliminations on the matrix.

**2:10** · But since we want to simulate an exam setting, it always pays off to see what tasks lie ahead of us.

**2:18** · So in part C, we're asked to find the LU decomposition.

**2:25** · This means that when we do row operations, we'd better keep track what row operations we're doing exactly.

**2:34** · In particular, we'll write them down as elementary matrices.

**2:38** · And in part D, we'll be asked to compute the complete solution.

**2:45** · And therefore it's good to do row operations on the augmented matrix A. So let's do this.

**2:57** · I'm going to write this.

**3:00** · The augmented matrix A is the following beast, 1, 1, 1; 1 2, 3; 3, 4, k; and then 2, 3, 7.

**3:25** · So first thing, we subtract a multiple of row one from row two.

**3:32** · And it's exactly negative 1 times the first row plus the second.

**3:40** · Let me write down the corresponding elementary matrix that does this.

**3:47** · It's E\_(2,1).

**3:51** · And it's lower diagonal with 1's on the diagonal.

**3:55** · And it's going to be exactly minus 1 in the first entry of the second row.

**4:04** · So we get 1, 1, 1, 2; 0, 1, 2, 1.

**4:15** · And we copy down the third row.

**4:21** · Now we subtract a multiple of the first row from the third one.

**4:27** · And let me write this here.

**4:34** · Yeah, we'll multiply the first row by negative 3, and add it to the third one.

**4:40** · This is accomplished by the elementary matrix E\_(3,1) which is 1, 1, 1, negative three, and then 0, 0.

**4:54** · OK, 1, 1, 1, 2; 0, 1, 2, 1.

**5:01** · We copy the first two rows.

**5:03** · And then the third one will be 0, 1, k minus 3, and 7 minus 3 times 2, 7 minus 6, 1.

**5:17** · We have essentially one last row operation to perform.

**5:22** · Let me do it here.

**5:26** · So we'll subtract the second row from the third one.

**5:31** · And we'll get 1, 1, 1, 2; 0, 1, 2, 1; 0, 0, k minus 5, and then 0.

**5:51** · And this was achieved by the elementary matrix E\_(3,2), which was 1, 1, 1, and then negative 1.

**6:05** · Because we multiplied the second row by negative 1 and added it to the third one.

### Part b

**6:13** · So we got to a matrix, which is upper triangular.

**6:24** · And we want to figure out: for which value of the parameter k is this matrix of full rank.

**6:38** · This is a pivot.

**6:39** · This is a pivot.

**6:40** · And we want this one to be a pivot as well.

**6:43** · And that happens when k minus 5 is not 0.

**6:51** · So when k is different from 5, the matrix A is of full rank.

**6:58** · And therefore the system A\*x equals to \[2, 3, 7\] has a unique solution.

**7:05** · Now part B. For which k do we have infinitely many solutions?

**7:14** · So when are we in such a situation?

**7:21** · We are in such a situation when the null space of the matrix A is nontrivial.

**7:28** · So the null space will be nontrivial when this k minus 5 number here, which is what's the pivot in the first case, is 0.

**7:42** · So k minus 5 equals to 0.

**7:50** · You see there's a little caveat here.

**7:54** · When k is equal to 5, we get the third row of the augmented matrix, 0, 0, 0, equal to 0.

**8:02** · This means that the matrix is actually consistent, and we indeed have a solution But if this entry were nonzero, then we would get no solutions.

**8:15** · Now off to part C. We want to compute the LU decomposition.

**8:24** · Well, we already got what the matrix U is through performing row operations.

**8:34** · It's this guy here.

**8:35** · Let me write it down-- 1, 1, 1; 0 1, 2; 0, 0, k minus 5.

**8:47** · And when k is equal to 4, this entry's negative 1.

**8:56** · And now what about the matrix L?

**8:59** · Well, how did we get to this U?

**9:02** · We had the matrix A. We got the matrix U.

**9:07** · And what we did was first we applied E\_(2,1).

**9:11** · Then we applied E\_(3,1) and then E\_(3,2).

**9:24** · We get A by inverting this equation.

**9:28** · So it's going to be E\_(2,1) inverse E\_(3,1) inverse E\_(3,2) inverse times U. And this is our matrix L.

**9:48** · And we know it's fairly easy to invert these elementary matrices E. We flip the signs of the off-diagonal entries.

**10:01** · I'm not going to write down again the inverses of these guys.

**10:09** · I'm just going to write the product of the inverses.

**10:11** · And that's also very easy to compute.

**10:15** · Because one, we invert the signs.

**10:18** · We just send the numbers in their corresponding entry of L.

**10:28** · I mean the following thing.

**10:30** · So minus 1 becomes a 1.

**10:33** · And it comes here, in its respective entry.

**10:42** · For E\_(3,1), we flip the sign, first 3, and we plug it in here.

**10:54** · And for E\_(3,2), we flip the sign of this guy, becomes 1, and we plug it in here.

**11:03** · So give me a few moments to erase the board, and then I'll do part four.

**11:13** · We're back, and we're going to do part D now.

**11:18** · So we need to find the complete solution of the system for all k.

**11:24** · And we saw that for k equal to 5, the system had many, many solutions.

**11:30** · And for k not equal to 5, it had only one.

**11:34** · So first let's look at the case k not equal to 5, when the matrix A was invertible.

**11:46** · It's not hard to see what the solution of the system then is.

**11:51** · It's going to be-- let me just write it down.

**12:00** · So when k is not equal to 5, this was nonzero.

**12:05** · Therefore, x\_3 needs to be 0.

**12:11** · When x\_3 is 0, we have x\_2 plus 2 times x\_3.

**12:16** · So x\_2 plus 0 equals 1.

**12:20** · Therefore x\_2 is 1.

**12:24** · And then we go back to the first row.

**12:27** · We have x\_1 plus x\_2 plus x\_3 equals 2.

**12:32** · So x\_1 plus 1 plus 0 equals 2.

**12:38** · So x\_1 plus 1 equals 2.

**12:40** · And therefore x\_1 is 1.

**12:43** · Good.

**12:45** · Now what about k equal to 5?

**12:51** · Then we see that x\_3 is a free variable.

**12:58** · So the solution will be \[x 1, x 2, x 3\].

**13:07** · x\_3 can be any number c.

**13:13** · From the second row, we'll get the value of x\_2.

**13:16** · It's 1 minus 2 times x\_3.

**13:19** · So 1 minus 2 times c.

**13:22** · And x\_1 is 2 minus x\_2 minus x\_3.

**13:37** · So let me rewrite this.

**13:39** · It's 2 minus x\_2 is 1 minus-- aah, chalk-- 2c, minus c, 1 minus 2c, c.

**13:56** · So we'll decompose this vector here into a component which is independent of c and a component which is a multiple of c.

**14:06** · So this is 2 minus 1.

**14:10** · It should be \[1, 1, 0\] plus c times-- we'll have two c minus c, c, so c times 1.

**14:25** · Here we'll have minus 2c so negative 2.

**14:29** · And here we'll have 1.

**14:33** · And thus we get the particular solution for the system and the special solution for the system.

**14:43** · We're kind of done here.

**14:45** · If you're at an exam, you should immediately start the next problem.

**14:50** · Good luck, and Ill see you later.

关联：[[Linear Algebra/主页|线性代数]]
