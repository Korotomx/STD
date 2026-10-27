![](https://www.youtube.com/watch?v=AmQcoopBUTk)

MIT 18.06SC Linear Algebra, Fall 2011  
View the complete course: https://ocw.mit.edu/18-06SCF11  
Instructor: Ben Harris  
  
A teaching assistant works through a problem on least squares approximation.  
  
License: Creative Commons BY-NC-SA  
More information at https://ocw.mit.edu/terms  
More courses at https://ocw.mit.edu

## Transcript

**0:07** · PROFESSOR: Hi, and welcome.

**0:09** · Today we're going to do a problem about least squares approximations.

**0:13** · Here's the question.

**0:15** · Find the quadratic equation through the origin that is a best fit for these three points: (1, 1), (2, 5), and (-1, -2).

**0:27** · I'll give you a minute to work that out on your own.

**0:30** · You can hit the pause button now, and we'll be back in a minute to work the problem out together.

**0:47** · OK and we're back.

**0:50** · So what's the first step in a problem like this?

**0:53** · The first step is figuring out what our equation looks like, the one that we're going to find.

**1:00** · So our equation is going to look like c\*t plus d t squared equals y.

**1:10** · So that's what we're looking for.

**1:11** · We're looking for a quadratic equation through the origin.

**1:15** · Now, if it were just any quadratic equation, then we would have a constant term, but through the origin just means that the constant term is 0.

**1:25** · Now, what's the next step?

**1:28** · Next we need to set up a matrix equation.

### Set Up a Matrix Equation

**1:31** · So we need an A, a matrix A. And which matrix is that going to be?

**1:46** · Well, let me start with the first coordinate of these three points.

**1:52** · And I'm going to put them in the first column of this matrix, 1, 2, -1.

**1:59** · And then my second column is going to be the squares of these coordinates, 1, 4, and 1.

**2:08** · And my x hat-- that's just c and d.

**2:14** · And my b-- this is going to be the second coordinates, 1, 5, and -2.

**2:25** · OK, why did I set this problem up like that?

**2:28** · Well, multiply A times x hat.

**2:34** · The first coordinate of A times x hat is 1 times c plus 1 times d.

**2:41** · It's just the same as plugging in this first point into the left-hand side of this equation.

**2:48** · And similarly, if I took the second point and plugged it in here, I would just get 2 times c plus 4 times d, which is just the same as the second coordinate in the multiplication A times x hat.

**3:02** · 2 times c plus 4 times d.

**3:06** · OK, and where did the b come from?

**3:08** · Well, b came from plugging in these points to the right-hand side.

**3:12** · So 1, 5, and -2 are just the y-coordinates of these three points.

**3:19** · So it would be great if we could solve A x hat equals b.

**3:27** · But we can't solve A x hat equals b, because there isn't a quadratic equation through the origin that contains these three points.

**3:41** · But we need to find the best approximation to that, so that's the same as solving A x hat equals the projection of b onto the column space of A.

**3:51** · Because we only have a chance of solving A x hat equals something if it's in the column space of A.

**3:57** · And remember from our projections part of the class that this is the same as solving A transpose A x hat equals A transpose b.

**4:17** · So that's what we're really going to do.

**4:19** · We're really going to solve A transpose A x hat equals A transpose b.

**4:24** · And now all we have to do is just a computation.

**4:27** · So let's do it.

**4:32** · So what is A transpose A?

**4:36** · I'm going to do this kind of quickly, because you should be good at multiplying matrices by now.

**4:56** · Oh this-- I have the negative in the wrong place, thank you.

**5:02** · Thanks for that correction.

**5:03** · I have the negative backwards there.

**5:10** · And what do I get when I multiply these?

**5:13** · I'll let you check.

**5:14** · This is 6, 8; 8, and 10.

**5:22** · And what is A transpose b?

**5:34** · Well, if you multiply this out, I'll let you check that you get 13 and 19.

**5:46** · So this is just some computation.

**5:49** · And so what we're solving here is \[6, 8; 8, 10\] times x hat equals \[13; 19\].

**5:59** · And we remember how to do this just by using elimination.

**6:04** · We replace the second row by 3 times the second row minus 4 times the first row.

**6:11** · Again, I'm going to do this quickly because you know this from other parts of the class.

**6:18** · You similarly change the b vector, and we backsolve to get d is -5/2 and c equals-- let's plug that in and see-- think you're going to get 11 over 2.

**6:40** · So what's our final equation?

### Final Equation

**6:44** · Our final equation is y equals 11/2 t minus 5/2 t squared.

**7:04** · OK.

**7:04** · So this is our best fit quadratic equation through the origin.

**7:10** · Now before I end, let me do a couple things.

**7:13** · First, let me go back and review what the key steps were.

### Key Steps

**7:18** · Whenever you're faced with such a best fit equation, first, you want to see what the general form of the equation is.

**7:26** · Next you want to write it in terms of matrices.

**7:29** · Write down your matrix A and your vector b.

**7:33** · And lastly, you set up your projection equation.

**7:38** · And then all you have to do is just a computation.

**7:43** · But it might also be worth noting that these three points certainly aren't on this quadratic equation.

**7:51** · For instance, if I plug in 1 here, I don't get (1, 1), I get (1, 3).

**7:56** · But that's OK.

**7:58** · This is as close as we can do.

**8:01** · Thanks.

关联：[[Linear Algebra/主页|线性代数]]
