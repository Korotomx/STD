---
title: "An Overview of Key Ideas"
source: "https://www.youtube.com/watch?v=OZxzHcW663g&list=PL221E2BBF13BECF6C&index=6"
author:
  - "[[MIT OpenCourseWare]]"
published: 2018-07-26
created: 2026-10-20
description: "MIT 18.06SC Linear Algebra, Fall 2011View the complete course: https://ocw.mit.edu/18-06SCF11Instructor: Martina BalagovicA teaching assistant introduces key ideas found in the course 18.085. Li"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=OZxzHcW663g)

MIT 18.06SC Linear Algebra, Fall 2011  
View the complete course: https://ocw.mit.edu/18-06SCF11  
Instructor: Martina Balagovic  
  
A teaching assistant introduces key ideas found in the course 18.085.  
  
License: Creative Commons BY-NC-SA  
More information at https://ocw.mit.edu/terms  
More courses at https://ocw.mit.edu

## Transcript

### Problem introduction

**0:05** · MARTINA BALAGOVIC: Welcome.

**0:06** · Today's problem actually appeared in a quiz.

**0:10** · It appeared in quiz one in fall of 1999 as question four.

**0:16** · The problem puts the usual solve the following system upside down by saying we have some matrix and we know that all the solutions to A\*x equals this vector here, \[1, 4, 1, 1\], all the solutions to this problem are given by x equals \[0, 1, 1\] plus any number c times \[1, 2, 1\].

**0:38** · And we're asked to say everything that we can about the columns of the matrix A.

**0:43** · So I'm going to let you pretend that you are on an exam, try to solve it yourself, and then come back and compare your solution with mine.

### Analyzing matrix dimensions

**0:57** · OK, welcome back.

**0:58** · So the first thing that you should think about in this sort of situation is what is the size of A?

**1:04** · Well, we want to multiply A with an x that has three entries, so A should have three columns.

**1:14** · Let me call those columns c\_1, c\_2, and c\_3.

**1:25** · And when I take some linear combinations of c\_1, c\_2 and c\_3, I'm going to get this vector here, \[1, 4, 1, 1\].

**1:32** · So all the c\_i's, c\_1, c\_2, and c\_3 are vectors in R\_4.

### Particular and special solutions

**1:46** · Now, if you know about, if you learned about particular solutions and special solutions, then my notation here shouldn't surprise you.

**1:56** · I'm going to call this vector here x\_p, and this vector here x\_s.

**2:01** · And I'm going to use the fact that x\_p plus c times x\_s satisfies A times this equals b-- I will call this vector b-- for any number c.

**2:26** · In particular, what I'm going to conclude is that when c equals 0 we get A times x\_p equals b.

**2:40** · But also that when c equals 1, we get A times x\_p plus A times x\_s equals b.

**2:53** · Replacing this by b, we get that this implies that A times x\_s equals 0.

**3:04** · So in trying to find what are the columns c\_1, c\_2, and c\_3 of the matrix A, let's look at these two equations.

### Calculating matrix columns

**3:11** · x\_p satisfies A times x\_p equals b, and x\_s satisfies A times x\_s equals 0.

**3:19** · Again, if you know what particular and special solutions are this shouldn't surprise you.

**3:23** · But we also know what x\_p and x\_s are, so let's use them to try to calculate c\_1, c\_2, and c\_3.

**3:32** · A times x\_p equals b means that the linear combination of c\_1, c\_2, and c\_3 encoded in the vector x\_p, which is \[0, 1, 1\], gives the vector b.

**3:46** · So c\_1, c\_2, c\_3 times \[0, 1, 1\] gives us \[1, 4, 1, 1\].

**4:08** · In other words, c\_2 plus c\_3 equal b.

**4:17** · Let's turn our attention to A times x\_s equals 0.

**4:20** · This says that c\_1, c\_2, c\_3 times-- x\_s was defined to be \[0, 2, 1\]-- equals 0.

**4:37** · In other words, 2 times c\_2 plus c\_3 equals 0.

**4:47** · Now solving this system where the unknowns are vectors but it's still just a linear system, we can see, for example, from the second equation that c\_3 equals minus 2\*c\_2.

**5:00** · And plugging it back into the original equation, getting c\_2 minus 2\*c\_2 equals b, from which it follows that c\_2 is equal to minus b, and that c3 is equal to 2 times b.

**5:23** · So from this tiny amount of information-- we just knew the solutions to this one particular equation involving A-- we got the second column of A and the third column of A completely explicitly calculated.

**5:36** · Now, what can we say about the first column?

### Null space and rank

**5:39** · I said before that all the solutions of A\*x equals b are of the form a particular solution plus some number times a special solution.

**5:54** · And the information that we have is that there's just one number here.

**5:58** · So we said everything, once we remove this vector here, everything that we get here will satisfy A times x equals 0.

**6:09** · And the fact that everything that satisfies A times x equals 0 is a multiple of this one vector that was given to us means that the null space of A has dimension one.

**6:23** · There is just one special solution.

**6:26** · So dimension of the null space of A is 1.

**6:37** · So rank of A is the number of columns minus this dimension of null space, and it's equal to 2.

**6:49** · As rank of A is equal to 2, the number of linearly independent columns needs to be 2 as well.

**6:57** · So the only thing that we can say at this point is if the first column was also a multiple of b, as the second and the third are, then the rank would be smaller than 2.

**7:08** · So that is the only thing that cannot happen.

**7:11** · So c\_1 is not a multiple of b.

**7:22** · Not any multiple, including not a zero multiple.

**7:26** · And that's pretty much everything we can say.

**7:29** · Yes, if it was some other multiple of it, then we would be able to find some other vector here and we would have two parameters.

**7:34** · But it's not, and this is everything that we can say about it.