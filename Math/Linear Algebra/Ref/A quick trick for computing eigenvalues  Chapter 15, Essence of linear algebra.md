![](https://www.youtube.com/watch?v=e50Bj7jn9IQ)

How to write the eigenvalues of a 2x2 matrix just by looking at it.  
Need a refresher on eigenvalues? https://youtu.be/PFDu9oVAE-g  
Thanks to Tim for the jingle: https://www.youtube.com/acapellascience  
Help fund future projects: https://www.patreon.com/3blue1brown​  
An equally valuable form of support is to simply share the videos.  
Special thanks to these supporters: https://3b1b.co/quick-eigen-thanks  
  
Lockdown math lecture talking about the mean product formula:  
https://youtu.be/MHXO86wKeDY  
  
Timestamps:  
0:00 - Background  
4:53 - Examples  
10:24 - Relation to the characteristic polynomial  
12:00 - Last thoughts  
  
\------------------  
  
These animations are largely made using a custom python library, manim. See the FAQ comments here:  
https://www.3blue1brown.com/faq#manim  
https://github.com/3b1b/manim  
https://github.com/ManimCommunity/manim/  
  
You can find code for specific videos and projects here:  
https://github.com/3b1b/videos/  
  
Music by Vincent Rubinetti.  
https://www.vincentrubinetti.com/  
  
Download the music on Bandcamp:  
https://vincerubinetti.bandcamp.com/album/the-music-of-3blue1brown  
  
Stream the music on Spotify:  
https://open.spotify.com/album/1dVyjwS8FBqXhRunaG5W5u  
  
\------------------  
  
3blue1brown is a channel about animating math, in all senses of the word animate. And you know the drill with YouTube, if you want to stay posted on new videos, subscribe: http://3b1b.co/subscribe  
  
Various social media stuffs:  
Website: https://www.3blue1brown.com  
Twitter: https://twitter.com/3blue1brown  
Reddit: https://www.reddit.com/r/3blue1brown  
Instagram: https://www.instagram.com/3blue1brown\_animations/  
Patreon: https://patreon.com/3blue1brown  
Facebook: https://www.facebook.com/3blue1brown

## Transcript

### Background

**0:00** · This is a video for anyone who already knows what eigenvalues and eigenvectors are, and who might enjoy a quick way to compute them in the case of 2x2 matrices.

**0:08** · If you're unfamiliar with eigenvalues, go ahead and take a look at this video here, which is actually meant to introduce them.

**0:14** · You can skip ahead if all you want to do is see the trick, but if possible I'd like you to rediscover it for yourself.

**0:20** · So for that, let's lay out a little background.

**0:23** · As a quick reminder, if the effect of a linear transformation on a given vector is to scale that vector by some constant, we call it an eigenvector of the transformation, and we call the relevant scaling factor the corresponding eigenvalue, often denoted with the letter lambda.

**0:39** · When you write this as an equation, and you rearrange a little bit, what you see is that if the number lambda is an eigenvalue of a matrix A, then the matrix A minus lambda times the identity must send some non-zero vector, namely the corresponding eigenvector, to the zero vector, which in turn means that the determinant of this modified matrix must be zero.

**1:06** · Okay, that's all a little bit of a mouthful to say, but again, I'm assuming that all of this is review for any of you watching.

**1:12** · So, the usual way to compute eigenvalues, how I used to do it and how I believe most students are taught to carry it out, is to subtract the unknown value lambda off the diagonals, and then solve for the determinant is equal to zero.

**1:27** · Doing this always involves a few extra steps to expand out and simplify to get a clean quadratic polynomial, what's known as the characteristic polynomial of the matrix.

**1:37** · The eigenvalues are the roots of this polynomial, so to find them you have to apply the quadratic formula, which itself typically requires one or two more steps of simplification.

**1:47** · Honestly, the process isn't terrible, but at least for two by two matrices, there is a much more direct way you can get at the answer.

**1:55** · And if you want to rediscover this trick, there's only three relevant facts you need to know, each of which is worth knowing in its own right and can help you with other problem solving.

**2:03** · Number one, the trace of a matrix, which is the sum of these two diagonal entries, is equal to the sum of the eigenvalues.

**2:11** · Or, another way to phrase it, more useful for our purposes, is that the mean of the two eigenvalues is the same as the mean of these two diagonal entries.

**2:21** · Number two, the determinant of a matrix, our usual ad-bc formula, is equal to the product of the two eigenvalues.

**2:30** · And this should kind of make sense if you understand that eigenvalues describe how much an operator stretches space in a particular direction, and that the determinant describes how much an operator scales areas, or volumes, as a whole.

**2:42** · Now before getting to the third fact, notice how you can essentially read these first two values out of the matrix without really writing much down.

**2:49** · Take this matrix here as an example.

**2:51** · Straight away, you can know that the mean of the eigenvalues is the same as the mean of 8 and 6, which is 7.

**2:59** · Likewise, most linear algebra students are pretty well practiced at finding the determinant, which in this case works out to be 48 minus 8.

**3:08** · So right away, you know that the product of the two eigenvalues is 40.

**3:12** · Now take a moment to see if you can derive what will be our third relevant fact, which is how you can quickly recover two numbers when you know their mean and you know their product.

**3:22** · Here, let's focus on this example.

**3:24** · You know that the two values are evenly spaced around the number 7, so they look like 7 plus or minus something, let's call that something d for distance.

**3:33** · You also know that the product of these two numbers is 40.

**3:38** · Now to find d, notice that this product expands really nicely, it works out as a difference of squares.

**3:44** · So from there, you can find d.

**3:48** · d squared is 7 squared minus 40, or 9, which means that d itself is 3.

**3:56** · In other words, the two values for this very specific example work out to be 4 and 10.

**4:01** · But our goal is a quick trick, and you wouldn't want to think through this each time, so let's wrap up what we just did in a general formula.

**4:08** · For any mean m and product p, the distance squared is always going to be m squared minus p.

**4:17** · This gives the third key fact, which is that when two numbers have a mean m and a product p, you can write those two numbers as m plus or minus the square root of m squared minus p.

**4:30** · This is decently fast to re-derive on the fly if you ever forget it, and it's essentially just a rephrasing of the difference of squares formula.

**4:37** · But even still, it's a fact that's worth memorizing so it's at the tip of your fingers.

**4:41** · In fact, my friend Tim from the channel A Capella Science wrote us a nice quick jingle to make it a little bit more memorable: "m plus or minus squared root of m squared minus p".

**4:51** · Let me show you how this works, say for the matrix ((3, 1), (4, 1)).

### Examples

**4:58** · You start by bringing to mind the formula, maybe stating it all in your head ("m plus or minus squared root of m squared minus p").

**5:06** · But when you write it down, you fill in the appropriate values for m and p as you go.

**5:12** · So in this example, the mean of the eigenvalues is the same as the mean of 3 and 1, which is 2, so the thing you start writing is 2 plus or minus the square root of 2 squared minus.

**5:23** · Then the product of the eigenvalues is the determinant, which in this example is 3 times 1 minus 1 times 4, or negative 1, so that's the final thing you fill in, which means the eigenvalues are 2 plus or minus the square root of 5.

**5:40** · You might recognize that this is the same matrix I was using at the beginning, but notice how much more directly we can get at the answer.

**5:48** · Here, try another one.

**5:49** · This time, the mean of the eigenvalues is the same as the mean of 2 and 8, which is 5.

**5:55** · So again, you start writing out the formula, but this time writing 5 in place of m ("m plus or minus squared root of m squared minus ...").

**6:02** · And then the determinant is 2 times 8 minus 7 times 1, or 9 ("... p").

**6:09** · So in this example, the eigenvalues look like 5 plus or minus the square root of 16, which simplifies even further as 9 and 1.

**6:19** · You see what I mean about how you can basically just start writing down the eigenvalues while you're staring at the matrix?

**6:25** · It's typically just the tiniest bit of simplification at the end.

**6:29** · Honestly, I've found myself using this trick a lot when I'm sketching quick notes related to linear algebra and want to use small matrices as examples.

**6:36** · I've been working on a video about matrix exponents, where eigenvalues pop up a lot, and I realize it's just very handy if students can read out the eigenvalues from small examples without losing the main line of thought by getting bogged down in a different calculation.

**6:49** · As another fun example, take a look at this set of three different matrices, which comes up a lot in quantum mechanics.

**6:55** · They're known as the Pauli spin matrices.

**6:58** · If you know quantum mechanics, you'll know that the eigenvalues of matrices are highly relevant to the physics that they describe.

**7:05** · And if you don't know quantum mechanics, let this just be a little glimpse of how these computations are actually very relevant to real applications.

**7:12** · The mean of the diagonal entries in all three cases is zero.

**7:17** · So the mean of the eigenvalues in all of these cases is zero, which makes our formula look especially simple.

**7:25** · What about the products of the eigenvalues, the determinants of these matrices?

**7:29** · For the first one, it's 0 minus 1, or negative 1.

**7:33** · The second one also looks like 0 minus 1, but it takes a moment more to see because of the complex numbers.

**7:38** · And the final one looks like -1 minus 0.

**7:42** · So in all cases, the eigenvalues simplify to be plus and minus 1.

**7:46** · Although in this case, you really don't need a formula to find two values if you know that they're evenly spaced around 0 and their product is negative 1.

**7:54** · If you're curious, in the context of quantum mechanics, these matrices describe observations you might make about a particle's spin in the x, y, or z direction.

**8:03** · And the fact that their eigenvalues are plus and minus 1 corresponds with the idea that the values for the spin that you would observe would be either entirely in one direction or entirely in another, as opposed to something continuously ranging in between.

**8:18** · Maybe you'd wonder how exactly this works, or why you would use 2x2 matrices that have complex numbers to describe spin in three dimensions.

**8:26** · Those would be fair questions, just outside the scope of what I want to talk about here.

**8:30** · You know, it's funny, I wrote this section because I wanted some case where you have 2x2 matrices that aren't just toy examples or homework problems, ones where they actually come up in practice, and quantum mechanics is great for that.

**8:41** · The thing is, after I made it, I realized that the whole example kind of undercuts the point that I'm trying to make.

**8:48** · For these specific matrices, when you use the traditional method, the one with characteristic polynomials, it's essentially just as fast.

**8:56** · It might actually be faster.

**8:58** · I mean, take a look at the first one.

**8:59** · The relevant determinant directly gives you a characteristic polynomial of lambda squared minus 1, and clearly that has roots of plus and minus 1.

**9:08** · Same answer when you do the second matrix, lambda squared minus 1.

**9:13** · And as for the last matrix, forget about doing any computations, traditional or otherwise, it's already a diagonal matrix, so those diagonal entries are the eigenvalues.

**9:24** · However, the example is not totally lost to our cause.

**9:27** · Where you will actually feel the speedup is in the more general case, where you take a linear combination of these three matrices and then try to compute the eigenvalues.

**9:36** · You might write this as a times the first one, plus b times the second, plus c times the third.

**9:43** · In quantum mechanics, this would describe spin observations in a general direction of a vector with coordinates (a, b, c).

**9:50** · More specifically, you should assume that this vector is normalized, meaning a squared plus b squared plus c squared is equal to 1.

**9:58** · When you look at this new matrix, it's immediate to see that the mean of the eigenvalues is still 0.

**10:04** · And you might also enjoy pausing for a brief moment to confirm that the product of those eigenvalues is still -1.

**10:13** · And then from there, concluding what the eigenvalues must be.

**10:17** · And this time, the characteristic polynomial approach would be by comparison a lot more cumbersome, definitely harder to do in your head.

### Relation to the characteristic polynomial

**10:25** · To be clear, using the mean product formula is not fundamentally different from finding roots of the characteristic polynomial.

**10:31** · I mean, it can't be, they're solving the same problem.

**10:34** · One way to think about this actually is that the mean product formula is a nice way to solve quadratics in general.

**10:39** · And some viewers of the channel may recognize this.

**10:42** · Think about it, when you're trying to find the roots of a quadratic, given the coefficients, that's another situation where you know the sum of two values, and you also know their product, but you're trying to recover the original two values.

**10:55** · Specifically, if the polynomial is normalized, so that this leading coefficient is 1, then the mean of the roots will be -1/2 times this linear coefficient, which is -1 times the sum of those roots.

**11:08** · With the example on the screen, that makes the mean 5.

**11:11** · And the product of the roots is even easier, it's just the constant term, no adjustments needed.

**11:17** · So from there, you would apply the mean product formula, and that gives you the roots ("m plus or minus squared root of m squared minus p").

**11:25** · And on the one hand, you could think of this as a lighter weight version of the traditional quadratic formula.

**11:30** · But the real advantage is not just that it's fewer symbols to memorize, it's that each one of them carries more meaning with it.

**11:36** · I mean, the whole point of this eigenvalue trick is that because you can read out the mean and product directly from looking at the matrix, you don't need to go through the intermediate step of setting up the characteristic polynomial.

**11:48** · You can jump straight to writing down the roots without ever explicitly thinking about what the polynomial looks like.

**11:53** · But to do that, we need a version of the quadratic formula where the terms carry some kind of meaning.

### Last thoughts

**12:00** · I realize this is a very specific trick for a very specific audience, but it's something I wish I knew in college, so if you happen to know any students who might benefit from this, consider sharing it with them.

**12:10** · The hope is that it's not just one more thing that you memorize, but that the framing reinforces some other nice facts that are worth knowing, like how the trace and the determinant are related to eigenvalues.

**12:20** · If you want to prove those facts, by the way, take a moment to expand out the characteristic polynomial for a general matrix, and then think hard about the meaning of each of these coefficients.

**12:32** · Many thanks to Tim for ensuring that this mean product formula will stay stuck in all of our heads for at least a few months: "m plus or minus squared root of m squared minus p".

**12:41** · If you don't know about A Cappella Science, please do check it out.

**12:46** · The molecular shape of you in particular is one of the greatest things on the internet.