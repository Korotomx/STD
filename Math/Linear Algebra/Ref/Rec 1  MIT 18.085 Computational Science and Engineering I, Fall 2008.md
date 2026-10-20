---
title: "Rec 1 | MIT 18.085 Computational Science and Engineering I, Fall 2008"
source: "https://www.youtube.com/watch?v=0oBJN8F616U&list=PL221E2BBF13BECF6C&index=5"
author:
  - "[[MIT OpenCourseWare]]"
published: 2009-02-26
created: 2026-10-20
description: "Recitation 1: Key ideas of linear algebraLicense: Creative Commons BY-NC-SAMore information at http://ocw.mit.edu/termsMore courses at http://ocw.mit.edu"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=0oBJN8F616U)

Recitation 1: Key ideas of linear algebra  
  
License: Creative Commons BY-NC-SA  
More information at http://ocw.mit.edu/terms  
More courses at http://ocw.mit.edu

## Transcript

### Introduction to the course

**0:01** · The following content is provided under a Creative Commons license.

**0:03** · Your support will help MIT OpenCourseWare continue to offer high quality educational resources for free.

**0:09** · To make a donation, or to view additional materials from hundreds of MIT courses, visit MIT OpenCourseWare at ocw.mit.edu.

### Linear combinations of vectors

**0:21** · PROFESSOR STRANG: This is the one and only review, you could say, of linear algebra.

**0:30** · I just think linear algebra is very important.

**0:33** · You may have got that idea.

**0:35** · And my website even has a little essay called Too Much Calculus.

**0:43** · Because I think it's crazy for all the U.S. universities do this pretty much, you get semester after semester in differential calculus, integral calculus, ultimately differential equations.

**0:57** · You run out of steam before the good stuff, before you run out of time.

**1:03** · And anybody who computes, who's living in the real world, is using linear algebra.

**1:10** · You're taking a differential equation, you're taking your model, making it discrete and computing with matrices.

**1:20** · The world's digital now, not analog.

**1:27** · I hope it's okay to start the course with linear algebra.

**1:33** · But many engineering curricula don't fully recognize that and so if you haven't had an official course, linear algebra, stay with 18.085.

**1:46** · This is a good way to learn it.

**1:48** · You're sort of learning what's important.

**1:51** · So my review would be-- And then this is-- Future Wednesdays will be in our regular room for homework, review, questions of all kinds, and today questions too.

**2:06** · Shall I just fire away for the first half of the time to give you a sense of how I see the subject, or at least within that limited time.

**2:17** · And then questions are totally welcome.

**2:22** · Always welcome, actually.

**2:24** · Right?

**2:24** · So I'll just start right up.

**2:26** · So essentially linear algebra progresses starting with vectors to matrices and then finally to subspaces.

**2:42** · So that's, like, the abstraction.

**2:45** · You could say abstraction, but it's not difficult, that you want to see.

**2:50** · Until you see the idea of a subspace, you haven't really got linear algebra.

**2:56** · Okay, so I'll start at the beginning.

**2:58** · What do you do with vectors?

**3:01** · Answer: you take their linear combinations.

**3:04** · That's what you can do with a vector.

**3:06** · You can multiply it by a number and you can add or subtract.

**3:11** · So that's the key operation.

**3:13** · Suppose I have vectors u, v and w.

**3:18** · Let me take three of them.

**3:20** · So I can take their combinations.

**3:22** · So some combination will be, say some number times u plus some number times v plus some number times w.

**3:33** · So these numbers are called scalars.

**3:36** · So these would be called scalars.

**3:39** · And the whole thing is a linear combination.

**3:44** · Let me abbreviate those words, linear combination.

**3:48** · And you get some answer, say b.

**3:54** · But let's put it down, make this whole discussion specific.

**4:00** · Yeah, I started a little early, I think.

**4:05** · I'm going to take three vectors, u, v and w, and take their combinations.

**4:12** · They're carefully chosen.

**4:14** · My u is going to be \[1, -1, 0\].

**4:20** · And I'll take vectors in three dimensions.

**4:23** · So that means their combinations will be in three dimensions, R^3, three-dimensional space.

**4:29** · So that'll be u and then v, let's take 0, I think, 1 and -1.

**4:40** · Okay.

**4:41** · Suppose I stopped there and took their linear combinations.

**4:45** · It's very helpful to see a picture in three-dimensional space.

**4:49** · I mean the great thing about linear algebra, it moves into n-dimensional space, 10-dimensional, 100-dimensional, where we can't visualize, but yet, our instinct is right if we just follow.

**5:02** · So what's your instinct if I took those two vectors, and notice they're not on the same line, one isn't a multiple of the other, they go in different directions.

**5:13** · If I took their combinations, say x\_1\*u + x\_2\*v. Oh now, let me push, this is a serious question.

**5:23** · If I took all their combinations.

**5:26** · So let me try to draw a little bit.

**5:28** · Okay.

**5:29** · I'm in three-dimensional space and u goes somewhere, maybe there and v goes somewhere, maybe here.

**5:39** · Now suppose I take all the combinations, so I could multiply that first guy by any number, that would fill the line.

**5:46** · I can multiply that second guy, v. So this was u and this was v. I can multiply that by any number x\_2, that would fill its line.

**5:56** · Each of those lines I would later call a one-dimensional subspace, just a line.

**6:01** · But now, what happens if I take all combinations of the two?

**6:06** · What do you think?

**6:08** · You got a plane.

**6:09** · Get a plane.

**6:11** · If I take anything on this line and anything on this line and add them up you can see that I'm not going to fill 3-D.

**6:19** · But I'm going to fill a plane and that maybe takes a little thinking.

**6:25** · It just, then it becomes sort of, you see that that's what it has to be.

**6:31** · Okay, now I'm going to have a third vector.

**6:34** · Okay, my third vector will be \[0, 0, 1\].

**6:38** · Okay, so that \[0, 0, 1\] is 0 in the x, 0 in the y and 1 in the z direction.

**6:44** · So there's w.

**6:48** · Now I want to take their combinations.

**6:51** · So let me do that very specifically.

**6:54** · How do I take combinations?

**6:57** · This is important.

**6:58** · Seems it's very simple, but important.

**7:01** · I like to think of taking the combinations of some vectors, I'm always putting vectors into the columns of a matrix.

**7:11** · So now I'm going to move to step two: matrix.

**7:15** · I'm going to move to step two and maybe I'll put it-- well no, I better put it here.

**7:20** · Okay, step two is the matrix has those vectors in its columns.

**7:26** · So in this case, it's three by three.

**7:31** · That's my matrix and I'm going to call it A.

**7:38** · How do I take combinations of vectors?

**7:44** · I should have maybe done it in detail here, but I'll just do it with a matrix here.

**7:52** · Watch this now.

**7:54** · If I multiply A by the vector of x's, what that does, so this is now A times x, so very important, a matrix times a vector.

**8:10** · What does it do?

**8:12** · The output is just what I want.

**8:15** · This is the output.

**8:17** · It takes x\_1 times the first column plus x\_2 times the second plus x\_3 times the third.

**8:24** · That's the way matrix multiplication works, by columns.

**8:28** · And you don't always see that.

**8:30** · Because what do you see?

**8:32** · You probably know how to multiply that matrix by that vector.

**8:35** · Let me ask you to do it.

**8:38** · What do you get?

**8:40** · So everybody does it a component at a time.

**8:43** · So what's the first component of the answer? x\_1, yeah.

**8:48** · How do you get that?

**8:49** · It's row times the vector.

**8:52** · And when I say "times", I really mean that dot product.

**8:56** · This plus this plus this is x\_1.

**9:00** · And what about the second row?

**9:05** · -x\_1 + x\_2.

**9:06** · Or I'll just say x\_2 - x\_1.

**9:09** · And the third guy, the third component would be x\_3 - x\_2, right?

**9:22** · So right away I'm going to say, I'm going to call this matrix A a difference matrix.

**9:28** · It always helps to give names to things.

**9:31** · So this A is a difference matrix because it takes differences of the x's.

**9:37** · And I would even say a first difference matrix because it's just the straightforward difference and we'll see second differences in class Friday.

**9:48** · So that's what A does.

**9:50** · But you remember my first point was that when a matrix multiplies a vector, the result is a combination of the columns.

**10:01** · And that's not always, because see, I'm looking at the picture not just by numbers.

**10:07** · You know, with numbers I'm just doing this stuff.

**10:10** · But now I'm stepping back a little bit and saying I'm combining.

**10:14** · It's this vector times x\_1.

**10:18** · That vector times x\_1 plus this vector times x\_2 plus that one times x\_3 added together gives me this.

**10:25** · Saying nothing complicated here.

**10:28** · It's just look at it by vectors, also.

**10:36** · It's a little interesting, already.

**10:39** · Here we multiplied these vectors by numbers. x\_1, x\_2, x\_3.

**10:47** · That was our thinking here.

**10:49** · Now our thinking here is a little-- we've switched slightly.

**10:52** · Now I'm multiplying the matrix times the numbers in x.

**10:57** · Just a slight switch, multiply the matrix times the number.

**11:01** · And I get some answer, b.

**11:03** · Which is this, this is b.

**11:07** · And of course, I can do a specific example like, suppose I take, well, I could take the squares to be in x.

**11:19** · So suppose I take A times the first three squares, \[1, 4, 9\].

**11:27** · What answer would I get?

**11:30** · Just to keep it clear that we're very specific here.

**11:35** · So what would be the output be?

**11:38** · I think of this as the input, the \[1, 4, 9\], the x's.

**11:42** · Now the machine is multiply by A and here's the output.

**11:48** · And what would be the output?

**11:49** · What numbers am I going to get there?

**11:51** · Yeah?

**11:52** · One, three, something? \[1, 3, 5\].

**11:57** · Which is actually a little neat that you find the differences of the squares are the odd numbers.

**12:06** · That appealed to me in school somehow.

**12:11** · That was already a bad sign, right?

**12:13** · This dumb kid notices that you take differences of squares and get odd numbers, whatever.

**12:21** · So now is a big step.

**12:25** · This was the forward direction, right?

**12:29** · Input, and there's the output.

**12:31** · But now the real reality-- That's easy and important, but the more deep problem is, what if I give you b and ask for x?

**12:48** · So again, we're switching the direction here.

**12:52** · We're solving an equation now, or three equations and three unknowns, Ax=b.

**12:58** · So if I give you this b, can you get x?

**13:02** · How do you solve three equations?

**13:06** · We're looking backwards.

**13:07** · Now that won't be too hard for this particular matrix that I chose; because it's triangular, we'll be able to go backwards.

**13:23** · So let me do that.

**13:25** · Let me take b to be-- It's a vector, it's got three components.

**13:31** · And now I'm going to go backwards to find x.

**13:36** · Or we will.

**13:39** · So do you see the three equations?

**13:41** · Here they are: x\_1 is b\_1, this is b\_2, that difference is b\_3.

**13:47** · Those are my three equations.

**13:49** · Three unknown x's, three known right-hand sides.

**13:53** · Or I think of it as A times x, as a matrix times x giving a vector b.

**14:00** · What's the answer?

**14:02** · As I said, we're going to be able to do this.

**14:05** · We're going to be able to solve this system easily because it's already triangular.

**14:11** · And it's actually lower triangular so that means we'll start from the top.

**14:17** · So the answers, the solution will be what?

**14:24** · Let's make room for it. x\_1, x\_2, and x\_3 I want to find.

**14:30** · And what's the answer?

**14:33** · Can we just go from top to bottom now?

**14:37** · What's x\_1? b\_1, great.

**14:42** · What's x\_2?

**14:44** · So x\_2 - x\_1.

**14:47** · These are my equations.

**14:48** · So what's x\_2 - x\_1?

**14:50** · Well, it's b\_2, so what is x\_2? b\_1 + b\_2, right?

**14:59** · And what's x\_3?

**15:03** · What do we need there for x\_3?

**15:05** · So I'm looking at the third equation.

**15:08** · That'll determine x\_3.

**15:11** · When I see it this way, I see those ones and I see it multiplying x\_3.

**15:16** · And what do I get?

**15:20** · Yeah, so x\_3 minus this guy is b\_3, so I have to add in another b\_3, right?

**15:28** · I'm doing sort of substitution down as I go.

**15:31** · Once I learned that x\_1 was b\_1 I used it there to find x\_2.

**15:38** · And now I'll use x\_2 to find x\_3.

**15:40** · And what do I get again? x\_3 is, I'll put the x\_2 over there.

**15:48** · I think you've got it. b\_1 + b\_2 + b\_3.

**15:55** · So that's the solution.

**15:59** · Not difficult because the matrix was triangular.

**16:02** · But let's think about that solution.

**16:06** · That solution is a matrix times b.

**16:13** · When you look at that-- So this is like a good early step in linear algebra.

**16:19** · When I look at that I see a matrix multiplying b.

**16:26** · You take that step up to seeing a matrix.

**16:29** · And you can just read it off.

**16:30** · So let me say, what's the matrix there that's multiplying b to give that answer?

**16:41** · Remember the columns of this matrix-- well, I don't know how you want to read it off.

**16:47** · But one way is, the think the columns of that matrix are multiplying b\_1, b\_2, and b\_3 to give this.

**16:57** · So what's the first column of the matrix?

**17:01** · It's whatever I'm reading off, the coefficients, really, of b\_1 here: \[1, 1, 1\].

**17:09** · And what's the second column of the matrix? \[0, 1, 1\].

**17:13** · Good.

**17:13** · Zero b\_2's, one, one.

**17:16** · And the third is? \[0, 0, 1\].

**17:19** · Good.

**17:23** · Now, so lots of things to comment here.

**17:27** · Let me write up again here, this is x.

**17:30** · That was the answer.

**17:34** · It's a matrix times b.

**17:38** · And what's the name of that matrix?

**17:42** · It's the inverse matrix.

**17:44** · If Ax gives b, the inverse matrix does it the other way around, x is A inverse b.

**17:50** · Let me just put that over here.

**17:53** · If Ax is b, then x should be A inverse b.

**18:01** · So we had inverse, I wrote down inverse this morning but without saying the point, but so you see how that comes?

**18:10** · I mean, if I want to go formally, I multiply both sides by A inverse.

**18:15** · If there is an A inverse.

**18:18** · That's a critical thing as we saw.

**18:20** · Is the matrix invertible?

**18:21** · The answer here is, yes, there is an inverse.

**18:24** · And what does that really mean?

**18:26** · The inverse is the thing that takes us from b back to x.

**18:32** · Think of A as kind of a-- multiplying by A is kind of a mapping, mathematicians use the word, or transform.

**18:40** · Transform would be good.

**18:42** · Transform from x to b.

**18:45** · And this is the inverse transform.

**18:49** · So it doesn't happen to be the discrete Fourier transform or a wavelet transform, it's a-- well, actually we could give it a name.

**18:57** · This is kind of a difference transform, right?

**19:00** · That's what A did, took differences.

**19:03** · So what does A inverse do?

**19:06** · It takes sums.

**19:09** · It takes sums.

**19:10** · That's why you see 1, 1 and 1, 1, 1 along the rows because it's just adding, and you see it here in fully display.

**19:20** · It's a sum matrix.

**19:21** · I might as well call it S for sum.

**19:25** · So that matrix, that sum matrix is the inverse of the different matrix.

**19:33** · And maybe, since I hit on calculus earlier, you could say that calculus is all about one thing and its inverse.

**19:45** · The derivative is A, and what's S?

**19:50** · In calculus.

**19:51** · The integral.

**19:53** · The whole subject is about one operation, now admittedly it's not a matrix, it operates on functions instead of just little vectors, but that's the main point.

**20:06** · The fundamental theorem of calculus is telling us that integration's the inverse of differentiation.

**20:14** · So this is good and if I put in b = \[1, 3, 5\] for example just to put in some numbers, if I put in b = \[1, 3, 5\], what would the x that comes out be?

**20:31** · \[1, 4, 9\].

**20:33** · Right?

**20:33** · Because it takes us back.

**20:35** · Here, previously we started, we took differences of \[1, 4, 9\], got \[1, 3, 5\].

**20:40** · Now if we take sums of \[1, 3, 5\], we get \[1, 4, 9\].

**20:46** · Now we have a system of linear equations.

**20:51** · Now I want to step back and see what was good about this matrix.

**20:56** · Somehow it has an inverse.

**20:59** · Ax=b has a solution, in other words.

**21:03** · And it has only one solution, right?

**21:05** · Because we worked it out.

**21:07** · We had no choice.

**21:08** · That was it.

**21:10** · So there's just one solution.

**21:12** · There's always one and only one solution.

**21:14** · It's like a perfect transform from the x's to the b's and back again.

**21:20** · Yeah so that's what an invertible matrix is.

**21:24** · It's a perfect map from one set of x's to the x's and you can get back again.

**21:33** · Questions always.

**21:36** · Now I think I'm ready for another example.

**21:39** · There are only two examples.

**21:41** · And actually these two examples are on the 18.06 web page.

**21:47** · If some people asked after class how to get sort of a review of linear algebra, well the 18.06 website would be definitely a possibility.

**22:06** · Well, I'll put down the OpenCourseWare website, mit.edu and then you would look at the linear algebra course or the math one.

**22:20** · What is it? web.math.edu, is that it?

**22:26** · No, maybe that's an MIT-- so is it math?

**22:34** · I can't live without edu at the end, right?

**22:39** · Is it just edu?

**22:41** · Whatever!

**22:49** · So that website has, well, all the old exams you could ever want if you wanted any.

**22:55** · And it has this example and you click on Starting With Two Matrices.

**23:06** · And this is one of them.

**23:09** · Okay, ready for the other.

**23:11** · So here comes the second matrix, second example that you can contrast.

**23:16** · Second example is going to have the same u.

**23:20** · Let me put-- our matrix, I'm going to call it, what am I going to call it?

**23:26** · Maybe C. So it'll have the same u.

**23:33** · And the same v. But I'm going to change w.

**23:39** · And that's going to make all the difference.

**23:41** · My w, I'm going to make that into w.

**23:48** · So now I have three vectors.

**23:52** · I can take their combinations.

**23:55** · I can look at the equation Cx=b .

**23:58** · I can try to solve it.

**24:00** · All the normal stuff with those combinations of those three vectors.

### Dependent vectors and solutions

**24:09** · And we'll see a difference.

**24:12** · So now, what happens if I do-- Could I even like do just a little erase to deal with C now?

**24:24** · How does C differ?

**24:26** · If I change this multiplication from A to C, to this new matrix.

**24:34** · Then what we've done is to put in a minus one there, right?

**24:38** · That's the only change we made.

**24:41** · And what's the change in Cx?

**24:49** · I've changed the first row, so I'm going to change the first row of the answer to what? x\_1 - x\_3.

**25:04** · You could say again, as I said this morning, you've sort of changed the boundary condition maybe.

**25:09** · You've made this difference equation somehow circular.

**25:14** · That's why I'm using that letter C.

**25:23** · Is it different?

**25:25** · Ah, yes!

**25:26** · I didn't get it right here.

**25:29** · Thank you, thank you very much.

**25:33** · Absolutely.

**25:35** · I mean that would have been another matrix that we could think about but it wouldn't have made the point I wanted, so thanks, that's absolutely great.

**25:42** · So now it's correct here and this is correct and I can look at equations but can I solve them?

**25:53** · Can I solve them?

**25:56** · And you're guessing already, no we can't do it.

**26:00** · Right?

**26:02** · So now let me maybe go to a board, work below, because I'd hate to erase, that was so great, that being able to solve it in a nice clear solution and some matrix coming in.

**26:17** · But now, how about this one?

**26:19** · Okay.

**26:24** · One comment I should have made here.

**26:27** · Suppose the b's were zero.

**26:30** · Suppose I was looking at, originally at A times x equal all zeroes, What's x?

**26:38** · If all the b's were zero in this, this was the one that dealt with the matrix A. If all the b's are zero then the x's are zero.

**26:50** · The only way to get zero right-hand sides, b's, was to have zero x's.

**26:58** · Right?

**27:01** · If you wanted to get zero out, you had to put zero in.

**27:06** · Well, you can always put zero in and get zero out, but here you can put other vectors in and get zero out.

**27:12** · So I want to say there's a solution with zeroes out, coming out of C, but some non-zeroes going in.

**27:22** · And of course we know from this morning that that's a signal that it's a different sort of matrix, there won't be an inverse, we've got questions.

**27:36** · Tell me all the solutions.

**27:39** · All the solutions, so actually not just one, well you could tell me one, tell me one first.

**27:44** · AUDIENCE: \[UNINTELLIGIBLE\] PROFESSOR STRANG: \[1, 1, 1\].

**27:46** · Okay.

**27:47** · Now tell me all.

**27:48** · AUDIENCE: C, C, C.

**27:50** · PROFESSOR STRANG: \[C, C, C\].

**27:51** · Yeah.

**27:52** · That whole line through \[1, 1, 1\].

**27:55** · And that would be normal.

**27:57** · So this is a line of solutions.

**28:01** · Right.

**28:01** · A line of a solutions.

**28:03** · I think of \[1, 1, 1\] as in some solution space, and then all multiples.

**28:08** · That whole line.

**28:10** · Later I would say it's a subspace.

**28:13** · When I say what that word subspace means it's just this-- linear algebra's done its job beyond just \[1, 1, 1\].

**28:23** · Okay.

**28:25** · So, again, it's this fact of-- if we only know the differences-- Yeah.

**28:38** · You can see different ways that this has got problems.

**28:42** · So that's C times x.

**28:43** · Now one way to see a problem is to say we can get the answer of all zeroes by putting constants.

**28:52** · All that's saying in words the differences of a constant factor are all zeroes, right?

**28:58** · That's all that happened.

**29:00** · Another way to see a problem if I had this system of equations, how would you see that there's a problem, and how would you see that there is sometimes an answer and even decide when?

### Solvability and subspaces

**29:13** · I don't know if you can take a quick look.

**29:17** · If I had three equations, x\_1-x\_3 is b\_1, this equals b\_2, this equals b\_3.

**29:27** · Do you see something that I can do to the left sides that's important somehow?

**29:36** · Suppose I add those left-hand sides.

**29:39** · What do I get?

**29:41** · And I'm allowed to do that, right?

**29:42** · If I've got three equations I'm allowed to add them, and I would get zero, if I add, I get zero equals -- I have to add the right-sides of course -- b\_1+b\_2+b\_3.

**29:57** · I hesitate to say a fourth equation because it's not independent of those three, but it's a consequence of those three.

**30:04** · So actually this is telling me when I could get an answer and when I couldn't.

**30:14** · If I get zero on the left side I have to have zero on the right side or I'm lost.

**30:19** · So I could actually solve this when b\_1+b\_2+b\_3=0.

**30:30** · So I've taken a step there.

**30:33** · I've said that okay, we're in trouble often, but in case the right-side adds up to zero then we're not.

**30:42** · And if you'll allow me to jump to a mechanical meaning of this, if these were springs or something, masses, and these were forces on them -- so I'm solving for displacements of masses that we'll see very soon, and these are forces -- what that equation is saying is, because they're sorta cyclical, it's somehow saying that if the forces add up to zero, if the resulting force is zero, then you're okay.

**31:19** · The springs and masses don't like take off, or start spinning or whatever.

**31:25** · So there's a physical meaning for that condition that it's okay provided, if, the b's add up to zero.

**31:35** · But of course, if the b's don't add up to zero we're lost.

**31:38** · Right yeah.

**31:40** · Okay.

**31:42** · So Cx=b could be solved sometimes, but not always.

**31:52** · The difficulty with C is showing up several ways.

**31:55** · It's showing up in C times a vector x giving zero.

**32:00** · That's bad news.

**32:02** · Because no C inverse can bring you back.

**32:05** · I mean it's like you can't come back from zero.

**32:07** · Once you get to zero, C inverse can never bring you back to x, right?

**32:14** · A took x into b up there, and then A inverse brought back x.

**32:21** · But here there's no way to bring back that x because I can't multiply zero by anything and get back to x.

**32:27** · So that's why I see it's got troubles here.

**32:30** · Here I see it's got troubles because if I add the left sides I get zero.

**32:35** · And therefore the right sides must add to zero.

**32:37** · So you've got trouble several ways.

**32:41** · Ah, let's see another way, let's see geometrically why were in trouble.

**32:46** · Okay, so let me draw a picture to go with that picture.

**32:53** · So there's three-dimensional space.

**32:56** · I didn't change u, I didn't change v, but I changed w to minus one, what does that mean?

**33:06** · Minus one sort of going this way maybe, zero, one is the z direction, somehow I changed it to there.

**33:13** · So this is w star maybe, a different w.

**33:17** · This is the w that gave me problems.

**33:23** · What's the problem?

**33:26** · How does the picture show the problem?

**33:37** · What's the problem with those three vectors, those three columns of C?

**33:45** · Yeah?

**33:46** · AUDIENCE: \[UNINTELLIGIBLE\] PROFESSOR STRANG: There in the same plane.

**33:49** · There in the same plane. w\* gave us nothing new.

**33:53** · We had the combinations of u and v made a plane, and w\* happened to fall in that plane.

**34:00** · So this is a plane here somehow, and goes through the origin of course.

**34:09** · What is that plane?

**34:10** · This is all combinations, all combinations of u, v, and the third guy, w\*.

**34:21** · Right.

**34:22** · It's a plane, and I drew a triangle, but of course, I should draw the plane goes out to infinity.

**34:28** · But the point is there are lots of b's, lots of right-hand sides not on that plane.

**34:36** · Okay.

**34:37** · Now if I drew all combinations of u, v, w, the original w, what have I got?

**34:45** · So let me bring that picture back for a moment.

**34:48** · If I took all combinations of those does w lie in the plane of u and v?

**34:55** · No, right?

**34:56** · I would call it independent.

**34:58** · These three vectors are independent.

**35:00** · These three, u, v, and w\* I would call dependent.

**35:05** · Because the third guy was a combination of the first two.

**35:09** · Okay, so tell me what do I get now?

**35:13** · So now you're really up to 3-D. What do you get if you take all combinations of u, v, and w?

**35:20** · AUDIENCE: \[INAUDIBLE\].

**35:23** · PROFESSOR STRANG: Say it again.

**35:25** · The whole space.

**35:29** · If taking all combinations of u, v, w will give you the whole space.

**35:33** · Why is that?

**35:34** · Well we just showed-- when it was A we showed that we could get every b.

**35:43** · We wanted the combination that gave b and we found it.

**35:48** · So in the beginning when we were working with u, v, w, we found -- and this was short hand here -- this said find a combination to give b, and this says that combination will work.

**36:06** · And we wrote out what x was.

**36:09** · Now what's the difference-- Okay, here.

**36:13** · So those were dependent, sorry, those were independent.

**36:21** · I would even call those three vectors a basis for three-dimensional space.

**36:25** · That word "basis" is a big deal.

**36:28** · So a basis for five-dimensional space is five vectors that are independent.

**36:35** · That's one way to say it.

**36:37** · The second way to say it would be their combinations give the whole five-dimensional space.

**36:42** · A third way to say it-- See if you can finish this sentence.

**36:45** · This is for the independent, the good guys.

**36:48** · If I put those five vectors into a five by five matrix, that matrix will be... invertible.

**37:01** · That matrix will be invertible.

**37:04** · So an invertible matrix is one with a basis sitting in its columns.

**37:09** · It's a transform that has an inverse transform.

**37:12** · This matrix is not invertible, those three vectors are not a basis.

**37:17** · Their combinations are only in a plane.

**37:21** · By the way, a plane as a subspace.

**37:24** · A plane would be a typical subspace.

**37:27** · It's like fill it out.

**37:29** · You took all the combinations, you did your job, but in that case the whole space would count as a subspace too.

**37:37** · That's the way you get subspaces, by taking all combinations.

**37:42** · Okay, now I'm even going to push you one more step and then this example is complete.

### Subspaces and matrix properties

**37:50** · Can you tell me what vectors do you get?

**37:56** · All combinations of u, v, w.

**37:58** · Let me try to write something.

**37:59** · This gives only a plane.

**38:08** · Because we've got two independent vectors but not the third.

**38:12** · Okay.

**38:15** · I don't know if I should even ask.

**38:17** · Do we know an equation for that plane?

**38:20** · Well I think we do if we think about it correctly.

**38:25** · All combinations of u, v, w\* is the same as saying all vectors C times x, right?

**38:41** · Do you agree that those two are exactly the same thing?

**38:48** · This is the key, because we're moving up to vectors, combinations, and now comes subspaces.

**38:56** · If I take all combinations of u, v, w\*, I say that that's the same as all vectors C times x, why's that?

**39:07** · It's what I said in the very first sentence at 4 o'clock.

**39:12** · The combinations of u, v, w\*, how do I produce them?

**39:17** · I create the matrix with those columns.

**39:21** · I multiply them by x's, and I get all the combinations.

**39:28** · And this is just C times x.

**39:31** · So what I've said there is just another way of saying how does matrix multiplication work.

**39:38** · Put the guys in its columns and multiply by a vector.

**39:46** · So we're getting all vectors C times x, and now I was going to stretch it that little bit further.

**39:55** · Can we describe what vectors we get?

**39:58** · So that's my question.

**40:02** · What b's -- so this is b = \[b 1, b 2, b 3\] -- do we get?

**40:09** · We don't get them all.

**40:14** · Right, we don't get them all.

**40:16** · That's the trouble with C. We only get a plane of them.

**40:21** · And now can you tell me which b's we do get when we look at all combinations of these three dependent vectors.

**40:36** · Well we've done a lot today.

**40:39** · Let me just tell you the answer because it's here.

**40:42** · The b's have to add to zero.

**40:45** · That's the equation that the b's have to satisfy.

**40:49** · Because when we wrote out Cx we noticed that the components always added to zero.

**40:58** · Which b's do we get?

**41:00** · We get the ones where the components add to zero.

**41:05** · In other words that's the equation of the plane, you could say.

**41:11** · Yeah.

**41:11** · Actually that's a good way to look at it.

**41:13** · All these vectors are on the plane.

**41:19** · Do the components of u add to zero?

**41:23** · Look at u.

**41:25** · Yes.

**41:26** · Do the components of v add to zero?

**41:30** · Yes.

**41:31** · Add them up.

**41:32** · Do the components of w\*, now that you've fixed it correctly, do they add to zero?

**41:38** · Yes.

**41:38** · So all the combinations will add to zero.

**41:40** · That's the plane.

**41:42** · That's the plane.

**41:44** · You see there are so many different ways to see, and none of this is difficult, but it's coming fast because we're seeing the same thing in different languages.

**41:56** · We're seeing it geometrically in a picture of a plane.

**41:59** · We're seeing it as a combination of vectors.

**42:02** · We're seeing it as a multiplication by a matrix.

**42:05** · And we saw it sort of here by operation, operating and simplifying, and getting the key fact out of the equations.

**42:21** · Well, okay.

**42:22** · I wanted to give you this example, the two examples, because they bring out so many of the key ideas.

**42:31** · The key idea of a subspace.

**42:34** · Shall I just say a little about what that word means?

**42:38** · A subspace.

**42:41** · What's a subspace?

**42:43** · Well, what's a vector space first of all?

**42:48** · A vector space is a bunch of vectors.

**42:51** · And the rule is you have to be able to take their combinations.

**42:56** · That what linear algebra does.

**42:57** · Takes combinations.

**42:59** · So a vector space is one where you take all combinations.

**43:05** · So if I only took just this triangle that would not be a subspace because one combination would be 2u and it would be out of the triangle.

**43:16** · So a subspace, just think of it as a plane, but then of course it could be in higher dimensions.

**43:25** · You know it could be a 7-dimensional subspace inside a 15-dimensional space.

**43:30** · And I don't know if you're good at visualizing that, I'm not.

**43:37** · Never mind.

**43:38** · You you've got seven vectors, you think okay, their combinations give us seven-dimensional subspace.

**43:44** · Each factor has 15 components.

**43:47** · No problem.

**43:48** · I mean no problem for MATLAB certainly.

**43:50** · It's got what, a matrix with a 105 entries.

**43:53** · It deals with that instantly.

**43:55** · Okay, so a subspace is like a vector space inside a bigger one.

**44:03** · That's why the prefix "sub-" is there.

**44:06** · Right?

**44:07** · And mathematics always counts the biggest possibility too, which would be the whole space.

**44:13** · And what's the smallest?

**44:15** · So what's the smallest subspace of R^3?

**44:19** · So I have 3-dimensional space-- you can tell me all the subspaces of R^3.

**44:23** · So there is one, a plane.

**44:25** · Yeah, tell me all the subspaces of R^3.

**44:28** · And then you'll have that word kind of down.

**44:31** · AUDIENCE: \[UNINTELLIGIBLE\] PROFESSOR STRANG: A line.

**44:34** · So planes and lines, those you could say, the real, the proper subspaces.

**44:39** · The best, the right ones.

**44:41** · But there are a couple more possibilities which are?

**44:45** · AUDIENCE: \[UNINTELLIGIBLE\] PROFESSOR STRANG: A point.

**44:47** · Which point?

**44:49** · The origin.

**44:50** · Only the origin.

**44:50** · Because if you tried to say that point was a subspace, no way.

**44:56** · Why not?

**44:56** · Because I wouldn't be able to multiply that vector by five and I would be away from the point.

**45:03** · But the zero subspace, the really small subspace that just has the zero vector, it's got one vector in it.

**45:12** · Not empty.

**45:13** · It's got that one point but that's all.

**45:15** · Okay, so planes, lines, the origin, and then the other possibility for a subspaces is?

**45:25** · The whole space.

**45:26** · Right.

**45:26** · Right.

**45:27** · So the dimensions could be three for the whole space, two for a plane, one for a line, zero for a point.

**45:35** · It just kicks together.

**45:41** · How are we for time?

**45:42** · Maybe I went more than half, but now is a chance to just ask me, if you want to, like anything about the course.

**45:53** · Is at all linear algebra?

**45:54** · No.

**45:55** · But I think I can't do anything more helpful to you then to for you to begin to see-- when you look at a matrix, begin to see what is it doing.

**46:09** · What is it about.

**46:11** · Right, and of course matrices can be rectangular.

**46:14** · So I'll give you a hint about what's coming in the course itself.

**46:20** · We'll have rectangular matrices A, okay.

**46:26** · They're not invertible.

**46:28** · They're taking seven-dimensional space to three-dimensional space or something.

**46:33** · You can't invert that.

**46:35** · What comes up every time-- I sort of got the idea finally.

**46:40** · Every time I see a rectangular matrix, maybe seven by three, that would be seven rows by three columns.

**46:48** · Then what comes up with a rectangular matrix A is sooner or later A transpose sticks its nose in and multiplies that A. And we couldn't do it for our A here.

**47:07** · Actually if I did it for that original matrix A I would get something you'd recognize.

**47:14** · What I want to say is that the course focuses on A transpose A. I'll just say now that that matrix always comes out square, because this would be three times seven times seven times three, so this would be three by three, and it always comes out symmetric.

**47:34** · That's the nice thing.

**47:36** · And even more.

**47:37** · We'll see more.

**47:39** · That's like a hint.

**47:41** · Watch for A transpose A. And watch for it in applications of all kinds.

**47:52** · In networks an A will be associated with Kirchhoff's voltage law, and A transpose with Kirchhoff's current law.

**48:00** · They just teamed up together.

**48:04** · We'll see more.

**48:06** · Alright now let me give you a chance to ask any question.

### Q&A and closing remarks

**48:10** · Whatever.

**48:14** · Homework.

**48:15** · Did I mention homework?

**48:17** · You may have said that's a crazy homework to say three problems 1.1.

**48:24** · I've never done this before so essentially you can get away with anything this week, and indefinitely actually.

**48:37** · How many are-- Is this the first day of MIT classes?

**48:42** · Oh wow.

**48:43** · Okay.

**48:43** · Well, welcome to MIT.

**48:46** · I hope you like it.

**48:49** · It's not so high pressure or whatever is associated with MIT.

**48:57** · It's kind of tolerant.

**49:01** · If my advisees ask for something I always say yes.

**49:04** · It's easier that way.

**49:05** · AUDIENCE: \[LAUGHTER\].

**49:11** · PROFESSOR STRANG: And let me just again-- and I'll say it often and in private.

**49:19** · This is like a grown-up course.

**49:21** · I'm figuring you're here to learn, so it's not my job to force it.

**49:26** · My job is to help it, and hope this is some help.