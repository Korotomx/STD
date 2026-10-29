![](https://www.youtube.com/watch?v=B17h10EF59g)

MIT 18.06SC Linear Algebra, Fall 2011  
View the complete course: https://ocw.mit.edu/18-06SCF11  
Instructor: Linan Chen  
  
A teaching assistant works through a problem on determinants.  
  
Watch this video in Chinese: https://youtu.be/ZyYGJc9jNno  
License: Creative Commons BY-NC-SA  
More information at https://ocw.mit.edu/terms  
More courses at https://ocw.mit.edu

## Transcript

### Introduction to examples

**0:06** · LINAN CHEN: Hi everyone.

**0:07** · I'm Linan.

**0:08** · Welcome back to recitation.

**0:10** · In recent lectures, we have studied the properties of the determinant.

**0:14** · And we also derived the formula to compute it.

**0:17** · Today we're going to put what we learned into practice by considering these two examples.

**0:23** · So we want to find out the determinants of these two 5 by 5 matrices.

**0:29** · And as you can see, matrix A has x along this diagonal, and in the first four rows, y to the right of x, except for the last row.

**0:41** · And zero entries everywhere else.

**0:44** · And matrix B also has x along this diagonal and y everywhere else.

**0:52** · Before starting, let me help you review what you can do to compute determinants.

**0:58** · Of course, you can carry out elimination to transform your original matrix into upper triangular matrix.

**1:07** · Or you can use this big summation formula.

**1:11** · Another choice would be you can do it by cofactors.

**1:16** · Namely, you can expand your original matrix along any row or any column, and then the determinant is simply given by the dot product of that row or that column with its cofactors.

**1:30** · Why don't you pause the video now and try to work on them yourself.

**1:34** · Whenever you're ready, I'll come back and show you my way.

### Determinant of matrix A

**1:46** · I hope you just had some fun with these two problems.

**1:49** · Now let's look at them together.

**1:52** · Let's look at matrix A first.

**1:55** · As you can see, there are a lot of zero entries in matrix A.

**1:59** · So perhaps you don't need elimination to introduce more 0's.

**2:04** · Furthermore, we observe this pattern of A, and you notice that if I cover the last row and the first column, so if this column and this row are not here, what is left over is simply a 4 by 4 lower triangular matrix.

**2:23** · And similarly, if you cover the first column and the first row, what is left over here is simply a 4 by 4 upper triangular matrix.

**2:36** · This is telling us that we should calculate the determinant of A by the third method.

**2:42** · So we should expand along the first column of A, and we calculate the cofactors.

**2:48** · Let's do it now.

**2:51** · So determinant of A, is equal to the (1, 1) entry of A, which is x, times the cofactor of that spot, which is the determinant of the leftover 4 by 4 matrix.

**3:13** · And it's upper triangular, so its determinant is simply given by x to the power 4.

**3:21** · Plus, the only other nonzero entry in that column is the y at the very bottom.

**3:28** · So you put y here.

**3:32** · And you multiply y by the cofactor of that spot, which is the determinant of the leftover 4 by 4 matrix again.

**3:42** · In this case, it's lower triangular and its determinant is y to the power 4.

**3:47** · So I have a y to the power 4.

**3:51** · But not quite.

**3:53** · In principle, there should be another factor here indicating the sign.

**3:59** · And the sign in this case, well because the y is the entry in the fifth row and the first column, so this factor should be negative 1 to the power 5 plus 1.

**4:14** · And of course, it's just 1.

**4:16** · So the determinant of A is simply equal to x to the fifth power plus y to the fifth power.

**4:29** · Did you get the correct answer?

**4:32** · Well, the determinant of A is not too bad, because A has a lot of zero entries.

**4:37** · Now let's look at the determinant of matrix B.

### Elimination on matrix B

**4:42** · I have another copy of B here.

**4:45** · So B also has a very clear structure.

**4:48** · It has x along its diagonal, and y everywhere else.

**4:53** · But in general, B does not have any zero entry.

**4:57** · So perhaps our first step should be carrying out elimination to introduce zero entries into matrix B.

**5:07** · Of course, you can do it by the regular routine.

**5:10** · You start with the first row, find a pivot, and eliminate the second row and the third row and so on and so forth.

**5:17** · But in this case, there's a shortcut.

**5:20** · If you compare two rows that are next to each other, for example, if we compare the fourth row and the fifth row, you notice that they have a lot of entries in common.

**5:33** · And they're only different at these two spots.

**5:37** · So imagine if I subtract the fourth row from the fifth row.

**5:42** · So if I do the following operation-- so I subtract this row from the last row.

**5:54** · Then the new fifth row should become the following.

**6:00** · So this row will become 0, 0, 0, y minus x, x minus y.

**6:12** · You see, just by this simple operation, I have introduced three zero entries at once.

**6:22** · And it's similar with the fourth row and the third row.

**6:25** · They have common entries here, here, and here.

**6:30** · So you subtract the third row from the fourth row.

**6:36** · You update the fourth row to 0, 0, y minus x, x minus y, 0.

**6:46** · Again, three zero entries.

**6:49** · And same thing happened to the second row and the third row.

**6:52** · So you subtract the second row from the third row and your new third row will become 0, y minus x, x minus y, 0, 0.

**7:08** · Finally, you subtract the first row from the second row, and then you update the second row to y minus x, x minus y, 0, 0, 0.

**7:25** · Let's keep the first row unchanged.

**7:27** · So I'm going to copy here.

**7:33** · All right.

**7:34** · By row elimination, we have introduced many zero entries to matrix B. Is there anything else that I can take advantage of?

### Column operations on B

**7:46** · Let's observe the pattern of this new matrix.

**7:50** · As you can see, in each row, you have two nonzero entries, except for the first row.

**7:56** · And they're only different by a sign.

**7:58** · So if, somehow, you can figure out a way to sum them up, you will get even more zero entries.

**8:05** · So let's do it.

**8:06** · That's going to involve the operations on column.

**8:10** · So here is how I do it.

**8:16** · I'm going to keep the last column unchanged.

**8:21** · So the last column is y, 0, 0, 0, x minus y.

**8:32** · What I will do is I will add a copy of the last column to the fourth column.

**8:39** · So this is what I'm going to do.

**8:41** · Add one copy of the last column to the fourth column.

**8:46** · Now the new fourth column will become 2y, 0, 0, x minus y, 0.

**8:57** · As you can see, by doing this, I have killed this spot.

**9:02** · So I have introduced one more zero entry into my fourth column.

**9:07** · If you continue, you may want to add the fourth column to the third column.

**9:13** · Let's see what will happen if you do that.

**9:15** · So if you add the fourth column to the third column, now what should appear here is 2y, 0, x minus y, 0, y minus x.

**9:38** · But in this new third column, you still have two zero entries, which is the same as the original third column.

**9:48** · So although you've killed this spot, but you've introduced a new nonzero entry.

**9:55** · So is there a way that we can kill this spot too?

**10:00** · You may have noticed that if you add a copy of the fifth column to this column again, then that spot will have been killed.

**10:11** · So let's do it.

**10:12** · If I add this column to this one-- I'm going to just update it here-- then the first entry should become 3y.

**10:24** · These are unchanged.

**10:27** · And the last spot becomes 0.

**10:34** · It reflects here as you are adding a copy of the fourth column and a copy of the fifth column to the third column.

**10:44** · Now you've got the idea.

**10:46** · And you continue.

**10:48** · What do you do with the second column?

**10:51** · This time you will have to add a copy of the third column, a copy of the fourth column, and the copy of the fifth column.

**11:06** · So you update the second column to be 4y, x minus y, 0, 0, 0.

**11:19** · Eventually, what you will do to the first column would be you add everything to the first column.

**11:29** · So a copy of each.

**11:41** · Then the first column will become-- so I don't have enough spot here, so make it here-- x plus 4y.

**11:50** · Then everything else is 0.

**11:56** · This is fun.

**11:57** · And the result's really nice.

**11:59** · This is wonderful because this is simply upper triangular matrix.

**12:03** · Now you tell me: what is the determinant of B?

**12:06** · The determinant of B is the determinant of this upper triangular matrix.

**12:14** · So you simply multiply everything together, that's x plus 4y times x minus y to the fourth power.

**12:29** · So I hope you enjoyed these two examples.

**12:33** · Maybe your method is different from mine, but at least these two examples teach us that you can be flexible in combining methods in calculating determinants.

**12:43** · Thanks for watching, and I'm looking forward to see you soon.