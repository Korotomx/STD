![](https://www.youtube.com/watch?v=kYB8IZa5AuE)

Quite possibly the most important idea for understanding linear algebra.  
Help fund future projects: https://www.patreon.com/3blue1brown  
An equally valuable form of support is to simply share some of the videos.  
Home page: https://www.3blue1brown.com  
  
Full series: http://3b1b.co/eola  
  
Future series like this are funded by the community, through Patreon, where supporters get early access as the series is being produced.  
http://3b1b.co/support  
  
Thanks to these viewers for their contributions to translations  
Hebrew: Omer Tuchfeld  
Spanish: Juan Carlos Largo  
Vietnamese: @ngvutuan2811  
  
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

### Visualizing transformations

**0:00** · \[Submit subtitle corrections at criblate.com\] Hey everyone!

**0:13** · If I had to choose just one topic that makes all of the others in linear algebra start to click, and which too often goes unlearned the first time a student takes linear algebra, it would be this one.

**0:22** · The idea of a linear transformation and its relation to matrices.

**0:26** · For this video, I'm just going to focus on what these transformations look like in the case of two dimensions, and how they relate to the idea of matrix-vector multiplication.

**0:35** · In particular, I want to show you a way to think about matrix-vector multiplication that doesn't rely on memorization.

**0:43** · To start, let's just parse this term, linear transformation.

**0:47** · Transformation is essentially a fancy word for function.

**0:50** · It's something that takes in inputs and spits out an output for each one.

**0:53** · Specifically, in the context of linear algebra, we like to think about transformations that take in some vector and spit out another vector.

**1:02** · So why use the word transformation instead of function if they mean the same thing?

**1:07** · Well, it's to be suggestive of a certain way to visualize this input-output relation.

**1:11** · You see, a great way to understand functions of vectors is to use movement.

**1:16** · If a transformation takes some input vector to some output vector, we imagine that input vector moving over to the output vector.

**1:25** · Then to understand the transformation as a whole, we might imagine watching every possible input vector move over to its corresponding output vector.

**1:34** · It gets really crowded to think about all of the vectors all at once, each one as an arrow.

**1:39** · So as I mentioned last video, a nice trick is to conceptualize each vector not as an arrow, but as a single point, the point where its tip sits.

**1:48** · That way, to think about a transformation taking every possible input vector to some output vector, we watch every point in space moving to some other point.

**1:57** · In the case of transformations in two dimensions, to get a better feel for the whole shape of the transformation, I like to do this with all of the points on an infinite grid.

**2:06** · I also sometimes like to keep a copy of the grid in the background, just to help keep track of where everything ends up relative to where it starts.

**2:14** · The effect for various transformations moving around all of the points in space is, you've got to admit, beautiful.

**2:21** · It gives the feeling of squishing and morphing space itself.

**2:25** · As you can imagine though, arbitrary transformations can look pretty complicated.

**2:30** · But luckily, linear algebra limits itself to a special type of transformation, ones that are easier to understand, called linear transformations.

### Linearity properties

**2:39** · Visually speaking, a transformation is linear if it has two properties.

**2:43** · All lines must remain lines without getting curved, and the origin must remain fixed in place.

**2:50** · For example, this right here would not be a linear transformation, since the lines get all curvy.

**2:56** · And this one right here, although it keeps the lines straight, is not a linear transformation, because it moves the origin.

**3:02** · This one here fixes the origin, and it might look like it keeps lines straight, but that's just because I'm only showing the horizontal and vertical grid lines.

**3:09** · When you see what it does to a diagonal line, it becomes clear that it's not at all linear, since it turns that line all curvy.

**3:16** · In general, you should think of linear transformations as keeping grid lines parallel and evenly spaced.

**3:23** · Some linear transformations are simple to think about, like rotations about the origin.

**3:28** · Others are a little trickier to describe with words.

**3:32** · So, how do you think you could describe these transformations numerically?

### Basis vectors and matrices

**3:35** · If you were, say, programming some animations to make a video teaching the topic, what formula do you give the computer so that if you give it the coordinates of a vector, it can give you the coordinates of where that vector lands?

**3:48** · It turns out that you only need to record where the two basis vectors, i-hat and j-hat, each land, and everything else will follow from that.

**3:57** · For example, consider the vector v with coordinates (-1, 2), meaning that it equals −1 times i-hat plus 2 times j-hat.

**4:08** · If we play some transformation and follow where all three of these vectors go, the property that grid lines remain parallel and evenly spaced has a really important consequence.

**4:19** · The place where v lands will be -1 times the vector where i-hat landed plus 2 times the vector where j-hat landed.

**4:25** · In other words, it started off as a certain linear combination of i-hat and j-hat, and it ends up as that same linear combination of where those two vectors landed.

**4:35** · This means you can deduce where v must go based only on where i-hat and j-hat each land.

**4:41** · This is why I like keeping a copy of the original grid in the background.

**4:45** · For the transformation shown here, we can read off that i-hat lands on the coordinates (1, -2), and j-hat lands on the x-axis over at the coordinates (3, 0).

**4:55** · This means that the vector represented by -1 i-hat plus 2 times j-hat ends up at -1 times the vector (1, -2) plus 2 times the vector (3, 0).

**5:07** · Adding that all together, you can deduce that it has to land on the vector (5, 2).

**5:14** · This is a good point to pause and ponder, because it's pretty important.

**5:18** · Now, given that I'm actually showing you the full transformation, you could have just looked to see that v has the coordinates (5, 2).

**5:25** · But the cool part here is that this gives us a technique to deduce where any vectors land so long as we have a record of where i-hat and j-hat each land without needing to watch the transformation itself.

**5:38** · Write the vector with more general coordinates, x and y, and it will land on x times the vector where i-hat lands, (1, -2), plus y times the vector where j-hat lands, (3, 0).

**5:51** · Carrying out that sum, you see that it lands at (1x + 3y, -2x + 0y).

**5:58** · I give you any vector, and you can tell me where that vector lands using this formula.

**6:04** · What all of this is saying is that a two-dimensional linear transformation is completely described by just four numbers, the two coordinates for where i-hat lands and the two coordinates for where j-hat lands.

**6:17** · Isn't that cool?

**6:18** · It's common to package these coordinates into a 2x2 grid of numbers called a 2x2 matrix, where you can interpret the columns as the two special vectors where i-hat and j-hat each land.

### Matrix multiplication

**6:30** · If you're given a 2x2 matrix describing a linear transformation and some specific vector, and you want to know where that linear transformation takes that vector, you can take the coordinates of the vector, multiply them by the corresponding columns of the matrix, then add together what you get.

**6:48** · This corresponds with the idea of adding the scaled versions of our new basis vectors.

**6:54** · Let's see what this looks like in the most general case, where your matrix has entries "a", "b", "c", "d".

**7:01** · And remember, this matrix is just a way of packaging the information needed to describe a linear transformation.

**7:06** · Always remember to interpret that first column, (a, c), as the place where the first basis vector lands, and that second column, (b, d), as the place where the second basis vector lands.

**7:17** · When we apply this transformation to some vector (x, y), what do you get?

**7:22** · Well, it'll be x times (a, c) plus y times (b, d).

**7:28** · Putting this together, you get a vector (ax + by, cx + dy).

**7:33** · You could even define this as matrix vector multiplication, when you put the matrix on the left of the vector like it's a function.

**7:41** · Then, you could make high schoolers memorize this without showing them the crucial part that makes it feel intuitive.

**7:48** · But, isn't it more fun to think about these columns as the transformed versions of your basis vectors, and to think about the result as the appropriate linear combination of those vectors?

**8:00** · Let's practice describing a few linear transformations with matrices.

### Example transformations

**8:04** · For example, if we rotate all of space 90 degrees counterclockwise, then i-hat lands on the coordinates (0, 1).

**8:13** · And j-hat lands on the coordinates (-1, 0).

**8:17** · So the matrix we end up with has columns (0, 1), (-1, 0).

**8:22** · To figure out what happens to any vector after a 90-degree rotation, you could just multiply its coordinates by this matrix.

**8:31** · Here's a fun transformation with a special name, called a shear.

**8:35** · In it, i-hat remains fixed, so the first column of the matrix is (1, 0).

**8:39** · But j-hat moves over to the coordinates (1, 1), which become the second column of the matrix.

**8:45** · And at the risk of being redundant here, figuring out how a shear transforms a given vector comes down to multiplying this matrix by that vector.

**8:55** · Let's say we want to go the other way around, starting with a matrix, say with columns (1, 2) and (3, 1), and we want to deduce what its transformation looks like.

**9:04** · Pause and take a moment to see if you can imagine it.

**9:08** · One way to do this is to first move i-hat to (1, 2), then move j-hat to (3, 1).

**9:15** · Always moving the rest of space in such a way that keeps gridlines parallel and evenly spaced.

**9:21** · If the vectors that i-hat and j-hat land on are linearly dependent, which, if you recall from last video, means that one is a scaled version of the other, it means that the linear transformation squishes all of 2D space onto the line where those two vectors sit, also known as the one-dimensional span of those two linearly dependent vectors.

**9:44** · To sum up, linear transformations are a way to move around space such that gridlines remain parallel and evenly spaced, and such that the origin remains fixed.

### Conclusion and summary

**9:54** · Delightfully, these transformations can be described using only a handful of numbers, the coordinates of where each basis vector lands.

**10:02** · Matrices give us a language to describe these transformations, where the columns represent those coordinates, and matrix-vector multiplication is just a way to compute what that transformation does to a given vector.

**10:15** · The important takeaway here is that every time you see a matrix, you can interpret it as a certain transformation of space.

**10:22** · Once you really digest this idea, you're in a great position to understand linear algebra deeply.

**10:27** · Almost all of the topics coming up, from matrix multiplication to determinants, change of basis, eigenvalues, all of these will become easier to understand once you start thinking about matrices as transformations of space.

**10:41** · Most immediately, in the next video, I'll be talking about multiplying two matrices together. See you then!