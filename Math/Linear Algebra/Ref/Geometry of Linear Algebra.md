---
title: "Geometry of Linear Algebra"
source: "https://www.youtube.com/watch?v=My5w4MXWBew&list=PL221E2BBF13BECF6C&index=4"
author:
  - "[[MIT OpenCourseWare]]"
published: 2018-07-26
created: 2026-10-20
description: "MIT 18.06SC Linear Algebra, Fall 2011View the complete course: https://ocw.mit.edu/18-06SCF11Instructor: Linan ChenA teaching assistant works through a problem on the geometry of linear algebra."
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=My5w4MXWBew)

MIT 18.06SC Linear Algebra, Fall 2011  
View the complete course: https://ocw.mit.edu/18-06SCF11  
Instructor: Linan Chen  
  
A teaching assistant works through a problem on the geometry of linear algebra.  
  
Watch this in Chinese: https://youtu.be/mgbjhzDndOY  
License: Creative Commons BY-NC-SA  
More information at https://ocw.mit.edu/terms  
More courses at https://ocw.mit.edu

## Transcript

**0:06** · PROFESSOR: Hello, I'm Linan.

**0:08** · Welcome to the recitation of Linear Algebra.

**0:11** · It's my great pleasure to guide you through the first recitation.

**0:15** · In the first lecture, we learned some important concepts.

**0:19** · We discussed how to view a linear system of equations from different points.

**0:26** · And we discussed the concepts such as row picture, column picture, and the form in matrix.

**0:34** · Some of them may be new to you.

**0:36** · So today, we're going to use this simple example to review those concepts.

**0:43** · We're going to work with this simple system of two equations with two unknowns.

**0:51** · So I would like you to first solve it, and then to find out the associated row picture and column picture with this system.

**1:02** · After you're done, we're also going to discuss the matrix form of this linear system.

**1:08** · Why don't you pause the video now and try to work them out on your own.

**1:14** · A good suggestion would be, you can try to sketch your answer in an xy coordinate like this.

**1:22** · OK, I'll see you in a while.

**1:35** · I hope you have just had some fun with it.

**1:38** · Let's work on it together.

**1:40** · Well, we're going to solve these equations.

**1:44** · As you can see, we have two unknowns, x and y.

**1:48** · And they have to satisfy these two equations at the same time.

**1:54** · How would you solve it?

**1:56** · A very simple way would be you substitute x by y, in terms of y.

**2:04** · So let's do it this way.

**2:06** · So we use the second equation to rewrite x as 2y minus 1.

**2:14** · So 2y minus 1.

**2:18** · Then you plug this into the first equation.

**2:24** · This implies twice-- x would be replaced by this-- 2 times 2y minus 1 plus y is equal to 3.

**2:38** · When you simplify this equation here, you will arrive at that 5y minus 2 is equal to 3.

**2:53** · That simply tells you y is equal to 1.

**2:59** · If y is equal to 1, then we go back to this formula.

**3:04** · We see that x is also equal to 1.

**3:09** · That's it.

**3:10** · This is the answer to this linear system.

**3:13** · And it's easy enough.

**3:15** · Both x and y are 1.

**3:18** · Now, let's try to find out its row picture and column picture.

**3:24** · So I'm going to work on this xy coordinate here.

**3:30** · First, let's look at row picture.

**3:37** · Please review what a row picture is.

**3:42** · So by row picture, I mean you have to look at this linear system according to each row.

**3:50** · So what is the first row?

**3:52** · Well, the first row is an equation with two unknowns.

**3:55** · So 2 times x plus y is equal to 3.

**3:59** · What is this equation, exactly?

**4:03** · As you may remember, this equation actually gives you a straight line in xy-plane.

**4:09** · So now let's put the line here.

**4:12** · I want a line that satisfies 2x plus y is 3.

**4:19** · Let's first set x to be 0.

**4:23** · If x is 0, by the first equation, y should be 3, which is here.

**4:32** · Now, let's set x to be 1.

**4:34** · If x is 1, then y is also 1.

**4:41** · So what I have now are two points on the line.

**4:46** · And this is enough, because on the xy-plane, two points will uniquely determine a straight line.

**4:53** · And that's the line we're looking for.

**4:55** · So all we need to do is to connect these two points.

**5:00** · Let me try to draw this line straight.

**5:15** · So this is the line that is given by 2x plus y is equal to 3.

**5:23** · This is the easiest way to determine a line.

**5:26** · You just need to pick two points that are on the line.

**5:30** · Then you connect them, and here you have the straight line.

**5:35** · So that's the first row.

**5:38** · Now let's look at the second row.

**5:40** · The second row is x minus 2y is equal to -1.

**5:45** · Same thing.

**5:46** · We're going to locate two points on the second line.

**5:49** · So again, let's set x to be 0 first.

**5:53** · If x is 0, then y should be 1/2, right?

**5:57** · So this line has to cross this point.

**6:01** · That's x, 0; y, 1/2.

**6:05** · Then let's put x to be 1 again.

**6:07** · So if x is 1, then y is also 1.

**6:11** · So we're going to use the same point here.

**6:15** · Now we have two points in the second line to connect them.

**6:21** · So by connecting them, I will have my second straight line.

**6:28** · So this is the line corresponding to x minus 2y is -1.

**6:39** · This is the row picture, because we have separated the two equations, and we look at them respectively.

**6:48** · The first equation gives me this line, and the second equation gives me this line.

**6:55** · Then what do I mean by solving this linear system?

**7:00** · Well, we are putting these two lines together, and we are looking at a point which is on the first line and second line at the same time.

**7:09** · Then clearly, that's the point where they intersect, right?

**7:14** · We can see from the answer over there, the coordinate of this point should be (1, 1).

**7:25** · This is also clear from the construction of the two lines.

**7:28** · We have noticed that this point is on the first line and the second line at the same time.

**7:35** · Two lines meeting at the point (1, 1).

**7:39** · That's the row picture of this linear system.

**7:43** · Now, let's move on to the column picture.

**7:48** · Again, I will need an xy coordinate.

**7:59** · So, where can I find my columns?

**8:04** · If you look at the two equations, then you focus on the coefficient in front of x in both equations.

**8:17** · What would that be?

**8:19** · Well, in the first equation, I have a 2 in front of x.

**8:25** · In the second equation, I have a 1 in front of x.

**8:29** · I want to put them together as a column vector.

**8:36** · Let me call it v\_1.

**8:43** · And I'm going to do the same thing to the coefficients in front of y.

**8:48** · In the first equation, I have a 1 in front of y.

**8:52** · In the second equation, I have a -2 in front of y.

**8:57** · Put them together.

**8:59** · Call it a column vector v\_2.

**9:07** · These are the columns I'm looking for.

**9:11** · Then what does that linear system say?

**9:14** · Well, I have extracted the coefficients in front of x.

**9:19** · Now I can consider x to be the coefficient of this vector.

**9:25** · And same thing, I'm going to view y as the coefficient of this vector.

**9:33** · Then what that linear system is doing is just to sum them up.

**9:40** · That gives you the left-hand side of the linear system.

**9:44** · What is the right-hand side?

**9:47** · Again, you put the two constants as a column vector, which is \[3, -1\].

**9:56** · That is the right-hand side.

**10:00** · So what I'm doing here is I'm taking the linear combination of v\_1 and v\_2.

**10:08** · And the coefficients are given by x and y, respectively.

**10:13** · And I want the result of this combination to be \[3, -1\].

**10:21** · Now let's incorporate this into this picture.

**10:25** · I have a v\_1, so I'm going to draw a vector v\_1.

**10:30** · x is 2, y is 1, so v\_1 is here.

**10:39** · That's v\_1.

**10:42** · And I need a v\_2.

**10:44** · x is 1.

**10:45** · y is -2.

**10:49** · So that's my v\_2.

**10:56** · I want to take the sum of x multiple of v\_1 and y multiple of v\_2.

**11:05** · And I want the result to be \[3, -1\].

**11:09** · Well, taking a hint from the previous consideration, we know that both x and y should be 1.

**11:21** · So I'm actually summing one copy of v\_1 and one copy of v\_2.

**11:30** · So how do you indicate the sum of these two vectors?

**11:35** · You complete the parallelogram spanned by these two vectors.

**11:43** · Then the vector given by the diagonal is the sum of v\_1 and v\_2.

**11:54** · Is this vector going to be \[3, -1\]?

**11:58** · Well, we can check.

**11:59** · The x-coordinate will be 2 plus 1, which is 3.

**12:04** · That's 2 plus 1, 3.

**12:08** · And the y-coordinate will be 1 minus 2.

**12:13** · So 1 minus 2, which should be -1.

**12:18** · That's it.

**12:20** · That's one multiple of v\_1 and one multiple of v\_2.

**12:24** · The sum will be \[3, -1\].

**12:28** · And that's the row picture.

**12:30** · Where does that that "x is equal to y is equal to 1" come from?

**12:35** · It comes from solving the linear system.

**12:37** · It comes from the row picture.

**12:41** · So here, we have found out the row picture and the column picture of this linear system.

**12:48** · What I would like to mention is the matrix form of this linear system.

**12:55** · So what is the matrix form?

**13:06** · What if I put these two column vectors together?

**13:10** · So I want to put them back to back, v\_1 and v\_2.

**13:18** · And I call this matrix to be A. So if you write it out, A should be given by 2, 1; 1, -2.

**13:33** · Matrix A has v\_1 and v\_2 as its column vectors, and it's a 2-by-2 matrix.

**13:41** · If I consider-- if I take this into account, then what will be the left-hand side of the linear system?

**13:51** · In other words, what would be the left-hand side of this equation?

**13:56** · This is actually matrix A multiplying a vector given by x, y.

**14:03** · So that's \[2, 1; 1, -2\] multiplying x and y.

**14:12** · So you put both unknowns together as a column vector.

**14:17** · That's the left-hand side of the equation.

**14:21** · And again, the right-hand side is given by this column vector, \[3; -1\].

**14:30** · This is the matrix form of this linear system.

**14:34** · We can actually solve this directly.

**14:36** · In other words, we can get this unknown vector at once, both x-coordinate and y-coordinate.

**14:47** · Let's recall, if you have a scalar equation like this-- let's say a is some constant times x is unknown is equal to b.

**14:58** · If a is non-zero, what would be x?

**15:02** · So clearly, x should be b over a.

**15:06** · I can also write it as a inverse times b.

**15:12** · That's what we do when we have numbers.

**15:14** · So here, what we want to apply is a similar idea but to matrix.

**15:21** · What you want to find is a matrix A inverse such that A inverse times A is equal to an identity matrix, which is \[1, 0; 0, 1\].

**15:41** · This may be new to you, but as you go further into this course, this idea will become more and more natural.

**15:50** · If such an inverse matrix exists, then what would be this vector here?

**15:58** · Then \[x; y\] will simply be A inverse times \[3; -1\].

**16:12** · That will give you the answer.

**16:16** · Here, I'm not going to go into detail, but we will return to this later in this course.

**16:23** · I hope this simple example is helpful to you in reviewing what you've learned in the lecture.

**16:30** · Thank you for watching, and I'm looking forward to seeing you again.