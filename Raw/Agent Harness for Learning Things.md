![](https://www.youtube.com/watch?v=nfTDljFG2g0)

This is my full system for learning things with AI.  
Repo: https://github.com/amosblomqvist/learnharness  
  
0:00 Intro  
0:17 Goal  
1:18 Understanding  
2:44 Optimization prerequisite  
4:07 Teaching  
6:03 Practice  
7:35 Model of your understanding  
8:36 Agent harness for learning  
9:16 Demo start  
10:52 Teaching session  
12:21 Probing phase  
15:22 Teaching phase  
17:58 Practice session  
20:08 Other things  
22:00 Close

## Transcript

### Intro

**0:00** · This is my system for learning with AI.

**0:02** · What began as a simple teaching loop has now developed into a full system for not just learning new things, but also for strengthening existing understanding.

**0:11** · So, same video structure as always, ideas and design first and then a live demo. So, a lot of things have changed since last time, but the goal has remained the same. So, we want to optimize learning. And what that means is maximizing understanding built per unit of mental effort spent. And specifically what we want is real, strong, and usable understanding.

### Goal

**0:34** · So, we can't just focus on minimizing mental effort, cuz clearly struggle with the material is where the most learning happens. I think the biggest risk in learning with AI is not hallucinations or errors by the LLM. It is accidentally skipping the struggle part and creating sort of an illusion of learning.

**0:59** · So, we don't want to outsource the thinking, but what we can do is allocate our mental effort better so that a maximal share of it goes into direct interaction with the material, the stuff that most contributes to learning, and a minimal share to everything else. All right, next. I think it's helpful to make a distinction between understanding something and being able to use it.

### Understanding

**1:25** · Let's say we're in a lecture. We're following along. We understand everything and we really do gain new understanding. But later, faced with a problem, the relevant ideas might never come to mind. And this doesn't mean that the understanding we built was somehow fake or something. It's just that following the reasoning and recognizing when and how to use it are two different things.

**1:49** · And what I'm referring to here is recall in a very general sense. So, the right things, facts, connections, some problem-solving moves, whatever, but the right things come into mind in the right situations. And recall operates on cues.

**2:07** · So, features of a situation that bring a certain piece of understanding to mind.

**2:13** · A newly learned idea only really comes reliably to mind in the context that it was taught in. So, it starts off with a very narrow and weak set of cues. And then the job of practice is to broaden and strengthen that set of cues. All right, so two processes, at least for the purposes of this video and this system, we'll think of learning as two processes. Teaching installs understanding and practice solidifies it and makes it more usable.

**2:42** · Now, if you want to optimize these processes, we have to realize that whatever optimal really means here, it's clearly defined relative to the learner's understanding. A step in teaching is redundant only relative to what you already understand and unreachable only relative to what you don't. There's no optimal lesson or optimal practice problem in the abstract. So, before anything can be optimized, the system needs a detailed picture of your understanding.

### Optimization prerequisite

**3:13** · So, not just what you understand, but how. Your mental models, your particular ways of reasoning about the thing with all of its nuances and subtleties, you know?

**3:28** · And the right or wrong answer alone isn't able to provide that. I mean, two people can have the same wrong answer for very different reasons. The agent needs the data about the process and not just the final answer. And this is what the thinking fields in the system are for. So, almost every interaction has a field where you talk or type your raw thinking into basically just unfiltered messy stream of consciousness. Whatever comes to mind really.

**3:57** · This gives the agents continuous data about your understanding. All right, so two processes. Let's go through both. First, the teaching, how we install new understanding. The core ideas and the general process from the previous version have remained the same. So, three phases. One, probe. Quick multiple choice questions that kind of binary search your edge on everything that the lesson will depend on. Two, plan.

### Teaching

**4:24** · The agent reasons out the minimal dependency tree from what you already know to what you want to understand. And then three, teach. The goal level of understanding is something feeling obviously true. So, given a detailed picture of what you already hold as obviously true, the agent can simply walk down the path one reasoning step at a time in a way that each intermediate step lands as obviously true.

**4:53** · And it's going to be very easy cuz it's just one reasoning step. And we just repeat that process until the goal itself is one of them and also lands as obviously true. And this is the shape of each individual step.

**5:09** · First, you predict, then the agent teaches, and then it finally checks your understanding. So, before anything is explained, you get to predict the next move. And this not only gives the agents more context and even more of your thinking before the teaching, but it also serves as a very valuable learning opportunity. You try to reason out the next step yourself. So, two questions per step and this leads to a very Socratic back and forth.

**5:34** · Errors and confusions will surface immediately and can get fixed before anything is built on top. The agent also has access to four kinds of sub-agents. A researcher for fact-checking, a PDF reader for reading PDFs efficiently, an SVG maker for creating diagrams, visuals, and other kinds of graphics, and a demo builder for creating interactive demos.

**6:02** · Right, next, practice. And again, the goal here is to broaden and strengthen the set of cues that bring a piece of understanding to mind. So, the agent's job is not framed as making practice problems. It's posing demands for the learner to recall the right things given some set of cues. The practice session is basically just a stream of problems that adapt.

### Practice

**6:27** · And as you work through the problems, your thinking is going to give the agent very detailed evidence of where the difficulties actually are and what you struggle with. And then in the next problems, it can target and strengthen what needs to be strengthened. Really, the goal is recall that succeeds with effort. Enough difficulty that you have to work and struggle, but not so much that you can't make progress. There are two main ways that the difficulty can adapt.

**6:58** · One, by changing how many ideas a problem combines. And two, how familiar the cues are. The thinking is submitted in chunks, and the agent is able to infer whether you actually solved it without you having to write down a final solution by hand. And this also means that when you really struggle, it's going to be able to give you the minimal hints, sort of little nudges toward the right directions.

**7:26** · So, when you don't know something, it'll lead you to discovering the solution yourself instead of just giving it to you. All right, so so far we have established the two main systems. And now, the component that connects the two. All right, so we need some kind of persistent record that accumulates as you learn things.

### Model of your understanding

**7:47** · The format should be one that can hold a very large body of understanding in few enough tokens that is still useful for context sharing cuz that's the main use case here. But, we also want to preserve as much precision as possible, especially when it comes to how ideas connect. So, the model that I've decided to go with and what I've found to have a nice balance of both compression and precision is propositions and reasoning chains.

**8:21** · These are extracted from the teaching sessions into one persistent structure of what you've been taught and it can be rendered as a very nice graph. Ideas and the reasoning that connects them growing out as you learn. All right, so what we get is an agent harness for learning things. Quick tangent, what are agent harnesses? Well, basically everything around an LLM that lets it explore and act in some external system. For a coding agent harness, the system is a computer.

### Agent harness for learning

**8:53** · For a research harness, the system is the internet. So, for a learning harness then the system is your brain and the agent's job is to build understanding in there. In every other harness, the human is the operator, the one driving the agent. But, here you are the system being acted on. All right, I think this is enough talking. Uh let's see the system in action. All right, we're in the app now and yes, it is a desktop application.

### Demo start

**9:24** · Completely free, open source. You just plug your own keys in and it works. But, anyways, this is the graph. So, we get a very nice overview of all the sessions, the core reasoning chains. Uh yeah, they can also form uh between sessions, like for example here. And then you can see the exact sessions that the node appeared in, and you can navigate to the original message. And apparently we also have a connection from the differential forms session to the gradient descent one.

**9:58** · Yeah, this is the same differential forms session that I did last time. You can import your own notes any kinds of text files into this, which is what I've done here. But anyways, one more thing about the graph before we begin. Here the arrows, the links have a very precise meaning. They indicate the direction of reasoning. For example here, this and this lead to this. So, a cool thing that we can do is make the Y axis the depth of reasoning like this.

**10:33** · So, now we have the bottom level Hold on, let me actually adjust the physics a bit. Yeah, so now we have the bottom level nodes at the bottom, and then the reasoning, the argumentation always goes upwards.

**10:46** · And I I like this way of visualizing the sessions. But anyways, let's begin. All right, so we need a topic for the demo.

### Teaching session

**10:55** · And well, I'm thinking we learn LLMs.

**10:58** · It's going to clearly fit into this, maybe build on top of neural networks, machine learning. That's also something I want to really learn.

**11:07** · Teach me LLMs.

**11:09** · Oh yeah, I'm I'm using this dictation here.

**11:12** · So, if you don't use like WhisperFlow or some other dictation software, then you can just use this.

**11:19** · Yeah, you just need a Deep Gram API key here, which is free.

**11:25** · I want to learn and understand the transformer architecture, heavy math and theory focus.

**11:32** · So yeah, let's begin. It's going to look at the graph.

**11:35** · First question regarding the goal. I want to understand like a full conceptual understanding of what's going on under the hood.

**11:43** · And then the thinking is always going to be sent along with the answers.

**11:48** · Now, it's dispatch day research agent.

**11:50** · That's good. Yeah, it's going to run in the background. Same mechanics as my interactive sub-agents. You can keep asking questions here. And oh, yeah.

**12:00** · Another thing. I've got this new confidence slider here. So, you can assign a confidence level to your answer, which basically just means the probability that you think that your answer is correct. It's going to give really good data. A really easy way to give valuable data to the agents. By anyways, the thinking is still the main channel. But, yeah. First question.

### Probing phase

**12:22** · Okay, let's X and say in one token representation per row.

**12:27** · Soft maxing the rows. Yes. Query key.

**12:31** · And yeah, then we add the mask. And then value vector, right? I mean, a value matrix. What's the difference between these two? Oh, yeah. Columns or rows?

**12:40** · It's It's rows. So, this one I'm fairly confident.

**12:44** · And we got it. And then it's always going to have an explanation here as well. Right, next one. For one query None of these immediately like look familiar. But, this is just like applying the chain rule, right?

**13:00** · Yeah, okay. Let me clean up the name also. LLMs.

**13:04** · All right, next. The attention score uses Q transpose K over Now, in this probing phase, you'll notice that the agent finds my edge the edge of my understanding very quickly. And then it just drills into specifics to get a very detailed picture. For example, last time it spent a long time just locating uh, the edge. But, here cuz it has the graph context, it has found the, like, almost immediately. You'll see that we're at the edge of what I know just from the amount of thinking I put into every question.

**13:36** · Variance one for the division is what I'm thinking.

**13:43** · Okay, that took some work. You can see You can see the thinking. Also, research is finished.

**13:49** · Uh, this up. So, the variance is going to be scaled by the square, so by nine, so 18.

**13:57** · That would make the most sense.

**14:00** · Zoomed in on the uncertainty in the previous question. Anyways, for rotary positional embeddings, I don't know what that is.

**14:10** · But, just working it out from the formula, that makes sense. Transpose rules.

**14:15** · Perfect. And, yeah, the the thinking is very important, cuz this was, like, algebraically very simple, but the answer and the confidence alone, uh, wouldn't be able to tell you that I have no idea what what this is.

**14:31** · Uh, I'm not sure what this is asking.

**14:36** · Uh, I don't know.

**14:39** · Uh, I have no idea, really.

**14:43** · All right, good.

**14:45** · Well, I don't know.

**14:48** · CX plus F and effects, uh, but this is a guess.

**14:55** · The stuff at later positions, J is going to change because we made an edit to R at an earlier position.

**15:03** · Okay, that was wrong.

**15:07** · I'm fairly confident in this answer.

**15:10** · Uh, a lot of thinking again. I'm giving it a ton of thinking at every step. Uh, it's going to get a very very detailed picture. Okay, yeah, it's concluding the assessment now. So, probing is done. All right, agent is planning now. It's dispatching more researchers. That's good. We want to guarantee correct information. Now, it's drawing the dependency graph.

### Teaching phase

**15:33** · All right, there we go. This is what we got. Yeah, looks good. Accept the plan.

**15:38** · And then, teaching is going to begin first with a prediction. And yeah, the map is going to be visible here on the side and it's going to update. So, you you're always going to see where you are. Um but anyways, the same embedding matrix E is used 50. Okay, good. All right, now first step. And there's this thinking while reading field to give the agent even more context cuz it's important that you're going to have like questions while you read. You're going to be thinking about things. I just like to have this on at almost all times.

**16:08** · Two independent matrices, A for input embedding lookup and B for output scoring.

**16:17** · All right, okay.

**16:20** · And then, the verification question.

**16:23** · Consider the scalar analog.

**16:26** · So, 18.

**16:29** · All right, so I'm just going to have a time lapse here.

**16:32** · The teaching style and the methodology is the same as last time. And this is of course something that you can edit. All the system prompts are visible. You can edit and tweak them as you wish. But yeah, methodology is fundamentally the same, but this time it gets even more of your thinking per reasoning step cuz there are two questions and three thinking fields per step. So, the explanations are going to be even more tightly fitted to your specific understanding at every step of the way.

**17:04** · And yeah, this also keeps it very interactive.

**17:09** · No long walls of text. But, this brings up a very important points about why walls of text are bad in this context cuz cuz it's not about long pieces of text being unpleasant to read or something like that. No, it is precisely because we want to feed the agent data about your understanding as continuously as possible. That's the reason why. All right, now we've got an extraction process going on here.

**17:40** · It says distilling the session so far into reasoning chains.

**17:48** · All right, the extraction finished.

**17:49** · Yeah, we got a LLM session tree here.

**17:52** · Let me adjust the physics a bit. Yeah, so this is the session so far. Yeah, and it's making connections to the other ones. All right, now that we've got these in the graph, what we can do is run a practice session on them. So, we just select the reasoning chains from this view, which just shows the raw reasoning chains, ideas and how they connect. But anyways, we select the ones that we want to practice and then we start a practice session. LLM's math focus. Yes.

### Practice session

**18:21** · We get our first problem.

**18:23** · A model receives a token matrix X and computes All right, so immediately the multiplying by the weight matrix and it's not going to I mean that keeps the rows of X independent. They don't influence each other and value acts coordinate-wise. So, everything is just computed in parallel here.

**18:46** · All right, I got to thinking. All right, so it seems like I wasn't being rigorous enough here. So, gave me a little hint so I have that right idea, it seems like, but I need to write down Z4 explicitly in terms of X4. Okay.

**19:03** · Is that sufficient? Let's see. No coordinate expansion needed. Keep W and U as matrices.

**19:10** · Oh, yeah, that's dotted with the eyes column of you.

**19:14** · That's what I've got currently.

**19:17** · All right, so that was one problem. Oh, yeah, and also all the problems are we we can look at the metadata here. This one had three nodes that it was testing.

**19:27** · So, the targets of that problem were these three nodes. And because all of the problems are tagged with their exact propositions, well, I haven't implemented it yet, but that's going to allow us to get some very targeted assessment data. This currently the graph doesn't tell you anything about how well you understand something. It just shows what has been covered. Yeah, the next step is to wire the assessments back into the graph, but that's that's later on. But anyways, next problem.

**19:56** · A layer computes So, we get delta Y is 0 0.

**20:06** · Yeah, I think you get the idea here. All right, so a few more things before we finish. The agents here have got the basic read-only tool sets of read, ls, find, and grep. So, what you can do is well, for teaching sessions, you can obviously you can give them your own sources, your own materials.

### Other things

**20:25** · Um let me do find my abstract algebra lecture notes.

**20:31** · Teach me.

**20:33** · Yeah, I don't know. Not even giving it a path here. Um hopefully finds it.

**20:38** · Uh it's it's hidden away somewhere. Okay, yeah, I found it.

**20:43** · Perfect. And also, for the practice sessions, you don't have to run them based off of the reasoning chains. You can, for example, just give them your own problems. For example, I've got this complex analysis problem here. I'll give it the path, then it's going to load that into the practice session, and we're going to be able to do that problem.

**21:05** · So, yeah, now it's reconstructed the problem here and we're able to work on it in the practice session. Uh cuz I think this is a very comfortable format.

**21:16** · Uh so, yeah. I don't think I've demoed the interactive demos yet. Uh let's go to an older session here, gradient descent session. Make a visual SGD demo.

**21:27** · Yeah, it's going to know how to do this proactively when it fits the session and helps with the teaching. Uh now, I'm just forcing it to make one.

**21:38** · Well, let's see what it comes up with.

**21:40** · All right, we got a flashbang. Um and this is why I have this switch over here so that you can invert the colors.

**21:49** · Um All right, we got a demo.

**21:53** · Okay, yeah, we can set the starting point, learning rate. Anyway, I think you get the idea. Okay, so that's the system as of now. Uh cuz this is Uh this is really only the beginning. I think I've got the I think I've got the basic ideas, the general shapes down. So, now the experimentation can really begin. So, I'm very excited to hear your thoughts, your ideas, what works, what doesn't, you know.

### Close

**22:26** · Whatever comes to mind, really.

**22:29** · But anyways, I guess that's it. I'll have all the links in the description.

**22:33** · So, yeah. Uh thanks for watching. I'll see you in the next one.

关联：[[Artificial_Intelligence/Unlimited/主页|Unlimited]]
