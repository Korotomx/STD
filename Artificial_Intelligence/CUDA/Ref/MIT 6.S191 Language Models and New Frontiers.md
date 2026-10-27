---
title:
source:
author:
published:
created:
description:
tags:
---
![](https://www.youtube.com/watch?v=ev7cLSd-ySE)

MIT Introduction to Deep Learning 6.S191: Lecture 6  
Language Models and New Frontiers  
Lecturer: Ava Amini  
\*\* New 2026 Edition \*\*  
  
For all lectures, slides, and lab materials: http://introtodeeplearning.com​  
  
Subscribe to stay up to date with new deep learning lectures at MIT, or follow us @MITDeepLearning on Twitter and Instagram to stay fully-connected!!

## Transcript

### Course logistics and updates

**0:12** · All right, let's get started again.

**0:15** · So, this will be the last lecture given by myself and Alexander and personally it's perhaps my favorite one where we're going to talk about deep learning from the lens of not only how far we've come, but also what is still left unanswered and still opportunities for overcoming some of the limitations of this technology and highlight a couple of the main directions today in terms of how as we've been discussing throughout the course, how powerful these deep learning based AI systems have gotten.

**0:49** · So, as Alexander mentioned, tomorrow we will have the distribution of the t-shirts. So, please come in person after the guest lectures, we will actually to to receive your t-shirts.

**1:04** · Uh it's always very exciting to have the memento as part of taking this course.

**1:10** · And to kind of orient you all with where we are logistically in terms of the schedule. So, we're on day three now.

**1:18** · This is the last lecture given by Alexander and myself and tomorrow and Friday we will have awesome guest lectures which I'll speak a little bit more about and then Friday the course will conclude with the project proposal competition.

### Final project requirements

**1:34** · So, on that note, we have a tremendous amount of prizes lined up for both the software labs and the project proposal competition.

**1:44** · We to remind you right, we have these three labs which hopefully you've been working towards and each is associated with a top prize in terms of the winner judged according to the submission criteria and grading rubric that is at the end of each of these labs. The detailed instructions for each of these is on the course syllabus including the link to a Dropbox file request where you will submit your labs. So please do to be eligible for the competitions they're currently wide open.

**2:18** · Okay, so for those who take this course for credit as MIT students you have two options to fulfill your credit requirement.

**2:27** · And the first is our famous project proposal competition which is kind of like a shark tank style pitch where you will present a novel deep learning research idea or application. And depending on the number of groups that we have presenting the presentation time is going to be between three to five minutes.

**2:50** · Importantly a couple of deadlines by tomorrow night at midnight strict you have to submit your group if you would like to participate in the competition.

**3:01** · Um we're going to do a basically a freeze of the Google sheet sign up at that time and we need that to logistically plan you know the actual proposals on Friday.

**3:12** · As well there's a shared slide deck where you will drop your slides and we need those slides in by 1 p.m. basically the start of class since we will be presenting off our laptop.

**3:24** · So importantly the prizes here are very very exciting and as John mentioned on day one there's an opportunity if you're a winner of the project proposal competition to kind of expand your idea and contribute it as a TEDx TEDx talk as part of TEDx MIT.

**3:43** · And we have some great prizes so again please please participate.

**3:48** · If you're taking the course for credit and you don't want to do the project proposal competition, you can submit a one-page written review of a deep learning AI paper, and we'll effectively take a look at, you know, do you do the assignment? Is it clear? Is it, um, you know, capturing the technical contribution of the work? And that is also due Friday.

### Guest lecture lineup

**4:14** · Really, really excitingly, we have an amazing lineup of guest lecturers this this year.

**4:21** · And in particular, tomorrow we're going to kick things off by a guest lecture from Chris Bishop, who is a technical fellow at Microsoft. He has done very pioneering work at the intersection of AI and the natural sciences, particularly physics and chemistry. And beyond that, he's made seminal contributions in terms of, uh, books and technical papers in the foundations of machine learning. So, it should be a fantastic talk.

**4:49** · And that will be followed by a talk from Matthias, co-founder and CTO of Liquid AI. So, if you've been playing with the liquid language models in Software Lab 3, and as Alexander demonstrated in lecture one, these are really, really efficient and high-quality, um, language models. And Matthias will be doing kind of a behind-the-scenes look at what it takes to actually train language models in today's world, and the secrets behind that.

**5:18** · And then on Friday, we will follow on with a lecture from Doug Blank, who is head of research at Comet ML, uh, talking about deployment considerations of AI in the wild. And finally, we have one of the, uh, co-creators of JAX, which is a third, very popular machine learning framework developed out of Google. And he's going to provide a detailed rundown of all the secrets behind Jax and what it's all about.

**5:52** · And Jax was is the language that Gemini, Google's premier frontier AI model, is developed in.

**6:01** · So, please come. It's going to be amazing. I personally am really excited to learn from all these amazing innovators.

**6:09** · I also want to give a very, very special shout-out to some of the program staff who has been instrumental in helping with this course. In particular, John Werner who hosted the social kickoff on Monday, which many of you attended. He's been instrumental in helping us, you know, bring this together as a community. And namely as well, Anisha and Shrika who are our lead TAs this year and perhaps you've interfaced with them during office hours and they've been amazing in help as well as the rest of the program TAs.

**6:43** · Okay, so that ends kind of the logistics orientation portion of this last lecture. So, now let's dive into really the technical content for this particular talk.

### Foundations and history

**6:56** · So, so far we've really talked about deep learning in many, many different forms, right? From what deep learning even is all the way up to the frontiers of reinforcement learning.

**7:06** · And we've been thinking about how deep learning gives us a toolkit, a technological foundation to answer some really outstanding challenges across different research areas and areas of society.

**7:19** · From autonomous vehicles and robotics to biology, medicine, health care, reinforcement learning, and unlocking new advances in strategy and language modeling, generative models, applications beyond in humanoids, and a whole host of other areas from finance to security and beyond.

**7:42** · And hopefully through this class you've gotten a sense of both the technical foundations, but also an understanding of how these methods can be applied to particular scenarios and research areas that may be relevant to you.

**7:57** · And we've talked about kind of two different paradigms for thinking about how deep learning gives us a toolkit to map data to outputs and learn these functions in this way. Where we've seen how we can go from data to decision in the traditional supervised setting, but also in the context of RL, but also to go back from desired outcomes and

**8:23** · decisions back to the data itself in the context of these generative models that help us solve what we call these inverse problems, right? In actually being able to model data distributions themselves.

**8:37** · And in both these cases, you know, we've talked about kind of implicitly how neural networks learn these very very complex functions that go from data to output or over a distribution of data itself.

### Generalization challenges

**8:51** · And to understand this idea in more detail, I think it's very helpful to go back to some of the origins of AI and the origins of the theory of neural networks in the first place.

**9:03** · And there was in particular this theorem that was posited back in 1989 that said the following. And this theorem is known as the universal approximation theorem.

**9:16** · And it says that a neural network, a feedforward neural network with a single hidden layer would be sufficient to approximate to some precision any continuous function.

**9:33** · And so, we've talked about deep neural networks, deep learning, right? Stacking multiple layers together.

**9:40** · But this theorem is not even saying that we need multiple layers stacked together. It's saying you just need one fully connected feedforward layer.

**9:50** · And if you believe that a problem can be reduced to a mapping between inputs and output, a neural network with that one layer should be sufficient to approximate that function to some degree of precision.

**10:05** · Now, this seems very, very powerful, right? But there are a few important caveats to consider here.

**10:12** · Which is there's no guarantee on the size of that layer that this theorem proposes, right? The number of hidden units or individual neurons within within that layer could be very, very, very high, right? There's no guarantee or limit on the size.

**10:29** · And the second one is perhaps even more important, right?

**10:33** · Which says basically that this theorem is placing no guarantees on the generalization capacity of such a model.

**10:42** · Thinking back to lecture one, we talked about the problems of overfitting and how when we overfit to our data, we very closely reach low error on training, but maybe this means poorer performance on the test set or the generalization scenario.

**11:00** · And it gets really at this, you know, kind of two considerations that are very dominant in deep learning today, which is how large do we have to make these models so that they have these general-purpose capabilities, and can they actually possess general-purpose capabilities that enable generalization to the new scenarios that we really care about?

**11:25** · And so I really, really like this theorem and this historical perspective because it sets into context that, like any technology, AI, deep learning is just that. It's a technology. It's going to go through waves of, you know, growth, goes through waves of criticism and limitations, and we have to take these all into context when we think of this technology.

**11:50** · And, you know, straightforwardly, right now we're in this phase of exponential growth with the emergence of these large very large and very general-purpose AI systems. But, it wasn't always the case, both due to practical hardware constraints, but also from the community. People There were times when these deep learning models were under very, very heavy scrutiny from the scientific community in terms of whether they would actually lead to real breakthroughs.

**12:21** · So, I hope that this sets into perspective from a theoretical point of view and a thought experiment point of view, but also the historical point of view, just how much this moment that we are in today means in terms of the history of AI.

**12:39** · And so, in the next part of this lecture, we're going to talk about some of the concrete limitations that neural networks still face today.

**12:49** · And the first, I think, is very interesting to show and connects back to this idea proposed by the universal approximation theorem, is what we actually mean by generalization and fitting too closely to our training data.

### Neural network failure modes

**13:07** · So, there was this paper several years back now that really, I think, contextualizes this better than anything else, which is understanding deep neural networks requires rethinking generalization.

**13:20** · So, in this paper, they took example images from this very large-scale data set called ImageNet, And each of these images is associated with a particular label, right?

**13:32** · Describing what's in the image, as you see here.

**13:35** · And they did a very simple experiment where for every image in this data, not class, but image. So, not across labels, but across individual images.

**13:47** · They flipped a K-sided die, where K was the total number of classes in the data set.

**13:55** · And re-assigned the label of that image according to what the random choice, right? The The die's outcome was.

**14:06** · And as you can see here, this yields to arbitrary mappings across these examples. Where now you can even have two instances that belong to the same class, but are now mapping to completely different labels. Neither of which, you know, are the actual semantic label of the image.

**14:29** · Now, they took this data and they trained a deep neural network model on this, you know, perturbed data, ranging from the original data untouched with the original labels to if they did progressively increasing amounts of randomization to, you know, flip and mess up the the labels in this data.

**14:53** · And what you What was really startling to see was, as you may expect, right? If they held out a test set, again, with these randomized labels, as you increase the degree of randomization, the performance on the test set gets increasingly worse.

**15:11** · But what was startling is if you look now on the performance on the training set, it didn't matter how much you randomized the data, if you trained your your model long enough on those training set examples, you could still fit a very very high classification model.

**15:31** · And so really this this showcases that this idea of function approximation with respect to the training set and what is the capacity of these models to generalize versus you know, fit training data to some degree of precision.

**15:49** · And so this shows this principle of the universal approximation theorem kind of in practice.

**15:55** · Granted, there's a big difference because this is a deep model and you know, that theorem talks about a single layer, but still it's this principle of mapping functions to some degree of precision and therefore limiting generalization on test sets.

**16:12** · So this in total, right, gets at this idea, again, to drive this point home of neural networks being very powerful function approximators.

**16:23** · And when we think about what it takes to approximate a function, let's say we have the these examples here, we what the universal approximation theorem states is that we can, you know, train and build a very good function approximator to such data.

**16:43** · And in the theory of deep learning, we can think about these neural networks as learning some maximum likelihood, most likely estimate of data within this distribution.

**16:55** · Such that if we gave the model a new data point here in purple, we can produce a reasonable prediction, but if we think about the extensions beyond this regime, we don't yet have solid theoretical guarantees on the behavior of these models in these out of distribution scenarios.

**17:18** · And so this raises this question of how do we know when these models do or do not know? How can we understand the limits on their capacities and their capability to generalize out of distribution to these harder and harder scenarios?

**17:36** · And so I think that in concert all of these points come together to, you know, ground us in what the capabilities and limitations of these models are generally speaking.

**17:48** · And often times I think there's a sort of myth and a conception in the field, especially when we come to a technology like deep learning or AI, and say, "Okay, can it be this magic be-all end-all solution to, you know, the world's problems?"

**18:08** · And there's this comparison that we like to draw to the historical alchemist trying to turn, you know, heavy metals into gold.

**18:17** · Maybe there's some magic solution where you turn the crank and this is the result that you get out.

**18:23** · And often times deep learning has been cast in this lens, but there's an equal maxim which says, "Garbage in, garbage out." Right? If you train your data on your model on a very limited set of data, on a problem that may not be appropriate, or, you know, you mismatch the size of the model to the complexity of the task, all these sorts of issues can result in real problems in terms of you're not actually getting a capable model. Right?

**18:53** · You may be able to learn your training data, but will it actually perform well on test scenarios?

**19:01** · The answer often is no.

**19:04** · So as you go out and think about your final projects and maybe work in your real lives and and jobs or studies, I really really encourage you to think about, you know, task at hand, inputs and outputs. What is the quality of data that you can curate or generate for the task, and does deep learning even make sense in the first place as the approach to take for such a problem?

**19:29** · And so, we can see this issue of, you know, garbage in, garbage out manifested in a couple of different ways. Not explicitly necessarily garbage, but it's right, but in terms of the limitations of training data distributions and how that manifests in the behavior of these models.

### Safety, bias, and ethics

**19:49** · So, let's say we have this example, right? We're training a vision model on images of natural images.

**19:58** · And if we train this network to, let's say, colorize black and white images, perhaps what we could get out as a result if we did this was a output like this.

**20:12** · Now, let's take a close look at this example with this image of a dog, and let's say the the picture Sorry, the model is trained to colorize these images. That is, convert from black and white to color.

**20:26** · Anyone notice anything interesting about Green on the ear, yeah.

**20:36** · The tongue is also kind of reddish, right? Yeah, so why could this be the case?

**20:44** · Well, in the tongue example, probably there are a lot of images of dogs in the data set where the dog is sticking their tongue out, right? That's the overrepresented example in the data, and often this behavior can be replicated as a result.

**21:03** · This can also have much more real and serious consequences when it comes to real world scenarios and thinking about data diversity and abundance in training neural network models.

**21:15** · So, infamously and very, very tragically uh a few years ago an autonomous vehicle that was operating in autonomous mode crashed and ended up the driver ended up not surviving the accident. And it turned out actually that the driver that was killed was reporting multiple instances over several weeks where the car in autonomous mode would swivel towards a construction barrier that ended up being the site of the accident.

**21:47** · And it turned out that when when uh investigations were conducted into this that in the past images from street view of that location, the construction barrier was not present.

**22:03** · But more recently when the car was actually, you know, uh driving in the real world, that construction barrier had been erected. And so, it was this out of distribution outlier that had not been in the training set. And in in since it resulted in this instance, very tragically, um resulting in this accident. And so, this gets at this notion of again, data diversity, data quality, abundance, and how this also closely relates to this notion of uncertainty in AI models.

**22:34** · How do we know effectively when the models are confident in their predictions or when they're lacking information and need human intervention.

**22:47** · And this is very particularly critical in safety-critical applications, right?

**22:52** · Things like autonomous vehicles, biology, medicine, health care.

**22:57** · And also in security and public surveillance and facial detection systems.

**23:03** · And as we saw, right, this can be attributed sometimes in relating to how imbalances or noise in our data can yield these uh regions of more uncertainty in terms of the network's outputs and decisions.

**23:21** · So, as you perhaps have experienced as well in working through lab two, right, these are very, very real issues that we have strategies for both algorithmically and from a data perspective to try to counteract.

### Overcoming model limitations

**23:37** · Another failure mode that I'd like to consider and and highlight because it's very um famous and well-known in this field is this idea of adversarial attacks or jailbreaks, right?

**23:49** · And the idea here is to take some example or create some synthetic example that basically fools the neural network model.

**23:59** · And this started out from these adversarial attacks on vision models, CNNs in particular, where we realized that we could take an natural image, apply a sort of perturbation, a noise-based perturbation to that image, and when this perturbed image, which has these perturbations that are imperceptible to the human eye, is now input to the model as a test example, it completely

**24:31** · screws up and fools the model in terms of producing now an incorrect classification, right? Going from a correct classification of temple to incorrect classification of ostrich with very, very high probability.

**24:47** · And really the core aspect to this is what is happening in this perturbation, this application of noise that is somehow tripping up the network so severely.

**25:00** · And to get at and understand how this actually works, recall again back to lecture one. The way we train neural networks is with this algorithm of gradient descent, where we have some objective, a loss function J, and what we are trying to optimize is our set of weights W to minimize the error on that loss.

**25:24** · How can we change our weights in some way to minimize the loss?

**25:29** · When we train our networks with a fixed image and a true label, this is the uh update that is occurring, right, over the weights itself.

**25:41** · Conversely, when we think about generation of an adversarial image or an adversarial attack, the question is the the inverse, right? How can we modify the input such that it yields a very very large change, uh an increase in the loss. Perturbing the input X to now, given a fixed set of weights and a true label, increase the loss function to then yield this adversarial perturbation.

**26:12** · And so, it goes even further to not only apply to 2D images, but an extension was proposed by a group out of MIT CSAIL right here, where they were actually able to take this concept and synthesize 3D objects in the real world that were constructed adversarially such that images of these real physical objects could fool a CNN-based classification system.

**26:42** · And so, this goes to show kind of the power of these these types of approaches, very simple approach where instead of updating weights, we're perturbing the input that yield measurable differences in the outputs of these models.

**26:59** · Finally, we'd as you've been exploring right, a very real and severe limitation of neural networks in terms of implications for safety and fairness and ethics is the now very well-appreciated notion of algorithmic bias, right? And so, again emphasizing the integration between the lectures and the software labs, hopefully you've had the chance to explore some of these ideas hands-on.

**27:28** · And so, this is not comprehensive at all, right? These are just some of the limitations of neural networks that exist. But, I like to highlight these because you know, we can look at limitations from the lens of opportunity. Where is there still opportunity to develop new technologies and solutions to counteract some of these limitations, whether it's algorithmic bias, interpretability, uncertainty, or other limitations that are highlighted here.

**27:59** · Okay, so transitioning a little bit, right? For the remainder of this talk, I want to take a couple of these limitations and focus on the new advances in AI that are happening today that directly overcome some of these. In particular, how we can go beyond this really achieve strong capabilities in the lens of generalization.

**28:23** · Going beyond just the training distribution to build these models that have very general-purpose capabilities.

**28:34** · And as we've seen right, neural networks depend heavily on the data, but we've also unlocked advances where we found that scaling the data and scaling the models themselves lead to emerging capabilities that improve generalization very, very significantly as we've seen with language models today, for example.

**28:58** · Okay, so yesterday I kind of teased the first of these two new frontiers that I'd like to talk about, which is the new frontiers in generative modeling and in particular a class of models called diffusion models that have unlocked really, really strong capabilities in generative modeling.

### Generative diffusion models

**29:18** · And as we saw in lecture four, right? We talked about in depth the foundations of generative models. Going back to the ideas of autoencoding, how we can learn these compressions captured in these latent variables and the beginnings of sample generation that we saw with GANs.

**29:39** · Yet, as we discussed in a lot of the Q&amp;A and in the lecture four, these approaches have a few very notable limitations. Namely, that they can collapse to basically generate average instances, what we call model collapse.

**29:57** · It's very difficult as a result to generate instances that stretch the distributions of the data.

**30:04** · And in particular with approaches like GANs, they're very tricky to train from the perspective of having these two neural networks that are, you know, posed with this adversarial objective.

**30:17** · And so those limitations lead into challenges in terms of training stability, training efficiency, as well as the quality and novelty of the instances that are produced by these generative models.

**30:32** · And so recently, the latest work in generative modeling has explored and expanded an approach called diffusion modeling, which has become one of the dominant paradigms in generative models today. And we're going to talk in-depth about how these diffusion models work and really why they are so powerful.

**30:53** · And as as you may have experienced, right, with common text-to-image systems where you can input a text-based prompt and have the image generated conditioned on that prompt, the backbone to these approaches is very often a diffusion-based model.

**31:13** · So, what is a diffusion model? And how does it relate to some of the principles that we introduced in lecture four?

**31:22** · We saw with VAEs and GANs, right, grounding ourselves in the foundations, that the concept was to be able to generate a sample in sort of one shot, directly from some distribution of noise or low-d- low set of latent variables back to the data space X.

**31:44** · In diffusion, there's a fundamental difference to this approach.

**31:49** · Which says that rather than doing generation in a single shot, what if we can decompose the problem into iterative generations that make the task easier?

**32:02** · And this is the principle behind how diffusion models operate.

**32:06** · They generate new samples iteratively by learning how to remove noise and doing this consecutively step by step to refine the generation and refine the generative process.

**32:21** · And as you can perhaps intuit from this kind of idea of refining and removing noise, what that means is when we build a diffusion model, there are two processes. One is the deterministic forward noising process that transforms data to noise.

**32:40** · And to break that down, what we do is we start with training data, let's say images.

**32:46** · And in the forward noising process, noise is iteratively added to the data instance, step-by-step, such that we slowly wipe out the details in the data instance until the instance is pure random noise.

**33:02** · And these basically now constitute iterative samples that we can use to train the model. We have taken one image and gone step-by-step and noised it. And now the neural network actually learns the denoising process, the reverse process, to go from noise to data.

**33:23** · So, again, if we break this down in terms of steps, right? Given an image, we sample some random noise pattern, as shown on the right. And in forward process, this noise is progressively and increment progressively added step-by-step, such that we get these iterative time steps of noising, right?

**33:46** · We're now at T equals 0 to T equals 4 in this instance, we have these images which differ by a step-wise addition of random noise.

**33:59** · Now, the question really becomes how do we define this reverse denoising process?

**34:05** · And the task, very fundamentally, is given an image at time step T at input, can we learn to estimate the image at T minus 1, right? The prior time step, looking at one instance that's less noised.

**34:23** · The task, right, when we're actually training the neural network, is to learn the neural network to do this denoising estimation. Given an image at T, find a way to arrive at the image at the preceding step T minus 1.

**34:41** · How can we actually do this, right?

**34:44** · What would be the formulation for a loss function that we could define to train this network?

**34:52** · Any ideas?

**34:58** · Yeah.

**34:58** · Remove one color.

**34:59** · Or remove one shade.

**35:03** · So, the idea was to remove one color. Remember that the noise is random noise, right? This is Gaussian noise. There's no Right. The This is defined from a sampling from a Gaussian distribution and just applying that, right? But, we have these two instances side by side. One differs by that addition of that Gaussian noise relative to the other.

**35:30** · So, the way is to calculate how far T3 is from the original image at T1.

**35:35** · Right.

**35:35** · So, the proposal was look at the difference in the pixel values between uh T2 and T3 in this instance and compute the difference, how far they are. That's exactly right, right? We can train this model using a like a mean squared error style loss comparing the step the image at T equals 3, T equals 2, where the difference is going to be the pixel values.

**36:00** · And so, if these images differ by additions of random noise, then the model can learn how to, you know, remove this noise from these stepwise pairs that we have generated. And that's exactly right. And so, it turns out that predicting the difference, which is the noise, is a very, very effective way to train these diffusion models.

**36:26** · And so, that gives us our recipe, right?

**36:28** · We have this forward noising process.

**36:31** · We've defined a loss to learn to train the neural network in the reverse denoising process. Now, once we've trained our model, how do we actually produce a new data instance?

**36:44** · At inference time, using the trained model, we can start with a pattern of of noise here. And to sample a brand new generation, we take this and we take our trained neural network to predict that residual difference and then use this to define a new instance at that next time step, incrementally having less noise.

**37:09** · And we do this process repeatedly time step by time step as this denoising occurs, we can see our image kind of come to life step-wise such that at our final time step, we're back to the image space and we have the newly generated sample.

**37:27** · So, putting this all together, right?

**37:30** · In training, we learn the neural network model to predict these additions of noise and to define this reverse denoising process. And at inference to sample a brand new generation, we take that trained model, start with noise, and perform this iterative denoising process to construct new data samples out.

**37:52** · And so, in practice, right, what this means is that in starting with random noise, but still decomposing the actual objective into these iterative steps, that means that the task is simplified, right, for the model to learn, but we still have a very, very high capacity of basically information capacity at the beginning to actually produce very diverse generations.

**38:18** · And so, there's maximum variability encapsulated such that diffusion models can produce very diverse, high-quality samples through through this way. And so, different instances, starting with a completely different instance of noise, can yield a strikingly different sampled image as the end result. So, I think there were a couple of questions. Yeah, go ahead.

**38:46** · Would that suggest that what is being called noise is not noise at all? In fact, there's some sort of order to the noise that that is turning one image into that other noise-looking image.

**39:01** · Yeah, that's a that's a great point. So, the question is, does this suggest that the noise itself is actually not noise?

**39:10** · Well, the difference is subtle here because where the model actually gets its signal is in that comparison of step T versus step T minus 1. That gives enough supervisory signal to actually basically bring semantic structure to the problem, even if the application of noise is still a noise function. So, the noise itself is not, you know, structured meaningfully in any way.

**39:38** · It's the difference between those two time steps that have been created in this forward process that actually lends signal and semantic structure to the problem.

**39:50** · So, we started with a text-to-image problem, right?

**39:53** · Yeah.

**39:53** · So, are we also capturing some kind of description of the image that gets represented in latent space through the noise?

**40:00** · A great question. So, the question is about now, how does text-to-image work?

**40:04** · So, the examples I've shown are what we call about like unconditional generation. So, here in this example, it's just showing image generation without injection of text.

**40:17** · So, that allows for generation of images basically from the data space. The way now we can think about conditioning on a text-based prompt and doing examples like this is leveraging the signal from the text to basically guide the the generation process. And in practice, one way that this works is by taking an embedding of the text, right?

**40:40** · So, you you know, you do your tokenization, you have the text uh numerical representation, and there's a language-based encoder model or embedding model that then produces a vector representing that text. And then in then signal from that vector can be then basically mixed with signal uh from the corresponding image such that you can basically um learn patterns between that text representation and the image representation.

**41:18** · And in practice with these uh diffusion models that can do like text-conditioned generation um you can basically in training train some percent of the time using the text prompts, some percent of the time on just the images, and use this as signal to basically push push the model based on the text prompts to produce high-quality generations based on the semantic content there.

**41:45** · So, it's really about like aligning the text with the image, using this some percent of the time in training, but still having some percent of training where you're just going over images, so you still get high-quality generations out. Yeah.

**42:01** · And is the embedding trained separately or is Yeah, so in this case, often in practice, the embedding model would have been trained separately, and maybe you use that prior. Sometimes also you could refine the embedding model based on the um image training as well, so you get signal back there. Yeah.

**42:24** · Yeah, so on that note, right, text to image generation is perhaps the the medium that you may be most familiar with in interacting with these diffusion models. But beyond that, right, it goes um beyond images, it goes beyond text to other modalities as well. So, in in recent years, we have seen quite strong capabilities in molecular design in particular, taking these concepts of diffusion models to the biology and chemistry space, right?

**42:54** · Where now you can think about as input, you perhaps have um 3D coordinates of atoms in a molecule or atoms in a protein that you can then uh do diffusion over in continuous space, because like pixels in an image, right, these are continuous values. And so, tremendous efforts have been uh achieved here, and and really strong capabilities now being translated into many real-world applications.

### Large language models

**43:28** · Okay.

**43:30** · So, the final piece of this this lecture is going to talk about really a foundation to large language models. As we all know, right, this is a very prominent frontier of AI and deep learning today. And what we want to do is really convey again core principles of what language models are, how they operate, and how that has yielded some of the very strong capabilities that we've seen in practice.

**44:00** · So, at this point, right, it's no secret. GPT, Gemini, all the you know, Copilot, all these tools that are out there, these powerful language models have revolutionized our world. But fundamentally, what are large language models or LLMs?

**44:17** · We started this class off with this definition of what is AI, what is deep learning. LLMs are simply a special class of deep learning models that for simplicity, let's think about them as very large neural networks that are trained on very large sets of text. And we have different types of tasks or objectives that we can use to train these models in general purpose ways.

**44:47** · And to break that down, the core sort of flow or pipeline behind how LLMs like GPT work is that we have some general purpose, you know, unannotated, really, data set. For example, something that's scraped from the web, like the Common Crawl, Wikipedia, web text, code, you know, all these different sources of text-based data.

**45:12** · And the first step in training these models, as we discussed in the sequence modeling lecture, is to basically split this text up into sequences or chunks. Sequences of chunks, rather. And these chunks are called tokens. So if you hear of tokenization or tokens in the context of LLMs, that is referring to this chunking procedure. We then, right, these chunks have IDs numerically, and those numerical IDs can be used as input to the LLM training process.

**45:48** · And to give you a sense of scale, right, of these models, something like GPT-3 was reported to have 175 billion individual parameters. And we know that models, GPT-4, 5, etc., have often scaled beyond that, but we have also seen these small language models, such as those from uh Liquid AI, that are scaled back in terms of their parameters by orders of magnitude, but still demonstrate strong capabilities.

**46:22** · And really the dominant task in modern language modeling is a task that we refer to as next token prediction. And that is formulated according to this objective, where very similar to what we saw in sequence modeling, given a sequence of tokens, predict the next token. And we update the model's parameters, its weights, based on how good that next token prediction is.

**46:53** · But how does this work, really? This is the concept. What is actually the loss that we formulate to the model to train it in this way?

**47:02** · So, let's break that down, right?

**47:05** · Looking at the next token prediction task. So, say we have this raw text, MIT Deep Learning is so awesome, and we break that into tokens, these chunks, which I'm just showing as words for simplicity. And there's going to be the process of converting those into IDs and embedding them, right, to get this numerical representation that's going to now be input into the large language model.

**47:32** · In next token prediction, the task, right, is given a series of tokens, predict the next token. And when we look at this and break this down, what we do is we can compute the model is outputting actually probabilities over what the most likely next token is in the sequence, over the whole set of possible tokens.

**47:56** · Meaning, if the model is predicting the token at this position in the sequence, it's actually computing the likely probabilities for all the possible tokens in the vocabulary. And just as we saw in lecture one with losses that define classification, right? This is a classification problem.

**48:19** · Because we have a discrete set of tokens in our vocabulary, we can look at the true next token and the predicted probabilities over the possible next tokens and compute a cross-entropy loss using this.

**48:37** · And why this is so powerful is because of the way we have set this up using the data itself as its signal, we don't require any external labels other than what signal is in the structure of the text and the structure of the data itself.

**48:57** · And so, this is is a very, very, very powerful idea and so beautiful in its simplicity because you can just use that classification cross-entropy loss to compare the probably predicted probabilities over your token vocabulary to the true identity of the true next token and use this to basically learn structure in these very complex text-based data.

**49:25** · So, with that in hand, right?

**49:28** · Of this task of, you know, given a sequence of tokens, predict the next token, when we actually take trained language models and deploy them, we can see this come to life in the fact that now, you know, a base language model does this next token prediction task, but they've actually been tuned and refined following that to be able to follow structured prompts and act as these chatbots and interactive agents, where now there's a clear definition of what

**50:00** · you as the user provide as a prompt to the model, and then what the LLM generates out as a response.

**50:08** · And so, what makes this so powerful is we combine this very simple objective function of next token prediction using a cross entropy loss with the scale of data that's available and the scale of the models and compute that we are able to achieve. And together this lends powerful capabilities because now we can learn patterns in these really large-scale data sets.

**50:34** · And so, as you probably have experienced, right, today's language models are extremely capable in assisting with writing, assisting with planning, doing knowledge retrieval, and they have shown this mastery over natural language.

**50:49** · But, still they face challenges in terms of, again, some of these same principles that I introduced at the beginning of this lecture. How do we know if the generations are confident, right? Maybe they're very likely, they're very probable, but that's not the same as being high confidence. And so, how can we quantify the uncertainty of these LLMs? It's still a very open research direction.

**51:17** · And probably if you, you know, worked with these models long enough, you've seen instances where the generated text seems feasible and consistent and logical, but if you know about, maybe it's it's a particular field, you know it's not really like all the way there. And this is the notion of hallucination. And actually there's been very recent work that has shown that language models that are well calibrated will necessarily produce hallucinations as a result.

**51:52** · And similar to the principles of adversarial attacks, there are still ways to jailbreak these models and basically probe them to expose these types of you know, adversarial failure modes. And there are still limitations in long-term planning, logic, which recent advances in reasoning have uh enabled tremendous new capabilities, but they're still a long way to go. And so, this highlights still that even with this powerful technology, there are key challenges remaining.

**52:30** · Finally, and and I think perhaps, you know, what has really struck a chord with many of us over the past couple of years is this observation that these modern language models can generalize. They can, you know, perform tasks in domains that stretch their capabilities. And a lot of this is due to this notion of emergent properties or emergent abilities.

**52:59** · And work that actually systematically evaluated the performance of these models as a function of the amount of training data that they've seen and as a function of model capacity. And in particular, seminal work showed that past a particular threshold of model scale, once you cross that threshold, you get new inflection points and state step changes in model capabilities that seem to only come with scaling the data, scaling the compute, and scaling the model parameters.

**53:35** · And so, as this concept has highlighted, the the idea is that there's a basically a hierarchy of abilities that can be unlocked as the models scale towards larger and larger sizes, they're able to achieve more complicated emergent abilities.

**53:58** · And I think that this notion of emergence, thinking about how these language models are effectively modeling our world through the lens of natural language, spawns and inspires a powerful idea that I would like to leave you all with as a close to this class of how do we actually think about reasoning? How do we think about augmenting and accelerating our own capabilities with AI?

**54:24** · Because I think that especially for someone who works on these models and closely alongside these models, you know, the goal is ultimately that these stay as technology, right?

**54:38** · That we as humans can use to accelerate our own creative process and our own capabilities in ways that the models can't. And similarly that our own limitations can be augmented by the capabilities the models possess that are still very far out of reach for us as humans.

**54:59** · And so I think and and inspire you and encourage you to really think closely about these relationships and connections between these two worlds and how you can utilize and build these models in your own life to augment and accelerate your own work and ideas.

**55:18** · So with that, I'll close the the lecture and I you know, kind of close out by thinking about the opportunity that you have at hand to actually experience and work with these models hands-on, right?

### Conclusion and final labs

**55:33** · You're here in this class. Not everyone has this opportunity or comes to to sit here in front of us. And so, I highly highly encourage you to dive in, get your hands dirty, play with these models, and and actually see what it takes because it will give you new understanding that the lectures um complement but don't directly give. And so, please have your hand at lab three on fine-tuning language models.

**56:03** · And thank you so much for that your attention, and please stay tuned for tomorrow's guest lectures, t-shirt delivery, and much more still to come. Thank you so much.

关联：[[Artificial_Intelligence/MIT 6.S191/主页|6.S191]]
