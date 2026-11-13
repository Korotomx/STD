![](https://www.youtube.com/watch?v=eNtADpJ2EC4)

👉Get Rust training from Let’s Get Rusty: https://letsgetrusty.com/start-with-jorge  
  
In this video we talk about Instruction Set Architectures and Micro Architectures.  
  
Join CodeCrafters and learn by creating your own Claude Code, Redis, Git, Http server, Interpreter, Grep... in your favorite programming language:  
https://app.codecrafters.io/join?via=jdvillal  
  
Sponsor my work on Github: https://github.com/jdvillal  
  
Questions and business inquires:  
contact.coredumped@gmail.com  
  
Follow me on twitter:  
https://twittter.com/coredumpped  
  
Join our discord server:  
https://discord.gg/szyQsXfzuv

## Transcript

**0:00** · This video was sponsored by Let's Get Rusty.

**0:02** · There's this word in tech that appears everywhere.

**0:04** · architecture architecture architecture architecture architecture architecture They can refer to slightly different things depending on the context in which we use it. So, today, we are going to explore what exactly the term computer architecture refers to. Hi friends. My name is George, and this is Core Dumped. At this point, we should know that computers are built from transistors that, when combined, create logic gates.

**0:31** · And these logic gates can be combined to create circuits that do all sort of things, like adding numbers and performing all kind of math operations, to circuits that select between multiple options, like a binary decoder does. Modern computers, however, are described as general-purpose because they can perform many different tasks based on instructions. These special-purpose circuits can therefore be combined to create much more complex behavior.

**0:57** · A clear example of this is the ALU, short for arithmetic logic unit. For those who are new to the channel, an ALU is a component that receives two binary data inputs and an op code input. The op code tells the internal circuitry which operation to perform on the two input values.

**1:14** · The result of that operation is then placed on the data output. This component is more general-purpose because it no longer performs only one task. Instead, it can perform one of several possible operations depending on the instruction it receives.

**1:29** · But, how does it do that?

**1:31** · Well, some time ago, I showed you a very simple way to build an ALU. But, let's not get too far ahead of ourselves. Before talking about circuits, I want you to think about something. In software, when we are presented with a problem to solve, there are usually multiple ways to solve it using different algorithms. We have a term for each of these solutions, an implementation. A single problem can be solved correctly using multiple implementations.

**1:58** · The same is true in the hardware world. A hardware component can also be implemented in different ways. Even a component as fundamental as an XOR gate, for instance, can be built using different configurations of more basic logic gates. This is the basic idea behind architectures. In a very vague and simplified sense, an architecture is to hardware design what an algorithm is to software design.

**2:22** · Now, let's continue talking about the ALU. How could we implement a component like this? How could we even tell a circuit to perform one operation instead of another?

**2:32** · Well, as I just mentioned, there can be multiple ways to do it. The simplest approach is this. Because the ALU must be able to perform multiple operations, we can use multiple purpose-specific components to perform each operation. The op code input can then be passed to an internal binary decoder, which selects the desired operation.

**2:53** · Each operation is encoded as a specific sequence of bits. In this example, only two bits. 0 0 means addition. 0 1 means subtraction. 1 0 means bitwise AND. 1 1 means bitwise OR. If we allow the two data inputs to reach all the internal components, we can use the outputs of the binary decoder to select which component's result is allowed to reach the ALU's data output.

**3:18** · And just like that, we have our ALU, a component that receives two data inputs and an op code that tells it which operation should be performed on those inputs and placed on the output. Now, you might be wondering why I'm talking about this. Well, it's because there are different ways to build this component.

**3:36** · You can think of the op code as an instruction that tells the ALU which specific action to perform. However, the exact bit pattern used to encode each operation can vary. It could be organized like this, but it could also be organized like this, or like this, and so on. It all depends on the design of the component. In this design, for instance, the order of the internal components matters.

**4:00** · When placed side by side, both components are ALUs. Technically speaking, however, they use different ALU architectures. In this example, an instruction sent to one of the ALUs causes the other ALU to produce a completely different result, even though the data inputs are identical. We can describe this as incompatibility. Traditionally, it is said that electronic computers understand ones and zeros.

**4:26** · However, the same sequence of ones and zeros can mean one thing to one computer, and something entirely different to another. And the differences go beyond how individual operations are encoded. One ALU, for example, might support operations that another does not. Another ALU might work with wider data inputs, allowing it to perform operations on larger numbers.

**4:51** · The point I'm trying to make is that, even though the term ALU has a specific definition, that definition does not specify every detail of the component. There is still a great deal of ambiguity that must be resolved when designing one, as these examples demonstrate. This ambiguity is inherited as we move through higher levels of abstraction, all the way up to the CPU.

**5:13** · A CPU also has a specific definition, but that definition leaves out many details about exactly how the processor operates. As a result, two designs can be completely different while still satisfying the definition of a CPU. However, a different architecture does not necessarily mean incompatible hardware. Two architectures can be different internally, while still exhibiting the same behavior.

**5:38** · But before talking about that, if you follow this channel, I'm pretty sure you love low-level systems. And that's exactly why I'm excited to say that this video is sponsored by Let's Get Rusty. Big companies are betting big on Rust for building critical systems. Google, Microsoft, even the Linux kernel itself are now integrating Rust into their core systems. That's not hype.

**5:59** · That's happening.

**6:00** · And if you're thinking about leveling up your Rust skills, whether for personal growth or to land a job working on real systems, Let's Get Rusty is the go-to place for Rust training. Created by a fellow YouTuber and one of the most beloved names in the Rust online community, Let's Get Rusty has helped thousands of developers, myself included by the way, master the language and break into systems programming.

**6:23** · They're running a new cohort very soon, and since spots are limited, now's a great time to check it out. Visit letsgetrusty.com/startwithgeorge or just click the link in the pinned comment below. And now, back with the video. As I was saying, a different architecture does not necessarily mean incompatible hardware. Think about what our first ALU design is doing. It performs all the operations at the same time and then selects the result of the requested operation.

**6:52** · But not every ALU has to work that way. Instead of routing the outputs of the internal components, we could design the ALU to route the inputs. The input values would then reach only the internal component responsible for the requested operation. Another possible implementation would allow the data inputs to reach all the internal components while using the op code and binary decoder to activate only the component responsible for the requested operation.

**7:24** · If we place these three designs side by side, we can clearly see that they are completely different internally, but they produce the same results from the same inputs. They are different architectures, but they are compatible. This is where the term architecture becomes somewhat ambiguous. Saying that one piece of hardware uses a different architecture from another does not necessarily mean that they are incompatible, but it does not necessarily mean that they are compatible either.

**7:52** · To avoid this confusion, we can use two more specific terms: instruction set architecture and microarchitecture. When we talk about computer architecture as a whole, we are usually referring to the combination of both. The instruction set architecture, or ISA, defines rules such as which instructions are available, which combinations of ones and zeros encode those instructions, and how those instructions must be formatted.

**8:18** · More generally, it defines every programmer-visible contract between software and the processor. And by the way, there are so many of these details that I couldn't cover even half of them in a single video, as shown here. Now, I know that all this information might be a little difficult to process.

**8:37** · But from a high-level perspective, the main effect of an instruction set architecture is this: For a given task, the ISA defines which individual, simpler operations are available to construct a solution, and it also defines how those instructions must be translated and formatted in binary so that a CPU can receive, understand, and execute them.

**9:00** · An instruction set architecture is therefore an abstract specification. It defines the rules that software must follow to interact with a processor. The microarchitecture, on the other hand, specifies how a particular instruction set architecture is implemented. It includes all the internal circuitry and organization required to make the processor behave as specified by the ISA.

**9:22** · In the same way that a software problem can have multiple implementations using different algorithms, a single instruction set architecture can be implemented through multiple microarchitectures.

**9:33** · Remember our ALU example?

**9:35** · Multiple ALUs can be designed in completely different ways while still producing the same result from the same set of inputs. The externally visible rules, what inputs exist, what each op code means, and what output should be produced, are comparable to the instruction set architecture. The different internal designs used to follow those rules are comparable to microarchitectures.

**9:59** · These are all different microarchitectures, but they implement the same instruction set architecture because they all follow the same externally visible rules. As a result, a program compiled for a particular instruction set architecture can run on any compatible processor microarchitecture that correctly implements that ISA. When it comes to real-world instruction set architectures, some of the most widely used today are x86-64, ARM, and RISC-V.

**10:29** · On the x86-64 side, we have dozens of different microarchitectures, some designed by AMD, and others by Intel. If you look through this list, I'm pretty sure you'll recognize at least one of them. If we examine a few examples, we'll notice that their internal designs, circuitry, and implementations can be very different from one another. However, because they all implement the same instruction set architecture, a program compiled for x86-64 can generally run on all of them.

**11:00** · But that same program will not run natively on a processor that implements a different ISA, such as Apple's M-series processors, which use the ARM instruction set architecture. To run the program on those processors, it must be compiled for the ARM instruction set architecture instead. Once that is done, the same principle applies. The software can run on different microarchitectures that correctly implement that ISA.

**11:27** · So, when you see companies announcing new CPUs based on a new architecture in the news or during a keynote, what they usually mean is a new microarchitecture built to implement an existing instruction set architecture. Creating an entirely new instruction set architecture every year would be extremely inconvenient for them because existing software would not automatically be compatible with it. Developers would need to recompile, adapt, or potentially rewrite their programs to support the new ISA.

**11:56** · And if you don't know how much of a nightmare that would be, just ask anyone who worked in the computer industry during the 1980s. Here's a clip from Prime that perfectly illustrates what I mean.

**12:05** · The operating system would have to be rewritten for each computer architecture. By the way, this is one of the big reasons why people don't realize how difficult it was to port programs back then. The memory, the word length, was different on like every computer and they were insane numbers. Like, some numbers just had 72-bit word lengths.

**12:18** · Like, what the hell? Or some were like just 32, some were like 36. They're not even powers of two, they're just 36 bits of word length. And you're like, what is What is happening here?

**12:25** · This also helps explain why, unlike in the broader IT world, the word architecture in programming almost always refers to the instruction set architecture. It directly influences how programs must be written, compiled, and executed. And let's wrap things up for now. If you'd like to support the channel, don't forget to check the sponsors in the description below.

**12:45** · Or consider subscribing. And if you liked this video or learned something new, please hit the like button. It's free and that would help me a lot. See you in the next one.