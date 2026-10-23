> 对应主课笔记：[[L7 求解Ax=0主变量与特解]]（18.06SC 习题课）

![](https://www.youtube.com/watch?v=3cMyj8EKFGo)

MIT 18.06SC Linear Algebra, Fall 2011  
View the complete course: https://ocw.mit.edu/18-06SCF11  
Instructor: Martina Balagovic  
  
A teaching assistant works through a problem on solving Ax=0.  
  
License: Creative Commons BY-NC-SA  
More information at https://ocw.mit.edu/terms  
More courses at https://ocw.mit.edu

## Transcript

### Introduction to the problem

**0:07** · MARTINA BALAGOVIC: Hi.

**0:08** · Welcome back.

**0:09** · Today's problem is about solving homogeneous linear systems, A\*x equals 0, but it's also an introduction to the next lecture and next recitation section, which are going to be about solving non-homogeneous linear systems, A\*x equals b.

**0:24** · The problem is fill the blanks type.

**0:26** · And it says the set S of all points with coordinates x, y, and z, such that x minus 5y plus 2z equals 9 is a blank in R^3.

**0:39** · It is in a certain relation to the other blank S\_0 of all the points with coordinates x, y, and z that satisfy the following linear equation, x minus 5y plus 2z equals 0.

**0:54** · After we solve this, we have the second part of the problem, which says all points of x have a specific form, x, y, z equals blank, 0, 0, plus some parameter times blank, 1, 0 plus some other parameter times blank, 0, 1.

**1:12** · And we need to fill out all six blanks.

**1:15** · Now you should pause the video, fill in the blanks, and then come back and see some pretty pictures that I prepared for you.

### Identifying the planes

**1:28** · And we're back.

**1:30** · So you probably picked this up in lectures already.

**1:35** · If you have a three-dimensional space with three degrees of freedom, and put in one constraint, so put in one equation, you get something that has two degrees of freedom, something that's two-dimensional.

**1:48** · If this equation is linear, rather than quadratic or cubic or exponential, this something is something two-dimensional and flat.

**1:57** · Something two-dimensional and flat in R^3 is also called a plane, or a two-plane.

**2:05** · Similarly, S\_0 is also a plane.

**2:12** · Now, what's the relation between S and S\_0 if they're given by these two equations?

**2:17** · Well first let's look at the general positions in which two planes in R^3 can be.

**2:23** · First one is that they're intersecting along a line.

**2:27** · What's going to happen here is that all points on this plane are points whose coordinates satisfy the equation of this plane.

**2:35** · The points in this plane are points whose coordinates satisfy the equation of this plane.

**2:40** · And the points on the line are points whose coordinates satisfy the system of this equation and this equation.

**2:48** · The other position in which two planes can be is that they're not intersecting at all, that they're parallel.

**2:54** · So let's start by trying to find this line here.

### Analyzing the relationship

**2:58** · The equation of one plane is x minus 5y plus 2z equal 9.

**3:14** · The equation of the other one is x minus 5y plus 2z equals 0.

**3:23** · Now you can just look at it and see how many solutions it's supposed to have, or you can try doing elimination, and after one step of elimination get 0 equals 9, which never happens.

**3:33** · There cannot exist numbers x, y, and z such that this combination of them produces 0, and the same combination of them produces 9 at the same time.

**3:43** · So this red line here doesn't exist, and the situation of these two planes S and S\_0 is this one, they're parallel.

**3:51** · So let's add the word parallel in here.

**3:59** · And let's move on to the other half of the problem.

### Determining the specific form

**4:03** · The other half said all points of S have this specific form.

**4:08** · Now let me call this point here P\_0.

**4:14** · If all points of S have this form, we can plug in any parameter c\_1 and c\_2 here and we're going to get a point of the plane.

**4:22** · So in particular, we can plug in c\_1 and c\_2 equal to 0.

**4:30** · What we get then is that the point (x, y, z) equals P\_0 is a point of the plane S. So P\_0 is in S.

**4:43** · What do we know about the point P\_0?

**4:46** · Well the fact that it's in S means that its coordinates, x minus 5y plus 2z equal 9.

**4:58** · That's the equation of S. But we also know that y and z are equal to 0 and 0.

**5:11** · Solving this system we get that the x-coordinate of this point P\_0 is 9, and we can just add 9 here.

**5:25** · So we just have two blanks left to fill.

**5:28** · Before we'll fill them, let me show you a picture that I drew here.

### Visualizing parallel planes

**5:32** · So we have these two planes, S\_0 and S, which are parallel.

**5:38** · They're given by these equations.

**5:42** · And the plane S\_0 has a point 0 in it, because the equation is x minus 5y plus 2z equals 0, so it satisfied by 0, 0, 0.

**5:52** · The plane S has this point P\_0 in it, which is (9, 0, 0)-- we just figured this out.

**6:00** · And there's this vector connecting one plane to the other.

**6:05** · Now, since those two planes are parallel and there's this vector going between them, what we can see is that a good way to get any point in S is to go to any point in S\_0 and go up by this vector.

**6:21** · Now let me write this down.

**6:25** · What I just said is that any point in S is of the form-- use this vector to go up-- plus any point in S\_0.

**6:48** · And if we compare this to this expression here, we also get P\_0 plus this linear combination.

**6:55** · So this here has to be a point in S\_0.

**7:03** · Now we're left with a question of how to parameterize all points in S\_0.

### Solving the linear system

**7:06** · What are all the points in S\_0, and what does this problem have to do with solving homogeneous linear equations?

**7:12** · Well, let me write this equation of S\_0 in a slightly different way.

**7:18** · Let me write it as 1, minus 5, 2, x, y, z, equals 0.

**7:35** · And let me think of this as a matrix of the system.

**7:38** · It's a very tiny matrix, but it's a matrix.

**7:41** · And think of it as a matrix dot a vector equals 0, and trying to find all solutions of the system.

**7:47** · Well let's do row reductions here.

**7:50** · It's already as upper triangular as these tiny matrices get.

**7:54** · This is a pivot.

**7:58** · So we have a pivot variable x.

**8:05** · These are free variables, y and z.

**8:13** · And if you remember how to solve these systems, for each free variable we get one particular solution.

**8:24** · So we get one particular solution when we plug in y is 1 and all the other free variables are 0.

**8:33** · Plugging it in here, we just get that in that case, x-- so we get x minus 5 times 1 plus 2 times 0 equals 0.

**8:46** · So x is equal to 5.

**8:50** · And the other solution is for setting all free variables equal to 0, except z which we set equal to 1.

**8:57** · And then we get x minus 5 times 0 plus 2 times 1 equals 0.

**9:03** · So we get that in this case, x equals minus 2.

**9:10** · And any solution of this system is going to be of the form some constant times this plus some other constant times this.

**9:20** · And if we walk back to our original problem here, we see that these parameters, these numbers here, have been set up exactly so that we can just take these numbers and just copy them over, 5 and minus 2.

**9:36** · And this is the general form of any point of the plane S.

**9:39** · It's go up this vector, and then add a point in S\_0, in the parallel plane that passes through the origin.

**9:46** · This finishes our problem.

**9:47** · But what I would encourage you to do now is to go on to the next lecture, watch the next recitation video, and then come back here and think about what is it that we really did here on this half of the board.

**10:00** · Thank you.