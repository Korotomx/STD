![](https://www.youtube.com/watch?v=B2PJh2K-jdU)

Part 6: https://youtu.be/gj4kvpy1eCE  
  
Can we visualise this algebraic procedure of adding diagonal entries? What is really happening when we add them together? By visualising it, it is possible to almost immediately see how the different properties of trace comes about.  
  
This channel is meant to showcase interesting but underrated maths (and physics) topics and approaches, either with completely novel topics, or a well-known topic with a novel approach. If the novel approach resonates better with you, great! But the videos have never meant to be pedagogical - in fact, please please PLEASE do NOT use YouTube videos to learn a subject.  
  
Files for download:  
Go to https://www.mathemaniac.co.uk/download and enter the following password: traceisdiv  
  
The concept of the whole video starts from one line the Wikipedia page about trace, and I am surprised this isn't on YouTube: "A related characterization of the trace applies to linear vector fields. Given a matrix A, define a vector field F on R^n by F(x) = Ax. The components of this vector field are linear functions (given by the rows of A). Its divergence div F is a constant function, whose value is equal to tr(A)."  
  
Actually, this is one of the last concepts in linear algebra that I really wanted a visualisation for, the other being transpose, but this is already on the channel: https://www.youtube.com/watch?v=g4ecBFmvAYU  
  
Chapters:  
00:00 Introduction  
00:48 Matrix as vector field  
02:24 Divergence  
04:50 Connection between trace and divergence  
10:12 Trace = sum of eigenvalues  
13:32 Determinant and matrix exponentials  
15:15 Trace is basis-independent  
18:10 Jacobi's formula  
  
Further reading:  
Trace (the origin of the whole video): https://en.wikipedia.org/wiki/Trace\_(linear\_algebra)#Derivative\_relationships  
Divergence (more qualitative, and subtly different from the video): https://en.wikipedia.org/wiki/Divergence#Physical\_interpretation\_of\_divergence  
Jacobi's formula (more formal proof): https://en.wikipedia.org/wiki/Jacobi%27s\_formula  
  
Other than commenting on the video, you are very welcome to fill in a Google form linked below, which helps me make better videos by catering for your math levels:  
https://forms.gle/QJ29hocF9uQAyZyH6  
  
If you want to know more interesting Mathematics, stay tuned for the next video!  
  
SUBSCRIBE and see you in the next video!  
  
If you are wondering how I made all these videos, even though it is stylistically similar to 3Blue1Brown, I don't use his animation engine Manim, but I use PowerPoint, GeoGebra, and (sometimes) Mathematica to produce the videos.  
  
Social media:  
  
Facebook: https://www.facebook.com/mathemaniacyt  
Instagram: https://www.instagram.com/\_mathemaniac\_/  
Twitter: https://twitter.com/mathemaniacyt  
Patreon: https://www.patreon.com/mathemaniac (support if you want to and can afford to!)  
Merch: https://mathemaniac.myspreadshop.co.uk  
Ko-fi: https://ko-fi.com/mathemaniac \[for one-time support\]  
  
For my contact email, check my About page on a PC.  
  
See you next time!

## Transcript

### Introduction

**0:00** · Given a particular matrix, if you want to compute its trace, you will be basically adding up the diagonal entries.

**0:07** · But this is quite an algebraic approach in thinking about trace.

**0:12** · Can we visualise what’s really happening when we add these diagonal entries?

**0:17** · The visualisation will also explain many properties of trace you might have seen.

**0:23** · There is one particular property that I’m saving for the end of the video series, which is tr(AB) = tr(BA).

**0:32** · However, in the majority of cases where one of A or B is invertible, we can derive it using one of the other properties.

**0:42** · But in any case, let’s start the visualisation.

**0:47** · At the end of the previous video, we have described a matrix as a vector field.

### Matrix as vector field

**0:52** · Let’s expand on that a little bit.

**0:55** · If you are given a matrix A, then the vector field will be constructed by attaching every point with position vector x by the vector Ax.

**1:05** · A little note on the illustration on screen here.

**1:10** · Technically if this illustration really describes Ax, then the vector field would look very messy because some of the vectors would be too long, so the usual thing to do is to standardise the lengths of the vectors, which will still give you the direction.

**1:28** · If you really need the length, then add colours to indicate how long the vector should have been.

**1:35** · In particular, these two vectors are the important ones, because they are the vectors attached to the points (1,0) and (0,1) respectively.

**1:46** · The vector attached to (1,0) would be the first column of A, while the vector attached to (0,1) would be the second column of A.

**1:56** · With this visualisation of matrices, the intuition for trace is just 1 sentence.

**2:02** · The trace of A is the divergence of this vector field created by the matrix A.

**2:10** · We are going to see what divergence is.

**2:12** · I am aware that this has been talked about on YouTube, but I want to be more quantitative, so bear with me if you already know the visual intuition of divergence.

**2:23** · Given a particular vector field, we can define divergence at a point, say this red dot.

### Divergence

**2:31** · We now consider a very small region around this dot, and write down the area of this small region.

**2:39** · The next thing is to let every point in this small region evolve together along the vector field.

**2:47** · As you see, the area of this region changes.

**2:51** · For divergence, we are interested in thinking about how quickly the area changes initially per area, as the area of the initial region shrinks to 0.

**3:03** · In this case, let’s look at how the area evolves again.

**3:08** · We can see that it initially decreases, and in fact keeps decreasing along the way, so because the area change is negative, we have the divergence at this red dot to also be negative.

**3:22** · However, one reminder is that this rate of area change is per area.

**3:29** · In this case, if we compare the final area with the initial area, we can record a change of -0.148 during the evolution.

**3:39** · Now if we quadruple the initial area, and again play the same game and let this area evolve under the flow of the vector field, and this time we record a change of -0.595 in area.

**3:56** · If we compare this change to the previous area change, this is exactly a factor of 4, accounting for rounding errors in my computer animation.

**4:08** · So in our intuition of divergence, the per area part is very important.

**4:15** · So that’s the divergence part, but why is this related to the trace of the matrix generating the vector field?

**4:24** · Actually the first question that comes up would be that the divergence is a local property.

**4:29** · This means that if we consider another point on the vector field, the divergence could be different.

**4:36** · So why does this statement seem like the divergence is the same everywhere?

**4:41** · Well, it’s because it is!

**4:43** · But just in this specific case where everything is generated by the matrix A. To see why the divergence is same everywhere, let’s first denote this point with its position vector x, and any point within our small region around x to be x + d, for small displacements d from x.

### Connection between trace and divergence

**5:06** · Now the vectors attached to these two points are Ax and A(x+d) respectively.

**5:13** · This means that the initial displacement between these two points is d, and after a very short time epsilon, the displacement is increased by epsilon times A d.

**5:26** · Here, A d is the difference in their velocities, or the rate where they drift apart.

**5:33** · However, notice that there is absolutely no x here.

**5:38** · This result does not depend on x.

**5:41** · So if we have this exact shape of the small region, let’s illustrate it with just three points, each with displacement d\_i from the point we try to compute divergence of.

**5:54** · After a short epsilon period of time, the displacements are changed to d\_i + epsilon A d\_i.

**6:04** · But these are independent of our position!

**6:07** · So even if we have this initial region elsewhere, we will still have the exact same shape after time epsilon.

**6:16** · So the change in area is the same everywhere.

**6:21** · Because the divergence is the area change per area, divergence is the same everywhere in this case.

**6:30** · This also means we can choose a convenient region to see how its area changes, and this region doesn’t have to be infinitesimal either.

**6:40** · This is because if we chop any normal region into very small ones, then from our intuition of divergence, each small region U\_i has its area changed from A\_i to A\_i (1+ epsilon times divergence) after time epsilon.

**7:00** · Most importantly, we know now the divergence is the same across all these regions.

**7:07** · Then for the entire region U, which has its area being the sum of these small regions, would also scale by the same factor of 1 + epsilon times divergence.

**7:22** · Since we can basically choose any region to see how the area evolves, a convenient choice is the unit square containing points (1,0) and (0,1), as the initial area would automatically be 1, so we focus on rate of area change.

**7:41** · If we suppose that A is the square matrix (a,b; c,d), then as said before, the vector attached to (1,0) would be the first column (a,c); and the vector attached to (0,1) would be the second column (b,d).

**7:57** · Let’s focus on the point (1,0) and its attached vector (a,c).

**8:03** · Here, its vertical component doesn’t really matter here, because it doesn’t change the area of the region.

**8:12** · The base and height of the parallelogram have not changed.

**8:16** · So the vertical component doesn’t matter, but what about the horizontal component?

**8:21** · This time it absolutely matters.

**8:24** · The area has changed.

**8:27** · The rate of change here is given by precisely the horizontal component of the attached vector, which is a.

**8:36** · You can run a very similar argument on the other point (0,1) here.

**8:41** · This time, the horizontal component does not matter because again the area wouldn’t change in that case, and the vertical component provides the change in area.

**8:53** · In this case, the vertical component is d.

**8:56** · So altogether, the rate of change in area would be a + d, which is exactly the sum of the diagonal entries of the matrix A, so we have demonstrated that trace is really the divergence of the vector field.

**9:14** · Now if you are not convinced by these horizontal component or vertical component argument, all we are doing is computing the determinant of this slightly different matrix.

**9:27** · The first column is where the point (1,0) moves to after time epsilon with this velocity (a,c).

**9:35** · Similarly, the second column is where the point (0,1) moves to after time epsilon with the velocity (b,d).

**9:45** · If you actually compute this determinant, then we see that this is really the rate of change of the area, that is also the trace.

**9:55** · Anyway, the fact that trace is just the divergence of this vector field is very useful for understanding the many properties of trace.

**10:05** · And these properties, one by one, would be the focus of the video from this point onwards.

**10:11** · Let’s first start with why trace is the sum of eigenvalues.

### Trace = sum of eigenvalues

**10:17** · When visualising matrices this way with vector fields, if the position vector x is an eigenvector of A, then the vector attached to it, which is Ax, would face the same or opposite direction as the position vector.

**10:34** · In fact, once you are on this line, you will stay on this line because the position and velocity vectors are on this line.

**10:44** · In the case where there are two such lines where the position vector and the velocity vector attached are on the same line, then to investigate the divergence of this vector field and hence the trace, one convenient choice of region is a parallelogram aligned with these two lines.

**11:03** · Let’s label the two lines by their eigenvalues lambda\_1 and lambda\_2 respectively, and let’s say the side lengths of the parallelogram are a and b.

**11:16** · Focus on this corner of the parallelogram.

**11:19** · The length of the vector attached to it should be lambda\_1 a.

**11:24** · That’s because on this line, every position vector satisfies Ax = lambda\_1 x.

**11:32** · Since the position vector has length a in our notation, the vector attached to it should be with length lambda\_1 a.

**11:41** · So after a very short time epsilon, we will have an extra length of epsilon lambda\_1 a along this line.

**11:50** · Using the same argument on the other corner of the parallelogram, the extra length on the other line would be epsilon lambda\_2 b after time epsilon.

**12:01** · In this illustration, lambda\_2 is negative, and so the so-called extra length is actually the length lost.

**12:11** · So after a short time epsilon, the length along this lambda\_2 line would be b(1+epsilon lambda\_2), and similarly, the length along the lambda\_1 line would be a(1+epsilon lambda\_1).

**12:27** · So the new area is the product of the side lengths and sin theta, where theta is the angle between these two lines.

**12:38** · Compare this with the old area which is ab sin theta.

**12:43** · If we now compute the divergence of this vector field, which is the rate of area change per area, then we would have this expression, which is new area minus the old area over the time period of epsilon, divided by the initial area which is ab sin theta.

**13:04** · If you really compute this, we would have lambda\_1 + lambda\_2 + a small bit involving epsilon.

**13:13** · However, as epsilon tends to 0, then the epsilon bit does not contribute and we are left with the sum of eigenvalues, so the trace is the sum of the eigenvalues in this illustration.

**13:27** · So this is the first property of trace.

**13:31** · The next property has something to do with the exponential of matrices, which I have described in the previous video as well.

### Determinant and matrix exponentials

**13:40** · Essentially, given a vector field created by the matrix A, the flow of this point with position vector x along the vector field is precisely given by e^(tA) applied to x, where t is the time elapsed when you flow along the field.

**14:00** · The determinant of a matrix is the scaling factor of this unit square under the matrix transformation.

**14:08** · Applying the matrix e^(tA) to this square is equivalent to letting the region flow along the vector field, so the area of whatever we end up with is the determinant of the matrix exponential.

**14:22** · And we actually know how the areas evolve along the vector flow.

**14:26** · Let’s denote the area of this region as S(t), which depends on time elapsed along the vector field.

**14:35** · The trace of A is the rate of area change per area, with the rate of change in area being the derivative of S, and the area being S(t).

**14:48** · By rearranging this formula, we obtain a differential equation in S. Note that trace of A doesn’t depend on t, it is a constant, so the determinant S(t) can be solved as e^(t trA).

**15:06** · This neatly explains why the determinant of exponential matrix is the exponential of trace.

**15:14** · Now let’s go to the property that the trace is independent of basis vectors.

### Trace is basis-independent

**15:21** · Given a matrix A, as usual we consider the vector field generated.

**15:26** · This time, we apply a linear transformation Q to the whole picture.

**15:32** · In general, where the vectors emanate from would change, and the vectors attached would also change.

**15:40** · More specifically, what had been x is now transformed to Qx, and what used to be Ax is now QA x.

**15:51** · This one needs a bit of explanation.

**15:53** · Initially, the attached vector to the point x is going from point x to x + Ax, so when we apply the transformation Q on the whole picture, then the attached vector goes from Qx to Qx + QAx, so this attached vector is QA x.

**16:17** · Now let’s call this new position vector y.

**16:21** · Then in terms of y, the attached vector is QAQ^(-1) y, if Q is invertible.

**16:30** · So for any position vector y, the attached vector is QAQ^(-1)y, which suggests that this is actually the vector field of another matrix QAQ^(-1).

**16:45** · Now the trace is the rate of change in area per area, but in applying Q to the whole thing, all areas scale by the determinant of Q, and this factor of determinant cancels when we consider the quotient.

**17:02** · So in other words, the trace of A equals the trace of QAQ^(-1).

**17:09** · Or if you want to go for the usual change of basis formula P^-1 AP, simply substitute the matrix Q as P^(-1).

**17:19** · Using this relation, we are able to derive another famous property of trace, which starts from rewriting trace of AB.

**17:29** · If B is invertible, then we can simply add in B^(-1) B, and the expression stays the same.

**17:38** · However, written like this, we can use the property we just derived, and then we can obtain the trace of BA.

**17:47** · Now this property of trace is perhaps more well-known, but we have done a bit of algebra to get here.

**17:55** · There is a better way, but we will introduce the concept of Lie bracket, a story for another time.

**18:04** · So we can obtain this property of trace by transforming the whole plane by P^(-1), and the final property we will see is this perhaps less famous formula.

### Jacobi's formula

**18:16** · This formula is known as Jacobi’s formula for a matrix A that depends on time t.

**18:22** · Well, technically, this is only true if A(t) in this formula is invertible, because there is A^(-1) in the formula.

**18:32** · A more general formula involves the adjoint matrix, which is defined even if A is not invertible.

**18:40** · But for the purpose of visualisation, we are going to assume A is invertible, and try to understand this formula first.

**18:49** · First off, what does the left hand side really mean?

**18:53** · The determinant can refer to the area of a parallelogram described by A(t) acting on the two basis vectors.

**19:03** · This area will change because A itself evolves with time.

**19:08** · In fact, these points would also change as A changes.

**19:13** · The rate at which these corners move is exactly A’(t) acting on the basis vectors.

**19:22** · If we can somehow make this into a whole vector field, generated by the matrix M, then we know how the area evolves.

**19:31** · Specifically, we know that the trace of M is the rate of area change per area.

**19:38** · In this case, the rate of area change is the derivative of det A. And the area is of course just the determinant of A. So if we rearrange this, then we have something that really looks like the Jacobi formula.

**19:56** · The problem now is what is M?

**20:00** · What is the matrix M that generates this vector field?

**20:04** · Now particularly at the points A(t) acting on the basis vectors, we know what the vectors attached should be.

**20:11** · To go from the position vector to the attached vector, we can simply apply A’ A^(-1) on the position vector.

**20:23** · So the matrix M we are looking for is A’ A^(-1).

**20:28** · If we go back to what we have obtained previously about derivative of determinant, we simply substitute the matrix M to be A’ A^(-1).

**20:40** · This is \*almost\* the same as Jacobi's formula.

**20:44** · Just that the matrix in the trace has the other order in multiplication.

**20:49** · A^(-1) before A’ here.

**20:52** · Don’t worry, there are two approaches here: either use the property we discovered that trace AB = trace BA for A or B being invertible; or similar to how we dealt with the previous property, we just apply A inverse to the whole picture.

**21:12** · In that case, the corners of the parallelogram go back to their standard places (1,0) and (0,1), but the vectors attached to these places are simply A^(-1) A’ acting on the basis vectors.

**21:28** · This is because previously they were just A’ acting on them, but we have applied A^(-1) to the whole picture.

**21:37** · This means that the matrix generating the vector field would be A^(-1) A’, and the matrix M to be put into the formula that we derived previously would be A^(-1) A’.

**21:52** · And this is exactly the Jacobi’s formula where the matrices in the trace are in the right order, A^(-1) A’.

**22:02** · So this is the Jacobi’s formula derived in the case when A is invertible.

**22:08** · We are able to derive and understand many properties of trace visually by thinking of trace as divergence, or the rate of area change per area when the area evolves along the vector field.

**22:23** · As always, thanks for the patrons, and please like, subscribe, comment so that more people can watch it.

**22:31** · See you next time!