![](https://www.youtube.com/watch?v=wjYpzkQoyD8)

## Transcript

### Introduction

**0:00** · \[Music\]

**0:16** · in this video I would like to provide some clarity on how to understand what the transpose of a matrix is about in my experience explanations of the transpose tend to air toward one of two extremes either explaining how to take the transpose while providing no real intuition for what this actually means or providing so much detail with higher level math concepts that new students can't make any sense of it so I'm aiming here for a middle ground that should give you a better idea of what the transpose is all about but without getting bogged down in really abstract

### Prerequisites

**0:48** · concepts for this video I'm going to assume that you understand how we can think of a matrix as a linear transformation of space what a matrix inverse and the identity Matrix are and what a do product of two vectors is if you aren't familiar with these Concepts or need a review see the excellent video series on the essence of linear algebra by three blue one brown it would also be

**1:10** · helpful if you know a bit about the singular value decomposition but if not don't worry about it we'll go over what you need to know so what is the transpose you've probably learned before that to find the transpose of a matrix you take that Matrix and merror reflect it over its diagonal elements on the Diagon stay put while elements off the diagonal get swapped with their Mirror On The Other Side Square matrices stay the same shape when you take the

### How to Take the Transpose

**1:42** · transpose but non-square matrices have their Dimension flipped around a few useful properties that come up a lot are if you want the transpose of a sum of two matrices you can distribute the transpose into the sum and so take the transpose of the individual matrices and then add them up here's a little demonstration of

### Properties of the Transpose

**2:13** · \[Music\] that if you want the transpose of the product of two matrices you can distribute the transpose into the product but you also have to flip the order of the \[Music\] \[Music\]

**2:52** · \[Music\] product if you take the transpose twice so the transpose of the transpose then this gets you back to where you started that makes good sense because you're just doing the mirror flipping

**3:12** · twice if you take the transpose of the inverse of a matrix you'll get the same result as if you swap the operation order taking the inverse of the transpose of the Matrix here's a quick proof of that \[Music\]

**3:37** · and lastly we can represent a dotproduct of two column vectors by taking the transpose of the first vector and then doing standard matrix \[Music\]

**3:55** · multiplication okay but now let's think geometrically so say we start start off with some Vector X in space then we do a linear transformation using the Matrix a applying the Matrix a to the vector X is going to give us some new Vector which we'll call xbar let's do the same thing with another Vector that we'll call V and we'll call the result V \[Music\]

### Motivating Question

**4:22** · bar so here's our motivating question suppose that before we do the transformation we take the dotproduct of V and X and after we do the transformation we take the dotproduct of the newly transformed vectors V bar and xar the question we want to ask is will we get the same number or a different number or in other words do linear Transformations preserve the dot product between two vectors you might want to pause the video and think about that for a moment okay the answer it turns out is

**4:54** · only sometimes let's see that first write v.x as V transposed X and we can write v. xar as V transpose xar next remembering that V bar and xar came to us from multiplying by a let's write the transform versions in terms of the original versions multiplied by a then distribute the transpose into the

### Linear Transformations Do Not Necessarily Preserve the Dot Product

**5:20** · product in order for the dot product of the transformed vectors to be the same as the dotproduct with the original vectors for any choice of vectors we need for this term in the middle here a transpose a to not affect the calculation at all in other words we need for a transpose a to be the identity Matrix if it were then we would have V transpose time the identity Matrix \* X

**5:46** · which would just give us V transpose X the same as the original dot product and in order for a transpose a to be the identity Matrix that would have to mean that a transpose is equal to a inverse this this is not true for plenty of matrices that we could have used as a and therefore it will not in general be true that the dot product of the transformed vectors is the same as the dot product of the original vectors so

**6:12** · we have our answer linear Transformations do not in general preserve the dot product this actually makes pretty good sense visually remember that the value of the dot product is a function of the lengths of the two vectors and the angle between them and linear Transformations

### Linear Transformations and Dot Products, Visually

**6:32** · can stretch space in ways that change angles and also change lengths differently in different directions for example look at these two vectors which are pointing in roughly the same direction and so should have some positive number for their dot product and next consider the transformation that shears space like this now the vectors are perpendicular and perpendicular vectors always have a dotproduct of zero so the dotproduct must have changed \[Music\]

### How Can We Preserve the Dot Product?

**7:04** · but what if what we want to do is to preserve the dot product that is suppose we'd like to know two sets of vectors one from before the transformation and one from after such that both sets have the same dotproduct this is what the transpose can do for us so let's do this we know that we can't multiply both X and V by a so what if we multiply V by

**7:29** · something else is there some other Matrix that we can multiply by that will preserve the dot product well let's try it and see call that Matrix M and let's see what M would have to be in order to preserve the dot product from before and after the multiplication similar logic as earlier gets you to the conclusion that for this to work for any two vectors then the transpose of M has to be equal to the inverse of a and so M must be the

**7:58** · transpose of the in inverse of a great so we've done it if you want to keep the dot product the same before and after a matrix multiplication then you might have to transform the vectors A bit differently and if you transform the first Vector using a matrix a then the Matrix that tells you how to transform the second Vector is the transpose of the inverse of a in the specific case that the inverse of a is also the transpose of a then this just gives you back a

### Preserved Dot Products, Visually

**8:31** · for a graphical example if we take these two vectors here then apply this transformation we can see that the dot product changes a lot the angles before and after are fairly similar but both vectors have gotten longer I'm going to reverse the transformation again but now I'll leave the teal Vector behind which I'll indicate with a dash that Dash teal Vector is xar the a inverse transpose

**8:58** · Matrix we derived earlier can now tell us what we have to transform V2 to keep the dotproduct the same and that would be this Vector here I'll Dash this one too and then put the original vectors back on the screen non dashed so again the point here is that the dotproduct of the solid vectors is equal to the dotproduct of the dashed

**9:23** · vectors as we said though there are some Transformations like this one here which just so happen to have their inverse equal to the transpose in which case we can do the same transformation to both vectors and the dot product stays the same before and

### Orthogonal Matrices

**9:41** · after next I want to try to give you some geometric intuition for what these Transformations are doing this can be difficult to do but bear with me here to start let's look more at that special case when the transpose of a matrix is the same as its inverse this actually turns out to correspond to a special class of matrices called orthogonal matrices we saw before that in this case

**10:06** · we can use the transformation a to transform both vectors and the dot product won't change so a is some transformation that on its own preserves dot products can you think of what kind of Transformations this might be maybe pause the video to ponder

**10:24** · that well because the value of the dot product depends on the length and Ang angles between vectors it must be that the transformation preserves lengths and angles so an example might be a reflection like this one or a rotation like

**10:40** · this the key point is that they have no stretching or squishing of space just rotation or reflection those are called orthogonal Transformations and because the transpose is the inverse that means that for a reflection or rotation doing the transformation given by the transpose will undo that original

**11:02** · transformation that's our first Insight at what the transpose does geometrically which is pretty nifty and we're going to use it again in a moment so remember that to go deeper we'll need another tool from linear algebra called the singular value decomposition I'm not going to go deep on this here we'll just hit the headline which is that you can break down any linear transformation into a combination of three parts those parts are a

### Singular Value Decomposition Introduction

**11:27** · rotation or reflection then a scaling of space at the axes followed by another rotation or reflection so that looks something like this first here's some linear transformation now let's undo that and watch it again broken into stages I'm also going to add this circle to track the stretching so first we do a rotation then we stretch or squish at the axes then we do a final rotation and

**11:59** · there we are the same transformation as earlier because matrices represent linear Transformations and matrix multiplication represents applying Transformations successively what this means is that we can Factor any Matrix into three matrices where the first one does the rotation the second one does the stretching and the third one does the final rotation note that the notation I'm using here is not standard you'll more commonly see it written like this

**12:29** · but I like my version better so indulge me also I'm not going to explain how to actually calculate these things all we need to know here is that it can be done so let's go back to our forward transformation rule which looked like this if we now represent a by its SVD

### Using the SVD on the Inverse-Transpose

**12:49** · factorization then look what we get for a inverse transpose we can distribute the inverse into the parentheses if we reverse the order of the multiplication \[Music\] when we distribute the transpose we're going to keep in mind some important facts about the SVD matrices first because Sigma is a matrix that stretches along the axes it's actually a diagonal matrix meaning it has entries only along the diagonal and the rest are zero when

**13:19** · we take the transpose of a diagonal matrix we actually just get the same Matrix back so taking the transpose of Sigma would just give us Sigma because the inverse of a diagonal matrix is also a diagonal matrix this is going to be true for Sigma inverse 2 its transpose is just Sigma inverse for the RS on the other hand these are pure rotations or Reflections I.E they are orthogonal matrices and like we said before for orthogonal matrices its transpose is its

**13:50** · inverse which means that the transpose of the inverse is just the original rotation so now we're ready to distribute that transpose and the result is this and I encourage you to stop and try to appreciate what a nice result this is it says if we transform X

**14:08** · According to some rotation scaling then rotation and our goal is to preserve the dot product then we have to transform V according to the same first rotation then the inverse scaling then the same final rotation let's take a look at that geometrically here's the same Vector X and transformation we we looked at already now let's undo that and look at the decomposition of that transformation which consists of a rotation then a scaling at the

**14:43** · axis then another rotation I'm going to restore here but leave our xar Vector behind now let's see the V vector and figure out what we have to do to get V bar we do the same first rotation as before but then the inverse scaling and then the same final rotation and now if you'll indulge me just a little bit I want to show you both of those at the same \[Music\]

**15:22** · time come on tell me that isn't delightful let me just show you some more examples while you watch this time I'd like you to think about what happens to the dot product between the two vectors during each one of these steps in an orthogonal transformation like a rotation the dot product is preserved so

### Additional Examples with the SVD

**15:43** · the first step doesn't affect it at all in the scaling step because the components of V are being scaled in the exact opposite proportion as the components of X the dot product remains unchanged which like come on that's awesome and then the final step is another orthogonal transformation which again leaves the dot product unchanged and that's how we get our invariant DOT

**16:09** · product here's one last example the thing that's new this time is that both of the scaling factors which are called singular values by the way are greater than one because of that the circle grows in size in both directions and so in the inverse transpose transform it shrinks in both directions

### What if A is not invertible?

**16:31** · I said this video was about understanding what the transpose of a matrix does and so you might be wondering are we ever actually going to get to that okay fair to get us there you might also be noticing that our formula of multiplying V by the transpose of the inverse of a seems to depend on a being invertible and if you

**16:52** · think about it that should make you uneasy after all even if a is not invertible you can still take the dot products of vectors before and after the transformation so how can we generalize all this to the case when a isn't invertible the answer is that we'll have to make a little mental shift so we have a set of vectors in the untransformed or input space which are X and V and we

**17:19** · have another set of vectors in the transformed or output space which are xar and V bar now before we picked two arbitrary vectors in the input space and then picked a rule to transform them and that

**17:35** · gave us the new vectors in the output space we're going to keep doing that for X but now for V I'd like you to shift your mindset a little instead of picking a vector v in the input space we're going to pick a vector v bar in the output space and then we'll use a rule to get from there to a vector v in the input space this may be a bit confusing

**17:58** · so we pause and think about that if need be but it doesn't change all that much ultimately we still have two sets of two vectors and for each set we pick only one vector then use some rule to find the other to do that let's solve this equation for v to get V equal a transpose V bar and now we're finally looking Square on at the transpose of a and the equation that represents this whole lesson looks like this

### Main Equation

**18:35** · I definitely encourage you to pause the video and take in this equation a bit same as before on the left side is a DOT product in the input space and the right side is a DOT product in the output space and to transform X between input and output we'll use a and to transform V from output to input we use

**18:58** · a transpose I will say though that the bar here over the V is not standard and so in the wild you might encounter an equation that looks more like this but I like the bars so I'm going to put them back anyway that all look something like this we'll start again with our Vector X and then we'll multiply by a to get our xar the dashed

### Visualization Revisited

**19:24** · Vector but now we'll pick a vector v bar and multiply by a transpose to get the vector v what the transpose does for us here is that it ensures that the dotproduct of the vectors X and V is the same as the dotproduct of xbar and V

**19:42** · bar so people often ask if the transpose of a matrix is like its inverse and we can see here that it does have a sort of inverse equality to it for one thing it does transform back from the output space to the input space of the original

### Transpose vs. Inverse

**20:00** · transformation this is especially easy to see for non-square matrices since the dimensions get swapped so for example if the original transformation goes from three-dimensional space to two-dimensional space then the transpose is a transformation from two-dimensional space to three-dimensional space But as

**20:18** · before it is not necessarily the same as the inverse and we can also see this nicely with non-square matrices if our original transformation goes from three dimensions to two diens dimensions then that won't be invertible because we're losing all that information from the third dimension but it will still have a

**20:37** · transpose to make sense of the transpose by itself geometrically I'd go back to the singular value decomposition we saw before that the transpose of the inverse preserves dot products in the forward Direction by doing the same initial rotation as a then the inverse scaling

### SVD of the Inverse and Transpose

**20:56** · then the same final rotation fairly logically we can think of the inverse of a as just doing everything in Reverse it reverses the final rotation then reverses the scaling then reverses the initial rotation maybe pause the video here and see if you can figure out what the form of a transpose should be since the same

**21:19** · relationships should hold for the pair of equations on the right as the pair on the left a little logic tells us that it must look like this we can see that a transpose first reverses the final rotation then does the same scaling as a and then reverses the initial rotation so let's see it here on the screen is the forward transformation a we're looking at doing a rotation then a

### SVD of Each Matrix, Visualized

**21:52** · scaling then a rotation \[Music\] looking at the inverse of a first that would just reverse the second rotation then reverse the scaling then reverse the first \[Music\]

**22:20** · rotation now the transpose of the inverse of a is going to do the same initial rotation but then the reverse scaling and then the same final \[Music\] rotation and finally the transpose of a is going to undo the second rotation but then do the same scaling as

**22:44** · a but then undo the first \[Music\] rotation just for fun now let's reset and see a few of those at the same time first the forward transformations \[Music\] now the backward \[Music\] \[Applause\] \[Music\]

**23:17** · Transformations for the case when a isn't invertible then Sigma won't be invertible either so we can't use these two formulas so we're left with a to transform in the forward Direction and a transpose to transform in the backward \[Music\] Direction as a final as side I want to briefly mention a special case this is when the second rotation happens to be just the reverse of the first rotation which we might as well just call R so

### Symmetric Matrices

**23:46** · then we can think of the Matrix as doing a rotation then scaling then undoing the rotation if we take a look at the form of the transpose for this case and make the same substitutions you'll notice that it ends up having the exact same form so what we have here is that the Matrix is equal to its own transpose for

**24:07** · matrices like these when you flip elements over the diagonal in order to take the transpose you get back the same thing you started with for that reason these are called symmetric matrices since they're symmetric about the matrix's diagonal here's an example

### Summary

**24:30** · so I'm going to stop there to summarize linear Transformations do not in general preserve the dotproduct of vectors the exception to this are orthogonal transformations which are pure rotations or Reflections where the transpose of the Matrix is equal to its inverse but otherwise to maintain the dot product if we transform one of the vectors in the input Space by some transformation a

**24:56** · then we'll need to transform the other input vector by a inverse transpose alternatively we can pick a vector in the output space and transform it to one in the input Space by using a transpose and we'll have to do this if a isn't invertible so the transpose of a is a different transformation which goes from the output space to the input space and helps us preserve the dot product in both spaces we saw this visually and

**25:24** · looked at the singular value decomposition of all the Transformations involved to see just how it is that they preserve the dot product hopefully this gives you a bit better understanding of what the transpose means but without muddying the waters too much if you want to go way deeper on these topics than you can and I'll leave some links in the description thanks for watching \[Music\]

**25:57** · \[Music\]