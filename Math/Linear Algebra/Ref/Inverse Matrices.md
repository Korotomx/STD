![](https://www.youtube.com/watch?v=zWxhmBCdvFs)

MIT 18.06SC Linear Algebra, Fall 2011  
View the complete course: https://ocw.mit.edu/18-06SCF11  
Instructor: Ana Rita Pires  
  
A teaching assistant works through a problem on inverse matrices.  
  
License: Creative Commons BY-NC-SA  
More information at https://ocw.mit.edu/terms  
More courses at https://ocw.mit.edu

## Transcript

**0:05** · PROFESSOR: Hi there.

**0:06** · My name is Ana.

**0:07** · Welcome to recitation.

**0:09** · In lecture, you've been learning about how to multiply matrices, and how to think about that multiplication in different ways, and also about when a matrix is invertible or not, and how to compute the inverse when it is invertible.

**0:21** · And that's what today's problem is about.

**0:24** · We have a matrix A that has variables a and b instead of numbers.

**0:29** · And the question is: what are the conditions on a and b that make that matrix invertible?

**0:36** · And when it is invertible, what is A inverse?

**0:40** · Why don't you hit Pause and work on it for a little while.

**0:43** · And then we'll come back and work on it together.

**0:53** · And we're back.

**0:55** · I hope you had success in solving that.

**0:59** · Let's do it ourselves.

**1:01** · So, remember from lecture, we talked about-- well, Professor Strang talked about how it's easy to spot-- some easy tests to spot when a matrix is not invertible.

### Tests To Spot When a Matrix Is Not Invertible

**1:15** · Those were: if you have a column of 0's or a row of 0's, then the matrix is not invertible.

**1:20** · Or if you have two columns that are the same, or two rows that are the same, the matrix is also not invertible.

**1:25** · So let's see if this matrix satisfies any of those easy conditions.

**1:31** · Well, here you have a row of a's.

**1:34** · If a is equal to 0, you have a row of 0's, the matrix is not invertible.

**1:38** · So a is-- What was the other one?

**1:51** · Two of the same column or of the same row.

**1:54** · Well, if a is equal to b, then all the entries in the matrix are the same, so all the rows are the same, all the columns are the same, the matrix is not invertible.

**2:04** · So that's the other easy condition.

**2:05** · A is not invertible if a is equal to 0 or a equals to b.

**2:12** · There's not any other easy condition that I can spot.

**2:15** · So we have to do it in a more systematic way.

**2:18** · So to do that, actually what we do is we start with A, we try to find its inverse, and if in the process we run into something fishy, those are our conditions.

### How To Find the Inverse of a Matrix

**2:28** · So remember how to find the inverse of a matrix?

**2:32** · You start by writing a giant matrix that has A and the identity next to it.

**2:40** · And then you perform elimination steps until-- let's put dots here, because there's lots of steps-- and you stop once you've reached the identity matrix on the left side.

**2:56** · And when you do that, what you have on the right side will be your A inverse.

**3:01** · Easy enough.

**3:01** · So let's do the computations.

**3:08** · a, b, b; a, a, b; a, a, a; and my identity matrix next to it.

**3:20** · And now I know you learned about elimination in the past recitation.

**3:26** · So I'll do the first few steps slowly, and then I'll just write the solution for the last steps.

**3:33** · So we want to eliminate this a.

**3:37** · We want to turn it into 0.

**3:38** · So let's subtract the first row from the second.

**3:42** · Let's do row 2 minus row 1, and write it instead of row 2.

**3:45** · So a, b, b, 1, 0, 0; 0, so a minus a, a minus b, b minus b is 0, 0 minus 1, 1 minus 0, 0 minus 0.

**4:01** · And then we want to do the same with the third row.

**4:04** · So let's do row 3 minus row 1.

**4:07** · 0, a minus b, it doesn't fit.

**4:13** · a minus b.

**4:14** · Can you understand that?

**4:16** · And then 0 minus 1, 0 minus 0, 1 minus 0.

**4:21** · All right.

**4:22** · Let's continue up here.

**4:28** · Now I want to eliminate this a minus b.

**4:31** · I want to turn it into a 0.

**4:33** · So the first row stays the same.

**4:35** · a, b, b, 1, 0, 0; 0, a minus b, 0, -1, 1, 0.

**4:46** · And now 0 minus 0, a minus b minus a minus b is 0.

**4:51** · a minus b minus 0, that's easy.

**4:54** · -1 minus -1, 0 again.

**4:58** · -1 and 1.

**5:02** · Almost there.

**5:03** · We already have 0's down here.

**5:04** · It's looking more and more like the identity matrix.

**5:06** · So we have to turn all these diagonal entries into 1's, so let's do that now.

**5:13** · 1, b over a, b over-- oh.

**5:18** · I'm dividing by a.

**5:19** · a better not be 0.

**5:21** · Let me signal that here.

**5:23** · a different from 0.

**5:29** · 1 over a, 0, 0.

**5:33** · 0.

**5:34** · I want to make that into a 1.

**5:36** · So 1 over a minus b, and-- you guessed it-- a minus b has to be different from 0.

**5:47** · 0.

**5:52** · -1 over a minus b.

**5:56** · 1 over a minus b.

**5:58** · 0, 0, 1, 0, -1 over a minus b.

**6:05** · 1 over a minus b.

**6:09** · AUDIENCE: \[INAUDIBLE\] PROFESSOR: Someone's pointing a mistake.

**6:13** · AUDIENCE: Yeah, the (2, 2) entry, you should have a 1.

**6:16** · PROFESSOR: Oh, you're absolutely right.

**6:22** · Thank you.

**6:25** · All right.

**6:27** · So not much left to do.

**6:29** · We only have to eliminate b over a and b over a.

**6:31** · That's a little bit computationally heavy.

**6:35** · So what do you have to do?

**6:39** · You just have to basically subtract-- replace row 1 by row 1 minus b over a times row 2 plus row 3.

**6:47** · Let me write that down.

**6:50** · row 1 minus b over a times row 2 plus row 3.

**6:59** · You want that to go into your row 1.

**7:02** · These stay the same.

**7:07** · -1 over a minus b.

**7:09** · 1 over a minus b.

**7:21** · This is where I'm going to go to my notes and tell you that these numbers are 1 over a minus b, 0 minus b over a, a minus b.

**7:37** · That looks pretty awful.

**7:39** · But that is A inverse.

**7:41** · And we're done.

**7:43** · Except it looks terrible.

**7:45** · So let me just write it in a nicer way.

**7:48** · A inverse equals-- see, you're dividing everything by a minus b, so pull out that factor.

**7:57** · 1, 0, minus b over a; -1, 1, 0; 0, -1, 1.

**8:06** · Looks much better now.

**8:07** · So here's your A inverse.

**8:09** · And the other question was: what are the conditions on a and b for the matrix A to be invertible?

### The Conditions on a and B for the in Matrix a To Be Invertible

**8:16** · Well, a has to be non-zero, and a has to be different from b.

**8:20** · And we're done.

**8:21** · That's it for today.

**8:22** · See you next time.