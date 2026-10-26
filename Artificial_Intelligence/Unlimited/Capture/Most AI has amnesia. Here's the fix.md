---
title: "Most AI has amnesia. Here's the fix"
source: "https://www.youtube.com/watch?v=PAoe7mmmvp0"
author:
  - "[[Artem Kirsanov]]"
published: 2026-04-02
created: 2026-10-20
description: "Get a 20% discount to my favorite book summary service at https://shortform.com/artem=====My name is Artem, I'm a neuroscience PhD student at Harvard University. 🌎 Website and Social links: https"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=PAoe7mmmvp0)

Get a 20% discount to my favorite book summary service at https://shortform.com/artem  
  
\=====  
My name is Artem, I'm a neuroscience PhD student at Harvard University.  
🌎 Website and Social links: https://kirsanov.ai/  
📥 "Receptive Field" neuro-newsletter: https://artemkirsanov.substack.com/  
✨ Support me on Patreon to get access to Discord community: https://patreon.com/artemkirsanov  
\=====  
  
Most neural networks have no concept of time: they analyze each input in complete isolation, with no memory of what came before. In this video, we explore how Recurrent Neural Networks (RNNs) solve this problem by adding a single new term to the network equation: the echo. We build up the intuition from scratch, starting with feedforward networks, then showing why the naive approach to memory fails, and arriving at gated architectures like LSTMs and GRUs through a natural chain of reasoning — discovering along the way that the simplest working memory mechanism turns out to be the same one biology already uses.  
  
  
🕒 OUTLINE:  
00:00 Introduction  
02:10 ANN Background  
05:53 Adding Recurrence  
11:04 Sponsor: Shortform  
12:05 Leaky Integration  
14:40 Gated Memory  
17:18 Putting it together  
  
\=====  
Icons by Freepik and Biorender  
Music by Artlist  
This video was sponsored by Shortform  
\=====  
  
\*Disclaimer:\* This channel is my personal project. The views and content expressed here are my own and are separate from my research role at Harvard University.  
  
#artificialintelligence #machinelearning #deeplearning

## Transcript

### Introduction

**0:00** · For all their incredible power, most artificial neural networks have a fundamental flaw. They have no concept of time.

**0:09** · Take this network right here. This is AlexNet. When it was unveiled in 2012, it marked a turning point in the history of AI.

**0:18** · AlexNet is a deep neural network built for just one thing, scene.

**0:23** · You can feed it an image and it spits out a list of 1,000 probabilities, telling you what it thinks is in the picture.

**0:31** · For example, you show it this picture right here and its output neurons fire up. Most are silent, close to zero, but one neuron, number 29 in the list, lights up with a value near one.

**0:44** · We'll look up class 29 and sure enough, it stands for axolotl. Impressive, but what if we wanted to analyze a movie?

**0:53** · The straightforward approach would be to feed in one frame at a time and look at the predictions. But this method is deeply flawed. Each analysis is completely independent of the rest. The network has no memory and no context. In fact, you could shuffle the movie's frames into a completely random order and the network wouldn't even notice.

**1:14** · It is like an expert with an extreme case of retrograde amnesia. It can tell you what it thinks is in the image, but the moment that image vanishes, it forgets it ever existed.

**1:26** · This is a massive problem because it's not how our brains work at all.

**1:31** · When we watch a movie, our perception of the current frame is profoundly shaped by the one we just saw before. We build context. We anticipate what's next. We understand the arrow of time.

**1:44** · So, how do we build a neural network that does the same thing? How do we endow a machine with memory? That is the motivation behind recurrent neural networks, machines that bake the concept of sequence into their very fabric.

**1:59** · But to understand how we build time into the machine, we first must get a clear picture of the network itself. So, let's get a very quick reminder on the classic neural networks.

### ANN Background

**2:13** · The fundamental building block of a neural network is the neuron. You can think of it as a tiny evidence waiting machine.

**2:20** · It receives incoming signals, multiplies each one by a corresponding weight, and sums them all up, building an internal state.

**2:29** · Think of it as voltage building up across a cell membrane.

**2:33** · This is where the computation lives.

**2:35** · However, neurons don't communicate their voltage numbers directly to their neighbors. Instead, they convert that internal state into a spike train, a sequence of distinct electrical pulses sent through the wires to other neurons.

**2:50** · A mathematical abstraction for this is an activation function sigma.

**2:55** · It takes the internal state and maps it to the actual signal sent downstream.

**3:00** · Typically, it might look like a threshold gate, sending only positive numbers through and squashing the negative values to zero. But a neuron by itself doesn't really do much. To enable useful computations, thousands of these neurons are organized into layers.

**3:16** · All neurons in a specific layer look at the exact same signals coming in from the layer before them, but just weight them differently. Writing out the math for every single neuron would be a nightmare of indices. This is where the beautiful shorthand of linear algebra comes in.

**3:33** · It allows us to stop thinking about individual neurons and start thinking about the state of the layer as a whole.

**3:40** · Consider any pair of adjacent layers, layer L minus 1 and layer L.

**3:47** · First, let's bundle the internal states of all of neurons in a layer into a single object, a vector.

**3:53** · Think of it as a column of numbers representing the internal pressure of every neuron in that layer.

**4:00** · The question is, given the state of layer L minus 1, how do we determine H sub L?

**4:06** · Well, layer L doesn't see the raw internal states of the previous layer directly. It sees the signals generated by those states.

**4:15** · So, first, the previous layer must fire.

**4:19** · We apply our activation function to the previous state.

**4:23** · Then, the signals travel along the connections to the next layer.

**4:27** · Since every neuron in layer L minus 1 connects to every neuron in layer L, these weights form a massive grid of numbers, the weight matrix WL.

**4:38** · This matrix represents the wiring diagram of a pair of layers.

**4:42** · When we multiply this matrix by the incoming signals, we're calculating the weighted sum for every neuron in the new layer simultaneously.

**4:51** · This gives us the new internal voltages.

**4:54** · So, that entire web of interactions compresses into one elegant equation.

**4:59** · We take the old internal state, convert it to the signal through sigma, run it through the wiring with the weight matrix, and that establishes the new internal state.

**5:11** · This is the fundamental formula for a feedforward neural network. It's a static, one-way transformation of information.

**5:19** · By stacking many of these layers together, we can build a machine that does remarkable things, like mapping the pixels of an image to the label of a handwritten digit. So, we've captured the entire logic of the feedforward network in a single elegant equation.

**5:35** · Fire and project. Fire and project, layer after layer. But, notice something crucial about it.

**5:41** · The new state depends only on the signal coming in from the the before it. It has no knowledge of what happened 5 minutes ago.

**5:49** · And this is exactly what we're about to change.

### Adding Recurrence

**5:53** · Let's introduce time into the equation.

**5:56** · Think about real physical systems like a capacitor or a vibrating membrane of a drum. They don't just reset to zero instantaneously. They carry the echo of their past states.

**6:08** · So, let's rewrite our fundamental equation for the state of layer L at time T.

**6:13** · It is now influenced by what signals the previous layer is sending right now, just like in the feedforward case, but it also senses an echo of its past self.

**6:24** · Here we have M as a general memory function that describes how states propagate in time.

**6:30** · And depending on the choice of M, you get different species of neural networks.

**6:35** · Let's think about what would be the most natural choice. To clearly see things, let's change the layout. Horizontal axis here shows the progression across layers of the network as before. But now there is a vertical axis that shows the progression of time across the elements of the sequence.

**6:54** · On this 2D grid, each node receives two sources of information. An arrow flowing into it from the left, communicated by the previous layer, as well as an arrow flowing into it from the top, information communicated across time from its past self via the M function.

**7:13** · Now, imagine you are a researcher inventing this for the very first time, and you're pondering what the memory function should be.

**7:21** · Here is the most natural choice.

**7:23** · Let's take the propagation logic of horizontal arrows and make the vertical arrows have the same functional form, making the grid symmetric.

**7:32** · After all, from feedforward networks we know that this pattern of activation function followed by a linear projection with a set of weights, this fire and project works pretty well.

**7:44** · So, let's have a separate set of recurrent weights so that the temporal propagation of state is a fire and project transform copy.

**7:53** · In other words, M has the exact same form as the feedforward transformation from one layer to the next.

**8:00** · And then the actual state is just a sum of those two similar looking terms, just with different set of connection matrices. One for how each neuron in a layer connects to neurons in the next layer, and one for how each neuron connects to its neighbors in that same layer, communicating information across time.

**8:20** · And this is exactly what the researchers tried initially in the '80s. This is the vanilla formulation of recurrent neural networks you'd normally find.

**8:30** · However, there is a major problem in practice.

**8:33** · While vanilla RNNs can track what happened a few time steps ago, their memory horizon is severely limited. They are fundamentally incapable of learning long-range dependencies.

**8:45** · And the reason is baked into the very operation we chose for the echo.

**8:50** · Think about what happens to a piece of information as it travels along the vertical axis.

**8:55** · At every single time step, it gets passed through sigma and then multiplied by W rec.

**9:01** · That is, it gets processed, squished, rotated, and projected.

**9:05** · After 10 time steps, the original signal has been processed 10 times. After 100 100 times.

**9:12** · It's like a game of telephone, but at every step, the message isn't whispered, it's paraphrased, condensed, and reinterpreted.

**9:21** · In hindsight, this shouldn't surprise us. Remember, we chose this memory function by copying it from the feedforward pathway.

**9:29** · And the feedforward pathway was designed to throw information away.

**9:33** · That is its entire purpose.

**9:35** · To map all possible images of cats in different poses, lighting, and on different backgrounds onto the same output. In other words, compression, not preservation.

**9:47** · We took the operation that was deliberately built for progressively discarding variation and asked it to do the exact opposite, to preserve information faithfully across time. So, no wonder that it fails.

**10:01** · And here lies the key insight. To store information reliably across time, we need a pathway where information can flow without being repeatedly processed, carried forwards largely intact with only selective controlled modifications.

**10:17** · In fact, the deep learning community already stumbled upon this exact insight, but in a different context.

**10:23** · As vision networks grew, people realized that even across layers, it's useful to preserve some information unchanged.

**10:32** · The breakthrough was the residual connection, a direct shortcut that lets a signal bypass the transformation of a layer entirely.

**10:41** · This was the revolution that made very deep networks trainable.

**10:45** · Our vanilla RNNs are missing exactly this across time.

**10:50** · Instead of a handful of processing stages horizontally, we have hundreds of thousands of time steps vertically, and we need important information to ripple through unchanged.

**11:00** · We need a residual connection-like mechanism, but for memory.

### Sponsor: Shortform

**11:04** · If you're curious about the people and stories behind the ideas we discussed, from the key breakthroughs in neural network design to the hardware that made it all possible, I'd highly recommend checking out the book The Thinking Machine on Shortform, who are kindly sponsoring today's video.

**11:21** · Shortform offers in-depth book guides that go way beyond simple summaries.

**11:26** · They unpack the key ideas and weave in related insights from other books and research papers, which really helps to see the big picture.

**11:35** · Their library covers a huge range of topics, from science and technology to psychology, with new guides being published every week. And subscribers actually get to vote on what books to cover next.

**11:47** · They also have a browser extension that can generate similar in-depth guides for articles and YouTube videos you encounter online.

**11:56** · If you want to supercharge your reading, follow the link down in the video description to sign up for a free trial and 20% off the annual membership.

### Leaky Integration

**12:05** · So, what is the simplest echo that preserves information instead of processing it?

**12:11** · What if instead of the fire and project operation, the echo is just keep a fraction alpha of your previous state?

**12:19** · This alpha is a single knob that controls memory.

**12:23** · Let's explore what happens as we turn it.

**12:26** · When alpha equals zero, the echo vanishes. Each time step is independent.

**12:31** · We're back to the amnesic feedforward network we started with. When alpha equals one, the state is fully preserved and new input is simply added on top.

**12:41** · This looks exactly like the residual connection we were looking for. So, problem solved? Well, not quite.

**12:48** · When the residual connections are used across layers, the number of layers is fixed, say 10 or 50. The network is always the same depth. Every training example passes through the same number of additions, and the network learns to calibrate its own outputs accordingly.

**13:05** · The architecture is built around a fixed, known amount of accumulation.

**13:10** · Sequences don't have this luxury. A video might be a handful of frames, or it might be the extended version of Lord of the Rings, half a million frames.

**13:20** · With alpha equals one, the new state equals the previous state plus new input.

**13:26** · Unroll it, and the state is a running sum of every input ever received. After 10,000 time steps, it's a pile of 10,000 contributions stacked on top of each other.

**13:38** · Nothing is discarded, but nothing is findable, either.

**13:42** · It's like never throwing away a single piece of mail. Technically, nothing is lost, but your desk is buried, and every single letter is equally inaccessible.

**13:52** · This is not memory. This is hoarding.

**13:55** · So, the right value must be somewhere in between.

**13:58** · Let's set alpha to be between zero and one, and now something interesting happens.

**14:03** · Recent inputs remain strong, but older inputs fade exponentially.

**14:09** · This is a leaky bucket. Information pours in and slowly drains out. And here is the satisfying twist. This turns out to be nature's favorite memory mechanism.

**14:19** · A neuron's membrane voltage works exactly this way.

**14:23** · Charge builds up from synaptic inputs and leaks away through ion channels in the membrane.

**14:29** · In fact, one of the most widely used models in computational neuroscience, the leaky integrate-and-fire neuron, is precisely this equation.

**14:39** · But this leaky bucket has a problem of its own.

### Gated Memory

**14:43** · Right now, alpha is a single number shared by every neuron and fixed for all time points.

**14:49** · But say you're watching a movie. A character's name, mentioned once in the opening scene, needs to persist for the entire film.

**14:57** · The exact framing of each shot is useful right now, but irrelevant a moment later.

**15:03** · A single alpha cannot do both. High enough to retain the name, and it also retains a growing pile of stale visual details. Low enough to flush the details, and the name fades, too.

**15:15** · What we need is for every neuron to have its own retention rate, one that changes at every time step depending on the context.

**15:24** · The fix is to replace the scalar alpha with a vector f of t, one gate per neuron, recomputed at each time step.

**15:32** · Notice that the memory function m now takes the input as an argument, too, because what you should forget depends on what is arriving.

**15:41** · But where does this forget gate come from?

**15:44** · It needs to look at both what the layer is currently holding and what's coming in, and produce a number between zero and one for each neuron.

**15:53** · We already have a machine that does this, a small neural network with a sigmoid activation.

**16:00** · When the neuron's gate is close to one, its state passes almost untouched. When it's close to zero, the old value is erased, making room for new information.

**16:10** · On our 2D grid, the vertical arrows now carry adaptive valves, each controlled by a small side circuit that reads both the echo from above and the input from the left, and decides how much of the echo to let through.

**16:26** · This gated retention is the core mechanism at the heart of a family of architectures known as gated RNNs.

**16:33** · In practice, these architectures often involve additional refinements.

**16:38** · The two most prominent members of this family are GRUs and LSTMs.

**16:43** · They differ in their specific plumbing.

**16:45** · The GRU pairs our forget gate with a complementary update gate, while the LSTM separates what a neuron knows from what it's shouting to its neighbors by maintaining two state vectors instead of one.

**17:00** · But these are engineering choices. The core mechanism in both is the one we just derived, a learned adaptive valve on the echo.

**17:09** · And that single idea, selective context-dependent forgetting, is what finally gave recurrent networks the ability to learn long-range dependencies.

### Putting it together

**17:19** · Looking back, here is what we have done.

**17:21** · We started with a static memoryless network and asked how to give it a sense of time.

**17:27** · The answer was a single additional term, the echo, and the entire zoo of recurrent architectures turned out to be different answers to one question, what should the memory function be?

**17:39** · A symmetric copy of the feedforward path gives you a vanilla RNN, elegant but forgetful.

**17:46** · A fixed scalar decay gives you a leaky integrator, nature's default, but a learned context-dependent gate gives you the GRUs and LSTM networks that can finally choose what to remember and what to forget.

**18:01** · But we've only scratched the surface. We haven't talked about how these networks are actually trained. How do they propagate errors backwards in time? We haven't explored what recurrent networks can teach us about the brain or the fascinating field of reservoir computing, where we leverage the complexity of recurrence without training it at all.

**18:22** · But those are stories for future videos.

**18:25** · If you enjoyed the video, share it with your friends, subscribe to the channel if you haven't already, and press like button. Stay tuned for more computational neuroscience and machine learning topics coming up.