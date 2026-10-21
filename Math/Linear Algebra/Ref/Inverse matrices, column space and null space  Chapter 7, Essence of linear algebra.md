![](https://www.youtube.com/watch?v=uQhTuRlWMxw)

How to think about linear systems of equations geometrically.  
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

### Introduction to Linear Systems

**0:10** · As you can probably tell by now, the bulk of this series is on understanding matrix and vector operations through that more visual lens of linear transformations.

**0:19** · This video is no exception, describing the concepts of inverse matrices, column space, rank, and null space through that lens.

**0:27** · A forewarning though, I'm not going to talk about the methods for actually computing these things, and some would argue that that's pretty important.

**0:34** · There are a lot of very good resources for learning those methods outside this series, keywords Gaussian elimination and row echelon form.

**0:42** · I think most of the value that I actually have to add here is on the intuition half.

**0:46** · Plus, in practice, we usually get software to compute this stuff for us anyway.

### Geometric Interpretation

**0:51** · First, a few words on the usefulness of linear algebra.

**0:54** · By now, you already have a hint for how it's used in describing the manipulation of space, which is useful for things like computer graphics and robotics.

**1:01** · But one of the main reasons that linear algebra is more broadly applicable and required for just about any technical discipline is that it lets us solve certain systems of equations.

**1:11** · When I say system of equations, I mean you have a list of variables, things you don't know, and a list of equations relating them.

**1:18** · In a lot of situations, those equations can get very complicated.

**1:22** · But, if you're lucky, they might take on a certain special form.

**1:26** · Within each equation, the only thing happening to each variable is that it's scaled by some constant, and the only thing happening to each of those scaled variables is that they're added to each other.

**1:37** · So no exponents or fancy functions or multiplying two variables together, things like that.

**1:43** · The typical way to organize this sort of special system of equations is to throw all the variables on the left and put any lingering constants on the right.

**1:53** · It's also nice to vertically line up the common variables, and to do that, you might need to throw in some zero coefficients whenever the variable doesn't show up in one of the equations.

**2:04** · This is called a linear system of equations.

**2:08** · You might notice that this looks a lot like matrix-vector multiplication.

**2:11** · In fact, you can package all of the equations together into a single vector equation where you have the matrix containing all of the constant coefficients and a vector containing all of the variables, and their matrix-vector product equals some different constant vector.

**2:28** · Let's name that constant matrix A, denote the vector holding the variables with a bold-faced X, and call the constant vector on the right-hand side V.

**2:38** · This is more than just a notational trick to get our system of equations written on one line.

**2:43** · It sheds light on a pretty cool geometric interpretation for the problem.

### Matrix and Vector Equations

**2:47** · The matrix A corresponds with some linear transformation, so solving Ax equals V means we're looking for a vector X, which, after applying the transformation, lands on V.

**2:59** · Think about what's happening here for a moment.

**3:02** · You can hold in your head this really complicated idea of multiple variables all intermingling with each other just by thinking about squishing and morphing space and trying to figure out which vector lands on another.

**3:13** · Cool, right?

**3:14** · To start simple, let's say you have a system with two equations and two unknowns.

**3:19** · This means the matrix A is a 2x2 matrix, and V and X are each two-dimensional vectors.

**3:25** · Now, how we think about the solutions to this equation depends on whether the transformation associated with A squishes all of space into a lower dimension, like a line or a point, or if it leaves everything spanning the full two dimensions where it started.

**3:40** · In the language of the last video, we subdivide into the cases where A has zero determinant and the case where A has non-zero determinant.

**3:51** · Let's start with the most likely case, where the determinant is non-zero, meaning space does not get squished into a zero-area region.

### Inverse Matrices

**3:58** · In this case, there will always be one and only one vector that lands on V, and you can find it by playing the transformation in reverse.

**4:06** · Following where V goes as we rewind the tape like this, you'll find the vector x such that A times x equals V.

**4:15** · When you play the transformation in reverse, it actually corresponds to a separate linear transformation, commonly called the inverse of A, denoted A to the negative one.

**4:25** · For example, if A was a counterclockwise rotation by 90 degrees, then the inverse of A would be a clockwise rotation by 90 degrees.

**4:34** · If A was a rightward shear that pushes j-hat one unit to the right, the inverse of A would be a leftward shear that pushes j-hat one unit to the left.

**4:44** · In general, A inverse is the unique transformation with the property that if you first apply A, then follow it with the transformation A inverse, you end up back where you started.

**4:54** · Applying one transformation after another is captured algebraically with matrix multiplication, so the core property of this transformation A inverse is that A inverse times A equals the matrix that corresponds to doing nothing.

**5:08** · The transformation that does nothing is called the identity transformation.

**5:11** · It leaves i-hat and j-hat each where they are, unmoved, so its columns are 1,0 and 0,1.

**5:19** · Once you find this inverse, which in practice you'd do with a computer, you can solve your equation by multiplying this inverse matrix by v.

**5:29** · And again, what this means geometrically is that you're playing the transformation in reverse and following v.

**5:40** · This non-zero determinant case, which for a random choice of matrix is by far the most likely one, corresponds with the idea that if you have two unknowns and two equations, it's almost certainly the case that there's a single unique solution.

**5:53** · This idea also makes sense in higher dimensions, when the number of equations equals the number of unknowns.

### Zero Determinant Cases

**5:59** · Again, the system of equations can be translated to the geometric interpretation where you have some transformation A and some vector v, and you're looking for the vector x that lands on v.

**6:15** · As long as the transformation A doesn't squish all of space into a lower dimension, meaning its determinant is non-zero, there will be an inverse transformation A inverse, with the property that if you first do A, then you do A inverse, it's the same as doing nothing.

**6:33** · And to solve your equation, you just have to multiply that reverse transformation matrix by the vector v.

**6:43** · But when the determinant is zero, and the transformation associated with the system of equations squishes space into a smaller dimension, there is no inverse.

**6:52** · You cannot unsquish a line to turn it into a plane.

**6:55** · At least that's not something that a function can do.

**6:58** · That would require transforming each individual vector into a whole line full of vectors.

**7:03** · But functions can only take a single input to a single output.

**7:08** · Similarly, for three equations and three unknowns, there will be no inverse if the corresponding transformation squishes 3D space onto the plane, or even if it squishes it onto a line or a point.

**7:19** · Those all correspond to a determinant of zero, since any region is squished into something with zero volume.

**7:26** · It's still possible that a solution exists even when there is no inverse.

### Rank and Column Space

**7:30** · It's just that when your transformation squishes space onto, say, a line, you have to be lucky enough that the vector v lives somewhere on that line.

**7:43** · You might notice that some of these zero determinant cases feel a lot more restrictive than others.

**7:48** · Given a 3x3 matrix, for example, it seems a lot harder for a solution to exist when it squishes space onto a line compared to when it squishes things onto a plane, even though both of those are zero determinant.

**8:02** · We have some language that's a bit more specific than just saying zero determinant.

**8:06** · When the output of a transformation is a line, meaning it's one-dimensional, we say the transformation has a rank of one.

**8:15** · If all the vectors land on some two-dimensional plane, we say the transformation has a rank of two.

**8:22** · So the word rank means the number of dimensions in the output of a transformation.

**8:28** · For instance, in the case of 2x2 matrices, rank two is the best that it can be.

**8:33** · It means the basis vectors continue to span the full two dimensions of space, and the determinant is not zero.

**8:39** · But for 3x3 matrices, rank two means that we've collapsed, but not as much as they would have collapsed for a rank one situation.

**8:47** · If a 3D transformation has a non-zero determinant and its output fills all of 3D space, it has a rank of three.

### Null Space

**8:54** · This set of all possible outputs for your matrix, whether it's a line, a plane, 3D space, whatever, is called the column space of your matrix.

**9:04** · You can probably guess where that name comes from.

**9:06** · The columns of your matrix tell you where the basis vectors land, and the span of those transformed basis vectors gives you all possible outputs.

**9:16** · In other words, the column space is the span of the columns of your matrix.

**9:23** · So a more precise definition of rank would be that it's the number of dimensions in the column space.

**9:29** · When this rank is as high as it can be, meaning it equals the number of columns, we call the matrix full rank.

**9:38** · Notice the zero vector will always be included in the column space, since linear transformations must keep the origin fixed in place.

**9:46** · For a full rank transformation, the only vector that lands at the origin is the zero vector itself.

**9:52** · But for matrices that aren't full rank, which squish to a smaller dimension, you can have a whole bunch of vectors that land on zero.

**10:01** · If a 2D transformation squishes space onto a line, for example, there is a separate line in a different direction full of vectors that get squished onto the origin.

**10:11** · If a 3D transformation squishes space onto a plane, there's also a full line of vectors that land on the origin.

**10:20** · If a 3D transformation squishes all of space onto a line, then there's a whole plane full of vectors that land on the origin.

**10:32** · This set of vectors that lands on the origin is called the null space, or the kernel of your matrix.

### Summary of Linear Systems

**10:39** · It's the space of all vectors that become null, in the sense that they land on the zero vector.

**10:45** · In terms of the linear system of equations, when v happens to be the zero vector, the null space gives you all of the possible solutions to the equation.

**10:56** · So that's a very high level overview of how to think about linear systems of equations geometrically.

**11:02** · Each system has some kind of linear transformation associated with it, and when that transformation has an inverse, you can use that inverse to solve your system.

**11:12** · Otherwise, the idea of column space lets us understand when a solution even exists, and the idea of a null space helps us to understand what the set of all possible solutions can look like.

**11:24** · Again, there's a lot that I haven't covered here, most notably how to compute these things.

**11:29** · I also had to limit my scope to examples where the number of equations equals the number of unknowns.

**11:34** · But the goal here is not to try to teach everything, it's that you come away with a strong intuition for inverse matrices, column space, and null space, and that those intuitions make any future learning that you do more fruitful.

**11:47** · Next video, by popular request, will be a brief footnote about non-square matrices.

**11:51** · Then after that, I'm going to give you my take on dot products, and something pretty cool that happens when you view them under the light of linear transformations. See you then!