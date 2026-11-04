![](https://www.youtube.com/watch?v=mmns33BsBcY)

Learn more about Quantization here → https://ibm.biz/~NdqpU881V  
  
Huge AI models come with huge memory requirements.Grace Ableidinger explains how quantization compresses LLMs using lower-precision formats like INT8 and INT4. Learn how model size, GPU memory, speed, and accuracy trade off during AI inference.  
  
00:00 – Understand What Quantization Does  
00:23 – See Why LLMs Need Quantization  
00:51 – Connect AI Parameters to Memory Requirements  
01:31 – Calculate the Memory Cost of a 70B LLM  
02:13 – See How Quantization Reduces Precision  
02:53 – Follow Quantization Layer by Layer  
04:21 – Compare FP16, FP8, INT8 & INT4  
05:34 – Balance Memory Savings with Model Accuracy  
06:33 – Compare PTQ vs Quantization-Aware Training  
07:17 – Choose the Right Quantization Tradeoff  
  
AI news moves fast. Sign up for a monthly newsletter for AI updates from IBM → https://ibm.biz/~SLKUNTFaQ  
  
AI was used in the creation of the transcript and metadata for this video.  
  
#llm #aimodels #aiinference #machinelearning #aiengineering  
  
\---------------------------------------------------------------------------------------------------------  
Find us on YouTube:  
🔵 IBM Technology: https://www.youtube.com/@IBMTechnology  
🔵 IBM: https://www.youtube.com/@IBM  
🔵 IBM Developer: https://youtube.com/@IBMDeveloperAdvocates

## Transcript

### Understand What Quantization Does

**0:00** · Quantization is everywhere from digital communication to signal processing to the edge devices that you use every day.

**0:09** · In our modern digital world, quantization is key.

**0:14** · Quantization is the process of taking numerical information and storing it at a lower precision in order to save space or computation.

### See Why LLMs Need Quantization

**0:23** · Most of you may have heard the term in the context of AI, specifically around quantizing LLMs or large language models.

**0:32** · Today, we're going to take a deep dive into LLM compression via quantization.

**0:37** · Quantization is one of the simplest, most effective ways to shrink a model's footprint without losing much accuracy.

**0:44** · And it's used almost everywhere in production AI today, from the models running on your phone to huge inference clusters.

**0:50** · A model as we know it is just a huge collection of weights and activations or parameters stored together.

### Connect AI Parameters to Memory Requirements

**0:57** · You can think of these each as little dials tuned during training to represent knowledge. But knowledge is complex.

**1:07** · So models have tons of these parameters.

**1:09** · Gymaphor for example has a dense model with over 30 billion parameters.

**1:15** · Llama 3 has a model with 70 billion parameters and frontier models are estimated to have trillions. Every parameter has to be stored somewhere.

**1:23** · And how much detail you store for each determines how much space, memory, and compute the whole model needs.

**1:30** · So let's do the math on a 70 billion parameter model to see why quantization is so important.

### Calculate the Memory Cost of a 70B LLM

**1:38** · Most models store information in FP16 or BF16 format. This means that they allocate 16 bits or two bytes to each parameter.

**1:56** · Multiply that across 70 billion parameters and it would take about 140 GB to store.

**2:08** · This is more memory than a lot of single data center GPUs even have.

**2:12** · So we need to shrink how much space each parameter takes up. The problem is you can't just chop a number in half and call it lower precision.

### See How Quantization Reduces Precision

**2:21** · These numbers aren't stored as a simple string of digits that make up a value.

**2:26** · They're split into separate parts that each encode information. Something like the sign, the size, or the detail of the number.

**2:40** · If you cut off the wrong bits, you could end up with a completely different number.

**2:44** · We need an actual process for converting a value down to a lower precision and back again consistently. So let's use a simple example to see how quantization works under the hood.

### Follow Quantization Layer by Layer

**2:56** · A model is made up of layers and each layer contains a set amount of these weights.

**3:02** · Quantization like inference happens layer by layer. For each layer, we'll look at the full range of values present.

**3:09** · Let's say that this first layer holds values from 0 to 100.

**3:20** · We'll map that entire range down to a smaller set of values that fits in fewer bits. Let's say here we want to store numbers from 0 to 10.

**3:33** · We'll scale down any value from our original range and round it to the closest one in that smaller set.

**3:40** · For example, let's take an original value of 53 right here.

**3:47** · Scaling it down to our smaller size that would be 5.3 and then rounded to the nearest representation would end up being five.

**3:59** · Done well, this mapping will hold on to as much of the original range as possible and minimize the information lost.

**4:06** · This is definitely an oversimplification of the values that would be manipulated in a real model, but it's essentially the idea. In real life, this smaller set of values maps on to a few standard formats.

**4:20** · Like we saw earlier, FP16 is 16 bits or two bytes. FP8 and int8 are, as you could probably guess, eight bits or one byte, and int 4 is four bits or half a byte.

### Compare FP16, FP8, INT8 & INT4

**4:48** · Going back to this 70 billion parameter model from earlier at full FP16 it will take 140 GB at FP8 or int8 it would take closer to 70 gigabytes.

**5:04** · And down here at end four, it would only take 35 gigabytes to store all of these weights.

**5:12** · This is much more manageable. You'll often see the precision in the model names.

**5:17** · For example, something like this means the model has 8 billion parameters quantized to FB8 or floating point 8, or this means that the model weights are at 8 bit precision while the activations are still at 16 bit.

**5:33** · But quantization giveth and taketh away.

### Balance Memory Savings with Model Accuracy

**5:36** · As we reduce the precision of the weights, we reduce the memory footprint, but also the level of detail of information stored.

**5:43** · It's kind of like a photo becoming more and more pixelated until it's hard to decipher the original image. Too much quantization and accuracy starts to drop.

**5:53** · In IN int 8 quantization, most models hold on to their accuracy and show significant improvements in latency.

**6:03** · IN4 is a bigger cut, so accuracy loss becomes a real risk.

**6:08** · With well-built mapping, however, INT4 can still land close to the original model's accuracy.

**6:14** · It just takes more careful rounding to get there. And to be clear, when I say real risk, I'm talking in the order of tenths of percentages to 1%.

**6:25** · Typically, accuracy stays above 90% of the original model's accuracy. There's also two different points where quantization can come into play.

### Compare PTQ vs Quantization-Aware Training

**6:33** · First, post-training quantization or PTQ. PTQ takes a model that's already fully trained and compresses it afterward.

**6:45** · It's fast and it's the more common approach. The other side is quantization-aware training or QAT.

**6:56** · QAT simulates the lower precision while the model still training.

**7:00** · So the model adjusts for that precision loss as it learns. QAT costs more time in compute, but it holds up better at more aggressive quantization levels like INT 4, where PTQ is more likely to lose accuracy.

**7:16** · So to recap, quantization takes the numbers a model is built from and stores them with less precision layer by layer down to a level like in8 or in4.

### Choose the Right Quantization Tradeoff

**7:28** · It can happen after training with PTQ or during training with QAT. Other why, either way, you're trading some precision for memory and speed.

**7:38** · And how far you push that trade depends on what your model needs to hold on to.

**7:43** · Drop your questions in the comments or let me know what precision you're running your models at in production.