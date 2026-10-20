![](https://www.youtube.com/watch?v=GLFg2UBMAxc)

MIT 18.06SC Linear Algebra, Fall 2011  
View the complete course: https://ocw.mit.edu/18-06SCF11  
Instructor: Martina Balagovic  
  
A teaching assistant works through a problem on elimination with matrices.  
  
License: Creative Commons BY-NC-SA  
More information at https://ocw.mit.edu/terms  
More courses at https://ocw.mit.edu

## Transcript

**0:07** · PROFESSOR: Hi.

**0:08** · Welcome to recitation.

**0:10** · My name is Martina, and I'll be your recitation instructor for some of these linear algebra videos.

**0:14** · Today's problem is a straightforward solve the following linear system with four equations and four unknowns, using the method of elimination.

**0:22** · The system is x minus y minus z plus u equals 0, 2x plus 2z equals 8, minus y minus 2z equals -8, and 3x minus 3y minus 2z plus 4u equals 7.

**0:36** · And although you might know different ways to solve the system at this point, the method of elimination is going to show up a million times during these videos, so it's really important to get it right.

**0:47** · So I suggest you try solving this system now, using the method of elimination as it was described in class.

### The Method of Elimination

**0:52** · I'm going to leave you alone with the problem.

**0:54** · You should pause the video, solve it yourself, and then come back and compare your solution with mine.

**1:06** · And we're back.

**1:07** · So the method of elimination, if you remember it from class, consisted of replacing this system with an equivalent system-- equivalent meaning they have the same solution-- by a series of row operations.

### Method of Elimination

**1:19** · Row operations are not supposed to change the solution to the system.

**1:23** · And they're, for example, exchange the order of two equations.

**1:26** · Multiply an equation with a nonzero number, and add a nonzero multiple of one equation to the other.

**1:32** · So let's do that.

**1:33** · As we're going to do this series of arithmetic operations, we don't really want to copy the names of the variables and the equality signs every time.

**1:41** · So we're going to keep the important information which are these numbers.

**1:45** · these coefficients here, we're going to keep that information in a matrix.

**1:52** · So let's write a matrix.

**1:54** · Each row is going to correspond to an equation, and each column is going to correspond to an unknown.

**1:59** · So the first row is 1, -1, -1, 1.

**2:13** · The second row, corresponding to the second equation, is 2, 0, 2, 0.

**2:24** · And you want to be very careful to put 0's on the right spots here.

**2:28** · The third equation is 0-- I haven't left myself enough room-- 0, -1, -2, 0.

**2:38** · And the fourth row, corresponding to the fourth equation, is 3, -3, -2, 4.

**2:49** · And as we care about the right-hand side as well, we're going to copy this information as well, and get the augmented matrix of the system.

**2:57** · 0, 8, -8, 7.

**3:03** · OK, and now let's try reducing this matrix to an upper triangular one.

**3:10** · We start with the first column, and we're going to use this number, called a pivot, to get rid of all the numbers under it, so to get 0's here and here.

**3:18** · A way to do it is-- well, to get rid of this 2, I have to multiply the first row by -2, and add it to the second one.

**3:29** · Writing this here is not strictly necessary, but I like to do a bit of bookkeeping, because I'm prone to make a lot of errors while doing this simple arithmetic operations.

**3:37** · And then if I get to the end, figure out I made a mistake somewhere, this bookkeeping makes it easier to backtrack and find the place where I made this mistake.

**3:45** · So we replace this matrix with another matrix.

**3:48** · The first row stays the same.

**3:51** · 1, -1, -1, 1, 0.

**3:57** · The second row gets replaced by the second row minus 2 times the first row.

**4:02** · The aim of that is to get a 0 here, so that's good.

**4:06** · Next, on this position here, we get -2 times -1, which is 2, plus 0 which is 2.

**4:13** · -1 times -2, which is 2, plus 2, which is 4.

**4:20** · -2 plus 0 which is -2.

**4:23** · And 8 minus 2 times 0 which is 8.

**4:27** · The third row already has a 0 here, so I can just copy it over.

**4:31** · 0, -1, -2, 0, -8.

**4:37** · And to get a 0 here, I'm going to multiply the first row by -3 and add it to the fourth row and get 0, -3 times -1 is 3, minus 3 is 0.

**4:53** · -3 minus 1-- oh, sorry-- 3 minus 2 is 1, and -3 plus 4 is 1.

**5:09** · And there we go.

**5:10** · The first column looks like a first column of an upper triangular matrix.

**5:14** · Now let's do the same to the second column.

**5:16** · This is going to be our pivot, the number that we use to get rid of numbers under it.

**5:21** · And we see that to get rid of this number here, we will need to multiply it with 1/2.

**5:28** · So multiply the whole second row with 1/2, and add it to the third row.

**5:31** · The matrix that we get will have the first row the same.

**5:38** · It stays the same.

**5:39** · 1, -1, -1, 1, 0.

**5:48** · The second row stays the same.

**5:50** · 0, 2, 4, -2, 8.

**5:59** · The third row gets replaced by the third row plus 1/2 times the second row and becomes 0, 0, 2 minus 2 which is 0, -1 plus 0 which is -1, and 4 minus 8 which is -4.

**6:22** · And the fourth row already has a 0 here so I just copy it over.

**6:28** · 0, 0, 1, 1, 7.

**6:34** · And now let's look at this matrix.

**6:35** · It has the first two columns as they're supposed to be, 0's under the diagonal.

**6:41** · And now we want to get a 0 here.

**6:43** · Normally what I would do is to circle this number here, multiply it by something so that I get a -1, and add it to this row to get a 0 here.

**6:53** · But that's not going to work.

**6:54** · You might remember from lecture that 0's can never be pivots.

**6:58** · Or you can just try finding a number such that 0 times this number equals -1, and seeing that such a number doesn't exist, because you're always going to get 0.

**7:06** · So we can proceed as we did until now.

**7:09** · But is there another way to get a 0 here?

**7:12** · There is a very simple row operation, which consists just of switching the third and the fourth row.

**7:20** · It certainly doesn't change the solution of the system.

**7:23** · So let's do that.

**7:25** · And let's get the next matrix which is 1, -1, -1, 1, 0.

**7:35** · 0, 2, 4, -2, 8.

**7:42** · Then we put the fourth row here.

**7:43** · 0, 0, 1, 1, 7.

**7:47** · And we put the third row here, 0, 0, 0, -1, -4.

**7:59** · And there it is.

### Upper Triangular Matrix

**8:01** · This is an upper triangular matrix.

**8:03** · So in the same way as at the beginning, we had a system and then wrote the matrix representing it, this matrix also represents a system.

**8:11** · And this system has the same solutions as the initial system but is much easier to solve.

**8:15** · Now let's write this back as a system, and let me do that not starting from the first equation, but starting from the last equation.

**8:23** · So the last equation here reads -u equals -4, which is, as equations go, a pretty easy one to solve.

**8:39** · The solution is u equals 4.

**8:41** · Now let's go back to the third equation.

**8:43** · The third equation reads y-- no, I'm sorry-- z-- the third column corresponds to z-- plus u equals 7.

**8:59** · But we know what's u now.

**9:01** · So, it reads z plus 4 equals 7, which just becomes z equals 3.

**9:13** · The second equation is 2 times y plus 4 times z, but z is 3, minus 2 times u, but u is 4, equals 8.

**9:33** · And from this, one can easily compute that y is equal to 2.

**9:37** · And finally, the first equation reads x minus y minus z plus u equals 0, or x equals 1.

**9:58** · And this is our solution.

**9:59** · x, y, z, and u equal 1, 2, 3, and 4.

**10:04** · This finishes the problem, but I would very strongly encourage you now to take this solution and plug it back into the original system and check if it's really a solution.

**10:13** · And that's all I wanted to say today.