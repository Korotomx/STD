---
title: "MIT 6.S191: AI for Science"
source: "https://www.youtube.com/watch?v=rZACoZD8AG8"
author:
  - "[[Alexander Amini]]"
published: 2026-05-18
created: 2026-10-30
description: "MIT Introduction to Deep Learning 6.S191: Lecture 8AI for ScienceLecturer: Chris Bishop (Technical Fellow)Microsoft** New 2026 Edition **For all lectures, slides, and lab materials: http://intr"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=rZACoZD8AG8)

MIT Introduction to Deep Learning 6.S191: Lecture 8  
AI for Science  
Lecturer: Chris Bishop (Technical Fellow)  
Microsoft  
  
\*\* New 2026 Edition \*\*  
  
For all lectures, slides, and lab materials: http://introtodeeplearning.com​​  
  
Subscribe to stay up to date with new deep learning lectures at MIT, or follow us @MITDeepLearning on Twitter and Instagram to stay fully-connected!!

## Transcript

### Introduction and context

**0:12** · It is my great pleasure and honor to introduce our first guest speaker for introduction to deep learning 2026. And he's a very special one.

**0:22** · Chris Bishop is a technical fellow at Microsoft. This is the highest technical distinction that one can receive and the founding um the founder of Microsoft Research AI for Science, which is a global organization overseeing a portfolio of work at the intersection of machine learning, AI, and the natural sciences.

**0:42** · And Chris comes from a background deep in physics and machine learning and has brought that to a really unique perspective in terms of thinking about bringing AI and deep learning to real-world problems in these domains.

**0:56** · And he's also done great contributions for the community in terms of deep learning education, publishing seminal books on machine learning and deep learning in particular. So, please join me in giving him a big round of applause and welcome to Dr. Chris Bishop.

**1:21** · No.

**1:23** · Thank you, Alida.

**1:24** · I'd like to begin by asking you to think for a moment about what you consider to be the greatest scientific discovery ever made. Now, I haven't given you a metric, so this is really a matter of opinion. I'm sure there will be many different opinions here, but in my view, the most extraordinary thing that science has ever uncovered is the fact that our world is described by mathematics.

**1:49** · It's not obvious, right? Making marks on a piece of paper allows you to predict the future. It's extraordinary. And it's not just mathematics, it's simple mathematics. Even if you're not familiar with these equations, um I think you'll agree these are very simple equations. And yet these equations, perhaps a little bit of relativity uh sprinkled on top, really describes everything that we experience in our everyday lives. Everything we can experience without using specialist equipment.

**2:16** · So, that's extraordinary. But these aren't just rough and ready models of the world. They have extraordinary precision. So, the electron, which is one of the building blocks of matter, is like a little magnet. And we can use theory to calculate the strength of that magnet. And this is what we come up with. And the error bars at at the end are because we neglect some terms in a kind of series expansion.

**2:39** · And then we can go and do an experiment and we can measure uh that magnetic moment. And this is the number we come up with. Again, there are some experimental error bars. And you'll see that these agree to 13 significant figures. That's just staggering precision. So, we live in a world that's described by mathematics where areas like the Earth's atmosphere, materials, new drugs, we have the equations that describe them very precisely.

**3:13** · So, we ought to be able to just design a new drug on a computer and we're done. But we can't. And the reason is rather ironic. Those equations are very simple to write down, but solving them turns out to be extremely difficult.

**3:27** · So, you could say that the underlying physical laws necessary for the mathematical theory of a large part of physics and the whole of chemistry, and that includes biochemistry, which is just complex chemistry of course, are thus completely known. The difficulty is only that the exact application of these laws uh leads to equations much too complicated to be soluble. Now, those aren't my words. Those were said by the theoretical physicist Paul Dirac nearly 100 years ago.

**3:55** · So, in this fascinating but very frustrating situation that for a century now we have these beautiful simple equations that describe the world with exquisite precision. And yet we're frustrated cuz we can't solve them in order to go and tackle lots of real-world applications.

**4:13** · So, the question is how can we best use the knowledge of those equations in order to accelerate scientific discovery?

**4:20** · And to address that I just want to step back for a moment and think about the scientific discovery process itself. So, we have a scientist and of course today a scientist would generally be a team of scientists or a team of people from many different disciplines working together, but let's just call that a scientist. The scientist formulate hypotheses.

**4:41** · Uh those hypotheses are then tested against experiment. This is really the foundation of the scientific method gathering evidence from the real world.

**4:49** · So, those observations from the experiment can then inform the scientist and the scientist can go and modify their hypotheses. For example, if you're looking for a drug, you're searching the vast space of potential drug molecules, you dream up by whatever mechanism some candidates, you synthesize them in the laboratory, test them against proteins, some of them bind, some of them don't, and you use that information to refine your list of drug candidates.

**5:14** · So, that fundamental iterative loop of science of course has been with us for a long time. Um and it doesn't operate in isolation. The scientist of course talks to other scientists, reads the literature. So, this is part of a whole scientific ecosystem.

**5:29** · One development that I think is very important happened really in the 1960s with the development of digital computers. And for the first time this really allowed us to bring those equations in into play because we can solve the equations in for other than toy problems by using digital computation. It's very, very expensive typically to do that, but it gives us a different kind of oracle.

**5:50** · Since we know that the equations are accurate, instead of doing an experiment, we can do a simulation. Of course, there are pros and cons to experiment and simulation, and they're sort of complementary, but it adds another pathway, if you like, to the scientific process. Now, we're in the early dawn, I suppose, of a of a remarkable AI revolution, which is touching many things, including, of course, scientific discovery.

**6:14** · And so, AI is really impacting every aspect of this process, from the formulation of hypotheses, how could we design a million molecules rather than half a dozen, something that a human alone couldn't do.

**6:27** · Um, analyzing data from experiments and helping us interpret them, um, driving automated wet labs. There are uh several companies, I think, in even in the Boston area, looking at um automated wet labs and how can AI help to automate and accelerate the experimental process. And of course, helping the scientist in their uh day-to-day work.

**6:47** · Addressing that vast literature of millions of papers, a human being can't read the papers, but a an AI can read the papers, and and and that's incredibly valuable. Um, and so, AI is impacting this whole process. This is enormously exciting and enormously important. And Microsoft is very involved in this. We have a platform called the Discovery Platform, which is an agentic AI platform built on Frontier LLMs that's helping to accelerate this whole discovery process.

**7:12** · That's not what I'm going to talk about today. I'm going to talk about a different and very exciting way of using those fundamental equations to accelerate scientific discovery, and that's what we'll call uh AI emulator. So, the AI emulator provides a third pathway, a third kind of oracle, to use within this scientific discovery loop.

**7:35** · And I'm so excited about this that um 4 years ago, I made a pitch to the chief technology officer of Microsoft to sort of give up my lab director job and form a new team called AI for Science. And this is this is what we're focused on in the AI for Science team. It is very complimentary to what we're doing in Microsoft with the Discovery platform.

**7:54** · So, to understand what an emulator is, I want to again just step back a minute and look at a very important theorem at the heart of machine learning, which has this wonderful name of the no free lunch theorem. So, the no free lunch theorem essentially says you cannot learn purely from data.

**8:15** · You can only learn from data in the context of some kind of assumption, um sometimes called prior knowledge, sometimes called inductive bias. It's phrased in different ways from different perspectives, but it all comes down to the same thing. You make a prediction by combining data with some assumptions.

**8:33** · Now, you're all familiar with large language models. And in large language models, we use data, lots of data. It's very, very data-intensive. In fact, we're using data at an unprecedented scale. And it's that scale to extremely large internet-scale data sets that's allowed large language models to achieve their extraordinary capabilities.

**8:53** · The assumptions, the inductive bias, are fairly lightweight. We have uh attention. The prediction for the next token depends um to greater or lesser degrees on previous tokens, and that weighting is itself data-dependent. So, that's the attention mechanism that's at the heart of the transformer, but it's very, very general, very lightweight inductive bias.

**9:12** · In science, we're in the opposite regime. In science, data is scarce, it's expensive. It can take a student a year to figure out the 3D structure of one protein. That's one data point. Um and yet we have, uniquely in science, this very rich inductive bias. We know the equations that describe the world. So, how can we combine that expensive data with this rich inductive bias.

**9:40** · So, let me just click down a level and say a little bit more about what I mean by inductive bias. So, we have these equations. If you're not familiar, this is Schrödinger's equation. We won't be doing any maths in the talk, don't worry. But this equation describes the properties of matter at the atomic level. Um describes uh it's an equation for an object called psi, the wave function.

**10:01** · I'll say a little bit more about the wave function uh a little bit later. But a relatively simple equation. That certainly should be part of our inductive bias. That's part of our prior knowledge. We have other things, too. Um invariants and equivariants. So, here's a molecule. If I calculate and measure the molecule as just in a vacuum, it's not interacting with anything, and it has some energy, I can calculate the energy.

**10:25** · If I rotate the molecule, the energy must be unchanged because space is isotropic. So, that's called an invariant property. Now, if the molecule is represented by the coordinates of the nuclei of the atoms in three dimensions, when it's rotated, all those numbers will change in some complicated-looking way.

**10:43** · That's what we feed into the neural net, but the output must remain the same. So, that would be called invariance. If the molecule has a magnetic moment, then when the molecule rotates, the magnetic moment must rotate with the molecule, and that's called equivariance. So, again, that's a property that we want our solution to satisfy.

**11:02** · In fact, that idea is really the foundation for a whole subfield of of deep learning called geometrical deep learning, very beautiful and fascinating field. Um we have conservation laws. Energy is conserved, mass is conserved, momentum, electric charge, and so on. These are exact conservation laws of the physical world, and again, we'd like to respect those.

**11:20** · So, how are we going to exploit these inductive biases?

**11:26** · We could um and a lot of work has gone into this, we could design specialist neural network architectures that sort of bake them in automatically. Instead of having a general feed forward, you know, multi-layer perceptron, if we structure the network in in a particular way, we can make sure that no matter what the values of the parameters and the weights, it will always satisfy some conservation property or some equivalence property. That's a very beautiful and very elegant again subfield. Um the equations, we can always write an equation as something equals zero.

**11:57** · So, the something squared can be a term in the loss function. We want to drive that term to zero, then the equation is satisfied. And there are lots and lots of other ideas that people have explored.

**12:10** · They work.

**12:11** · They can be quite good. But there's a little catch. And the catch is something called this become known as the bitter lesson. This is a blog written yes, 2019 by Rich Sutton. So, Rich is one of the pioneers of reinforcement learning.

**12:27** · Um if you haven't read this, every single one of you by the end of today should take 5 minutes and go and read this blog. And if you work in the field, I suggest that on the first day of every month you go and reread this blog. It could save you a lot of pain.

**12:43** · What it essentially says is that over the years many people have improved the performance of machine learning systems by baking in additional prior knowledge. But they've always lost out to somebody else who simply had more data. Because the speed of computers has been growing exponentially, we've been able to train bigger models with more data. And so, provided you have provided data is available, an important caveat, you can just use more compute to scale the model.

**13:13** · And the more data eventually overtakes the clever prior knowledge. So, here's the dilemma. We have these beautiful equations. We're not going to just ignore them.

**13:24** · And yet we know that data eventually wins out. So, how can we reconcile these?

### Deep learning emulators

**13:33** · So, the way we reconcile them is this concept of a deep learning emulator. And you can think of this as a sort of shift of mindset. So, let's write down his equation.

**13:42** · And we would think of Schrödinger's equation as an equation that we could solve, let's say to predict the property of a molecule. We're trying to design a new drug. We want molecules to have certain properties. In principle, we can solve Schrödinger's equation, but it's very, very expensive. But the cost of solving Schrödinger's equation grows exponentially with the number of electrons. So, we're really forced to look at relatively small systems.

**14:05** · But instead of solving Schrödinger's equation afresh every time we want to solve a new problem, let's do something different. Let's ahead of time solve Schrödinger's equation lots and lots of times for lots of different systems, say a whole bunch of different molecules. That'll be expensive, but we kind of do that once. And that generates a data set, and we'll use that as a training data set for machine learning.

**14:29** · Then in the second phase, we will train a neural network trained on that synthetic data. That again will be computationally expensive, nothing like the cost of training a frontier LLM because remember the data is expensive to calculate. The data sets are not huge, so the models are not huge. So, this this second stage is not too expensive, but it but it still costs something.

**14:51** · And once we've trained that neural network, we'll call that a deep learning emulator. And we can think of that as an emulator of the software that would solve the equation directly. So, think about solving the equation directly, we'll call that a simulator. It produces data, and the data is used to train the emulator.

**15:12** · And if we get this right, once the emulator is trained, it should produce the same answer that the simulator would produce, but it will be very, very much faster. Because solving those differential equations is an iterative numerical process that is computationally very intensive. Whereas once the network is trained, it's a feedforward network and it can just it's just a function and we can calculate that extremely quickly.

**15:38** · Now if we're going to do this once off, it wouldn't make sense. But if we're going to use that emulator thousands or millions of times, we're going to amortize the cost of all the data generation and the training um over those over those future uses.

**15:53** · So, what are the benefits of using emulators?

**15:58** · So remember we're training on synthetic data generated by simulation. And so by simulation, I mean you know, conventional software, the kind that's been around for many decades that iteratively or directly solves the differential equations, slow and expensive. But we use that synthetic data to train the emulator. Now that data is very richly labeled.

**16:20** · You know, it's very easy to collect images, but if you want to use those images for training a neural net, you may have to label them and labeling them is the expensive part. Having somebody going through and saying this is a bicycle, this is a tree and so on. The data here is automatically labeled. Whatever quantity we want to predict, once we've solved Schrodinger's equation and got the wave function, we can just calculate the properties, let's say of the molecule in in in that case.

**16:42** · So the data is perfectly labeled. We don't have to worry about personally identifiable information. You know, if you deal with a medical domain and you're dealing with um patients' medical records, you obviously have to extremely careful about privacy and consent and so on. Here we're just dealing with the solution of differential equations.

**17:01** · And this is a very important point. The quantity of data is is unlimited in a practical sense. We can always generate more data as long as we've got the compute to do so. So people who training frontier LLMs complain that they run out of data. Well, we'll never run out of data here because we can always generate more data and the scale and complexity of the problems we're trying to solve is such that more data will always be useful.

**17:28** · It will always improve the results and the predictions we can obtain because we're attacking such a vast problem. So, from a practical point of view, we can always generate more data just by using compute. And the other thing to appreciate is the compute that I'm talking about here in data generation is not the extremely expensive, huge clusters of highly interconnected top-end GPUs used to train frontier models. This could be single GPUs. It can even be CPUs.

**17:57** · We can also exploit underutilized compute. In a company like Microsoft, we have huge computer resources all around the globe. Some of those computer resources get more intensively used in a region during the daytime than at the nighttime. There's always some underutilized compute.

**18:12** · And because the process of generating these training points is uh massively parallel, um we can launch many, many jobs. And maybe some of them get preempted because a customer come comes along and obviously they get priority for the compute. But we can very efficiently soak up a lot of underutilized or unutilized compute in the in the training process.

**18:33** · And then most important of all, really the fundamental reason we're doing this is that trained emulator is much faster than the simulator. And typically, I would say more than three orders of magnitude.

**18:45** · Usually the first thing you try, you're about a few thousand times faster than the original simulator. Of course, it depends a lot on the on the actual application domain, but that's a good rule of thumb. You're looking at factors of several thousand acceleration and sometimes much more. And that that's huge. I mean, a factor of a thousand is is quite transformational. Now, I'll show you a concrete example a a little bit later.

### Applications in science

**19:09** · Uh in fact, I'll show you I'll show it to you now, in fact. Um so, let me make this concrete by giving you a sort of an everyday example, which is weather forecasting. So, if you go to your phone and you look up the weather forecast, it'll tell you what the weather in Boston is going to be for the next few days.

**19:23** · Where does that come from?

**19:25** · That forecast comes from something called numerical weather prediction. So, numerical weather prediction involves solving some relatively simple-looking differential equations, a bit like Schrödinger's equation, they're partial differential equations of a number of variables. They're not the fundamental equations of physics, but they're easily derived from the fundamental equations of physics and they describe the way um, air flows and the effects of Coriolis force and pressure gradients and and condensation in the air and so on.

**19:57** · We need a supercomputer because we have to solve this with quite fine time steps in order to get good accuracy. We need quite a uh, a rich spatial grid in in three dimensions. Um, and we have to solve it quickly cuz we have to solve it faster than the actual weather. We have to get a forecast, you have to overtake the reality. So, you have to solve it quite a bit faster than the real weather is evolving um, in order to get a forecast.

**20:20** · So, national centers around the world, um, you know, the UK Met Office or NOAA in the United States will have supercomputers and they run these launch these big jobs every 6 hours or or or whatever, um, initialized with the current state of the weather and then trying frantically to predict accurately what the weather's going to do a few days ahead.

**20:40** · Now, this is a great target for an emulator because for several decades now, many organizations around the world have been using supercomputers to simulate the Earth's atmosphere. So, there's a huge amount of simulated data available. Uh, much much of which is in the public domain and readily available and can be used to train emulators.

**20:57** · And quite a number of teams have trained emulators from various different uh, groups in industry and academia and it's been very successful. Um, I'll focus a little bit on on what we've done. We've done um, something a little bit different.

**21:09** · We've taken it a step further and rather than just produce an emulator of a particular simulator, we've trained an emulator on very diverse data. So, data from many different simulators, different length scales, different different resolutions, different time scales, and so on. In order to force the model to learn more fundamentally about the dynamics of the Earth system, the atmosphere and the oceans.

**21:33** · Now, we call it a foundation model because what we can then do is fine-tune it for particular applications. And and there are quite a few of these, but I'll just mention one of them. So, one problem is to predict the flow of pollutants, particularly nitrogen oxides, through the atmosphere.

**21:50** · Now, data sensors for pollution are relatively sparse compared to weather sensors. I mean, this building probably has a little weather station on the roof. There are weather sensors all over the place. So, data for weather is extremely dense and very very rich.

**22:04** · Data for pollution is much sparser. If we just use the pollution data to predict pollution flows, we don't get particularly good results. But instead, if we use an Earth system model, a foundation model, trained on that weather forecasting data as a foundation model and then fine-tune it, we get much more accurate predictions. So, this is the state of the art for predicting pollution flow through the atmosphere.

**22:26** · So, that's one example one practical example of an emulator. And because it's so much faster than running simulators, it's several thousand times faster. So, for example, we can produce the UK 8-day weather forecast in 1 minute on a single A100 GPU. It's very disruptive. It's not just Oh, it's faster, that's good. It's It's actually very disruptive. It changes the way we think about weather forecasting. So, it's it's it's very exciting.

**22:57** · But it's not just weather. This is very very broadly applicable. For the rest of this talk, I'm going to focus on the molecular scale, predicting the properties of um molecules and materials. That's the focus of of my team. This is still a vast space.

**23:11** · There's still a lot to do here. Um many many different uh um applications. You can see some of them listed here. But but let's just dive into this and see how we apply this in the at the molecular scale. Let me just give you another example here. This is a model we built called MatGen. Um I think you'll all have come across diffusion models for generating images where you um take images and you add noise and then you train a neural net to denoise the image successively. This is the same idea, but now for crystals. So, crystals specified by saying um what is the the unit cell?

**23:45** · Right? It's a periodic system, so you specify the coordinates of the the axes of the unit cell, the types of atoms and how many there are and where they're located. Um and so we can take known stable crystal structures, add noise, um and then learn to denoise them. So, this is the a little video of the denoising process.

### Challenges in quantum chemistry

**24:04** · So, starting from random and then it's denoising to choose the types of atoms, the uh geometry of the unit cell, and the locations of the atoms within the unit cell.

**24:16** · Um and when it's finished, what we should have here is a stable configuration of atoms, a stable material. So, if you just put atoms down at random and sort of let go, they'd all rearrange themselves. They wouldn't like it. Um what what we're trying to do with MatGen is to generate new stable crystal structures.

**24:32** · Now, we don't just want to generate crystals at random, of course. What we want to do is generate crystals that have desired interesting properties. So, MatGen is a conditional diffusion model. So, it can take as input properties of materials, electronic properties, magnetic properties, uh mechanical properties, and so on. And so, what you see here are examples of different crystals generated by MatGen having different uh desired um physical characteristics.

**25:02** · So, if you think about the molecular probably the problem of designing new materials and new molecules as a search problem, the space that we're searching is vast. If we just consider small organic molecules, the number this this space has been quite well characterized. The number of small organic molecules with drug-like characteristics is about 10 to the power of 60.

**25:27** · It's like the number of atoms in the solar system. It's a colossal space. So, finding a new drug is searching that vast space to find a molecule with a long laundry list of desired properties.

**25:38** · So, a huge search problem. Materials probably an even bigger space. When you went to proteins, it's a colossal combinatoric space. The space that we're trying to search in finding new molecules and materials is is truly vast. Something like Maturation, it doesn't immediately in one shot produce the miracle material, but what it does do is help you focus on a region of chemical space where you're more likely to find examples which have the desired properties.

**26:03** · So, if you then subsequently generate those potential materials and run a screening using an emulator that calculates the property. We have an emulator called Matta Sim that does that. That emulator, that screening is thousands of times faster. We've got another huge acceleration by looking at good candidates to start with. You're not generating crystals at random and then testing the service of magnet.

**26:27** · You're saying, "Please generate magnets that have relatively low rare earth metal content or whatever it might be." And then you're looking in the right region of chemical space. So, that's really a further acceleration. So, I'll talk a bit more. That's crystals. Let me talk about molecules.

**26:43** · Um before I do that again, let's just you know, click down a level and say, "What is it we're really trying to do when we when we're looking for a new material or new molecule?"

**26:52** · What we're really doing is solving a fundamental trade-off between three different things. So, these things are accuracy, speed, and generality. You can have any two of those, no problem at all, but you need all three. And they trade off against each other. And so, it's finding interesting regions of that space with better trade-offs than we have before. That's sort of fundamentally what my my team does in effect. Um speed here is computation, it's cost.

**27:25** · Generality, because we want it to generalize, we obviously don't want to make predictions of things we already know about. We want to generalize at least to other um parts of chemical space that are broadly similar. Um and we need accuracy that's sufficient to be of practical value. Let me say a little bit more about accuracy. There's a particular threshold of accuracy that we strive for. It's called chemical accuracy.

**27:48** · Um its value is about a kilocalorie per mole. And it, roughly speaking, chemical accuracy is the accuracy you would need to achieve such that your computational model is as good as experiment. If you can get to chemical accuracy, you're kind of in the ballpark where you could imagine doing far fewer laboratory experiments and now doing computational experiments instead. But it's a very high bar to achieve.

**28:12** · And one way to see that is is with an analogy. Um if you were asked to weigh the captain of the boat, you could do that by weighing the boat with the captain, weighing the boat without the captain, and then subtracting them. Now, mathematically, that's exact.

**28:26** · But in practice, the boat um is is much heavier than the captain. And so, to get a reasonably accurate value for the weight of the captain, you would have to measure the boat plus captain with very high precision.

**28:38** · And it's like that in chemistry. The energy changes involved in a chemical reaction are of course uh everything, they're crucial, and yet they're a small fraction of the total energy of the system. And so, when you calculate the energy of the system, you need very high precision. That's chemical accuracy. So, chemical accuracy is a very high bar. Um that's that makes this a very tough problem.

**29:01** · So, I'm going to take a moment now to um I'm going to tell this is a fairly intense course. So, we're going to be fairly intense for the next few minutes. And I'm going to take you on a little journey of a story which I think is absolutely fascinating. And it's one of the the core projects of my team.

**29:14** · Um we can look a little bit further at Schrödinger's equation, what it means to solve it, and why it's hard. So, Schrödinger's equation is equation for this object called the wave function denoted psi. And it's a function that is in a very high-dimensional space. So, so X1 to Xn are the coordinates in space of the electrons, the electron positions in space. And psi is a function jointly across that entire space.

**29:38** · So, it's um it's a very large space. Here's the caffeine molecule. It has um two dozen atoms. It has about 100 electrons. So, for the caffeine molecule, psi is a function of a 300-dimensional space. Now, uh for the experts in the audience, this following will be a slight oversimplification. It's not incorrect. It's just a simplification. Um but imagine we're going to try and solve that by dividing that 300-dimensional space up into a grid.

**30:08** · Now, if it's in one dimension, you know, we could divide it into 1,000 points. That's no problem. In two dimensions, the grid would be 1,000 by 1,000. So, that's a million points. Three dimensions, it would be a billion and so on. The number of grid points is growing exponentially with the dimensionality of the space. And so it is when we solve Schrödinger's equation, the cost grows exponentially with the number of electrons.

**30:28** · And that means that this tiny molecule, which is a lot smaller than many drug molecules, is already out of reach. Nobody's been able to calculate directly the properties of the caffeine molecule by direct solution of Schrödinger's equation. And we want to solve much, much bigger systems than this. So, that's the challenge that really Dirac was referring to nearly 100 years ago. But, something really interesting happened in 1965.

**30:53** · Walter Kohn discovered that instead of calculating the wave function, we actually don't need the wave function at all. Instead, we can calculate a much simpler quantity, which is just the electron density. The density of electron density of electronic charge over space. So, it's a function just of three dimensions.

**31:13** · And whereas it's exponentially costly to compute the wave function, and the wave function tells us everything we need to know, um instead, we can compute the density, which only has cubic cost in the number of electrons, and all things we want to know, we can calculate them from the electron density without ever needing the wave function.

**31:35** · Now, we're all familiar in computer science with problems that are exponentially or combinatorically hard, and then we have some approximation scheme that allows us to solve it in in realistic time, and often those work very well in practice, um even though potentially they're approximate. What's extraordinary here is that this is exact.

**31:53** · This is an exact transformation of an exponential problem into a cubic problem, and that's so extraordinary that in 1998, Walter Kohn was given the Nobel Prize in Chemistry for the discovery of density functional theory.

**32:05** · And density functional theory has become one of the most highly cited um topics in the whole of science. Here, you can see the exponential growth in the number of papers as digital computers became available, and it became more and more practical to use density functional theory. You can see this has become hugely important in many different fields. Roughly speaking, this is the only practical method we have of solving Schrödinger's equation for for realistic systems.

**32:32** · And if you look at um national supercomputers, this is from a national supercomputer center in the US and you look at their scientific simulation workloads, you find quite often that density functional theory accounts for maybe a third of the entire workload of that supercomputer when it comes to scientific simulation. So, it's hugely um hugely important in practice and and quite an extraordinary result.

**32:56** · Um and again, if you like a little little cartoon analogy to help you remember this after the talk, here's one way to think about density functional theory. So, it's an analogy um in three-dimensional space, we have this plastic molecular model. So, think of that as like the wave function, it's something very complicated, it's living in this three-dimensional space. Normally, we would calculate the wave function and then calculate everything from the wave function.

**33:16** · But instead, we don't need to work with the wave function, we can work with this lower dimensional projection, like a kind of shadow in this two-dimensional space. And that's what density functional theory is. And by the way, this isn't AI-generated, somebody did actually plug these bits of plastic together and took a photograph, so congratulations to them.

**33:35** · Now, this point, you're probably, you know, you're probably a bit suspicious, right? I mean, we've got this exponentially hard problem, and somebody comes along and says, "No, I can solve it all in cubic time." Uh and it's the exact. It sort of sounds a bit too good to be true. And in a way, it is a little too good to be true. There is a catch.

**33:52** · So, Kohn wrote down a set of equations, um the Kohn-Sham equations, which are iterative equations. Instead of solving Schrödinger's equation, you solve the Kohn-Sham equations. Um they have cubic cost, cubic in the number of electrons, but they contain a term. It's a really small term called the exchange-correlation functional. It's a contribution to the energy, but it's critical because as you as we saw, we have to have very high precision. So, although it's a relatively small term, it's essential that we get this uh exchange-correlation functional term um to be accurate.

**34:23** · And Kohn showed that it's universal. In other words, there is a single exchange-correlation functional that describes the whole of molecular space, all of the crystals, proteins, molecules, everything. One universal exchange correlation functional. He wasn't, however, able to write down an explicit analytical form. So, it's sort of a mystery. It's It's an unknown. So, what do people do in practice? Well, over the last 60 years, people have invented handcrafted, um, approximations to the exchange correlation functional.

**34:57** · Today, there are about 800 of these um, in use. It's sometimes called the zoo. Um, sometimes called Jacob's ladder because they can be arranged in a kind of sequence. Some Some cheap ones that are not very accurate or some very expensive ones that are quite accurate.

**35:12** · And so, there's a trade-off there. Um, these functionals, these, uh, handcrafted functionals, uh, each of them applies to some particular sub-domain. Some apply to molecules, some to crystals, some are good for metals, um, and and and so on. Um, what's missing is this this universal exchange correlation functional.

**35:29** · And there's nice paper written in, uh, 2002 in Science called In Pursuit of the Divine Functional, which is really sort of lamenting the fact that the whole field had had gone down this rabbit hole of these handcrafted approximate functionals and lost sight of the fact that exchange that, uh, that, uh, density functional theory is an exact theory. And there is this universal functional. We should get back to the heart of this of trying to find that universal functional.

**35:56** · So, the DFT zoo, then, is this gives us this trade-off. This is a graph. On the vertical axis is, um, the error, um, in kilocalories per mole. So, we want to get down into that blue region, that chemical accuracy or better. That That's what we're aiming for.

### The DFT zoo and machine learning

**36:15** · And here are a bunch of different, um, handcrafted functionals. You can see on the left we have some that have cubic scaling. So, they sit within the overall cubic framework of density functional theory. That's wonderful. They're very affordable, but the accuracy is terrible. Much, much worse than chemical accuracy. Um we we then have functionals that are much more expensive like into the power five. They're starting to approach chemical accuracy, but they're getting very, very expensive.

**36:40** · And yet we know from Kohn and his Nobel Prize that there's a single universal functional that applies across the whole of chemical space that should give us chemical accuracy or better um with cubic scaling.

### Developing the Skala functional

**36:54** · So that leads to the idea of could we not learn the exchange-correlation functional using machine learning?

**37:01** · Yeah, kind of an obvious idea really and quite a few people have looked at this over the years. And sometimes the results have been quite good in terms of accuracy, but the most accurate of these are very slow. And so nobody has been able to produce an exchange-correlation machine learning exchange-correlation functional that is both accurate and fast.

**37:24** · So we've had a project in the AI for Science team that's been going since the beginning, so more than three years now. We've we've been doing it kind of under the radar, but we sort of went public a few months ago. Um we've been doing um a couple of things that are different. So let me just explain. Um so we've produced a machine learned exchange-correlation functional called Scala. So Scala is from the Italian for for ladder.

**37:48** · Um and the idea is we've got electron density. So within the Kohn-Sham equations at any given time we're updating electron density. We need energy. Um there's a bunch of these big terms. We can easily calculate those, but that's not accurate enough. We need this final term, the exchange-correlation term. And that's where machine learning comes in.

**38:08** · And so um essentially the electron density is represented by a point cloud. Maybe have a million points. And one of the challenges here is that the dependence of the energy is non-local on that uh on that electron density. And uh even pairwise interactions on a in a million times a million would be out of hand.

**38:27** · So, what we do is we have um, a lower dimensional representation centered on the atoms. We use message passing from the point clouds to the atom centers, then between the atom centers, then back out to the to the electron point cloud and that gives us a scalable model that's also able to learn exchange correlation functional accurately. So, that's one innovation. The other is just you guessed it, more data.

**38:50** · So, we spent a lot of time over the last 3 years solving Schrodinger's equation using standard quantum chemistry methods to produce highly accurate training data for the exchange correlation functional. For an order of magnitude than the totality of all the public data previously available.

### Results and generalization

**39:06** · Um, and so here's just a glimpse at some of the results. So, this is a graph. The vertical axis is just the the total energy of the of the molecule and the horizontal axis is another standard benchmark looking at more general chemistry properties.

**39:21** · Um, some of which go beyond what we actually use in in training and you can see that Scala achieves chemical accuracy on the fundamental question of um, atomization energy and is comparable with um, other functionals having uh, quartic scaling for for more general chemistry. The the limitation here of Scala as existed today is it applies only to molecules, not yet to materials and it deals only with the so-called main group elements. So, we don't yet cover transition metals.

**39:53** · But, it's very interesting that even even in its current form, it generalizes quite well. Um, perhaps to do with the fact that we're learning a universal functional. So, perhaps that generalization is is less surprising. But, we're just uh, tremendously excited about this. We're really hitting hard on a a 50-year-old grand challenge at the at the heart of physics.

### Protein dynamics and biology

**40:14** · So, I'm going to um, finish by just asking a question, well, how far can we push this? We said direct solution of Schrodinger's equation for the caffeine molecule, that's out of reach. Biology looks crazy big and complicated. Can we push this to biology? So, let's just see how far we can go.

**40:29** · So, here's the whole of biology in one slide, in case you are wondering how biology works. So, we start with sequence, DNA sequence leads to an RNA sequence, and then that is then specifies the amino acid sequence, which is the protein. That protein then folds up into a three-dimensional structure, and then that structure, along with the dynamics of the proteins, determines function. So, sequence determines structure, determines function.

**40:58** · Um Sequence, DNA sequence and protein sequence, those were actually two Nobel prizes, both awarded to Fred Sanger in Cambridge, at the the other Cambridge, sorry about that. It's um And and of course Yeah, before last now, I guess, we had Nobel prizes in in protein structure, the three-dimensional structure. What we really care about is the function, and the function of proteins is not about static structure, it's about dynamics.

**41:27** · Proteins open and close, they dock with other proteins, they interact with molecules and so on. So, the last big piece of this puzzle is to do with the dynamics of how proteins change shape and how they interact. So, we can we can, again, in principle, we know all the equations, and so we can just compute. And and this field is called molecular dynamics. So, here's a molecule.

**41:50** · Each each of those balls, of course, represents one of the atoms, the the positions of the nuclei. So, we can represent each each atom in terms of its position and its velocity at each instant of time. And all we have to do is solve Newton's second law of motion. So, we can treat them classically, and we just update the positions of each atom step by step through time, just following Newton's second law of motion.

**42:14** · Um the challenge here is that the force term, which is the gradient of the energy, that energy comes from quantum physics. So, that's determined by the electrons. And so, there are two massive challenges here. One is that at each step of that integration, in principle, we should go back and solve Schrödinger's equation, which we've already seen is extremely hard. There's another challenge here as well. It's called the curse of sequentiality.

**42:37** · So, this shows you on a kind of log scale the different time scales involved. Right on the on the left-hand side there, we have the the fundamental vibrations and rotations of the atoms. That's happening on a femtosecond time scale. So, if we're to integrate Newton's laws for the atoms, we have to follow those vibrations. That means we have to have a time step, which is of the order of a femtosecond.

**43:01** · But the interesting stuff happens on much larger time scales. Things like protein folding happening on time scales of milliseconds, for example. So, there's our integration step. And the problem is we need something between 10 to the 6 or even 10 to the 15 sequential steps to follow that dynamics. Remember, at each step, we should compute the forces using uh quantum physics.

**43:23** · Um and you may think, "Well, that's okay. Computers are getting exponentially faster. We just have to wait a few weeks." But the problem is this is intrinsically sequential. And computers haven't got faster for many years now. If anything, they're getting slightly slower. What they are doing is becoming massively parallel. So, the speed up we see in computers through GPUs is through massive parallelism. The clock speeds haven't really changed for quite a while.

**43:44** · So, this is intrinsically sequential. So, it's sort of a double whammy. It's a really, really hard problem.

### Future directions and Q&A

**43:50** · Um so, can we use emulation to to get a handle on this? And this is something from um a couple of years ago now, where what we do is um we we make several carefully controlled approximations. The first is to take we take a protein, very large molecule, and we look at individual chunks of that protein. So, we don't model individual atoms, we group them together into chunks, and then we compute the forces between the chunks. We use density functional theory for that.

**44:19** · So, the bigger the chunks, the fewer of the things we have to integrate. But, as the chunks get bigger, so the force the relationship of the forces becomes more complicated, and there's a trade-off.

**44:29** · So, the chunks are as big as we can make them while still producing an accurate machine-learned emulator. So, we we can compute forces for lots of different configurations using DFT, train an emulator, and that emulator is now very fast. So, now we can run molecular dynamics on these chunks of protein, but at each stage, the update is just a call to a trained emulator. So, extremely fast, no iteration needed. So, here we can do um molecular dynamics simulation for proteins up to about 10,000 atoms.

**44:59** · So, that's an extraordinary advance. Look back to that caffeine molecule and we were able to before, and here we are doing molecular dynamics at uh the scale of a 10,000-atom protein.

**45:08** · So, again, you can see that sort of hierarchical process of using data from one level to train the emulator at the next level. We can take that even a step further and use data from molecular dynamics simulations combined with experimental data to avoid having to do the dynamics altogether and actually directly sample from the equilibrium distribution. So, this is work that was published in Science um a few months ago, and we are super happy that the editors chose to put it on the front cover, which is which is always nice.

**45:38** · So, yes, we can by using the power of emulators, we can extend this even to the scale of uh of biological molecules. Um I'm going to finish, I'll have to admit, with a just a shameless plug for a book.

**45:51** · This is a course on deep learning, so I'd like you all to at least uh be aware of this book. It's called Deep Learning, um published at the end of 2003. Um it's free uh freely available online. If you go to bishopbook.com, um you can get a see a get a high resolution um uh digital version of the book. Um but also if like me you quite like old-fashioned physical books, um then you might be interested to know that this is actually produced using a traditional binding technique called stitch signatures. So most books today are produced by gluing the pages in on edge.

**46:23** · They don't fold flat and if you open them more than two or three times the pages fall out. This is good old-fashioned stitch signatures. You print it on a sheet of paper and fold it fold it fold it trim it and then stitch it in with cord. So the book lays flat and it should should last for many many years.

**46:38** · Um also delighted I just heard that for the second year running this is Springer Nature's best-selling book. So Springer Nature and all their subsidiary publishing houses publish together something like 13,000 new titles every year. And for 2 years running since this was published it's the overall number one best-selling book. So really really delighted by that. Uh but actually the thing that I'm most proud of about this book is it was written with my son Hugh who's also in the machine learning field.

**47:05** · So thank you all for your attention. I think we have a little bit of time. I'm happy to take questions. Thank you.

**47:18** · Thank you so much.

**47:21** · Thank you so much Chris for a fantastic and inspiring talk. So we're going to take questions. We're going to run the mic so that we ensure that we capture that. So please if you have a question raise your hand and we'll go from there.

**47:39** · So previously you said that uh biology is mostly sequence to structure to function. And you talked a lot about the work you've been doing with protein structure and molecule structure in general. I was wondering uh what kind of work have you been doing in molecule and protein function especially?

**47:57** · So the main project that we work on is called a biomolecular emulator. And so, the first the first major output of that was the science paper that that you you saw the front cover of. And the focus there is really addressing that that third part. So, we view sequence, you know, we have this high-throughput sequencing that allows us to sequence your entire DNA for $1,000 or whatever it is. Quite incredible technology. Uh structure is sort of large static structure is sort of largely solved. What's unsolved is this is the dynamics of protein. So, our focus is on the protein dynamics.

**48:26** · And we're really doing something quite ambitious cuz we're trying to solve what's sometimes called the sampling problem. It's not specific to proteins.

**48:36** · It's it's just very generic of how you sample from these complex distributions efficiently. And the goal is to So, one way you can always do this is just to run molecular dynamics forever. And, you know, in the infinite time limit, it will sample the different Think of a an energy well with, you know, an energy surface with different wells. Um you you will sample them all in the correct proportion, and that's essentially what you want to know. Um that's that's an infinitely expensive route.

**49:00** · We want to be able to avoid the dynamics altogether and just know what are the what are the sort of the energy wells, and what are the relative proportions of the time the protein will spend in those in those wells. So, what those those wells correspond to is say a protein which um I don't know, maybe the spike protein on the on the um um COVID-19 virus has an open conformation, a closed conformation. But, if you if you look at down a microscope, all the atoms are wiggling and jiggling, and it's kind of wiggling and jiggling in this sort of closed thing.

**49:29** · And then, boing it brings it springs open, and it will wiggle and jiggle for a long time in this open configuration. When it springs from open to closed, it's crossed one of those energy barriers. If those barriers are high, that's a very rare event. So, in molecular dynamics, you simulate for very very very very long time, and then you'd see one of these rare events.

**49:46** · That's kind of crazy, right? And as you get as you get high energy barriers, it becomes extremely inefficient. So, we want to find ways to just, you know, given the protein, just tell me just sample directly from that equilibrium distribution. And what we saw in that in that first paper is the sort of the first light dawn, really, that yes, this looks like it could be possible. What we've done so far is one protein in vacuum.

**50:07** · What we really need to do now is proteins interacting with each other, proteins in the presence of water, then it becomes, you know, we get closer to clinical and biological relevance then, but very exciting that we can do one protein in isolation. So, yeah.

**50:21** · Thanks.

**50:22** · Uh thanks for a great talk. Um I was wondering for emulators, um we still have to know free lunch theorem.

**50:29** · And um how can you expect, or not even guarantee, but expect that these emulators will apply um I guess for problems like solving like a 10-electron Schrödinger's equation, how can an emulator that's only seen like a two or three electron systems be expected to solve these more complex like completely intractable problems that are you can't solve using a single even a single time.

**50:55** · And then I guess the second question is um for uh systems like weather, which was one of your examples, where I imagine data is already um you already have a ton of data, and why would you want to use emulators as opposed to just training it on the data?

**51:13** · Right.

**51:13** · So, I think there are several at it was at least three questions in there. So, let me make several comments that help to address the question. The first one about the no free lunch theorem. Um you know, we you could have a a model that that encodes, as I mentioned, let's say rotational equivariance. You bake it into the structure of the model. Much simpler thing to do is just replicate the data.

**51:33** · So, if you know this molecule has a certain energy, um it's trivial to just rotate the molecule in the computer. We just it's just simple 3D geometry. And so, let's have a hundred copies of that molecule in different orientations, all labeled with the same energy. So, 100 times as much data. That's called data augmentation. Really, really simple to do. And eventually, ultimately, that And that means you can use much more general architectures and you learn the invariants. The downside is you don't learn it exactly. If you bake it in, it's exactly true. But really, what the bitter lesson is telling us at the end of the day, just more data and just learn these things.

**52:02** · Um I think the second question you were asking there is about It was a great question, actually, very insightful question. So, let me just explain how I interpret that question, then. So, we spent a ton of time and energy and effort over 3 years generating high-accuracy quantum chemistry data in order to learn the exchange-correlation functional in order that we can then run DFT, cuz DFT is still an iterative process. It still has cubic scaling.

**52:23** · It's not a a a single pass. The functional is a is a is a fast emulator that is embedded in this.

**52:28** · And then we might run DFT to generate training data to learn a thing that we call a force field predict the properties of molecules very fast. Why do we bother? Why don't we just take that expensive quantum chemistry data, forget DFT, just train a a fast emulator? That emulator would be certainly be very fast. What we miss out is a effectively a way in which we've incorporated a lot of inductive bias.

**52:47** · That machinery of density functional theory has a lot of physics baked into it. In particular, I glossed over all of this and I did apologize to the experts earlier, but that wave function, for instance, has to be antisymmetric. Um that that that's why atoms exist. It's Pauli's exclusion principle. The The electrons can't occupy the same state.

**53:05** · They have to fill up different different shells. That's really critical physics to understanding the atom. In principle, if we could if we could generate vast amounts of quantum chemistry data with high accuracy very cheaply, yeah, maybe we could learn that stuff in the in the in a sort of data augmentation sense, but but in reality, the the power of DFT is that it encodes so much physics. You saw, I think, in the diagram there, there's a lot of physics that we can calculate fairly straightforwardly. It's the exchange-correlation term that's that's hard.

**53:32** · But but if but but you But to throw away all of that physics is to give up an enormous amount. So, so So, So why we want to use DFT in that hierarchy. Um and then I think, you know, part of it too, you're you're asking about generalization, partly is it embeds a lot of physics, but also and we're working out good ways to test this, but there's this beautiful fact that the exchange correlation functional is universal. So in that in that zoo, somebody invents one that's good at crystals, somebody invents one that's good at, you know, molecules or whatever.

**54:03** · Um but here because it's because we're learning a universal functional, we hope that should help with generalization. And we do see remarkable generalization to chemistry problems outside the domain in which it was tested, and we hypothesize that in part that may be due be due to the universality of the exchange correlation functional. So I hope that in a roundabout way addressed your questions, but very insightful question. Thank you.

**54:27** · Amazing. We'll take two more questions.

**54:30** · Uh so I have a question related to the no free lunch theorem. It seems to me that here you have no free lunch and no free winning in a way because you I mean, typically in the no free lunch is kind of a bias variance straight off with the capacity of the model or the models that you're considering, but here you're simulating data.

**54:53** · So you're essentially adding kind of a second uh distribution over which you are uh uh having a no free algorithm, right?

**55:04** · And a second bias variance straight off. So uh I'm curious about how that plays out in your like fundamental trilemma if like simulating data is better than actually gathering real world data, and if at some point you measure somehow like the seem to real uh bound between the simulated data and the real world uh data essentially. This happens a lot in reinforcement learning you in robotics, for example.

**55:33** · Uh so I I um I mean, it's two comes, I guess. One is that the experimental data will always be fundamental. At the end of the day, we're not changing the scientific method. It doesn't matter how brilliant our theory is or how many nature papers we get. If it doesn't agree with experiment, we're wrong and we have to re-rethink. So, there's one role for experiment. But also um what I've talked about today is what I think is a is a is a very substantial advance by many orders of magnitude in our ability to do computational science. But that doesn't mean we're going to just throw away experiments and and and and so on.

**56:01** · So, uh so the second role of experimental data is is is um very much to complement um the computational data. In fact, in in the case of the um uh protein dynamics that I showed you, the science paper, that's actually trained on a lot of molecular dynamics data, but then actually fine-tuned using experimental data from x-ray diffraction measurements. So, there's clearly a role there. So, in terms of the, you know, the no free dinner theorem, I like the that's a good good good terminology there.

**56:29** · Um but you know, it it it's still a fundamental cornerstone of machine learning that we have to combine um prior knowledge with um with data. And this is a very interesting way I think of extracting that prior knowledge in the form of data. So, it really I think takes on board the the idea of the bitter lesson and the fact that scaling the data is always a very powerful thing to do. And by generating the data from the equations, then then we're effectively incorporating that prior knowledge.

**56:57** · So, I don't I'm not sure if that really addressed your your question there, but um uh Amazing. Final question.

**57:04** · Hi. Um so, about um cellular and genetic therapeutics, um understanding of protein-protein interaction between um therapeutic transgenes and host cellular machinery, it is extremely crucial to have an idea about this before we dive into in vivo studies for any kind of therapeutics. So, do you think um AI-driven biomolecular dynamics could help the predicting of off-target interactions or any kind of stability issues before one moves towards the in vivo studies of that particular therapeutic.

**57:45** · Yeah, that's such a great question. And of course the answer is I certainly hope so. I think we've been surprised at how far I mean we're just starting from Schrodinger's equation. And the idea that we push this all the way to, you know, the dynamics of a single protein seems remarkable. What you're talking about with, you know, in vivo studies and the whole machinery of the cell, this is orders and orders of magnitude more complex still. So, I don't imagine that in my lifetime or, you know, the next 100 years, I don't know, that we're going to have a a first principle simulation of an entire human cell that's derived entirely from Schrodinger's equation, for example.

**58:16** · That that seems crazily out of reach.

**58:19** · But I do think we're approaching the point where things like off-target interactions of drugs could be informed through molecular dynamics simulations accelerated through the through the use of emulators. I'm not really very exciting because of course in in drug discovery a lot of drugs fail at the clinical stage through toxicity, through through off-target interactions. The more we can do at the discovery phase to eliminate those, the faster drug discovery can be and the cheaper drug discovery can be.

**58:44** · So, I am hopeful that these techniques will have real clinical relevance within the next two or three years or so. But but but we'll we'll we'll we'll not it for a long time, I think, be simulating anything as complex as a human cell using using these techniques. But nevertheless, I think they can make a very practical contribution.

**59:04** · Amazing. One more big round of applause for Chris Bishop.