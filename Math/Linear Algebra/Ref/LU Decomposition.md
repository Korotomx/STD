![](https://www.youtube.com/watch?v=-eA2D_rIcNA)

MIT 18.06SC Linear Algebra, Fall 2011  
View the complete course: https://ocw.mit.edu/18-06SCF11  
Instructor: Ben Harris  
  
A teaching assistant works through a problem on LU decomposition.  
  
License: Creative Commons BY-NC-SA  
More information at https://ocw.mit.edu/terms  
More courses at https://ocw.mit.edu

## Transcript

**0:05** · BEN HARRIS: Hi.

**0:06** · I'm Ben.

**0:08** · Today we are going to do an LU decomposition problem.

**0:12** · Here's the problem right here.

**0:14** · Find that LU decomposition of this matrix A.

**0:18** · Now notice that this matrix A has variables, as well as numbers.

**0:23** · So the sentence ends: when it exists.

**0:28** · And the second part of the question asks you: for which real numbers a and b does the LU decomposition of this matrix actually exist?

**0:38** · Now, you can hit pause now and I'll give you a few seconds.

**0:43** · You can try to solve this on your own, and then we'll be back and we can do it together.

**0:58** · And we're back.

**1:00** · Now, what do you have to remember when doing an LU decomposition problem?

**1:07** · Well, we do elimination in the same way that we did before in order to find U. But with this question we need to find L as well.

**1:20** · So we need to do elimination, but we also need to keep track of the elimination matrices along the way.

**1:27** · Good.

**1:28** · So let's do that.

**1:30** · So let me put my matrix up here.

**1:42** · And we want to do elimination.

**1:44** · So which entry do we eliminate first?

**1:47** · That's right.

**1:48** · It's this (2, 1) entry.

**1:52** · So we replace the second row by the second row minus a times the first row, and we get this.

**2:09** · But we're not just doing elimination, we're finding an LU decomposition.

**2:14** · So we need to keep track of the matrix that I multiplied the elimination matrix, that I multiplied this matrix A by on the left to get this matrix.

**2:24** · So what is that?

**2:26** · That's this E\_(2,1).

**2:28** · Since I eliminated the (2, 1) entry, I'll call it E\_(2,1).

**2:33** · And it's this matrix.

**2:37** · Why is it this matrix?

**2:38** · Well, remember how multiplication on the left works.

**2:43** · I replaced the first row by just the first row.

**2:47** · I replaced the second row by the second row minus a times the first row.

**2:53** · So you can just read off from these rows which operations I did.

**2:59** · Now, which entries should we eliminate next?

**3:01** · We need to eliminate this b.

**3:03** · So we will replace the third row by the third row minus b times the first row.

**3:18** · And which elimination matrix did we use?

**3:28** · Well, note, we replaced the third row by the third row minus b times the first row.

**3:34** · That's exactly what you should read off this elimination matrix.

**3:39** · Good.

**3:40** · Now, we only have one step left.

**3:43** · We only need to eliminate one last entry.

**3:45** · But this one's a little tricky, so let's be careful.

**3:50** · In order to eliminate this b, we need a to be a pivot.

**3:55** · In particular, we need a to be nonzero.

**3:59** · If a were zero here, then we would have to do a row exchange.

**4:03** · And that's no good.

**4:05** · You can't find an LU decomposition if you have to do a row exchange in elimination.

**4:11** · So we need to assume that a is non-zero in order to keep going.

**4:22** · So let's just assume there that a is non-zero.

**4:26** · Now, what do we do?

**4:28** · Well we can replace the third row by the third row minus b over a times the second row.

**4:38** · And we just get this.

**4:43** · a minus b.

**4:46** · And let's write down our elimination matrix.

**4:49** · E\_(3,2) now.

**4:59** · There's our elimination matrix.

**5:00** · We replaced the third row by the third row minus b over a times the second row.

**5:06** · Good.

**5:10** · So we found our U matrix.

**5:13** · That's what elimination does, it gives us our U matrix.

**5:16** · So let me write it up here.

**5:20** · 1, 0, 1; 0, a, 0; 0, 0, a minus b.

**5:35** · Good.

**5:37** · Now we have to find our L matrix, and we need to use these elimination matrices that we've been recording along the way in order to do that.

**5:46** · So remember that we started with A, and we got U.

**5:53** · And how did we do that?

**5:54** · Well we multiplied on the left by all of these elimination matrices, E\_(2,1), E\_(3,1) and E\_(3,2).

**6:05** · Sorry if that's scrunching together there.

**6:08** · Now, if we move these elimination matrices to the other side then we'll get L. So what do we have?

**6:17** · We have A equals E\_(2,1) inverse, E\_(3,1) inverse, E\_(3,2) inverse times U. And this is our L, this product of these three matrices.

**6:37** · Good.

**6:38** · So let's compute it now.

**6:43** · So L is the product of three matrices.

**6:45** · I need to get them by going back and looking at these three elimination matrices and taking their inverses.

**6:52** · Well the nice thing about taking an inverse of an elementary matrix like this is we just make a minus a plus or a plus a minus.

**7:02** · So that's easy enough.

**7:06** · We just change the off-diagonal entries, we just change their signs.

**7:12** · You can check that that does what we wanted it to.

**7:17** · It gives us the inverse.

**7:20** · Good.

**7:21** · And the last comment is that multiplying these three matrices is really easy in this order.

**7:26** · Turns out all you do is you just plop these entries right in.

**7:35** · 1, 1.

**7:36** · Good.

**7:36** · So this is our L matrix.

**7:41** · So now we have our U matrix and our L matrix, and we're done with the first part of the question.

**7:49** · The second part asks us for which real numbers a and b does this decomposition exist?

**7:55** · Now let's go back and remember that at one point we had to assume that A was non-zero.

**8:01** · That was the only assumption we had to make to get this decomposition.

**8:06** · So it exists-- it being this decomposition-- when a is non-zero.

**8:14** · And that's the answer to the second part.

**8:19** · So we have our LU decomposition, and we know when it exists.

**8:24** · Before I end, two comments.

**8:27** · First, always check your work.

**8:30** · Always go back and multiply L times U and make sure it's A, because it's easy to screw up the elimination process and it's easy to check your work.

**8:41** · So if you go back and make sure things are as they should be.

**8:46** · Second comment is that you might be worried when you do this elimination process that-- well OK, we had to assume a is non-zero because we wanted a non-zero pivot.

**9:01** · You might worry that we might have to have a minus b be non-zero.

**9:05** · But in fact, a minus b can be 0.

**9:09** · It's not a problem for this entry to be 0 because we don't have to do a row exchange to get U. That's the only time when we can't do the LU decomposition.

**9:24** · In particular, singular matrices can have LU decompositions.

**9:29** · Good.

**9:32** · Thanks.