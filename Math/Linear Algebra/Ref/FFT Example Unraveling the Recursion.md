![](https://www.youtube.com/watch?v=Ty0JcR6Dvis)

This video is meant as further support to the main video on the FFT https://youtu.be/h7apO7q16V0  
We break down how the FFT evaluates a particular polynomial at the roots of unity by unraveling the recursive process completely.  
  
0:00 Introduction  
1:13 FFT Example Breakdown  
  
Support: https://www.patreon.com/reducible  
  
This video wouldn't be possible without the open source manim library created by 3blue1brown: https://github.com/3b1b/manim  
  
Here is link to the repository that contains the code used to generate the animations in this video: https://github.com/nipunramk/Reducible  
  
Music:  
All music by Aakash Gandhi

## Transcript

### Introduction

**0:00** · i'm assuming most of you are coming to this video after watching the main video this video is meant to dig a little deeper into how the actual implementation of the fft works to give a super quick recap of the main ideas of the first video we motivated the idea of the fft through

**0:15** · polynomial multiplication the key idea there is that polynomial multiplication is much faster when we use a point value representation of polynomials but the question that we had to immediately address is how do we convert polynomials from a coefficient representation to a value representation this conversion was the fast fourier transform where if we pick our set of evaluation points to be the roots of unity we formulate a beautiful recursive algorithm to evaluate polynomials in just o of n log n time this was the

**0:46** · implementation for that algorithm so i'm going to be honest when i first learned the fft in a college algorithm class and saw this implementation this is basically in a nutshell what happened no matter how hard you try to understand everything up to this point i feel like most people will be like me and get lost in the details whenever you are lost one of the most helpful things you can do is completely break down a specific example let's do just that suppose i provide the

### FFT Example Breakdown

**1:16** · following input to the fft function which represents a degree 3 polynomial we first define n is equal to 4 this does not meet the base case criteria so we proceed to define omega as e to the power of 2 pi i over 4 which is equivalent to the complex number i what this means for us is that this will make sure that the roots of unity that we evaluate the polynomial at are the fourth roots of unity which correspond to the following points on the unit circle

**1:46** · we then define p e as the even degree terms of five and two which makes p e the linear function five plus two x p o is similarly defined with odd degree terms of three and one which makes it another linear function three plus x we now make two recursive

**2:03** · calls to the f of t functions with these linear functions as inputs let's see what happens in the recursive call on the even degree terms here we define n to be 2 and then define omega as e to the power of 2 pi i over 2 which is equivalent to negative 1 meaning that the polynomial will be evaluated at the second roots of unity or the following points on the unit circle we then proceed with another split of the polynomial into even and odd degree terms both of which are now just constants we

**2:34** · pass the zero degree polynomials into two more recursive calls both of these recursive calls end up hitting the base case and returning whatever input was just passed in the outputs of these recursive calls are then assigned to the variables y e and y o we can now proceed to define

**2:54** · our output y for this call which is initially a two element list of zeros we proceed into our for loop of which the first line assigns the zeroth index of y to be the zeroth index of y e plus omega to the power of zero multiplied by the zeroth index of y o this is essentially the

**3:13** · evaluation step required for the root of unity number one which is omega to the power of 0. this expression ends up being 7 which updates the y list accordingly proceeding to the second line of the for loop we assign the first index of the y list to be the zeroth index of y e minus omega to the power of zero multiplied by the zeroth index of y o this corresponds to the evaluation

**3:38** · step for root of unity number two which is omega to the power of one and the negative pair of our first root of unity the value of this expression is 3 which is then updated in the list we now return this value after finishing the recursive call on the even degree terms we proceed to do the same process on the recursive call on the odd degree terms the logic is exactly the same but with a different input so i'll let you just follow along with the animations at your own pace

**4:15** · \[Music\]

**4:49** · now on to the key step after we get the return values of the recursive calls on the even and odd degree term polynomials this is then assigned to the y e and y o variables in our current call now when we define our y list it has four values all of which are initially zero we then proceed into the for loop in the

**5:10** · first iteration the first line assigns the zeroth index of y to the zeroth index of y e plus omega to the power of zero times the zeroth index of y o this is essentially evaluating the original polynomial at the first root of unity omega to the power of 0 and the expression gives us the value 11. proceeding now to the second line of the for loop in our first iteration we now want to assign the second index of y to the zeroth index of y e minus omega

**5:39** · to the power of zero multiplied by the zeroth index of y o this is now evaluating the third root of unity omega squared which is the negative pair of the first root of unity the value of this expression is 3 which is now the second index of our output y list now we go to

**5:59** · the second iteration of the for loop which starts by assigning the first index of y to be the first index of y e plus omega to the power of 1 times index 1 of y o this corresponds to valuing the second root of unity in our unit circle which is just omega to the power of 1.

**6:17** · the value of this expression is the complex number 3 plus 2i which now is the index 1 of our output list in the second line of the for loop we now assign the third index of y to be the first index of y e minus omega to the power of one times index one of y o which evaluates the final root of unity when evaluated this ends up being the complex number three minus two i which is the final element in our output list y

**6:49** · we now have the final output of the f t on our original degree 3 polynomial as a final sanity check it's good to actually try evaluate the polynomial on the 4th roots of unity and check that the values we get do match the ones calculated by the fft if you do this exercise you will see that they do indeed match

**7:16** · that's all for this video and thanks for watching if you enjoyed the content please hit the like button so that this content will be recommended to more people if you want to see more content like this please don't forget to hit the subscribe button and if you want to more directly support the work of this channel please check out the patreon page linked in the description below i'll see you on the next video