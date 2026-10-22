---
title: "Hidden Symmetry: Why Deep Learning is Possible"
source: "https://www.youtube.com/watch?v=2qXF8JHcU5E"
author:
  - "[[ReLU]]"
published: 2025-12-31
created: 2026-10-22
description: "We often treat neural networks as incomprehensible black boxes. With billions of weights and extreme non-convexity, they should (theoretically) get stuck in \"local minima\" and fail to learn. Yet, they"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=2qXF8JHcU5E)

We often treat neural networks as incomprehensible black boxes. With billions of weights and extreme non-convexity, they should (theoretically) get stuck in "local minima" and fail to learn. Yet, they solve the world's most complex problems with remarkable efficiency.  
  
In this video, we go beyond the surface to explore the hidden geometry of deep learning. We delve into the extreme dimensionality of neural networks and discover that the secret to AI's success isn't just having a large number of weights; it's symmetry.  
  
\------------------  
  
These animations are largely made using a Python library, manim. For more information see:  
https://github.com/3b1b/manim  
  
Music by Vincent Rubinetti  
Download the music on Bandcamp:  
https://vincerubinetti.bandcamp.com  
Stream the music on Spotify:  
https://open.spotify.com/artist/2SRhEEt2tlDQWxzwfUo9Dl

## Transcript

### The black box problem

**0:07** · A neural network is often considered a black box.

**0:13** · The idea is that while we can train a neural network, we do not understand what is happening as they are training, and the final product is so complex that we can't possibly understand it.

**0:29** · And while this idea is not untrue, it is a little bit misleading.

**0:39** · Now, it's not surprising \[music\] that people have gotten this impression.

**0:45** · Modern neural networks, like those powering ChatGPT or Gemini, can have upwards of tens of billions of individual weights.

**0:58** · To really understand the sheer magnitude of this, just consider that the goal when training one of these neural networks is to find just one set of weights which solves your task.

**1:15** · The algorithms that we use to train these massive neural networks, known as optimizers, have to search through over 10 billion dimensions just to find that optimal set of weights.

**1:32** · The sheer volume of such a space is not something the human mind can even comprehend.

**1:38** · It's comparable to the number of galaxies in the observable universe.

**1:44** · Yet, despite these challenges, neural networks have become the de facto algorithm used to solve almost every task in machine learning.

**1:57** · As it turns out, the answer to why neural networks are so remarkably effective lies in symmetries.

**2:06** · It is the symmetries of neural networks which make them so efficient.

**2:12** · But before you can understand these symmetries, you first need to understand the loss landscape.

**2:22** · Consider this simple optimization task, fitting a line to a set of points. This line is defined by two weights, a slope \[music\] and a Y intercept.

### Understanding loss landscape

**2:37** · And with these two weights, we can \[music\] define any possible line.

**2:45** · But what is the best fit line to this specific set of points?

**2:52** · To find it, we need to define a loss function.

**2:58** · This function takes \[music\] in our two weights and returns a positive scalar value.

**3:07** · It is \[music\] defined as the sum of all squared errors between our line and the points on the graph.

**3:17** · With this loss function, for \[music\] any line we choose, we can compute how well that line fits the set of points on the graph.

**3:29** · Since there are only two weights describing a line, we can visualize the loss function with a 3D plot.

**3:38** · This is the loss landscape.

**3:43** · And it visualizes the value of the loss function for any line we can choose. So, where is the best fit line?

**3:54** · Well, it is at a minimum of this graph.

**3:58** · And when we look back at this line, we see that it is \[music\] in fact the best fit line.

**4:08** · But, this is a very simple example.

**4:12** · And in particular, it has a convex loss function.

**4:20** · A convex function is simply a function which only has \[music\] one minimum.

**4:29** · Which means that in such loss functions, you can always find the best solution.

**4:37** · A guarantee which remains true even \[music\] as we increase the number of weights.

**4:46** · The problem is that when we look at neural net works, they do not have convex loss functions.

**4:56** · But, before moving to neural networks, \[music\] let's see a simpler example of what a non-convex loss function even looks like.

### Non-convex optimization

**5:05** · This squared sinusoidal loss function has only one weight A.

**5:12** · And while it has only one global minimum, it has multiple local minima.

**5:20** · This loss function is non-convex because of those local minima.

**5:27** · Now, \[music\] suppose we choose a point M on the graph.

**5:31** · How do we find \[music\] one of these minima?

**5:34** · Well, over a series of steps, we compute the gradient of the loss and move in its negative direction.

**5:46** · And this process is repeated until we converge to one of these minima.

**5:54** · However, which minima we end up in depends entirely on where you start and which optimizer you use.

**6:07** · While we ideally want to find a good minimum, for example, \[music\] the global minimum, in rugged loss landscapes like this \[music\] one, this becomes very difficult unless you get very lucky on where you start. This is why non-convex loss functions are so difficult to work with.

**6:30** · Bad local minimum or saddle points can completely \[music\] derail the training process.

**6:39** · This is why traditionally machine learning practitioners preferred to work with convex loss functions because they are always guaranteed to give you the best possible model.

**6:54** · But, something changed when we started to use neural networks.

**6:59** · For some reason, they had this ability to avoid bad local minima.

**7:06** · Somehow, neural networks would always converge to a low loss solution.

**7:13** · This broke the traditional view of non-convex optimization.

**7:19** · But, to understand how this could even be the case, we first need to understand what neural networks even are.

**7:27** · A defining characteristic of a neural network is its modular structure.

### Structure of neural networks

**7:34** · Neural networks are arranged in multiple layers.

**7:38** · Each layer takes the input from the previous layer, transforms it in some way, then passes its output as the input to the next \[music\] layer.

**7:51** · While there is a lot of different types of layers used in neural networks, each based on a different type of mathematical operation, the particular type of layer we are focused on here today is known as a dense \[music\] layer.

**8:06** · Dense layers are based upon the operations of individual neurons.

**8:12** · So, let's look at how one of these neurons works.

**8:17** · The neuron begins by multiplying each one of its inputs by a corresponding weight.

**8:24** · The products are then summed up to get the pre-activation of the neuron.

**8:32** · That pre-activation is then fed through an activation function to get the final value of the neuron.

**8:41** · The activation function is there purely to allow the network to exhibit more complex behavior. For example, with the rectified linear unit activation function or ReLU, you zero out all negative values. But, dense layers don't have only one neuron. Typically, they have hundreds.

**9:06** · And after each one of the neurons in the dense layer computes their value, these values will then be passed as inputs to the next layer.

**9:16** · Which, in this visual, is just another dense layer.

**9:21** · So, what is so special with dense layers?

**9:26** · Well, let's look at a simple neural network to see.

**9:31** · This network has one input, two hidden neurons, and one output. There are also two input weights and two output weights, each associated with one of the neurons.

**9:48** · Let's assume the output weights are equal to each other.

**9:52** · For example, say both are equal to one.

**9:55** · Now, let's set the network's task to be fitting all the points shown in the plot in the top right.

**10:05** · Let's now visualize the loss landscape for the two input weights.

**10:11** · Notice that this entire loss landscape is mirrored along the line where both weights are equal to each other.

**10:21** · This mirroring remains even when we change the points we're training the network on.

**10:30** · What we have just observed is a fundamental symmetry \[music\] of dense layers, known as their permutation symmetries.

### Permutation symmetries

**10:41** · Because neurons perform the exact same operation, just with different weights, permutations of neurons in that dense layer will not change the loss of the network.

**10:57** · Importantly, as we increase the number of neurons in the dense layer, the number of possible permutations grows \[music\] factorially.

**11:08** · With just three neurons, we already have six symmetrical regions in our loss landscape.

**11:19** · Now, remember that when \[music\] we're training a neural network, what we're trying to do is minimize the loss function.

**11:27** · So, how does this affect network training?

**11:32** · Well, \[music\] if there's one minimum of the loss function, then you already know there has \[music\] to be five other equivalent minima somewhere else in the loss landscape because of the mirroring of the loss function.

**11:50** · Each moving line represents a different network initialized somewhere in this loss landscape. As we see here, all of them collapse \[music\] into one of these six identical minima. So, the loss function is beginning to exhibit properties of convex optimization.

**12:10** · But, this mirroring becomes even more extreme as we increase the number of neurons in our layer.

**12:18** · With just 67 neurons, we already have more permutations than the number of atoms \[music\] in the observable universe.

**12:31** · And each one of these permutations represents a distinct mirroring of the loss function and thus an additional equivalent minima of the loss function.

**12:47** · Suddenly, the massive volume that's the search space for weights in our neural network is full of equivalent global minima, making the optimization process much simpler.

**13:04** · But, as it turns out, permutation symmetries are small in comparison to other symmetries found in almost every neural network.

### Continuous scaling symmetries

**13:15** · These symmetries are the network's continuous symmetries.

**13:21** · And they represent continuous lines of equivalent minima in the loss landscape. However, to appreciate the symmetry, we need to revisit our simple one input, one output neural network. Except, let's remove one of the neurons. Consider the effect of scaling this neuron's input weight by two and output weight by 1/2.

**13:48** · Suppose for a moment that we have an identity activation function, which just means that if we give this identity function one, it'll return one.

**14:02** · If we give it two, it'll return two. It just returns its input. Notice that the particular scaling we have picked has no \[music\] effect on the output. Thus, the loss function is invariant under this particular scaling of weights.

**14:20** · However, it's not just two for which this symmetry holds.

**14:26** · This is a continuous symmetry because for any value we choose, scaling the input weight by this value and the output weight by its inverse will leave the loss function invariant. Thus, \[music\] we have an entire manifold of equivalent solutions to our loss function.

**14:53** · And this scale symmetry holds true for not just the identity activation function, which is rarely used in neural networks, but for any homogeneous activation function.

**15:08** · A homogeneous function is any function where if you input a scalar value, that scalar can be brought to the outside of the function with some integer exponent.

**15:23** · What's especially interesting is that one of the most commonly used activation functions in neural networks, the rectified linear unit, is a homogeneous activation function, except only with respect to positive scalars.

**15:42** · As we have just seen, in almost every neural network, there's not just one global minimum, or even six equivalent global minima. Instead, there's an infinite number of equivalent global minima spread throughout the loss landscape. Neural network training is not a black box. The loss landscape is not some rugged, unpredictable manifold.

**16:12** · It has predictable structures generated by the symmetries of the network, challenging our notions of non-convexity.

**16:23** · Permutation symmetries mirror the loss function for every possible permutation of a dense layer.

**16:31** · And continuous symmetries, like scale symmetries, infinitely mirror the loss function along continuous manifolds. \[music\] In modern neural networks, there are billions of dimensions in the loss landscape.

**16:47** · However, symmetries create an uncountably infinite \[music\] number of optimal solutions to a given loss \[music\] function.

**16:59** · The effectiveness of neural networks is not a miracle, but instead a consequence of profound mathematical structure in symmetries.

**17:09** · These symmetries ensure that no matter where the neural network starts, the optimizer is always able to find a good set of weights.