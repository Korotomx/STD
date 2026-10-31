![](https://www.youtube.com/watch?v=qEBi0K5wfOs)

MIT 18.06SC Linear Algebra, Fall 2011  
View the complete course: https://ocw.mit.edu/18-06SCF11  
Instructor: Linan Chen  
  
A teaching assistant works through a problem on determinants and volume.  
  
Watch this video in Chinese: https://youtu.be/ZuWAwCEMeWE  
License: Creative Commons BY-NC-SA  
More information at https://ocw.mit.edu/terms  
More courses at https://ocw.mit.edu

## Transcript

### Introduction

**0:07** · LINAN CHEN: Hello.

**0:07** · Welcome back to recitation.

**0:09** · I'm sure you are becoming more and more familiar with the determinants of matrices.

**0:15** · In the lecture, we also learned the geometric interpretation of the determinant.

**0:20** · The absolute value of the determinant of a matrix is simply equal to the volume of the parallelepiped spanned by the row vectors of that matrix.

### Problem

**0:32** · So today, we're going to apply this fact to solve the following problem.

**0:38** · I have a tetrahedron, T, in this 3D space.

**0:43** · And the vertices of T are given by O, which is the origin, A\_1, A\_2, and A\_3.

**0:54** · So I have highlighted this tetrahedron using the blue chalk.

**0:59** · So this is T.

**1:03** · And our first goal is to compute the volume of T using the determinant.

**1:10** · And the second part is: if I fix A\_1 and A\_2, but move A\_3 to another point, A\_3 prime, which is given by this coordinate, I ask you to compute the volume again.

**1:26** · OK.

**1:27** · So since we want to use the fact that the determinant is related to the volume, we have to figure out which volume we should be looking at.

**1:37** · We know that the determinant is related to the volume of a parallelepiped.

**1:43** · But here, we only have a tetrahedron.

**1:46** · So the first goal should be to find out which parallelepiped you should be working with.

**1:52** · OK, why don't you hit pause and try to work it out yourself.

**1:56** · You can sketch the parallelepiped on this picture.

**2:00** · And I will return in a while and continue working with you.

### Solution

**2:12** · All right.

**2:13** · How did your computation go?

**2:15** · Now let's complete this picture together.

**2:19** · As we were saying, we need a parallelepiped so that we can use the fact that the determinant is related to the volume.

**2:27** · Here, I have a tetrahedron.

**2:30** · And let's look at these three edges, OA\_1, OA\_2, and OA\_3.

**2:39** · All of them meet at the origin.

**2:42** · So why don't we just consider the parallelepiped spanned by those same three edges?

**2:49** · It's a natural choice, because at least it shares three edges with T.

**2:54** · OK, now let's move on to this picture here.

**2:58** · As you can see, I have drawn this parallelepiped in red chalk.

**3:05** · So the blue part is my original T.

**3:11** · And the red part, let me call it P.

**3:14** · It's the parallelepiped spanned by edges OA\_1, OA\_2, and OA\_3.

**3:21** · So that's the parallelepiped that I'm going to work with.

**3:25** · Now the next step is to relate the volume of T to the volume of P. OK, let's recall together what is the volume of a tetrahedron.

**3:37** · We note that the volume of a tetrahedron is going to be equal to 1/3 of the area of the base times the height, right?

**3:54** · Of course, you can choose any side, any face to be the base.

**3:59** · But for convenience, we're going to choose the triangle OA\_1A\_2 to be the base of T. So the volume of T is going to be equal to 1/3 times the area of triangle OA\_1A\_2.

**4:18** · So I use this A to indicate the area.

**4:22** · Then times the height.

**4:24** · Well, if I choose this to be my base, then this A\_3 becomes the apex.

**4:31** · Then the height is simply equal to the distance from A\_3 to the triangle OA\_1A\_2.

**4:39** · Let me use letter h to denote this quantity.

**4:43** · So that's the height.

**4:44** · And the volume of T is equal to 1/3 of the product of the area of the base times the height.

**4:52** · OK, this is the volume of T. Now let's see what the volume of P is.

**5:01** · So P is a parallelepiped.

**5:03** · The volume of a parallelepiped is simply equal to the area of the base times its height.

**5:12** · This time, which face would you choose to be the base?

**5:17** · Well, of course, you would like to choose this parallelogram to be the base because it contains the base of T.

**5:26** · If we do so, so we want to choose this parallelogram to be the base, then what is the area of this?

**5:35** · Well, it clearly contains two copies of the triangle OA\_1A\_2.

**5:43** · So the area of the parallelogram is simply equal to twice the area of the triangle OA\_1A\_2.

**5:56** · Then what is the height of P?

**5:59** · Again, if you choose this face to be the base, then A\_3 becomes the apex again.

**6:07** · Then the height of the parallelepiped is equal to the distance from A\_3 to the base, which is the same as the distance from A\_3 to triangle OA\_1A\_2.

**6:20** · So here, the height is also equal to h.

**6:28** · Now you can compare these two formulae.

**6:31** · You see that volume of T is simply equal to 1/6 of volume of P. That's the connection between the volume of the tetrahedron with the volume of the parallelepiped.

**6:51** · In order to compute the volume of T, we only need to compute the volume of P.

**6:57** · Now let's compute the volume of this parallelepiped.

**7:03** · We know that it's related to the determinant of a matrix.

**7:10** · And the row vectors of that matrix are given by these three edges.

**7:17** · So because all of them start from 0, we only need the coordinate of A\_1, A\_2, and A\_3.

**7:25** · So here, volume of P is equal to the absolute value.

**7:30** · So don't forget the absolute value sign.

**7:33** · Absolute value of the determinant of a three by three matrix.

**7:39** · So we just need to copy the coordinates of the vertices down here.

**7:44** · The first one is \[2, 2, -1\].

**7:49** · These two are too close.

**7:54** · -1.

**7:55** · And A\_2 is \[1, 3, 0\].

**8:01** · A3 is \[-1, 1, 4\].

**8:07** · The absolute value of this determinant.

**8:11** · And if you compute this, this is a three by three matrix.

**8:17** · The determinant should be easy to compute.

**8:20** · And the result should be 12.

**8:25** · So that's the volume of P, which means the volume of the tetrahedron T is equal to 12 over 6, which is 2.

**8:38** · Did you get the correct answer?

**8:41** · OK, so in order to compute the volume of T, we have related to a parallelepiped, P, which contains T. All right.

**8:52** · Now let's look at the second part.

**8:54** · The second part says that if I keep A\_1 and A\_2 unchanged, but I move A\_3 to a new point-- so A3 is going to be moved to a point given by A\_3 prime, and the coordinate is -201, -199, and 104.

**9:23** · And I'm asking you to compute the volume of the new tetrahedron.

**9:29** · Well as you can see, this point seems to be far away from the origin.

**9:35** · I'm not even able to draw this point here.

**9:39** · But you can imagine, as this point goes far away from the origin, this spike is going to become more and more pointy.

**9:47** · In other words, the entire tetrahedron looks more and more like a needle.

**9:52** · But nonetheless, we can use the same method to compute the volume.

**9:56** · So we follow the same idea, the volume of T is going to be equal to 1/6 of the volume of P.

**10:08** · And in this case, that's going to become the absolute value of the determinant of a three by three matrix whose row vectors are given by these three edges.

**10:23** · So in this case, we again copy down the coordinates of three vertices.

**10:29** · The first one is \[2, 2, -1\].

**10:33** · The second one is \[1, 3, 0\].

**10:36** · The third one should become this, so \[-201, 199, 104\].

**10:48** · OK.

**10:49** · That should give me the volume of the new tetrahedron.

**10:53** · Let me call it T prime just to differentiate it from the previous tetrahedron.

**10:59** · And of course, you can compute this determinant explicitly.

**11:04** · If you do so, you will see the answer should be 2 again.

**11:12** · But in fact, there is a way that you can just read out the answer directly without any real computation.

**11:22** · Let's pay attention to the last row.

**11:24** · In other words, let's pay attention to this new A\_3, well, A\_3 prime.

**11:31** · What do you observe here?

**11:34** · A\_3 prime, if you consider the difference between A\_3 and A\_3 prime, in other words, if you consider how much you have moved your apex, you will see that's equal to -100\*A\_1.

**11:52** · Right?

**11:52** · So A\_3 is \[-1, 1, 4\].

**11:57** · A\_3 prime is this.

**11:59** · That's exactly equal to -100 times A\_1.

**12:04** · What does that mean?

**12:06** · Well from the point of view of the matrix, you are subtracting from the original third row 100 times the first row.

**12:18** · But this row operation does not change the determinant.

**12:22** · In other words, you know that this determinant should be the same as the previous one.

**12:27** · So you can write out 2 directly.

**12:31** · From this picture, we can also see that fact.

**12:36** · So from this picture, we know that this section is saying that I need to move A\_3 in the inverse direction of A\_1 by 100 times A\_1.

**12:50** · So you're moving A\_3 parallel to A\_1.

**12:54** · But it doesn't matter how far you've moved your apex.

**12:58** · You're moving in a way that remains parallel to the base, which is saying that this movement does not change the height.

**13:07** · Since A\_1 and A\_2 are fixed, your base is fixed, and you're not changing the height.

**13:14** · So of course, the volume is not changing.

**13:17** · That's also a reason, another way to see that the volume of T prime is simply equal to the volume of T.

**13:26** · OK, this completes this problem.

**13:29** · I hope this example was helpful to you.

**13:32** · And we should keep in mind that the fact that the determinant is related to volume sometimes can become very handy in computing the volume of certain geometric objects.

**13:44** · Thank you for watching, and I'm looking forward to seeing you soon.