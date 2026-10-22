![](https://www.youtube.com/watch?v=PFDu9oVAE-g)

A visual understanding of eigenvectors, eigenvalues, and the usefulness of an eigenbasis.  
Help fund future projects: https://www.patreon.com/3blue1brown  
An equally valuable form of support is to simply share some of the videos.  
Home page: https://www.3blue1brown.com  
  
Full series: https://3b1b.co/eola  
  
Future series like this are funded by the community, through Patreon, where supporters get early access as the series is being produced.  
http://3b1b.co/support  
  
A solution to the puzzle at the end:  
https://www.dropbox.com/s/86yddvprfuaafju/Eigenvalue%20puzzle%20solution.pdf?dl=0  
  
Typo: At 12:27, "more that a line full" should be "more than a line full".  
  
Thanks to these viewers for their contributions to translations  
Hebrew: Omer Tuchfeld  
  
\------------------  
  
3blue1brown is a channel about animating math, in all senses of the word animate.  
  
Various social media stuffs:  
Website: https://www.3blue1brown.com  
Twitter: https://twitter.com/3Blue1Brown  
Patreon: https://patreon.com/3blue1brown  
Facebook: https://www.facebook.com/3blue1brown  
Reddit: https://www.reddit.com/r/3Blue1Brown

## Transcript

### Introduction to eigenvectors

**0:00** · \[Submit subtitle corrections at criblate.com\] Eigenvectors and eigenvalues is one of those topics that a lot of students find particularly unintuitive.

**0:25** · Questions like, why are we doing this and what does this actually mean, are too often left just floating away in an unanswered sea of computations.

**0:33** · And as I've put out the videos of this series, a lot of you have commented about looking forward to visualizing this topic in particular.

**0:40** · I suspect that the reason for this is not so much that eigenthings are particularly complicated or poorly explained.

**0:46** · In fact, it's comparatively straightforward, and I think most books do a fine job explaining it.

**0:51** · The issue is that it only really makes sense if you have a solid visual understanding for many of the topics that precede it.

**0:59** · Most important here is that you know how to think about matrices as linear transformations, but you also need to be comfortable with things like determinants, linear systems of equations, and change of basis.

**1:10** · Confusion about eigenstuffs usually has more to do with a shaky foundation in one of these topics than it does with eigenvectors and eigenvalues themselves.

**1:19** · To start, consider some linear transformation in two dimensions, like the one shown here.

### Geometric interpretation

**1:25** · It moves the basis vector i-hat to the coordinates (3, 0), and j-hat to (1, 2).

**1:31** · So it's represented with a matrix whose columns are (3, 0), and (1, 2).

**1:36** · Focus in on what it does to one particular vector, and think about the span of that vector, the line passing through its origin and its tip.

**1:44** · Most vectors are going to get knocked off their span during the transformation.

**1:48** · I mean, it would seem pretty coincidental if the place where the vector landed also happened to be somewhere on that line.

**1:57** · But some special vectors do remain on their own span, meaning the effect that the matrix has on such a vector is just to stretch it or squish it, like a scalar.

**2:09** · For this specific example, the basis vector i-hat is one such special vector.

**2:14** · The span of i-hat is the x-axis, and from the first column of the matrix, we can see that i-hat moves over to 3 times itself, still on that x-axis.

**2:26** · What's more, because of the way linear transformations work, any other vector on the x-axis is also just stretched by a factor of 3, and hence remains on its own span.

**2:38** · A slightly sneakier vector that remains on its own span during this transformation is (-1, 1).

**2:44** · It ends up getting stretched by a factor of 2.

**2:49** · And again, linearity is going to imply that any other vector on the diagonal line spanned by this guy is just going to get stretched out by a factor of 2.

### Eigenvalues defined

**2:59** · And for this transformation, those are all the vectors with this special property of staying on their span.

**3:05** · Those on the x-axis getting stretched out by a factor of 3, and those on this diagonal line getting stretched by a factor of 2.

**3:12** · Any other vector is going to get rotated somewhat during the transformation, knocked off the line that it spans.

**3:22** · As you might have guessed by now, these special vectors are called the eigenvectors of the transformation, and each eigenvector has associated with it what's called an eigenvalue, which is just the factor by which it's stretched or squished during the transformation.

**3:40** · Of course, there's nothing special about stretching versus squishing, or the fact that these eigenvalues happen to be positive.

**3:46** · In another example, you could have an eigenvector with eigenvalue -1/2, meaning that the vector gets flipped and squished by a factor of 1/2.

**3:56** · But the important part here is that it stays on the line that it spans out without getting rotated off of it.

**4:04** · For a glimpse of why this might be a useful thing to think about, consider some three-dimensional rotation.

**4:11** · If you can find an eigenvector for that rotation, a vector that remains on its own span, what you have found is the axis of rotation.

**4:22** · And it's much easier to think about a 3D rotation in terms of some axis of rotation and an angle by which it's rotating, rather than thinking about the full 3x3 matrix associated with that transformation.

### Applications and context

**4:37** · In this case, by the way, the corresponding eigenvalue would have to be 1, since rotations never stretch or squish anything, so the length of the vector would remain the same.

**4:48** · This pattern shows up a lot in linear algebra.

**4:50** · With any linear transformation described by a matrix, you could understand what it's doing by reading off the columns of this matrix as the landing spots for basis vectors.

**5:00** · But often, a better way to get at the heart of what the linear transformation actually does, less dependent on your particular coordinate system, is to find the eigenvectors and eigenvalues.

**5:15** · I won't cover the full details on methods for computing eigenvectors and eigenvalues here, but I'll try to give an overview of the computational ideas that are most important for a conceptual understanding.

### Computing eigenvectors

**5:27** · Symbolically, here's what the idea of an eigenvector looks like.

**5:31** · A is the matrix representing some transformation, with v as the eigenvector, and lambda is a number, namely the corresponding eigenvalue.

**5:40** · What this expression is saying is that the matrix-vector product, A times v, gives the same result as just scaling the eigenvector v by some value lambda.

**5:51** · So finding the eigenvectors and their eigenvalues of a matrix A comes down to finding the values of v and lambda that make this expression true.

**6:01** · It's a little awkward to work with at first, because that left-hand side represents matrix-vector multiplication, but the right-hand side here is scalar-vector multiplication.

**6:11** · So let's start by rewriting that right-hand side as some kind of matrix-vector multiplication, using a matrix which has the effect of scaling any vector by a factor of lambda.

**6:21** · The columns of such a matrix will represent what happens to each basis vector, and each basis vector is simply multiplied by lambda, so this matrix will have the number lambda down the diagonal, with zeros everywhere else.

**6:36** · The common way to write this guy is to factor that lambda out and write it as lambda times I, where I is the identity matrix with 1s down the diagonal.

**6:45** · With both sides looking like matrix-vector multiplication, we can subtract off that right-hand side and factor out the v.

**6:54** · So what we now have is a new matrix, A minus lambda times the identity, and we're looking for a vector v such that this new matrix times v gives the zero vector.

**7:06** · Now, this will always be true if v itself is the zero vector, but that's boring.

**7:11** · What we want is a non-zero eigenvector.

**7:14** · And if you watch chapter 5 and 6, you'll know that the only way it's possible for the product of a matrix with a non-zero vector to become zero is if the transformation associated with that matrix squishes space into a lower dimension.

**7:29** · And that squishification corresponds to a zero determinant for the matrix.

**7:35** · To be concrete, let's say your matrix A has columns (2, 1) and (2, 3), and think about subtracting off a variable amount, lambda, from each diagonal entry.

### Practical calculation example

**7:46** · Now imagine tweaking lambda, turning a knob to change its value.

**7:50** · As that value of lambda changes, the matrix itself changes, and so the determinant of the matrix changes.

**7:58** · The goal here is to find a value of lambda that will make this determinant zero, meaning the tweaked transformation squishes space into a lower dimension.

**8:08** · In this case, the sweet spot comes when lambda equals 1.

**8:12** · Of course, if we had chosen some other matrix, the eigenvalue might not necessarily be 1.

**8:16** · The sweet spot might be hit at some other value of lambda.

**8:20** · So this is kind of a lot, but let's unravel what this is saying.

**8:22** · When lambda equals 1, the matrix A minus lambda times the identity squishes space onto a line.

**8:30** · That means there's a non-zero vector v such that A minus lambda times the identity times v equals the zero vector.

**8:40** · And remember, the reason we care about that is because it means A times v equals lambda times v, which you can read off as saying that the vector v is an eigenvector of A, staying on its own span during the transformation A.

**8:58** · In this example, the corresponding eigenvalue is 1, so v would actually just stay fixed in place.

**9:06** · Pause and ponder if you need to make sure that that line of reasoning feels good.

**9:13** · This is the kind of thing I mentioned in the introduction.

**9:16** · If you didn't have a solid grasp of determinants and why they relate to linear systems of equations having non-zero solutions, an expression like this would feel completely out of the blue.

**9:28** · To see this in action, let's revisit the example from the start, with a matrix whose columns are (3, 0) and (1, 2).

**9:35** · To find if a value lambda is an eigenvalue, subtract it from the diagonals of this matrix and compute the determinant.

**9:50** · Doing this, we get a certain quadratic polynomial in lambda, 3 minus lambda times 2 minus lambda.

**9:57** · Since lambda can only be an eigenvalue if this determinant happens to be zero, you can conclude that the only possible eigenvalues are lambda equals 2 and lambda equals 3.

**10:09** · To figure out what the eigenvectors are that actually have one of these eigenvalues, say lambda equals 2, plug in that value of lambda to the matrix and then solve for which vectors this diagonally altered matrix sends to zero.

**10:24** · If you computed this the way you would any other linear system, you'd see that the solutions are all the vectors on the diagonal line spanned by (-1, 1).

**10:35** · This corresponds to the fact that the unaltered matrix, (3, 0), (1, 2), has the effect of stretching all those vectors by a factor of 2.

### Special cases

**10:46** · Now, a 2D transformation doesn't have to have eigenvectors.

**10:50** · For example, consider a rotation by 90 degrees.

**10:53** · This doesn't have any eigenvectors since it rotates every vector off of its own span.

**11:00** · If you actually try computing the eigenvalues of a rotation like this, notice what happens.

**11:06** · Its matrix has columns (0, 1) and (-1, 0).

**11:11** · Subtract off lambda from the diagonal elements and look for when the determinant is zero.

**11:18** · In this case, you get the polynomial lambda squared plus 1.

**11:22** · The only roots of that polynomial are the imaginary numbers, i and -i.

**11:28** · The fact that there are no real number solutions indicates that there are no eigenvectors.

**11:35** · Another pretty interesting example worth holding in the back of your mind is a shear.

**11:40** · This fixes i-hat in place and moves j-hat 1 over, so its matrix has columns (1, 0) and (1, 1).

**11:48** · All of the vectors on the x-axis are eigenvectors with eigenvalue 1 since they remain fixed in place.

**11:55** · In fact, these are the only eigenvectors.

**11:58** · When you subtract off lambda from the diagonals and compute the determinant, what you get is 1 minus lambda squared.

**12:09** · And the only root of this expression is lambda equals 1.

**12:14** · This lines up with what we see geometrically, that all of the eigenvectors have eigenvalue 1.

### Non-unique eigenvectors

**12:21** · Keep in mind though, it's also possible to have just one eigenvalue, but with more than just a line full of eigenvectors.

**12:29** · A simple example is a matrix that scales everything by 2.

**12:33** · The only eigenvalue is 2, but every vector in the plane gets to be an eigenvector with that eigenvalue.

**12:42** · Now is another good time to pause and ponder some of this before I move on to the last topic.

**13:03** · I want to finish off here with the idea of an eigenbasis, which relies heavily on ideas from the last video.

### Diagonal matrices

**13:11** · Take a look at what happens if our basis vectors just so happen to be eigenvectors.

**13:17** · For example, maybe i-hat is scaled by -1 and j-hat is scaled by 2.

**13:23** · Writing their new coordinates as the columns of a matrix, notice that those scalar multiples, -1 and 2, which are the eigenvalues of i-hat and j-hat, sit on the diagonal of our matrix, and every other entry is a 0.

**13:38** · Any time a matrix has zeros everywhere other than the diagonal, it's called, reasonably enough, a diagonal matrix.

**13:45** · And the way to interpret this is that all the basis vectors are eigenvectors, with the diagonal entries of this matrix being their eigenvalues.

**13:57** · There are a lot of things that make diagonal matrices much nicer to work with.

**14:01** · One big one is that it's easier to compute what will happen if you multiply this matrix by itself a whole bunch of times.

**14:09** · Since all one of these matrices does is scale each basis vector by some eigenvalue, applying that matrix many times, say 100 times, is just going to correspond to scaling each basis vector by the 100th power of the corresponding eigenvalue.

**14:25** · In contrast, try computing the 100th power of a non-diagonal matrix.

**14:29** · Really, try it for a moment.

**14:31** · It's a nightmare.

**14:36** · Of course, you'll rarely be so lucky as to have your basis vectors also be eigenvectors.

**14:42** · But if your transformation has a lot of eigenvectors, like the one from the start of this video, enough so that you can choose a set that spans the full space, then you could change your coordinate system so that these eigenvectors are your basis vectors.

**14:57** · I talked about change of basis last video, but I'll go through a super quick reminder here of how to express a transformation currently written in our coordinate system into a different system.

### Eigenbasis and change of basis

**15:08** · Take the coordinates of the vectors that you want to use as a new basis, which in this case means our two eigenvectors, then make those coordinates the columns of a matrix, known as the change of basis matrix.

**15:20** · When you sandwich the original transformation, putting the change of basis matrix on its right and the inverse of the change of basis matrix on its left, the result will be a matrix representing that same transformation, but from the perspective of the new basis vectors coordinate system.

**15:37** · The whole point of doing this with eigenvectors is that this new matrix is guaranteed to be diagonal with its corresponding eigenvalues down that diagonal.

**15:46** · This is because it represents working in a coordinate system where what happens to the basis vectors is that they get scaled during the transformation.

**15:55** · A set of basis vectors which are also eigenvectors is called, again, reasonably enough, an eigenbasis.

**16:02** · So if, for example, you needed to compute the 100th power of this matrix, it would be much easier to change to an eigenbasis, compute the 100th power in that system, then convert back to our standard system.

**16:16** · You can't do this with all transformations.

**16:18** · A shear, for example, doesn't have enough eigenvectors to span the full space.

**16:23** · But if you can find an eigenbasis, it makes matrix operations really lovely.

**16:29** · For those of you willing to work through a pretty neat puzzle to see what this looks like in action and how it can be used to produce some surprising results, I'll leave up a prompt here on the screen.

**16:37** · It takes a bit of work, but I think you'll enjoy it.

**16:40** · The next and final video of this series is going to be on abstract vector spaces.

**16:45** · See you then!