---
title: "MIT 6.S191: Convolutional Neural Networks"
source: "https://www.youtube.com/watch?v=pqIcoskUuWs&list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI&index=3&t=4s"
author:
  - "[[Alexander Amini]]"
published: 2026-04-13
created: 2026-10-28
description: "MIT Introduction to Deep Learning 6.S191: Lecture 3Convolutional Neural Networks for Computer VisionLecturer: Alexander Amini** New 2026 Edition **For all lectures, slides, and lab materials: htt"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=pqIcoskUuWs)

MIT Introduction to Deep Learning 6.S191: Lecture 3  
Convolutional Neural Networks for Computer Vision  
Lecturer: Alexander Amini  
\*\* New 2026 Edition \*\*  
  
For all lectures, slides, and lab materials: http://introtodeeplearning.com​  
  
Subscribe to stay up to date with new deep learning lectures at MIT, or follow us @MITDeepLearning on Twitter and Instagram to stay fully-connected!!

## Transcript

### Introduction to computer vision

**0:05** · \[music\] Hi everybody. Welcome back to Introduction to Deep Learning day two.

**0:15** · Uh today we're going to be talking about a part of intelligence that I think most of us probably take extremely for granted and that's the sense of sight.

**0:24** · So sight and vision, these are one of the most important human senses and most of us rely on vision every single day, right? It was real this is everything from navigating the physical world, locomoting, manipulating the physical world uh to just even recognizing other objects, other humans, other objects and so on.

**0:45** · Now what is what is vision, right? Vision is to know what is where by looking, right?

**0:53** · But in reality, actually vision is so much more than just recognizing an image or recognizing what's in an image.

**1:00** · It's actually uh about understanding the dynamics of your scene, of your environment as well.

**1:07** · So take this scene for example. We can build computer vision systems that can identify objects in the scene, of course, right? So identify for example that we have cars that we have people but actually vision, true vision, is more about just identifying these objects. It's actually about understanding that okay, the two cars on the left are not actually the same, right? The car that's on the road is likely stopped and it's stopped for a causal reason. It stopped because there are pedestrians about to cross the road, but it will probably move again in the near future, whereas the car on the far left is probably stationary, right?

**1:39** · It's probably parked on the side of the road.

**1:42** · Even though these are two cars, they behave very differently and immediately when you see this picture, all of this information kind of floods in.

**1:50** · Now right, so and it goes obviously even more detailed. The The you look at this picture, the more details I come, and you can actually identify not just what's in the image, but the causal relationships between everything that are actually guiding and driving all of the behaviors that happen through this scene.

**2:09** · So, deep learning is really bringing forward this new wave of understanding all of this deep rich information in a very rich environment, right? In a very rich computer vision system. Right? These are These are algorithms that you've probably seen a lot in the press in the media. This rises This This expands from everything from robotics to mobile computing, biology, health care, medicine, autonomous driving, you know, accessibility, and so on.

**2:38** · There's so many different applications of visions because quite honestly, we as humans rely on vision so much in our daily lives as well.

**2:45** · Right? Deep learning has really taken from the beginning a lot of really recognition style approaches to computer vision, right? Not focusing as much on the behaviors, and focusing much more on the classification, the recognition.

**2:59** · This really started primarily in a lot of industrial applications with facial detection systems. Facial detection first, and then facial recognition second. Detection is just detecting a face, recognizing it goes one layer beyond it to actually relate that face to a particular person or identity.

**3:16** · Another common example that you've probably seen a lot is self-driving cars. Understanding what is around a self-driving car to be able to navigate its environment. Here's an example of a self-driving car that we actually built in this building. It actually lives right downstairs, a couple floors below where you're sitting. And this was built as part of a MIT Toyota collaboration.

**3:38** · Uh and it's it's a radically different type of self-driving car, but it actually relates to today's lecture because it is driven entirely using a single end-to-end computer vision system. There's no mapping in this car.

**3:51** · Uh so, in some sense, it actually behaves much more like a human would drive because humans also don't rely on HD maps. We only drive based off of our two eyes and also based off of a low dimensional map, not a high dimensional map. Low dimensional map being something like Google Maps or something like that on your phone.

**4:09** · And of course, all these other applications that we'll see throughout the lecture today, health care, medicine, diagnosing different types of diseases directly from uh x-ray scans or other medical imaging scans.

### Representing images as data

**4:22** · Now, I started this lecture by actually saying we take a lot of this for granted, right? And I really think that's true, right? And for a computer vision system, we probably need to also go back to the foundations to understand how all of this is represented to a computer, right? Because computers don't have eyes, right? And they actually don't see in color space, they see in numbers, right?

**4:43** · So, what does an image look like to a computer?

**4:47** · Well, to a computer, images are also just numbers, right? And suppose we have a picture of Abraham Lincoln, like you see here. This picture is nothing more than just a matrix, a 2D matrix of numbers. We can represent this looking across the rows and the columns, every cell in this matrix is just a single value. And that value could correspond in this example to the brightness of that cell, brightness ranging from zero to one with one being the most bright.

**5:15** · Now, this is a very simplistic representation, but it's actually extremely powerful, right? It covers already the full space of all grayscale images. And if we wanted to cover the space of colored images as well, we would simply extend this to not be a single two-dimensional matrix, but now a two-dimensional matrix \* 3 because we have three primary colors, red, green, blue.

**5:39** · And if we mix those together, each one of which is a one-dimensional 2D matrix, then we can have a colored image represented to a computer. So, to a computer, grayscale images are nothing more than just 2D images or 2D matrices.

**5:54** · And RGB images are nothing more than three-dimensional matrices, where the third dimension is exactly size three.

**6:03** · Now, two common types of machine learning algorithms for computer vision tasks are, like we saw in yesterday's class in both lectures, regression and classification. Let's start with the classification example to start with computer vision because it's much simpler, right? So, let's say on the left-hand side we have this image, and it's represented as a matrix that you can see in the middle.

**6:27** · And our task is that we want to identify or recognize who is in this image, right? So, it's a classification task.

**6:34** · It's ultimately going from this input of two-dimensional space into a one-dimensional vector of fixed size, and we define that fixed size based off of known categories, known people that we may want to recognize. So, we may want to classify this person into one of four categories in this example, Lincoln, Washington, Jefferson, or Obama.

**6:55** · And given these unstructured uh pixel inputs in grayscale on the left-hand side, can a machine learning model identify which of these four classes it belongs to, right? So, in order to identify these images, obviously, our pipeline needs to be able to tell what is unique and differentiated about each one of these four categories, right? So, let's let's consider that in a bit more detail, right? How does it actually do this?

**7:19** · In order to detect what's relevant in a whole image, we first need to detect what's relevant at these feature levels, right? What are the patterns that make up each of these different categories?

**7:32** · So, for each type of president, what are the features on their face that make up this person and differentiate it from each other person in that category? So, for example, this is a very common theme that you'll see out through today is that classification is simply done by detecting these lower level features and then composing them together in order to detect and classify the higher level groups. So, for example, if you want to detect to detect faces, you as a human might start by detecting eyes, noses, ears.

**8:01** · If you see those things in in an image, you're probably looking at something like a face.

**8:07** · Likewise, if you're looking for cars, you may look for lower level features like wheels, license plates, headlights, etc. Same thing for houses, doors, windows. Steps are the building blocks of those things and you can decompose those even further, right? In order to detect a door, you may be looking for a rectangle with four corners, right?

**8:26** · Um Now, one way to solve this problem is to leverage the knowledge about a particular field. So, like I just said, if you want to detect houses, you as humans, you know what a house looks like, so you can decompose that knowledge of what houses look like into the underlying lower level features, right? So, you could use your own knowledge to say the domain knowledge of what houses look like, I'm going to define these lower level features.

**8:51** · But, and then you could basically build the classification pipeline to first detect those lower level features and then thereby detect the higher level structures across them. But, of course, there's a big problem with this approach is that humans are very uh we take a lot of this for granted again, like I said. So, even detecting or knowing what to look for in let's say a house is a really hard problem for us to define. And in fact, there are so many different variations amongst houses that defining what makes up a house is actually really hard, right?

**9:23** · So, there are viewpoint variations, there are illumination variations that change the color of the scene, size variations, etc. So many both intra-class variations, variations within the class, as well as across different types of classes as well that you want to make sure that you covered the entire space.

**9:42** · So, ultimately, this problem really turns into more of a problem of saying, "How can you identify those lower-level features that are truly representative across the full space of a particular class whilst still being differentiated across those features from other classes as well?"

**10:03** · So, even though our pipeline could use features that we as humans predefine or manually define, this is where this task really starts to break down for human-level recognition because we as humans are just not very good at clearly defining what those lower-level features should be. And this is again due to the incredibly diverse variability of different types of images. So, the question really is, "How can we do better than this?"

**10:30** · And the the answer is that we want a way to both extract those features, but simultaneously learn what the good features even should be that we should be looking for in an image.

### Learning visual features

**10:42** · Now, we can use a neural network-based approach for this and learn directly from data this hierarchy, right? And we saw some of these examples yesterday in the class already is that we want to build this hierarchy of features where the hierarchy is learned through the depth of our layers in our neural network with every layer kind of identifying something key from the image and basically doing sub classification problems as we go deeper and deeper into the model.

**11:09** · And neural networks allow us to do exactly this. They allow us to learn visual features and from visual data what the underlying patterns of that data are. So, if you observe a lot of houses, for example, you show a neural network a lot of houses, it should be able to uncover what are the core underlying very, very low-level features that exist across all houses, And build those up and compose them into higher level features.

**11:34** · And again, this is nothing new. We saw exactly the same paradigm in lecture one using fully connected networks. And then we saw the same paradigm again using recurrent and sequence model networks in lecture two.

**11:48** · Now, I want to pose this as a as a problem now for lecture three because in lecture one we did learn about the fully connected paradigm and you can have these multiple hidden layers going from a one-dimensional input on the left-hand side to a one-dimensional output on the right-hand side. On the right-hand side, the one-dimensional output could be a classification output. But the problem we should focus on is more the input, right? The input here is a one-dimensional input. And let's say we wanted to use what we learned in lecture one now for image classification as well.

**12:19** · Well, what that would mean is that we have a two-dimensional image that we need to feed into our one-dimensional input of our neural network. How would we do this? Well, the way that people have done this is that they flatten the image, right? So, you take your two-dimensional image, you squash it, and you put it in one dimension.

**12:38** · And immediately you you kill all of the spatial information amongst your image, but it's okay. You have still a lot of information still there and the hope is that, you know, can your network still learn it uh just by observing a lot of those flattened one uh two-dimensional images?

**12:53** · But hopefully you can appreciate that just by doing this one operation, even though in theory this could be learned with a one-dimensional network, you've really killed or you've lobotomized so much of the learning capacity of this model just by flattening this input, right? Before you've even started anything with your neural network, you've really handicapped the model. And furthermore, you also have a ton of parameters in this network. So, think for example just a 100 by 100 dimensional or excuse me, 100 by 100 pixel image.

**13:24** · That's 10,000 dimensional 1D vector that you'll get flattened to.

**13:31** · Right? That means your input dimension is already 10,000 dimensions again before you even start your neural network. And these fully connected layers are fully connected, which means that you have 10,000 to your hidden layer. So your first matrix multiply is already 10,000 by something, right? Some big number again.

**13:49** · Right? This will really again blow up the number of parameters in your model.

**13:52** · It's not an efficient way at all and it's not a it's not feasible in practice to operate like this.

**13:59** · So instead, we ask ourselves, right?

**14:02** · What are the more structured ways that we can learn features that are also a bit more closely aligned to how we as humans operate in this two-dimensional spaces as well. And really it comes down to we want to be able to leverage spatial information. We want to leverage the spatial structure in images. We don't want to throw it out before we even start the learning process.

**14:24** · Now to do this, let's not flatten our image into 1D. Let's keep it in a two-dimensional spatial image array of pixel values.

**14:34** · And then one way that we could use the spatial structure inherent in the image is simply to represent or to connect not every pixel in our entire image to every neuron in the hidden layer in the next layer, but to connect only a patch of pixels in the image to the next neuron in the hidden layer.

**14:55** · Right? So because we're only operating at a small patch, we're encouraging now spatial connectivity, spatial relationships because we're only looking at a small receptive field in the in the image.

**15:07** · But at the same time, we're also preserving a lot of efficiency because now we're not forcing the network to look at everything. We're only looking at one small patch and being focused on that local patch. So notice here how the region of interest on the input layer influences this one neuron in the hidden layer here. Right? This neuron has no influence from anything else in the rest of the image.

**15:30** · Now, of course, to define connections across the rest of the image, because we don't want to look only at that one point at that one point in the image, we want to look at the entire image, we can extend this by just doing this patch-based approach, not just for one patch in the image, but for all patches in the image. So, we basically slide this patch across the image, and now we can see how the hidden layer and every neuron in the hidden layer relates to a single patch in the input layer, but each one is kind of locally

**16:01** · uh receiving information from a patch on the input side.

**16:07** · Right? In this way, we have solved this problem of taking to account spatial information, right? Because now we do look and we preserve the spatial information within each patch, but we also uh can enforce or and maintain some efficiency in the model as well, because now we're not learning a bunch of fully connected layers. We're really focusing at each patch level independently.

**16:29** · And we can we can basically now also say we want to learn a feature, like what is a feature from each patch, we can now say we can try to define what that would look like with this paradigm as well.

**16:43** · So, let's let's look at this in a bit more detail on how we could look at this from a feature learning perspective, like we saw earlier.

**16:50** · So, in practice, this operation that I just described to you, this patch-based operation, where we look at every patch as opposed to the entire image, this is called a convolution, basically sliding these patches across the image.

**17:04** · We'll think of this first at a high level, right? Suppose we have this 4x4 filter that you see here, right? In red.

**17:10** · This is a filter, I'll call it, because it is going to operate on the input side, and it just means that it is represented. This filter is defined, not just represents, it is defined by 14 numbers, right? It's defined by 14 numbers on the input image, the pixels.

**17:27** · It's also defined by 14 more numbers, which are the weights of the filter.

**17:31** · Right? So, we actually have, just like we saw in the previous lectures, we have the inputs to a neuron. We also have, for every input, we have a weight.

**17:40** · So, we have here a 4 by 4 inputs, and also 4 by 4 weights that define that filter.

**17:48** · Those 4 by 4 weights will undergo the same operation that we saw in lectures yesterday. They will be element-wise multiplied by the inputs, adding a bias, applying a non-linearity.

**18:00** · The only difference is that now we just do this repeatedly across the entire input. And that's exactly how to think of convolutions at a high level. Instead of learning these filters across the entire flattened one-dimensional image, we're going to the focus on smaller filters, uh apply the same equation that we saw yesterday, matrix multiply, add a bias, and apply a non-linearity, but just slide it across every time.

### The convolution operation

**18:27** · And you're probably wondering now, you know, the connection between these 16 numbers and the features, the high-level features that we were talking about before, right? So, we were talking about we want to detect features in these images, right? Think of things like doors for detecting houses.

**18:43** · But how do these features, you know, relate to the 16 numbers that these kernels or these filters are learning?

**18:50** · Let's make this a bit more concrete in this example.

**18:53** · So, suppose we want to classify an X. If this was an image, we want to classify if this is an image of an X, the letter X.

**19:01** · Right? And for simplicity, let's only consider images that are either black or white. I'll define a black pixel with -1, white pixel with +1. And to classify, we can already see that, okay, this is clearly not possible by simply just doing an equality between the left and the right images because both of these are images of X's, but they're clearly very different if you just look at their equality, right?

**19:24** · So, we need to be able to do this in a more feature-based approach.

**19:27** · Okay. So, instead of looking at the entire image, let's take what we just learned. Let's look at this patch by patch and every patch, let's look for different features. So, for example, we'll look for one patch that is this diagonal in this orientation, right?

**19:42** · This 45° diagonal in this orientation.

**19:44** · This is the green patch. We'll see if we can match this green patch on both sides. And yes, we can see this patch on both sides.

**19:52** · We also look for a crossing feature, right? And this we can also see on both sides, the orange patch.

**19:58** · And again, finally, we look for this other orientation diagonal feature, which again, we can see on both sides.

**20:05** · Right? So, you can see here that even though the model isn't or even though these images are quite different in pixel space, at the feature space, they're actually very, very aligned, right? And that's the key point to take away from today's lecture.

**20:20** · And every feature, every filter, is actually nothing more than just a miniature image, right? It's again just a small two-dimensional array of values and we can use filters to pick up on common features within our X's or our pictures of X's. So, in the case of X's, like we saw in the previous slide, we're basically looking for three different filters or three different features. We're looking for uh this diagonal, this cross, and this other diagonal.

**20:46** · If you can identify these three things, then probably it's a good likelihood that you're looking at an X in this image compared to other letters.

**20:56** · Now, notice that these smaller matrices that you see on the top here of weights, these are the ones that we'll be using to actually detect uh the final features in our image. So, all that's really left now is just to define the operation that plugs all this together, right? It plugs in the ability to relate the features that we want to find with the image that we're searching them in from and then passing those on that information on to the next layer. So, let's look at that operation.

**21:26** · That operation is exactly called a convolution, right? Convolution preserves the spatial relationships between pixels by learning these image features, uh, in small patches instead of the entire image, right? So, to do this, what we're going to do is perform these element-wise multiplications with every input with every weight of the patch. Every input of the patch with every weight of the patch. We add a bias and apply a non-linearity. So, let's ignore the the bias and the non-linearity for a second.

**21:59** · Let's do this just, uh, example uh, piece by piece for this image here.

**22:05** · Right? So, here's the patch that we Here's the filter, let me say, uh, formally, right? Here's the filter that we're searching for and these are the weights of the filter, right? These are learned weights or in this case I just wrote them down, right? Because I can look at the image and I wrote down the weights.

**22:20** · But, this is the image that we're searching that filter with.

**22:25** · So, we can say element-wise multiply every thing in this 3 by 3 matrix with everything in this green matrix.

**22:32** · Element-wise multiply it and we'll get positive ones everywhere, right? Because there's perfect matches. The negative ones times negative ones will turn to positive ones, the positive ones times positive ones will turn also to positive ones. So, everything turns to a positive one. We add up those results and this turns to a very positive number meaning that there was a very strong match between this patch in our image and this patch in our filter. Very positive means strong match, very negative will mean, uh, inverse inverted match.

**23:02** · Now, let's consider one more example and then we can pause for questions if there's any.

**23:07** · Suppose we wanted this convolution to convolve this 5 by 5 image with this 3 by 3 filter. Again, just defining the weights of the filter here uh in the slide. To do this, we need to cover the image entirely by sliding this filter across it, right? So, what does this look like? First, we start off in the top left corner.

**23:28** · Element-wise multiply the 3 by 3 patch elements with the 5 by 5 patch elements in that location.

**23:35** · And the result is our first entry in our hidden feature map, right? It's the next layer's feature map. So, this is basically the image in the next layer.

**23:45** · You're creating the image in the next layer, okay? So, you have an input image on the left, you have a filter, which are your weights, and you have an output image on the right.

**23:54** · And you repeat this. You move the filter over one slot.

**23:57** · You repeat the same operation. You element-wise multiply and add up all the results, and now you have a three in the next slot. And you keep repeating this point by point until you generate or you you compute your entire next uh your entire full hidden image. Right? And this hidden image, this is called a feature map.

**24:18** · This tells you exactly where are the feature that where is the feature that you're looking for in your filter? Where are they spiking? Where are they most prevalent in your image on the left-hand side, right? So, very positive values in your feature map will correlate to very strong matches of the patch with the filter. Very negative will say that there's no match there.

**24:40** · Okay, any questions on this part?

**24:44** · Yes.

**24:49** · Great question. Yes, so this is So, the weights of the filter are decided like the weights of any part of a neural network. They're learned. We haven't gotten to that part yet. Right now, we're just seeing if you manually define the weights, this is how the operation would look in the forward pass, and then we'll see how we learn them in the next part.

**25:08** · Yes.

**25:09** · When you slide the filter, do you overlap it from the previous one a little bit? Why is that?

**25:14** · Good question. So, when we slide the filter, why do we overlap it with the previous filter? This is First of all, a design choice, so you don't have to do this. It's It's up to the the practitioner, the creator of the neural network. Some neural networks don't overlap.

**25:28** · Often times, it's beneficial to overlap though, because you want shared information in case something is cut off in the middle of a filter, right? You want the the model to be able to reason across those cutoffs, and there's no reason why we should assume that things are perfectly obeying exactly where the filters lay. So, sometimes some overlap is actually helpful to the model.

**25:48** · Yes. I have a question about scale.

**25:52** · Mhm.

**25:58** · Great question. We'll get to this in in the next part, but the short answer is that this is why you have depth in your in your network, because as you go deeper and deeper into the model, you cover different scales, right? At the first layer, you can have very tiny filters, but which of course are meaningless at that scale. They will detect very small features, but then as you go deeper and deeper, you notice that the feature map is smaller than the input image. So, your images are actually getting smaller as you go deeper, which means that the relative size is getting bigger.

**26:27** · Right?

**26:29** · Awesome. Okay, let's let's push through, and I think some of the questions will get answered as we as we continue.

**26:35** · So, keeping with the theme of manually writing the filter weights for a second, let's actually see and get some intuition about how different filters can create different feature maps. So, here's an image on the left-hand side, and I'm going to show you the result of convolving that image with three different filters that I define. So, here's one filter that is a sharpening filter, right? It has a positive number in the middle, negative numbers on the edges, and zeros on the corners, right?

**27:06** · Let's not worry about like the details of how these filters are created, but the result is that this filter, when you convolve it, it will actually sharpen the image, right?

**27:16** · Another example is this edge detection filter. It kind of has the opposite type of trend. It has a very negative number in the in the middle and positive ones on the edges. You can actually see that when you convolve it, the filter map is identifying edges, right? And again, strong edge detectors are also possible as well, right?

**27:34** · Now, all of this to say is that don't worry about how the numbers in these filters are created yet. The point is that actually before convolutional neural networks existed, humans would actually manually write the weights of these filters out to create certain effects and to detect certain features. So, if they wanted to detect edges, they would for example, they created these filters for edge detection.

**27:55** · And there are papers, right, that are literally just defining singular filters for edge detection or, you know, different types of a feature detection for different types of operations. Now, we learn this, right?

**28:09** · Now, to answer the previous question, we don't manually write out these uh filters anymore. We learn what the weights of these filters are, but this is hopefully giving some intuition of the importance and the impact of what these filters actually represent.

**28:25** · So, there are three points maybe just to summarize this section before we start to lay on and see the convolutional neural network type taking shape across the entire model. So, the three points here are that we are able to now apply a set of weights not just to the entire image, but to individual patches within an image. This will allow us to extract local features.

**28:47** · We repeat this process over the entire image or we can also have multiple filters to detect different types of features. Right, so far we've only seen examples where we apply one filter to one image.

**29:00** · Of course, there's no reason to do that.

**29:01** · You could learn 100 different filters on that one image because you may say you want to detect in the X example in the X example three different filters on that image.

**29:12** · There's no reason to detect only one.

**29:14** · There is the two diagonal lines in different orientations and the cross as well.

**29:21** · Now that we've gotten convolutions, I think under the belt, I think we can now start to think of how we can utilize this operation and build it into a full neural network operator now or a CNN. A CNN is literally just a convolutional neural network. So, let's look at the CNN architecture for an image classification task.

### Components of a CNN

**29:42** · Okay. So, let's start by putting all of what we learned so far together into one piece. So, the goal here, again just to reiterate, is that we want to learn features directly from our input image.

**29:56** · And we want to use those learned features to map onto a classification task for those images, right?

**30:04** · So, there are three main operations in a CNN, right? First is convolutions, which we already saw.

**30:10** · Second is that we have to apply nonlinearities. This is something we learned about yesterday and the reason is the exact same as yesterday. The real world is nonlinear, so we want to be able to handle this. Right, so convolutions are first. This is the main workhorse. This is actually very similar to fully connected layers except now we just do it at patch level instead of across everything.

**30:30** · Apply nonlinearity. Now, the one new part of this is that we have pooling.

**30:35** · Now, what is pooling? Pooling is simply just downsampling after every layer that we do of convolution, we also want to downsample.

**30:43** · Now, why would we want to do this? It's simply because of the point that I was mentioned earlier, that the scale between our images and our features or filters in the beginning of the model is very big gap, right? It's a very big gap. So, we're identifying very small uh scale features.

**31:02** · If we downscale our image as we progressively go deeper into the neural network, we're actually lowering the ratio between the size of the image and the size of the filter, which means that we're detecting higher-level features.

**31:16** · Okay.

**31:18** · So, what we'll do here is to detect or to train, first of all, train our model on a set of images.

**31:24** · What that means is that we're simply training those features, those numbers in each of these filters across every one of these convolutional layers.

**31:33** · So, let's just go through one more time those three operations that make up a CNN. So, just as before, we have each neuron in a hidden layer will compute a weighted sum of its inputs. We apply this bias and activate with a non-linearity. Now, what's special here is the local connectivity, right? Like we saw before, we have only things in this red box are influencing this one neuron here.

**31:59** · And the next neuron next to it actually is influenced by a slid over red box.

**32:05** · Right? And remember we talked about this element-wise multiplication and addition is the convolution operation, right? So, this defines exactly how convolutional layers are connected by simply sliding these patches of weights and basically doing a weighted element-wise multiplication across the the features in the input image.

**32:26** · Now, within a single convolutional layer, we can have multiple filters like I mentioned earlier. Now, these are very important to learning because at one layer, of course, you may want to detect multiple different types of features in that image.

**32:42** · Now, the output layer, what what does that mean? If you're detecting multiple filters, it means that you're starting from an image, but you're going into a volume.

**32:51** · Right? Where every slice of that volume is a single output feature map that we saw before. Right? Before we were going just from image to filter to image.

**33:02** · But now, if we have many filters, that means we'll have a volume of images on the output side. And we can think of the connections of neurons in these convolutional layers in terms of their receptive field. Right? That's the really the way to think of it. Where every point within our uh depth of our output volume is being influenced by just a small patch of input pixels on our input image.

**33:29** · Okay. So, I think we're well on our way now to understanding the CNN. The next step is to apply a non- linearity after we have this volume of feature maps.

**33:39** · And as we introduced in the first lecture, we do this because data is highly non-linear. In CNNs, it's pretty common practice to apply non-linearities after every convolutional operation.

**33:50** · Right? So, after each time you convolve, you typically will apply your non-linearity there. And a common activation function is the rectified linear unit or ReLU.

**34:01** · Uh this is nothing more than just a pixel-by-pixel operation that takes anything that is negative, and it squashes it to zero, and takes anything that's positive, and it keeps it as the identity function.

**34:13** · So, you can actually also think of this Another way to think about this is a thresholding. If you're greater than zero, you pass the threshold. If you're less than zero, you get thresholded to zero, exactly. So, negative values actually just indicate negative directions basically after convolution, but you squash them to zero uh by the time that you have your your activated uh output on the other side.

**34:37** · Okay, final operation is pooling.

**34:40** · Pooling is this operation that just reduces the dimensionality of your feature maps. Why is that important?

**34:46** · Because you want to preserve the spatial invariance across your input images, but you also want to cover different scales of feature detection on the the convolution side as well. So, by scaling down the images, you're scaling up the relative size of what you search for across your feature maps.

**35:06** · Now, one way to do this, a very common way, is by max pooling. What that means is that if you have an input image over here or an input feature map after you convolve, max pooling simply says that you take a again a patch and you take the maximum value within that patch. So, you look at this 4 by 2 by 2 patch of four elements, take the maximum value, it's a six, it becomes the the top value there. So, you go from a 4 by 4 image or a feature map and you create a 2 by 2 feature map on the other side with this example.

**35:38** · Uh this is just one example of how to pool down information from larger scale to smaller scale.

**35:44** · Uh it's a very simple way, right? So, it's very fast to implement, but I encourage you actually to think about other ways that you could perform this down sampling because it's very flexible and there is a lot of tuning that you could do there.

**35:56** · Uh you had a question. Yes. Um isn't the aren't the patches kind of implicitly already down sampling the image to a degree and you could also just make the patch bigger to increase down sampling? Yes, the question is there's a there's a trade-off, obviously, right? Because the patches are inherently kind of down sampling the image already because you have to stop at the edges, right? So, you always have this kind of like slightly smaller image on the feature map than you had on the image side.

**36:21** · There's a trade-off, right? The point is you can't increase the patch size too much because as you increase the patch size, you're kind of killing the whole point of looking at local invariance.

**36:31** · You actually like the local invariance, right? That's why you want smaller patches. But you also want to uh you know, have efficiency in that you have these different scales. Right? So, that's the reason to kind of combine the best of both worlds, right? You start with actually relatively very small patches because you want to capture the very detailed information. Small patches are actually very good, right? Because it means you can like focus on the very minute details.

**36:54** · Uh but then eventually you do want to combine the results of each feature map into higher level compositions as well.

**37:02** · So, max pooling is just essentially lowering the resolution. \[clears throat\] Exactly. Yeah, max pooling is nothing more than lowering the resolution but doing so in a very structured way, right? So, it's keeping the Another way to think of this conceptually is that you want to keep the features that were maximally identified and preserve them onto the next feature map, right? So, the This point was maximally pulled was maximally identified, you want to preserve that over here on your input on your next input as well.

### Building and training CNNs

**37:32** · Okay. So, these are the key operations of convolutional neural networks and now we're basically ready to put them all three of them together to form a CNN.

**37:42** · Now, again, just to keep reiterating this point, the whole point of what we're doing here is to learn this hierarchy, right? We start from very small patches because we want to learn these types of low-level features on the left-hand side. And because the patches are small, that's what enables these low-level features to emerge. Every time we pull, we scale up the size, the relative size, and the compositionality of what those features represent so that we can combine features from previous layers like lines and edges into corners and curves into shapes and objects as you go deeper and deeper into the model.

**38:18** · Now, a CNN built for image detection or image classification can be broken down now into these two parts, right? The first part is a feature learning part and it's composed of exactly what we just saw in the lecture so far, right?

**38:31** · It's composed of convolutions, nonlinearities, pooling in succession, in sequence.

**38:36** · Um the second part is a classification part and this is where you basically take the result of your convolution and pooling layers. Those have now outputted these high-level features and finally now you do flatten them and you put them into a fully connected layer that can do your final classification because eventually you do need to go to that one-dimensional classification head. And you of course, just like we saw yesterday uh you train with a classification loss. You use a softmax output.

**39:04** · All of the same things that we saw yesterday because we want to output our categorical distributions in one-dimensional vector space. Yes.

**39:14** · Um different architectures are meant for different I think our our mind is from yesterday our event our event you can imagine here you can use it for classification.

**39:29** · Can you use CNN for language also or is it like Great question.

**39:34** · So, the question is about are different architectures meant for different purposes at a high level. So, the the short answer is yes, absolutely. I would say that different architectures are meant for different data modalities first of all, right? So, what we're seeing here is primarily focused on two-dimensional images or two-dimensional inputs is even a more accurate way to say that. It doesn't necessarily need to be images, but if your input is two-dimensional and spatial preserve spatial preserving, then you'd want to use a convolution.

**40:00** · If your input is sequential, you would want to use an RNN or or a sequence model.

**40:06** · Now, there are some exceptions, right?

**40:08** · You could also imagine doing creating a sequence model with convolutions as well, right? So, instead of operating on two-dimensional images, you could operate on one-dimensional vectors, right? But have convolutions of patches across that one dimension, and that's also a valid sequence model. So, in short, the the short answer is that there are many variations of what we're seeing here.

**40:29** · And actually, there's even though we're focusing on this lecture in image space, in two-dimensional space, a lot of the same ideas would extend to 1D, which is basically a sequence model, again, like we saw with the RNN lecture, or 3D, which extends even to other modalities as well, like like volumetric scans and so on.

**40:52** · Awesome. Okay, so let's put this all together into our first end-to-end convolutional neural network. So, what does this look like in code? We start by defining our feature extraction head.

**41:03** · Remember, there are these two parts.

**41:04** · There's a feature extractor and there's a classifier. The first part is the feature extractor. We start by defining those heads. Let's just walk through the numbers here. So, we start with the convolution first. 32 represents the number of filters that we want to learn with that convolution.

**41:20** · That means that we're looking for 32 different filters in that first layer.

**41:24** · Each filter is going to be of size three. That means 3 by 3 patches are the filter size.

**41:30** · And we have an activation as well, here at the ReLU activation.

**41:34** · And then finally, after that convolution, we apply a pooling. Just like we saw before, this is a max pooling layer.

**41:41** · We can do this again. As we go deeper into the model, we start to take the inputs of the previously detected features, instead of using the original image. So, now we're using the detected features as our new inputs. And now we're looking for not 32, but now 64 features in the deeper part of the model. So, we're basically building up this library of different features that we're detecting across the image.

**42:06** · And again, same idea, the filter size is 3 by 3, but of Of because we scaled down the image by a factor of two, it's it's not 3 by 3 in the original space, right?

**42:17** · Um and then we max pool. And finally, we feed all of these into our classification head, which is the dense part of the network. As we saw yesterday, this is responsible for actually performing the classification of our final answer and predicting the result. Again, very similarly in PyTorch, I'll go a bit quicker this time. We can start with convolutional layers. Looks very similar, as you'll see. Inputs are three-dimensional. Why three? Because you have an RGB image. Three dimensions.

**42:47** · Or three axes, uh I should say.

**42:50** · Uh three output channels. This corre- Excuse me, 32 output channels. This corresponds to the 32 features that you want to learn on that layer, followed by max pooling.

**42:59** · And again, same for the second part. And again, same for the third part. You now have your dense classifier model as well.

**43:09** · Okay. So, so far we've gotten Oh, yes, go ahead.

**43:13** · You said that in the max pooling layer, we are taking the max value from each block.

**43:18** · So, considering image in length, height, and in depth format, so what are we exactly reducing in the image?

**43:24** · Just the image Yeah, so it's a great question. Uh max pooling is reducing only across the spatial dimensions, height and width. It does not reduce across the depth dimension. So, if you start with 32 features in the feature map, you maintain 32 after max pooling, but you reduce only on the spatial axis, height and width.

**43:43** · Okay, excellent. Now, also tying back to the previous uh question that we had, we've really focused this lecture so far on image classification, right? And in reality, convolutions are applicable to so many different types of tasks beyond image classification. This is an architecture for so many applications, even sequence modeling, as we saw earlier. But we'll see some some examples now of how we can extend this into other applications.

### Advanced computer vision tasks

**44:07** · The amazing thing about CNNs is that this abstraction that I made earlier of basically having a feature detector part and a classifier part is actually a really nice abstraction because you can take the feature detection part and keep it very consistent for so many different applications. So for example, uh what makes a convolutional neural network so special is that it's able to do very general purpose feature learning across an image, right?

**44:35** · So the outputs of all these convolutional layers are very general purpose features that can be re-reused for, let's say, classification, prediction, forecasting, etc.

**44:47** · For example, that portion will now look different. Uh excuse me, this portion, the classification portion, will look different depending on an image classification domain versus other domains, right? So for example, uh we could have classification, object detection, semantic segmentation, control, forecasting, etc.

**45:09** · Let's consider a few different cases, right?

**45:12** · We already saw the classification example, right? There's significant impact for classification across so many different areas. I'll focus on one here with healthcare, where deep learning models you can take as input a scan of a patient and you can analyze a whole host of different types of uh classifications or tasks across that.

**45:34** · And this paper was basically demonstrating how CNNs can outperform expert radiologists at detecting breast cancer. This was actually paper from some time ago. Uh we've gone much farther than this.

**45:46** · Classification also tells us just a binary prediction for a particular uh container or for a particular class. But we can go much deeper into that problem and we can actually identify not just to classify, but but to localize, right?

**46:02** · This is a problem of uh drawing bounding boxes over our image of where the different objects are. So, for example, object detection is simply going from an image of a taxi to a class label, taxi.

**46:16** · Object detection is saying take that same image and output a bounding box for every object that you see in the image, not just one class label, but now also output the coordinates, the XY coordinates of a bounding box along with the height and width of that bounding box, and then a classification for that bounding box as well.

**46:35** · Right? The classification also following the same trend as what we saw before, but the bounding box being very new.

**46:43** · So, our network in this paradigm, it's still using the convolutional front part of the model, but now obviously the back part needs to be changed, right? It needs to be dynamic to infer not just one object in the scene, but also potentially many objects, right? If we have many boxes in the scene, the model on the output side needs to be flexible to be able to output any arbitrary number of boxes and predictions for those boxes, right? And that's something that we actually haven't seen in the class so far of having variable-sized outputs.

**47:17** · Now, this is very complicated because boxes can be actually anywhere in the image and they can also be of different sizes. So, let's look at a first very naive solution to this problem, right?

**47:27** · What's the simplest way that we could solve this problem? We could, if we want to detect a box, what we could literally do is take a random box in the image and pass it through our original detection model, right? And we see, does this thing have a class?

**47:44** · Right? We just picked a random box here, right? Uh and we would repeat that. We would keep picking random boxes. Now, of course, this is really expensive because there's so many random boxes to do. So, okay, this is a very naive solution, for sure.

**47:58** · Um there's way too many inputs here, way too many scales, right? Even if you fix the size of a box, there's a lot of inputs. Now, imagine you have also have to have different sizes, scales, aspect ratios, and so on.

**48:10** · Um how can we do better, right? So, instead of picking random boxes, the first intelligent thing that we might do is to use a heuristic of where from from another model, identify where are some blobs of information, you know, roughly in this image, right? There are good metrics, good good heuristic-based, not machine learning-based methods for just identifying where stuff is happening in images, right? Where there's blobs in images, and basically draw boxes around those things, and then just feed those into our CNN, right?

**48:40** · So, you have a good heuristic of just where to look, first of all, and then take boxes in those areas, so you cut away a lot of the space.

**48:50** · Now, this is this is much better, obviously, than the previous option that we had, but it's also having two key problems. Still, it's very slow, because you're relying on this first model, typically not a machine learning model, to extract possible boxes. You're still having to go over a lot of boxes, many of which are not relevant to the task. And it's also very brittle, right? Because you're operating off of these manually defined boxes. You're not actually learning where the boxes are, which kind of defeats the whole purpose of of deep learning as a field.

**49:23** · Now, how can we do better, again, right?

**49:26** · Many variants have been proposed to tackle this issue. It's such a big problem, actually, like this task of object detection, as you can imagine, is very foundational, right? It's a backbone for self-driving, it's a backbone for many uh type of real-world locomotive tasks, as well.

**49:41** · Um I'll touch on one solution that is very widely used in practice, right? The The goal here is that, again, we want to take our image. We'll use our convolutional feature extractor, exactly like we saw before. Nothing new here. And we're going to feed that into our convolutional layers. Why do we do this?

**49:59** · This is great because now it's very fast. Like we saw before, we feed in the entire image all at once. What's the output? It's going to just be a feature map, right? There's so far there's no boxes here. It's just features again.

**50:12** · But we can now use those features to propose. This is called a proposal step, to propose boxes and where candidate boxes may be. Because the features are detecting already some stuff happening in the image.

**50:26** · And those are blobs now that we can identify we can grab boxes just around those blobs. And again, we can use heuristic based approaches for this.

**50:34** · It's very easy to basically threshold the image and you know, identify where the blobs are.

**50:39** · And then for each of those, perform feature extraction and classification off of the the features in each of those boxes one by one. But now the key point is that we can actually back propagate through this entire model from the answer from the classifier all the way back to the input image.

**50:58** · Right? So, if our boxes were bad boxes, now we have a way of telling the model that these were bad boxes and it should propose better boxes the next time.

**51:07** · Right? The difference being from the previous model, now this is fully end-to-end differentiable. Right? We can actually learn from the end all the way back to the image side.

**51:18** · So, in classification, this is where we want to detect boxes. But of course, there are also other forms of even more flexible. Right? Maybe you don't want a box, but you actually want pixel level segmentation of what's happening in your image. That's even taking this one step further. Right? One example of this is where we input the full RGB image and we want to output another image. So, this is an image-to-image task now, not image to boxes or image to classification.

**51:44** · It's image to image. And we want to output for every pixel what class does this pixel belong to?

**51:52** · So here for example, you can see an a case where input is a picture of a cow or two cows.

**52:00** · And we want to output pixel by pixel classifications of cows, trees, sky, grass, etc.

**52:07** · Now the output here is it created simply by again keeping the same input as we saw before. This is convolutional layers followed by pooling layers and nonlinearities.

**52:18** · But the output side is the only thing that changes, right? The core theme that I'm trying to get at here is that the input feature extraction is very stable for many of these applications. You're always only really changing the output side. And here the output is actually needing to produce a new image. So you actually want to go from these down sampling operations that we saw on the input side now to up sampling operations to now produce and generate a new image.

**52:43** · And that image is going to be pixel by pixel classifications. You train it as a classifier at the end. So in some sense this is actually an image classification task as well, but now where your classification is not a one-dimensional vector, it's also an image.

**53:00** · Amazing. Okay, one more example, one final example of self-driving. Uh let's say we want to learn a neural network for autonomous control and specifically we want a model that can go from raw perception, so raw camera inputs from a image directly using those together with a noisy street view map. So here this is a top-down topological map that you might see from something like Google Maps even more sparse than what you would see in something like Google Maps. But again, this is actually an image.

**53:30** · We can feed both of or all of these inputs through different convolutional layers and try to predict possible control commands, right?

**53:39** · Um the entire model here can be trained as a large CNN. There's nothing really more to it than that because you have different camera inputs that the car sees. Each of these will get passed through convolutional layers. You also have a map also gets passed through convolutional layers because this is nothing more than an image.

**53:58** · You concatenate all of those features together and then you can learn different control commands that come out.

**54:04** · Of course, the interesting part here is that control is often not one number, right? It's you have many possible commands that you can take at any moment in time. So, this is actually more than just a forecasting problem. It's a probability learning It's a distributional learning problem because you have a distribution of possible actions that this car could take at any moment in time, potentially multi-modal uh actions as well, meaning that you could turn left or right. It's not just one modality that you could perform at any moment in time.

**54:34** · So, there are ways to also learn this using distributional learning, which we'll talk about later in the class as well.

**54:41** · Now, but just to summarize, right? This is nothing more than again the same feature extractors that we saw before using convolutions, pooling, and then finally learning on the other side.

**54:52** · Amazing.

**54:54** · Okay. So, the impact of CNNs has been wide reaching beyond these examples that I've shared today. And CNNs really are this incredibly general-purpose uh operation that works off of not just 2D images, but like we saw before, one-dimensional sequences as a as a whole as well.

**55:12** · Uh these are some of the examples that we talked about today, but it definitely does not uh end there, right? I'll conclude by just talking uh summarizing, right, very briefly what we considered today. We saw everything from manually defining these features by hand uh and

### Summary and lab overview

**55:28** · understanding their intuitions and their origins uh all the way to, you know, learning them with convolutional neural networks and then some of the applications and extensions of these models where you change the later part of the model, keep the feature extraction part, but change the later part, and actually understand what's going on under the hood with these different applications.

**55:49** · Now, I'll also highlight that in today's lab, later today, you will get hands-on exposure to these types of models first-hand. You'll build your own feature classifier and your own image detector for facial detection systems. You'll also understand how to debias these systems because one big problem is that you want to make sure that your features that you're learning cover a full spectrum of the of the distribution of your data. So, we'll cover that in today's lab, as well.

**56:18** · Amazing. And after this, we'll have Albus' lecture coming up. We'll just do it 2 minutes just to to to transition over. That will cover generative modeling.

**56:28** · And this will also be a really exciting lecture because it it's about not just predicting things, which is everything that we've seen in this lecture so far is just prediction, but now you actually want to generate new things, as well.

**56:38** · And that's what the next lecture will cover.

**56:40** · Awesome. Thank you.

**56:42** · \[applause\]

关联：[[Artificial_Intelligence/MIT 6.S191/主页|6.S191]]
