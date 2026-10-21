> 对应主课笔记：[[L3 矩阵乘法与逆]]

![](https://www.youtube.com/watch?v=XkY2DOUCWMU)

Multiplying two matrices represents applying one transformation after another.  
Help fund future projects: https://www.patreon.com/3blue1brown  
An equally valuable form of support is to simply share some of the videos.  
Home page: https://www.3blue1brown.com/  
  
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

### Linear transformations recap

**0:00** · \[Submit subtitle corrections at criblate.com\] Hey everyone, where we last left off, I showed what linear transformations look like and how to represent them using matrices.

**0:18** · This is worth a quick recap because it's just really important, but of course if this feels like more than just a recap, go back and watch the full video.

**0:25** · Technically speaking, linear transformations are functions with vectors as inputs and vectors as outputs, but I showed last time how we can think about them visually as smooshing around space in such a way that grid lines stay parallel and evenly spaced, and so that the origin remains fixed.

**0:41** · The key takeaway was that a linear transformation is completely determined by where it takes the basis vectors of the space, which for two dimensions means i-hat and j-hat.

**0:51** · This is because any other vector could be described as a linear combination of those basis vectors.

**0:57** · A vector with coordinates (x, y) is x times i-hat plus y times j-hat.

**1:03** · After going through the transformation, this property that grid lines remain parallel and evenly spaced has a wonderful consequence.

**1:10** · The place where your vector lands will be x times the transformed version of i-hat plus y times the transformed version of j-hat.

**1:18** · This means if you keep a record of the coordinates where i-hat lands and the coordinates where j-hat lands, you can compute that a vector which starts at (x, y) must land on x times the new coordinates of i-hat plus y times the new coordinates of j-hat.

**1:33** · The convention is to record the coordinates of where i-hat and j-hat land as the columns of a matrix, and to define this sum of the scaled versions of those columns by x and y to be matrix-vector multiplication.

**1:46** · In this way, a matrix represents a specific linear transformation, and multiplying a matrix by a vector is what it means computationally to apply that transformation to that vector.

**1:58** · Alright, recap over, on to the new stuff.

### Matrix composition concept

**2:01** · Oftentimes, you find yourself wanting to describe the effects of applying one transformation and then another.

**2:07** · For example, maybe you want to describe what happens when you first rotate the plane 90 degrees counterclockwise, then apply a shear.

**2:15** · The overall effect here, from start to finish, is another linear transformation, distinct from the rotation and the shear.

**2:22** · This new linear transformation is commonly called the composition of the two separate transformations we applied.

**2:28** · And like any linear transformation, it can be described with a matrix all of its own by following i-hat and j-hat.

**2:36** · In this example, the ultimate landing spot for i-hat after both transformations is (1, 1), so let's make that the first column of a matrix.

**2:44** · Likewise, j-hat ultimately ends up at the location (-1, 0), so we make that the second column of the matrix.

**2:52** · This new matrix captures the overall effect of applying a rotation then a shear, but as one single action, rather than two successive ones.

**3:03** · Here's one way to think about that new matrix.

### Visualizing matrix product

**3:05** · If you were to take some vector and pump it through the rotation, then the shear, the long way to compute where it ends up is to first multiply it on the left by the rotation matrix, then take whatever you get and multiply that on the left by the shear matrix.

**3:20** · This is, numerically speaking, what it means to apply a rotation then a shear to a given vector.

**3:26** · But whatever you get should be the same as just applying this new composition matrix that we just found by that same vector, no matter what vector you chose, since this new matrix is supposed to capture the same overall effect as the rotation then shear action.

**3:42** · Based on how things are written down here, I think it's reasonable to call this new matrix the product of the original two matrices, don't you?

**3:50** · We can think about how to compute that product more generally in just a moment, but it's way too easy to get lost in the forest of numbers.

**3:56** · Always remember that multiplying two matrices like this has the geometric meaning of applying one transformation then another.

**4:05** · One thing that's kind of weird here is that this has us reading from right to left.

**4:10** · You first apply the transformation represented by the matrix on the right, then you apply the transformation represented by the matrix on the left.

**4:17** · This stems from function notation, since we write functions on the left of variables, so every time you compose two functions, you always have to read it right to left.

**4:25** · Good news for the Hebrew readers, bad news for the rest of us.

### Computing composition

**4:29** · Let's look at another example.

**4:31** · Take the matrix with columns (1, 1) and (-2, 0), whose transformation looks like this.

**4:37** · And let's call it M1.

**4:40** · Next, take the matrix with columns (0, 1) and (2, 0), whose transformation looks like this.

**4:47** · And let's call that guy M2.

**4:49** · The total effect of applying M1 then M2 gives us a new transformation, so let's find its matrix.

**4:56** · But this time, let's see if we can do it without watching the animations, and instead just using the numerical entries in each matrix.

**5:04** · First, we need to figure out where i-hat goes.

**5:08** · After applying M1, the new coordinates of i-hat, by definition, are given by that first column of M1, namely (1, 1).

**5:16** · To see what happens after applying M2, multiply the matrix for M2 by that vector, (1, 1).

**5:25** · Working it out, the way I described last video, you'll get the vector (2, 1).

**5:30** · This will be the first column of the composition matrix.

**5:34** · Likewise, to follow j-hat, the second column of M1 tells us that it first lands on (-2, 0).

**5:42** · Then, when we apply M2 to that vector, you can work out the matrix-vector product to get (0, -2), which becomes the second column of our composition matrix.

**5:56** · Let me talk through that same process again, but this time I'll show variable entries in each matrix, just to show that the same line of reasoning works for any matrices.

### General matrix multiplication

**6:05** · This is more symbol-heavy and will require some more room, but it should be pretty satisfying for anyone who has previously been taught matrix multiplication the more rote way.

**6:14** · To follow where i-hat goes, start by looking at the first column of the matrix on the right, since this is where i-hat initially lands.

**6:22** · Multiplying that column by the matrix on the left is how you can tell where the intermediate version of i-hat ends up after applying the second transformation.

**6:31** · So the first column of the composition matrix will always equal the left matrix times the first column of the right matrix.

**6:42** · Likewise, j-hat will always initially land on the second column of the right matrix.

**6:48** · So multiplying the left matrix by this second column will give its final location, and hence that's the second column of the composition matrix.

**7:00** · Notice there's a lot of symbols here, and it's common to be taught this formula as something to memorize, along with a certain algorithmic process to help remember it.

**7:09** · But I really do think that before memorizing that process, you should get in the habit of thinking about what matrix multiplication really represents, applying one transformation after another.

**7:19** · Trust me, this will give you a much better conceptual framework that makes the properties of matrix multiplication much easier to understand.

### Non-commutativity

**7:27** · For example, here's a question.

**7:28** · Does it matter what order we put the two matrices in when we multiply them?

**7:33** · Well, let's think through a simple example, like the one from earlier.

**7:37** · Take a shear, which fixes i-hat and smooshes j-hat over to the right, and a 90 degree rotation.

**7:43** · If you first do the shear, then rotate, we can see that i-hat ends up at (0, 1) and j-hat ends up at (-1, 1).

**7:51** · Both are generally pointing close together.

**7:53** · If you first rotate, then do the shear, i-hat ends up over at (1, 1), and j-hat is off in a different direction at (-1, 0), and they're pointing, you know, farther apart.

**8:06** · The overall effect here is clearly different, so evidently, order totally does matter.

**8:12** · Notice, by thinking in terms of transformations, that's the kind of thing that you can do in your head by visualizing.

**8:18** · No matrix multiplication necessary.

**8:21** · I remember when I first took linear algebra, there was this one homework problem that asked us to prove that matrix multiplication is associative.

### Associativity and conclusion

**8:29** · This means that if you have three matrices, A, B, and C, and you multiply them all together, it shouldn't matter if you first compute A times B, then multiply the result by C, or if you first multiply B times C, then multiply that result by A on the left.

**8:44** · In other words, it doesn't matter where you put the parentheses.

**8:48** · Now, if you try to work through this numerically, like I did back then, it's horrible, just horrible, and unenlightening for that matter.

**8:55** · But when you think about matrix multiplication as applying one transformation after another, this property is just trivial.

**9:03** · Can you see why?

**9:04** · What it's saying is that if you first apply C, then B, then A, it's the same as applying C, then B, then A.

**9:12** · I mean, there's nothing to prove.

**9:14** · You're just applying the same three things one after the other, all in the same order.

**9:19** · This might feel like cheating, but it's not.

**9:21** · This is an honest-to-goodness proof that matrix multiplication is associative, and even better than that, it's a good explanation for why that property should be true.

**9:31** · I really do encourage you to play around more with this idea, imagining two different transformations, thinking about what happens when you apply one after the other, and then working out the matrix product numerically.

**9:42** · Trust me, this is the kind of playtime that really makes the idea sink in.

**9:47** · In the next video, I'll start talking about extending these ideas beyond just two dimensions. See you then!