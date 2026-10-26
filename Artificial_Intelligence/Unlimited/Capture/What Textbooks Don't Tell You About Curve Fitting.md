---
title: "What Textbooks Don't Tell You About Curve Fitting"
source: "https://www.youtube.com/watch?v=q7seckj1hwM"
author:
  - "[[Artem Kirsanov]]"
published: 2025-04-01
created: 2026-10-24
description: "Head to https://squarespace.com/artem to save 10% off your first purchase of a website or domain using code ARTEMKIRSANOV=====My name is Artem, I'm a neuroscience PhD student at Harvard University."
tags:
  - "clippings"
---

> 对应笔记：[[曲线拟合的概率视角 最小二乘与正则化]]

![](https://www.youtube.com/watch?v=q7seckj1hwM)

Head to https://squarespace.com/artem to save 10% off your first purchase of a website or domain using code ARTEMKIRSANOV  
  
\=====  
My name is Artem, I'm a neuroscience PhD student at Harvard University.  
🌎 Website and Social links: https://kirsanov.ai/  
📥 "Receptive Field" neuro-newsletter: https://artemkirsanov.substack.com/  
✨ Support me on Patreon to get access to Discord community: https://patreon.com/artemkirsanov  
\=====  
  
In this video we dive deep into a probabilistic interpretation behind the core linear regression algorithm from the ground up. We talk about how the least squares objective naturally arises when we try to maximize the probability of observed data under the model, and how the square is a result of assuming Gaussian distribution of the noise in the samples. We also explore how incorporating prior beliefs about the distribution of model parameters leads to different kinds of regularization in objective functions.  
  
🕒 OUTLINE:  
00:00 Introduction  
01:16 What is Regression  
02:11 Fitting noise in a linear model  
06:02 Deriving Least Squares  
07:46 Sponsor: Squarespace  
09:04 Incorporating Priors  
12:06 L2 regularization as Gaussian Prior  
14:30 L1 regularization as Laplace Prior  
16:16 Putting all together  
  
\*Disclaimer:\* This channel is my personal project. The views and content expressed here are my own and are separate from my research role at Harvard University.  
  
#LinearRegression #MachineLearning #Probability  
  
  
\_Description remastered: February 2026. Links & Bio updated; original context preserved.\_

## Transcript

### Introduction

**0:00** · this video was brought to you by Squarespace there is one Concept in machine learning that nearly every course in textbook starts with finding the equation of a straight line that best fits a scatter of points the typical explanation goes something like this we pick the line's parameters to minimize the average squared vertical distance from each point but why vertical distances why

**0:24** · squares and not absolute values or some other power where does that even come from you'll often hear justifications like squares are easier to optimize or the math just works out nicely Fair points but to me that always felt somewhat

**0:41** · unsatisfying in this video I want to share with you an alternative perspective a probabilistic take on linear regression that finally made everything click for me it leads to the same solution but offers a conceptual shift that I found invaluable not only does it answer those fundamental questions it also connects the seemingly simple problem to more complex topics like generative modeling and parameter regularizations in ways that might surprise you let's Dive Right

**1:13** · \[Music\] In let's first clarify what regression actually means at its core it's about uncovering a relationship between inputs call them X and outputs y then using that relationship to predict y for new values of X unlike classification where

### What is Regression

**1:33** · you are choosing between discrete categories like yes and no regression deals with continuous values a classic example is predicting house price from various features perhaps X1 is the number of bedrooms X2 distance to the subway Etc our task is to reconstruct

**1:52** · the price from these features at this point most explanations jump directly to minimizing squar errors in the line by reducing those vertical gaps and yes we'll get there but to truly understand why this works let's step back and reframe it through

### Fitting noise in a linear model

**2:11** · probability let's treat our data as if it emerges from a linear model plus some noise imagine that somewhere in the universe underlying source code the ideal price of each house is given precisely by a linear combination of features weighted by some coefficients for brevity let's Express this as the dot product between weights and features stacked into vectors however real world data is messy and it never perfectly follows the linear patterns actual house prices are

**2:44** · influenced not just by those features we collected but also by hidden variables that we can't access Plus Market fluctuations and human behavior in other words our observed values y are corrupted versions of those ideal underlying values with noise term Epsilon being added to them here Epsilon

**3:05** · represents everything we can't explain with our features all the unknown contributors to the price beyond our control the critical Insight is that our resulting regression equation depends on our assumptions about this noise namely Epsilon is shaped by countless tiny inferences measurement errors untrack variables random Market fluctuations all added together when many small independent effects accumulate additively something remarkable happens

**3:36** · according to the central limit theorem when you sum many independent random variables regardless of their individual distributions their sum approaches a normal or gorion distribution The Familiar B curve suppose we have a candidate set of Weights W our hypothesis about the underlying linear model when we examine a random house

**4:00** · with features X and price y we can calculate exactly how much noise was added to our hypothesis by taking the difference between the observed price Y and its ideal non-noise value with our noise model knowing that it follows a caution distribution we can calculate the probability of getting precisely the right amount of noise Epsilon that would push the underlying price to be registered as y this equals the

**4:30** · probability of observing that particular data point I want to reiterate that shift of perspective with a working set of Weights w we take the features X and compute their weighted sum given us where the ideal noiseless version of Y should lie around this point exists a cloud of uncertainty a bell curve centered at w transpose X when we

**4:55** · observe the actual value of y and calculate how much much noise must have been added we can compute the likelihood of that happening by plugging the noise amplitude into the gor equation this gives us the probability of observing a single data point as the probability of sampling just the right amount of noise from the caution distribution if we assume all data points in our scatter plot were sampled

**5:24** · independently then the probability of obtaining our entire data set with a fixed w can be found by multiplying the probabilities of these independent events what we have done is expressed the probability of observing our data given a particular model the coefficients W if presented with two

**5:44** · alternative models intuitively the better model would be the one with a higher probability of generating The observed data so when solving the regression problem and choosing the optimal w we just need to select the configuration that maximizes this probability given this optimization objective we can expand the formula for the probability of data now let's take

### Deriving Least Squares

**6:09** · the logarithm of the right hand side because logarithm is a monotonic function whichever weight configuration maximizes the total probability also maximizes its logarithm the two objectives are equivalent but the logarithm transforms our product of probabilities into a sum which is much easier to work with

**6:31** · notice that Sigma the amplitude of the underlying noise is a fixed value determined by factors like Market volatility from the perspective of the optimization objective it is a constant factor that doesn't affect which set of Weights is optimal this allows us to simplify the formula finally the logarithm and the exponent cancel each other out leaving us with this this is

**6:57** · exactly the well-known least squares of objective which states that the optimal coefficients should maximize the negative or minimize the positive of the sum of squared errors between the linear fit and The observed points importantly

**7:14** · though we arrived at this from the perspective of finding the linear model that maximizes the probability of observing our data and the square in the resulting formula is a direct consequence of assuming the Gau noise this problem can be then solved either through gradient descent by making small iterative adjustments to the weights or by directly jumping to this solution using a closed form expression found in any textbook my main

**7:42** · goal here was to show where this formula comes from in the first place just like linear regression helps us find the optimal fit for the data finding the right platform for your online presence is all about making smart choices which brings me to our today's sponsor Squarespace Squarespace

### Sponsor: Squarespace

**8:00** · transforms website creation and management into a straightforward process that anyone can Master while starting a site from scratch might seem challenging Squarespace design intelligence feature makes it remarkably simple this Innovative AI power tool kit

**8:16** · generates a website tailored to your specific business in brand Vision filled with relevant content and images from this starting point you can enjoy total creative freedom adjust all the visual elements to match your style organize content with their drag and drop tools and even Implement ey catch in animations to spice things up importantly Squarespace goes beyond just website building it's a comprehensive digital solution where you can develop online courses launch effective email

**8:44** · campaigns or set up payment processing through various methods all within one cohesive ecosystem experience it yourself with a free trial at squarespace.com and once you're ready to launch visit squarespace.com AUM to save 10 % off your first purchase of a website or

### Incorporating Priors

**9:04** · domain previously when choosing between different sets of Weights w we always pick the model with a higher probability of generating The observed data the lower means squared error but what if two models have identical values for that probability but differ in their exact values for w would we have a

**9:24** · reason to prefer one over the other if we know nothing about the nature of of our features we have no basis of comparing two equally performing models but often we have prior expectations about how features might contribute to the predictions and thus we have reasonable boundaries for their values let's illustrate it with an example suppose we have a coin with an unknown bias where the probability of heads is Theta between 0 and 1 we want

**9:54** · to estimate this value of theta by tossing the coin and tracking the results let's say we observe four hats out of five tosses if we ignore any assumptions about Theta and find the value that maximizes the probability of data we will conclude that Theta must be

**10:13** · 0.8 indeed this type of biased coin maximizes the probability of observing four heads out of five tosses but something doesn't seem right we know from experience that most coins typically land 50/50 maybe with a slight bias due to a symmetry but certainly not 80 to 20 the problem is that our solution only

**10:35** · cared about maximizing the probability of observed beta and completely ignored prior beliefs about Theta which likely is centered around 0.5 and decreases towards the edges but is there a systematic way to incorporate these prior assumptions into our regression

**10:54** · objective instead of maximizing the probability of data we can search for a set of Weights W that maximizes the joint probability of data and the weights in other words we look for weights that both explain the data well and align with our prior beliefs about what w should look like following the

**11:15** · conditional probability rule we can decompose the total probability into the following product the first factor is the likelihood exactly what we had before How likely a particular W is to have generated our observed dat AA given by the Cent formula for the noise the second factor is the prior where we incorporate assumptions about How likely different values of w are the key idea

**11:41** · is that different assumptions on prior distributions of Weights will lead to different criteria how to choose between alternative Solutions this shows up in the overall objective as so called regularization terms for the remainder of the video I'd like to focus on two most common types of regularization and show how they are born from two common

**12:05** · priors one of the most popular choices is to assume that weights W themselves follow a zeroc centered caution distribution why is that reasonable well in regression each component of w is a coefficient describing how a particular feature in the X Vector like the size of the house contributes to the prediction y if we randomly select features

### L2 regularization as Gaussian Prior

**12:31** · intuitively most will be probably irrelevant with values near zero while only a small subset will have significant weights additionally since each feature's coefficient in real data is shaped by many underly unobserved causes the central limit theorem applies to the coefficients as well formally we

**12:52** · can write that the prior probability of observing a particular set of Weights is given by the product of probab ities of individual components Each of which is given by the Gan formula with some variance tow now going back to our optimization objective we want to maximize The Joint

**13:12** · probability let's take the logarithm as before and substitute our formulas for the likelihood and the prior flipping the signs and grouping the two constants together we get the following this is what's known as rid regression or for L2 regularized linear

**13:31** · regression due to the square of the weight amplitudes the idea is that we are searching for the model that would both explain the data well but at the same time be not overly complex where complexity is measured as the sum of squares of the weights this regularization term penalizes large weight values pushing them toward zero exactly what we would expect from our gion prior assumption notice how beauti

**13:59** · this emerges the parameter Lambda which controls how strong the regularization is is the ratio between the data noise or the variance of the samples and the variance of the prior distribution of coefficients when we are very certain about our prior Lambda becomes larger given more weight to the regularization term conversely when the data is very reliable with small variance Lambda decreases placing more emphasis on fitting the data

### L1 regularization as Laplace Prior

**14:31** · but what if our intuition about the weights is different instead of just assuming they are generally small what if we believe most should be exactly zero with only a few significant ones this would correspond to a model where only a handful of features truly matter favoring sparse Solutions this assumption is particularly relevant for biological systems in genomics for example out of thousand of genes only a small subset

**15:01** · typically influences a particular trait similarly for Neuroscience only a small sparse subset of all neurons are responsible for encoding a particular feature in this case a gan prior is not ideal because it pushes weights towards zero too gently instead we might prefer

**15:20** · a distribution with a sharp Peak at zero which looks something like this this is known as the LL distribution and it is parametrized by symmetric exponentially Fallen tails the probability of the configuration of W's as a whole can be found by multiplying the probabilities of each component and following the same derivation as before taking the logarithm to counteract the exponent our

**15:47** · optimization objective becomes the following here Lambda is again the combination of constance of noise variance and the falloff of the weights prior this is known as L1 regular ization because the complexity penalizes the absolute values of w rather than their squares L1 regularization

**16:07** · typically leads to sparse Solutions where many weights are exactly zero which is preferable in many domains of science all right let's tie everything together today we explored the probabilistic view of linear regression and saw how the familiar least squares equation naturally emerges when we find the linear fit that maximizes the probability of observing our data importantly the squared error term wasn't just an arbitrary Choice it is a

### Putting all together

**16:39** · direct consequence of assuming caution noise in our model while this assumption is reasonable in most cases it may not be appropriate in specific settings where noise is correlated or multiplicative in nature we've also seen how incorporating prior beliefs about the coefficients lead to different regularization schemes providing a principled approach to balancing models accuracy with complexity the cion prior

**17:08** · gave us L2 regularization gently pushing all weights toward zero while the llos prior yielded L1 regularization favoring sparse Solutions where most weights become exactly zero this probabilistic

**17:23** · perspective extends far beyond linear regression to nearly all machine learning models whether examining deep neural networks as we saw in the previous video decision trees or clustering algorithms viewing them through the lens of probability provides a much deeper understanding of their underlying assumptions and design choices if you like the video share it with your friends subscribe to the channel if you haven't already and press the like button stay tuned for more neuroscience and machine learning topics coming up

**17:59** · \[Music\] \[Music\]