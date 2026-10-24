![](https://www.youtube.com/watch?v=fjsPjh0B2tU)

MIT 18.06SC Linear Algebra, Fall 2011  
View the complete course: https://ocw.mit.edu/18-06SCF11  
YouTube Playlist: https://www.youtube.com/playlist?list=PL221E2BBF13BECF6C  
Instructor: Martina Balagovic  
  
A teaching assistant works through a problem on solving Ax=b.  
  
License: Creative Commons BY-NC-SA  
More information at https://ocw.mit.edu/terms  
More courses at https://ocw.mit.edu

## Transcript

**0:06** · MARTINA BALAGOVIC: Hi.

**0:07** · Welcome.

**0:08** · Today's problem is about finding solutions of this non-homogeneous linear system: x minus 2y minus 2z equals b\_1, 2x minus 5y minus 4z equals b\_2, and 4x minus 9y minus 8z equals b\_3.

**0:25** · And as you can see, the system doesn't only have numbers and unknowns, it also has parameters, b\_1, b\_2, and b\_3, and the solution will depend on these parameters, but also the existence of the solution will depend on these parameters.

**0:38** · And we're asked to find a solution and find when it exists, depending on the values of b\_1, b\_2, and b\_3.

**0:45** · So now you should pause the video, solve the problem, and come back and compare your solution with mine.

**0:57** · And we're back.

**0:58** · Let's try it.

**0:59** · Let's start by solving this system as though b\_1, b\_2, and b\_3 were numbers.

**1:04** · So we write the matrix of the system, which is 1, minus 2, minus 2, b\_1; and then 2, minus 5, minus 4, b\_2; and 4, minus 9 minus 8, b\_3.

**1:35** · And we do elimination.

**1:37** · So we multiply the first row by minus 2 and add it to the second row.

**1:44** · And we multiply it by minus 4 and add it to the third row.

**1:51** · And we get 1, minus 2, minus 2, b\_1; 0, 4 minus 5 is minus 1, 4 minus 4 is 0, and minus 2 times b\_1 plus b\_2.

**2:16** · And here we get 0, 8 minus 9 is minus 1, and 8 minus 8 is 0.

**2:26** · Finally, on the right-hand side, minus 4\*b\_1 plus b\_3.

**2:34** · And you can already see that something's going to happen here.

**2:37** · But let's do one more step.

**2:40** · So eliminating further, we get 1, minus 2, minus 2, b\_1; 0, minus 1, 0, minus 2\*b\_1 plus b\_2.

**3:03** · And in the last row we replace it with the last row minus the second row, and we get 0, 0, 0, minus 4\*b\_1 plus 2-- so minus minus 2\*b\_2 is minus 2\*b\_1 minus b\_2 and plus b\_3.

**3:30** · I hope I did this right.

**3:34** · So now let's think of it as a system again.

**3:36** · The last equation says 0 equals this expression in b\_1, b\_2, and b\_3.

**3:44** · So this is something to note down.

**3:48** · If minus 2\*b\_1 minus b\_2 plus b\_3 is some number that's not 0, then the last equation is going to say 0 equals nonzero.

**4:02** · It's never going to be satisfied, and the entire system is never going to have a solution.

**4:06** · So in this case, we have no solutions.

**4:22** · If this is equal to 0, so minus 2\*b\_1 minus b\_2 plus b\_3 is equal to 0, then let's do one more step on this matrix here.

**4:36** · Let's turn this number into 1 by multiplying this row by negative 1.

**4:42** · And let's use it to eliminate this number here as well.

**4:47** · So in this case, we get-- let me write it from the last row, which now becomes 0, 0, 0, equals 0, which is fine.

**4:58** · The second row becomes 0, 1, 0, 2\*b\_1 minus b\_2.

**5:07** · And the first one, to get rid of this minus 2, we multiply this row by negative 2 and add it to the first one.

**5:15** · We get 1, 0, negative 2, and here we get b\_1 plus 4\*b\_1 which is 5\*b\_1, minus 2\*b\_2.

**5:36** · The reason why we did it was to get the identity matrix here.

**5:40** · And now let's solve this.

**5:42** · These two columns, corresponding to variables x and y, have pivots in them.

**5:48** · So these are the pivot variables.

**5:56** · This column here has no pivot in it, so it's a free variable.

**6:04** · And now we're going to calculate the solutions, but by picking particular values for z, and then calculating the values for x and y.

**6:13** · We have two kinds of solution.

**6:15** · One kind is the particular solution.

**6:22** · So this one solves A\*x equals b.

**6:28** · There's only one of them.

**6:29** · And we get it by setting the free variable equal to 0.

**6:35** · Setting the free variable equal to 0, we get, well this is equal to 0.

**6:46** · The second equation says y equals this thing here, so 2\*b\_1 minus b\_2.

**6:55** · And the first equation says x minus 2 times 0 equals this expression here.

**7:03** · So 5\*b\_1 minus 2\*b\_2.

**7:10** · That's our particular solution.

**7:14** · The next kind is the special solution.

**7:21** · So remember, those solve A\*x equals 0.

**7:27** · There's as many of them as there are free variables.

**7:31** · In our case, there's only one.

**7:34** · And we get it by setting all free variables equal to 0, except one equal to 1.

**7:40** · And do it for every free variable.

**7:42** · So in our case there's only one free variable and we set z equal to 1.

**7:49** · The solution that we get in this case, and remember we're solving Ax equals 0-- we don't care about the right-hand side anymore-- so z is 1.

**7:59** · This second equation says y equals 0, and the first equation says x minus 2 times 1 equals 0.

**8:12** · In other words, x equals 2.

**8:17** · So the special solution is \[2, 0, 1\].

**8:21** · And now all solutions are of the form x equals the particular solution plus any multiple of the special solution.

**8:38** · Let me recap.

**8:39** · In case this particular combination of parameters is not 0, there's no solutions.

**8:46** · In case this particular combination of parameters is equal to 0, there are solutions, there are as many of them as there are real numbers c, and they're all of this form for these two vectors.

**9:00** · And that's all I wanted to say today.