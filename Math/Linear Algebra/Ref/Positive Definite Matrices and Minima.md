![](https://www.youtube.com/watch?v=cfn2ZUuWPd0)

MIT 18.06SC Linear Algebra, Fall 2011  
View the complete course: https://ocw.mit.edu/18-06SCF11  
Instructor: Martina Balagovic  
  
A teaching assistant works through a problem on positive definite matrices and minima.  
  
License: Creative Commons BY-NC-SA  
More information at https://ocw.mit.edu/terms  
More courses at https://ocw.mit.edu

## Transcript

### Introduction to the problem

**0:06** · MARTINA BALAGOVIC: Hi.

**0:07** · Welcome to recitation.

**0:08** · Today's problem is about positive definite matrices.

**0:11** · And it's asking us: for which values of the parameter c, which is sitting here in the matrix, is the matrix B-- 2, minus 1, minus 1; minus 1, 2, minus 1; minus 1, minus 1, 2 plus c-- positive definite, and for which values of c is it positive semidefinite?

**0:30** · I'm going to leave you alone with the problem.

**0:32** · You should pause the video and then come back and compare your solution with mine.

**0:42** · And we're back.

**0:44** · As you remember from the lectures, there are several tests that you can do on matrices to find out if they're positive definite and if they're positive semidefinite.

**0:52** · And I'm going to demonstrate three to you.

**0:53** · First, I'm going to do the one that you should do in case you have very little time and you're asked to do a problem like this on the test, which is of course the determinant test.

### The determinant test

**1:13** · The determinant test asks us to compute determinants of the matrices in the upper left corner of all sizes.

**1:24** · And it says that it's going to be positive definite if they're all greater than 0 and positive semidefinite if some 0's sneak into that sequence.

**1:32** · So let's calculate the determinants.

**1:34** · The first determinant is the determinant of this tiny matrix here.

**1:39** · So it's just 2.

**1:43** · The next one is the determinant of this two by two submatrix, 2, minus 1; minus 1, 2; which is equal to 4 minus 1, which is 3.

**1:59** · And finally, we have the determinant of B, which I'm going to calculate for you.

**2:08** · I'm going to calculate it, I'm going to decompose it along the first line, first row.

**2:15** · So it's 2 times the determinant of this submatrix, 2, minus 1; minus 1, 2 plus c; minus minus 1, this one here, times this determinant, which is minus 1, minus 1; minus 1, 2 plus c.

**2:43** · And then plus minus 1, this one here, times this determinant, which is minus 1, 2; minus 1, minus 1.

**2:58** · And in total, that's 2 times 4 plus 2c minus 1 plus minus 2 minus c minus 1 and minus 1 plus 2.

**3:25** · And in total, this should give us 6 plus 4c minus 3 minus c minus 3, which is 3c.

**3:43** · So let's look at the determinants.

**3:45** · 2 is positive.

**3:46** · 3 is positive.

**3:47** · 3c is positive.

**3:49** · So the answer is: the matrix is positive definite if c is bigger than 0, and it's positive semidefinite if it's either strictly bigger than 0 or equal to 0.

**4:01** · And that's all.

**4:02** · If you're on the test, this is everything that you should do.

**4:06** · Now let me show you two more tests to demonstrate that first, they take longer, and second, to see these numbers and their quotients show up in other tests and to try to convince you that these tests really are equivalent.

**4:20** · Let me do the pivots test for you.

### The pivot test

**4:28** · So we take our matrix B, 2, minus 1, minus 1; minus 1, 2, minus 1; minus 1, minus 1, 2 plus c.

**4:39** · And let's pretend we're solving a system that has this as a matrix.

**4:45** · So we multiply the first row by 1/2, and we add it to the second and to the third row.

**4:53** · We get 2, minus 1, minus 1; 0, 3/2, minus 3/2; 0, minus 3/2, 3/2 plus c.

**5:12** · So the first column is good.

**5:14** · And then we just replace the third column with the third column plus the second column.

**5:22** · And we get 2, minus 1, minus 1; 0, 3/2, minus 3/2; 0, 0, and c.

**5:36** · And so the pivots are 2, 3/2, and c.

**5:44** · And again, the answer is as before.

**5:47** · It's positive definite if c is strictly bigger than 0, and it's positive semidefinite if c is greater or equal to 0.

**5:53** · But I want you to notice something else here.

**5:55** · So before, we had 2, 3, and 3c.

**6:00** · And now for determinants, as these pivots, we have 2, 3/2, which is the second determinant over the first determinant, and c, which can be thought of as 3c over 3, so the third determinant over the second determinant.

**6:16** · And something like this is always going to happen.

### The energy test

**6:19** · And finally, let me do the energy test, or completing the square.

**6:38** · So one of the definitions of positive definite, one could say the definition because of which we are really interested in such matrices, is the following.

**6:50** · It's positive definite if, when we consider this quadratic form, so a form that maps x, y, and z to this expression here that's going to be quadratic in x, y, and z, it's positive semidefinite if this is always greater or equal than 0.

**7:14** · And it's positive definite if, when we have an expression like this and try to solve this equals 0, the only solution is that x, y, and z all have to be 0.

**7:28** · So let's try calculating this form, completing the squares on it, and seeing these numbers show up again.

**7:35** · So when I multiply this like this, put in a B, do the multiplication, we get something like this.

**7:42** · 2 x squared plus 2 y squared plus 2 plus c z squared minus 2x\*y minus 2x\*z minus 2y\*z.

**8:02** · And now let's try completing the squares using the formulas that I prepared for you up here in this pop-up window in the corner.

**8:11** · So let's try completing-- we have a formula for the square of a plus b plus c and the square of a plus b.

**8:20** · So first, we try to get something squared so that this something has all the x's that appear here, so that we get something squared plus some expression that only takes y's and z's.

**8:36** · I'm not going to do the calculation in front of you to further embarrass myself with it.

**8:40** · But let me tell you that what you get is 2 times x minus 1/2 y minus 1/2 z squared.

**8:52** · And this ate all the x's that showed up here.

**8:55** · The remainder only has y's and z's.

**8:58** · When you use the second of those formulas in a pop-up window to complete the square of y's and z's, you get 3/2 times y minus z squared.

**9:12** · So this took up all the y's, and we're left just with a z that comes as c times z squared.

**9:22** · And now, let's look at the following.

**9:24** · This is a square of some real number.

**9:28** · So that's positive.

**9:30** · This is a square of some real number, so that's positive.

**9:33** · And this is a square of some real number, so that's positive.

**9:36** · They're all multiplied by positive numbers, 2, 3/2, and c, which we've already seen here.

**9:44** · And so if c is bigger or equal than 0, this is certainly always bigger or equal than 0.

**9:51** · Now to the question of if this can be equal to 0 without x, y, and z all being 0, well, let's look at two cases.

**10:02** · If c is strictly bigger than 0, then let me write this matrix here as 2, 3/2 and c times 1, minus 1/2, minus 1/2; 0, 1, minus 1; and 0, 0, 1.

**10:26** · Let's imagine c is strictly bigger than 0.

**10:28** · And let's see when can this expression be equal to 0.

**10:32** · Well, as we said, it's a sum of certain squares.

**10:36** · They're all greater or equal to 0, so they all have to be equal to 0 for this expression to be 0.

**10:41** · In other words, z needs to be equal to 0.

**10:44** · y minus z needs to be equal to 0.

**10:47** · And x minus 1/2 y minus 1/2 z also needs to be equal to 0.

**10:55** · And since this matrix has all the pivots, this can only happen if x, y, and z are all equal to 0.

**11:04** · On the other hand, if c is equal to 0, then let me write this matrix here again.

**11:13** · Take 2 out here.

**11:14** · Take 3/2 out here.

**11:16** · And write again 1, minus 1/2, minus 1/2; 0, 1, minus 1; and 0, 0, 0.

**11:29** · And so imagining that c is 0, when can this whole expression be equal to 0?

**11:33** · Well, the last bit is already 0.

**11:37** · We need to have y minus z equal to 0.

**11:40** · And we need to have 1 times x minus 1/2 times y minus 1/2 times z also equal to 0.

**11:48** · So we need to have x, y, z in the kernel of this matrix.

**11:52** · But this matrix only has two pivots.

**11:54** · It has one free variable.

**11:56** · So we can find a solution to this times x, y, z equals 0 that's not 0 itself.

**12:02** · Namely, if you remember how to solve systems like this, we set z equal to 1.

**12:14** · From this, we calculate that y has to be 1.

**12:18** · And then from this, we calculate that x has to be 1.

**12:22** · And you can check that for in case c is 0, this thing here, when you plug it in here, you really get 0.

**12:35** · In fact, this thing here is in the kernel of the matrix B. In fact, in case c is 0, the columns of matrix B sum up to 0 because of this here.

**12:47** · And that's all I wanted to say for today.