![](https://www.youtube.com/watch?v=rHLEWRxRGiM)

What do 3d linear transformations look like?  
Help fund future projects: https://www.patreon.com/3blue1brown  
An equally valuable form of support is to simply share some of the videos.  
Home page: https://www.3blue1brown.com/  
  
Full series: http://3b1b.co/eola  
  
Future series like this are funded by the community, through Patreon, where supporters get early access as the series is being produced.  
http://3b1b.co/support  
  
Thanks to these viewers for their contributions to translations  
Hebrew: Omer Tuchfeld  
  
\------------------  
  
3blue1brown is a channel about animating math, in all senses of the word animate. And you know the drill with YouTube, if you want to stay posted about new videos, subscribe, and click the bell to receive notifications (if you're into that).  
  
If you are new to this channel and want to see more, a good place to start is this playlist: https://goo.gl/WmnCQZ  
  
Various social media stuffs:  
Website: https://www.3blue1brown.com  
Twitter: https://twitter.com/3Blue1Brown  
Patreon: https://patreon.com/3blue1brown  
Facebook: https://www.facebook.com/3blue1brown  
Reddit: https://www.reddit.com/r/3Blue1Brown

## Transcript

### Introduction to 3D

**0:00** · \[Submit subtitle corrections at criblate.com\] Hey folks, I've got a relatively quick video for you today, just sort of a footnote between chapters.

**0:19** · In the last two videos I talked about linear transformations and matrices, but I only showed the specific case of transformations that take two-dimensional vectors to other two-dimensional vectors.

**0:28** · In general throughout the series we'll work mainly in two dimensions, mostly because it's easier to actually see on the screen and wrap your mind around.

**0:36** · But more importantly than that, once you get all the core ideas in two dimensions, they carry over pretty seamlessly to higher dimensions.

**0:43** · Nevertheless, it's good to peek our heads outside of flatland now and then to, you know, see what it means to apply these ideas in more than just those two dimensions.

### 3D transformations

**0:52** · For example, consider a linear transformation with three-dimensional vectors as inputs and three-dimensional vectors as outputs.

**1:00** · We can visualize this by smooshing around all the points in three-dimensional space, as represented by a grid, in such a way that keeps the grid lines parallel and evenly spaced, and which fixes the origin in place.

**1:13** · And just as with two dimensions, every point of space that we see moving around is really just a proxy for a vector who has its tip at that point, and what we're really doing is thinking about input vectors moving over to their corresponding outputs.

**1:27** · And just as with two dimensions, one of these transformations is completely described by where the basis vectors go.

**1:34** · But now, there are three standard basis vectors that we typically use.

**1:38** · The unit vector in the x direction, i-hat, the unit vector in the y direction, j-hat, and a new guy, the unit vector in the z direction, called k-hat.

**1:47** · In fact, I think it's easier to think about these transformations by only following those basis vectors, since the full 3D grid representing all points can get kind of messy.

**1:56** · By leaving a copy of the original axes in the background, we can think about the coordinates of where each of these three basis vectors lands.

**2:05** · Record the coordinates of these three vectors as the columns of a 3x3 matrix.

**2:11** · This gives a matrix that completely describes the transformation using only nine numbers.

**2:17** · As a simple example, consider the transformation that rotates space 90 degrees around the y-axis.

### Matrix representations

**2:24** · So that would mean that it takes i-hat to the coordinates (0, 0, -1) on the z-axis.

**2:30** · It doesn't move j-hat, so it stays at the coordinates (0, 1, 0).

**2:34** · And then k-hat moves over to the x-axis at (1, 0, 0).

**2:40** · Those three sets of coordinates become the columns of a matrix that describes that rotation transformation.

**2:49** · To see where a vector with coordinates (x, y, z) lands, the reasoning is almost identical to what it was for two dimensions.

**2:56** · Each of those coordinates can be thought of as instructions for how to scale each basis vector so that they add together to get your vector.

**3:06** · And the important part, just like the 2D case, is that this scaling and adding process works both before and after the transformation.

**3:16** · So to see where your vector lands, you multiply those coordinates by the corresponding columns of the matrix, and then you add together the three results.

### Composition and applications

**3:29** · Multiplying two matrices is also similar.

**3:32** · Whenever you see two 3x3 matrices getting multiplied together, you should imagine first applying the transformation encoded by the right one, then applying the transformation encoded by the left one.

**3:44** · It turns out that 3D matrix multiplication is actually pretty important for fields like computer graphics and robotics, since things like rotations in three dimensions can be pretty hard to describe, but they're easier to wrap your mind around if you can break them down as the composition of separate, easier-to-think-about rotations.

**4:04** · Performing this matrix multiplication numerically is, once again, pretty similar to the two-dimensional case.

**4:10** · In fact, a good way to test your understanding of the last video would be to try to reason through what specifically this matrix multiplication should look like, thinking closely about how it relates to the idea of applying two successive transformations in space.

**4:32** · In the next video, I'll start getting into the determinant.