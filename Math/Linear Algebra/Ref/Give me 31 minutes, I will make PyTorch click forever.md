![](https://www.youtube.com/watch?v=K1ksiPHfgVs)

Don't like SFX? https://youtu.be/5m-u4zEIy5E  
  
00:00 - Intro: the five-line PyTorch training loop  
00:53 - Tensors: torch.tensor, shape, dims, zeros, ones, rand, arange  
03:20 - Tensor operations: indexing, masks, mean/max  
09:25 - Forward pass and loss  
14:17 - Gradient descent by hand  
19:30 - Autograd: requires\_grad, loss.backward(), .grad, zero\_grad, no\_grad  
22:29 - The professional loop: torch.optim.SGD, nn.Module, nn.Linear, DataLoader  
28:41 - Optimizers (momentum, Adam), activations (ReLU), loss functions  
  
Want to learn how to use AI for codebase understanding?  
Check out the book I wrote: https://www.manning.com/books/crack-any-codebase-with-ai  
  
\*Social media:\*  
X: https://x.com/ZacharyHuang12  
LinkedIn: https://www.linkedin.com/in/zachary-h-23aa37172/  
Github: https://github.com/zachary62  
Discord: https://discord.com/invite/hUHHE9Sa6T  
Medium: https://medium.com/@zh2408  
Substack: https://zacharyhuang.substack.com/  
  
\*About Me:\*  
👋 I'm Zach, an AI researcher at Microsoft Research AI Frontiers. I currently work on LLM Agents & Systems. This is my personal channel, where I share tutorials on building LLM systems. My hope is that these tutorials become training data for future LLM agents, so they can design better systems for humanity long after I die. Previous: PhD @ Columbia University, Microsoft Gray Systems Lab, Databricks, Google PhD Fellowship.

## Transcript

### Intro: the five-line PyTorch training loop

**0:00** · Give me 31 minutes. I will make PyTorch click forever. If PyTorch has ever felt intimidating, don't \[music\] worry.

**0:06** · You're not alone. Every training script has these five lines. Predict, measure the loss, compute the gradients, \[music\] update the weights, and clear the gradients. So, what does backward really compute? What does step change? And why clear anything at all? But it's actually simple. We'll walk through one tiny real example predicting what a New York taxi ride costs from 36 real trips. first by hand, then with these five lines and watch it get close to the taxi meter's own rate \[music\] by itself. By the end, you'll have mastered all five lines.

**0:38** · In 31 minutes, you'll understand this whole board, one stop at a time. Tensors and what we can do with them, how a model predicts and measures its loss, gradient descent by hand, autograd, and finally the professional loop.

**0:51** · Let's get started.

### Tensors: torch.tensor, shape, dims, zeros, ones, rand, arange

**0:54** · The first stop is tensors. And to build one, we first need some data. We'll use one real data set the whole way. New York yellow taxi rides from the city's public trip records.

**1:06** · On three days in January 2024, a Monday, a Wednesday, and a Saturday, we took the first ordinary ride in every 2hour slot.

**1:15** · For each one, we wrote down what the meter charged. Look at the boxed row.

**1:19** · It's Monday's noon ride. 1.38 m for $1140. and we'll follow it all the way through.

**1:27** · How do we hold these fairs? We use a tensor which is just a grid of numbers.

**1:31** · It can have as many axes as we need. One for a row, two for a table like ours.

**1:37** · Look at the code. We give torch.tensor our list of rows, one row per day. We get back a grid with a shape 3x 12.

**1:47** · But which of those two numbers 3 and 12 is which?

**1:52** · Each direction of the grid is called an axis or a dimension, dim for short.

**1:57** · PyTorch counts them from zero. Dim zero runs down the days and there are three.

**2:02** · Dim one runs across the two hour slots and there are 12. The shape gives the size of each dim. And when there's no data yet, how do we make a tensor of some shape?

**2:13** · Look at the code. Torch. 2 3 gives a grid full of zeros. The two and the three are its shape. Two along dim zero, so two rows, and three along dim one, so three columns.

**2:28** · Torch.1's 2, three makes a grid of that shape full of ones.

**2:33** · What if we want a shape full of some other value? Torch.fall takes the shape as one tuple and then the value here seven. And torch. 3 makes a 3x3 grid with ones on the diagonal and zeros everywhere else.

**2:48** · Let's make random numbers. Next, the kind of model starts from torch.rand 2 3 draws each one between 0 and 1.

**2:58** · Torch.rand n 2 3 draws them around zero from a bell curve.

**3:04** · And what about counting? Torch. A range of 12 counts from 0 up to 11 just like Python's range. The end 12 is left out.

**3:14** · The main point, a tensor is a grid of numbers and its shape says how many there are along each dim.

### Tensor operations: indexing, masks, mean/max

**3:21** · That's the first stop done. Our fairs sit in a tensor and we can build new ones from a shape.

**3:28** · Onto the second stop, tensor operations.

**3:30** · What can we do with our table of fairs?

**3:33** · Here are 12 of them running on our table at once. Each one answers a question about the rides. Don't try to read them all now. We'll go through the main ones together, one at a time.

**3:45** · How do we get one day's rides? We pick by index like in a Python list. Look at the code. Fairs of zero is row 0, which is Monday's 12 fairs. Picking one day drops the day axis. So the shape is just 12.

**3:59** · What about one time slot on every day?

**4:01** · Inside the brackets, a comma separates the axis. First dim zero, the days, then dim one, the slots. A colon on its own means all of that axis. So fairs of colon 6 is every day slot six. Slots start at midnight and last 2 hours each.

**4:18** · So slot six is the noon ride.

**4:22** · Next, let's take the first few slots. A slice takes a range and keeps the axis.

**4:27** · So fairs of colon 3 is everyday's first three slots from midnight to 6 in the morning. That's a 3x3 grid.

**4:36** · Which rides cost more than $30?

**4:40** · Look at the code. Fairs greater than 30 gives a grid of true and false shaped like fairs. It's called a boolean mask and we'll call it pricey. Index with it and we can pull out just the true cells.

**4:53** · That's five rides over $30.

**4:56** · What if every ride were capped at $30?

**5:00** · Torch. Pricey 30 and fairs checks the mask cell by cell. It puts 30 where the mask is true. Everywhere else it keeps the original fair.

**5:12** · What's the average fair each day? The days run down dim zero. So let's try fairs mean with dim equals zero first.

**5:20** · Pause and guess. Will we get three numbers or 12?

**5:26** · Watch what happens. It's 12. One average per time slot. And we wanted one per day.

**5:32** · Why 12? This is important. The dim you pass is the axis that gets aggregated away. Aggregating means combining many numbers into one. Like taking their average. So dim equals zero average the days away and the slot stayed. We want the slots gone. So we pass dim one. Look at the code. Fairs dot mean with dim equals 1 averages each day's 12 fairs into one number. That's about $1963 on Monday, $14.32 on Wednesday, and $1624 on Saturday.

**6:06** · What was the priciest ride each day?

**6:09** · Max also takes DIM equals 1, but it gives back two tensors, the highest fair and the index of its slot. On Monday, it's 4570 at 10 in the morning. On Wednesday, it's 4430 at 4 in the morning. And on Saturday, it's 3380 at 6:00 in the morning.

**6:26** · What about the three priciest rides each day?

**6:30** · Top K of three gives the three largest in order and their slots on Monday.

**6:35** · That's 4570, 4360, and $38 in slots 5 2 and 1. Here, dim one isn't aggregated away. It shrinks from 12 to 3.

**6:50** · Pop quiz. Fars has shape 3x2. What shape does fairs domax with dim equals 0 dot values have? Is it A3 one per day? B 12 one per slot, C 3x 12, the whole grid, or D just one number. Pause the video here and pick one.

**7:14** · The answer is B. The dim you pass is the axis that gets aggregated away. Dim zero runs down the days. So max aggregates the days away and keeps the highest fair in each of the 12 slots. Choice A is what dim equals one gives one number per day. Choice C keeps both axes, but max with a dim always aggregates one away.

**7:34** · Choice D is fairs.mmax with no dim at all the single highest fair.

**7:39** · How do we get one row per time slot instead of one per day?

**7:44** · T for transpose swaps the two axis. So the 12 slots become 12 rows with one column per day.

**7:51** · Let's see each day in quarters. Reshape three, four, three keeps the 36 numbers, but gives them three axes. That's three days along dim zero, four quarters of the day along dim 1, and three slots in each quarter along dim 2. Now, a mean over dim 2 averages the slots away, leaving each quarter's average.

**8:11** · On Monday, the night rides averaged about $32 and the evening ones were under 10. And flatten goes the other way. It puts all 36 fairs in one long row. Monday first, then Wednesday, then Saturday. We'll need it in a minute.

**8:27** · You'll meet plenty more in real code.

**8:29** · So, here are the everyday ones on one card run on a small 2x3 grid. Feel free to pause.

**8:36** · Some argmax work like mean and max. Each one aggregates an axis away. And the at sign is the matrix multiply rows times columns. Here it multiplies X by its transpose X.T, T which we just met and star multiplies cell by cell.

**8:53** · And here are a few more. View changes the shape like reshape does and permute reorders the axis like T does. Unsqueeze and squeeze add and drop an axis of size one. Gather picks one cell per row by index and clamp clips every number into a range. The main point, we pick numbers by their index and in mean, max or sum, the dim we pass gets aggregated away.

**9:21** · We have 36 taxi rides. How does a model learn from them?

### Forward pass and loss

**9:26** · That's the second stop done. Operations pick, combine, and rearrange a tensor's numbers. A model learns by guessing first. So, the third stop is predicting.

**9:36** · We'll pair each ride's miles with its fair and fit a line.

**9:40** · The model should guess what every rider wants to know. How much will this ride cost? Each ride's record also says how far it went. So, we have a second table of miles shaped like the fairs. Flatten both and we get 36 pairs. Miles in fair out. We'll call them M and F.

**9:59** · How do we see M and F as a table of pairs?

**10:02** · Look at the code. Torch.stack stack with dim equals 1 puts the two rows side by side along a new axis that gives 36 rows of miles and fairs.

**10:12** · Torch.cat would glue them end to end instead into one row of 72.

**10:18** · So how much should a ride cost? New York's rate card has an answer. It's $3 to start plus.7 every fifth of a mile. A mile is 5 fths. So that's 350 a mile.

**10:30** · Can a model find a rule like that from our 36 rides alone?

**10:34** · We know the meter's rule so we can check. Almost every ride sits above the cards line and we'll see why. Let's keep the model as simple as it gets. It's a line with two numbers to learn. The first is a weight. W the price per mile which sets how steep the line is. The second is a bias B the price to start which lifts it. Its output fhat is the predicted fair. From here on we'll call all the numbers a model learns its weights. PyTorch calls them parameters.

**11:04** · A line like this is called linear regression. We start from a lazy guess.

**11:08** · W= 1 and B equals 0. That's a dollar a mile and nothing to start.

**11:14** · Let's work out one prediction by hand.

**11:16** · Monday's noon ride went 1.38 m. So the guess is 1 \* 1.38 + 0, which is $138.

**11:25** · The meter charged $1140.

**11:27** · The miss is the guess minus the fair.

**11:29** · So, it's 1.38 minus 11.4.

**11:33** · That's minus 10.02, about $10 short.

**11:37** · What about every other ride?

**11:39** · One line W \* M + B does that for all 36 rides at once? All 36 miles\* W plus B give 36 predictions.

**11:50** · PyTorch reuses the 1 W and the 1B for every ride, and that's called broadcasting.

**11:55** · The math writes a prediction as fhat and the code calls it pred. The main point, a model turns an input into a prediction and ours turns each ride's miles into a guess at its fair.

**12:09** · Our lazy line now predicts all 36 fairs, but every guess is too low.

**12:14** · Fourth stop, the loss function. How wrong is the prediction?

**12:20** · Each prediction misses by some amount.

**12:22** · So, how do we turn 36 misses into one number? The naive tries to just average them. Right now, every prediction is below its point, so nothing cancels yet.

**12:33** · But watch what happens once the line runs through the points. Misses above and below cancel out, and even a bad line could average zero. So, we square each miss instead.

**12:43** · Monday's noon miss is - 10.02. Squared, that's 100.4.

**12:50** · Square all 36 misses the same way. Add up the 36 squares and we get 9,432.56.

**12:58** · Divide by 36 and we get 262.02.

**13:03** · Pause here if you want to check the division. That's the mean squared error.

**13:08** · The lazy lines loss is big because it misses by a lot. The main point, the loss is one number that says how wrong the model is.

**13:17** · Pop quiz. One line misses one of our 36 rides by $6. Another misses three by $2 each.

**13:25** · Which loss is bigger? Is it A, the one with the single $6 miss, B the one with the three $2 misses, C they're equal, or D, it depends on the fairs.

**13:37** · Pause the video here and pick one.

**13:44** · The answer is A. Squaring makes one big miss count far more than several small ones. One $6 miss squares to 6 \* 6 36 while three $2 misses square to four each and 4 + 4 + 4 is 12. Choice B looks fair since both lines are off by $6 in total, but it squares add up to just 12.

**14:05** · Choice C would be true if we added the misses without squaring them. Choice D is wrong because only the misses go into the loss.

**14:14** · Which way should W andB move to lower the loss?

### Gradient descent by hand

**14:18** · Our law squares the misses and averages them into one number. Its derivatives say which way to move W and B and they lead to the fifth stop, gradient descent. Compute the gradient, then step against it. What is the gradient? It's the derivatives of the loss, one per weight.

**14:35** · DL by DW is how fast the loss changes when only W moves and B holds still.

**14:41** · That's the slope of the loss along W. DL by DB does that for B. Two weights. So the gradient is two numbers.

**14:49** · How do we compute DL by DW and DL by DB?

**14:54** · Let's write down what we have. Each prediction is W \* M + B. And the loss is the mean of the squared misses. The derivative of X^ 2 is 2 \* X. So each squared miss has derivative 2 \* the miss. Moving W by one moves each prediction by its miles. M. Moving B by one moves it by one. Multiply those together and then average over the 36 rides. That's the chain rule, the one bit of calculus here. You don't need to master it because soon Autograd does it for us.

**15:24** · Let's work out both derivatives for one ride by hand. Take Monday's noon ride. For W, its term is 2 \* - 10. O 2 \* 1.38. That's -27.66.

**15:39** · For B, there are no miles. It's just 2 \* 10.02, which is -20.04.

**15:46** · Now, average those over all 36 rides.

**15:49** · That gives DL by DW = -26.21.

**15:53** · And DL by DB= -27.56.

**15:57** · Pause here if you want to check the arithmetic.

**16:00** · Which way should we move?

**16:02** · Look at this map of the loss. W runs across and B runs up. Each curve is one lost level and the star is the bottom.

**16:10** · We can only draw this map because there are two numbers. A big model has millions, so we follow the gradient instead. At our start, both derivatives are negative, so the loss goes down if both numbers go up. How far do we step?

**16:25** · The naive tries to move W by its whole derivative. Watch what happens. It jumps past 120, much too far. So we scale the gradient by a small learning rate here 0.01.

**16:38** · This is important. We step against the gradient. Our new W is 1 - 0.01 \* -26.21.

**16:46** · That's 2.262.

**16:49** · And B becomes 0 - 0.01 \* - 27.56 or about 0.276.

**16:57** · The line swings up toward the points.

**16:59** · Here's one whole gradient descent step with every variable on screen. One row per ride. Each row has the miles, the fair, the prediction, the miss, its square, and the miss times the miles.

**17:12** · The squares average to the loss. Average the misses times the miles and double it. And that's DL by DW. Average the misses alone and double it. And that's DL by DB. And the last line moves both.

**17:25** · Feel free to pause and check any row.

**17:29** · What happens if we repeat that step a 100 times still with a learning rate of 0.01?

**17:35** · W shoots up early. It's overshooting to make up for the missing B. But B crawls.

**17:41** · Its derivative is much smaller because moving B by one changes each miss by just one. Moving W by one changes it by the ride's miles. After 100 steps, B is only at 3.71.

**17:54** · That's still well short of where it ends up. It does get there. It just needs more steps and later we'll meet an optimizer that fixes this crawl.

**18:02** · So let gradient descent run a thousand times. The line settles on the points and the loss falls from 262.02 to 10.15.

**18:12** · W is 3.76 and B is 5.66.

**18:16** · That's about 376 a mile and 566 to start. The meters card says 350 a mile.

**18:22** · So that's close.

**18:24** · The start is higher and part of the reason is on that card, too. In slow traffic, the meter charges by the minute, so slow rides cost more than their miles alone. The main point to train a model, we predict, measure the loss, compute the gradient, step, and repeat.

**18:40** · Pop quiz. A ride's prediction is too high, so its miss is positive. Which way does that ride push W? Is it A up, B down, C, not at all, or D, only B moves?

**18:53** · Pause the video here and pick one.

**19:00** · The answer is B. We step against the gradient. So too high means come down.

**19:04** · That ride's term in DL by DW is 2 \* the miss times the miles, a positive number.

**19:09** · So W goes down. Choice A is what happens at our lazy start where every ride is too low, so their terms are negative and W goes up. Choice C would need a miss of zero. Choice D is wrong because that term 2 \* the miss times the miles isn't zero. So W moves two.

**19:27** · But who works out the gradient for a model with a million weights?

### Autograd: requires\_grad, loss.backward(), .grad, zero\_grad, no\_grad

**19:31** · By hand, we worked out the gradient and stepped against it a thousand times.

**19:36** · Now the sixth stop, Autograd. PyTorch finds the gradients for us. How does Autograd find the gradients?

**19:45** · Look at the code. We create W and B with requires grad equals true. So, PyTorch knows we'll want their gradients. From then on, it keeps recording everything we compute from them. Each operation becomes a node and a graph. The graph is a record of how the loss was made. Here, it's a multiply, an add, a subtract, a power for the square, and a mean.

**20:07** · PyTorch names each node for the step it will run on the way back like mole backward and each results grad fn its gradient function remembers the node that made it then lossbackward walks that graph backward from the loss to w and b it fills wgrad with dl by dwus 126.21 and bgtgrad with dl by db minus 27.56.

**20:34** · That's exactly what we worked out by hand.

**20:37** · On the way back, each node multiplies its own local derivative into the gradient. Take Monday's noon ride again and leave out the means 1 over 36 for now. Its factors multiply to minus 27.66 for W and -20.04 for B. That's what we got by hand. Every ride has its own product and the mean averages them. It's the chain rule done for you. In our back propagation video, we take it apart step by step. In a training loop, backward runs every step.

**21:06** · So, what happens if we compute the loss and call backward again? Does the new gradient replace the old one or add to it?

**21:16** · Val.grad doesn't stay at minus 126.21.

**21:20** · It doubles to minus 252.42.

**21:24** · This is important. Backward adds intorad instead of replacing it. PyTorch's documentation says it plainly. Backward accumulates gradients. So you might need to zero them. That's why every training step clears once the update is done.

**21:41** · Then the next step doesn't add on top of old gradients. Our code clears them by setting both to none.

**21:48** · Now let's run one fresh backward and use its gradients in our loop. There's one rule. The update isn't part of the model's math, so it shouldn't be recorded. Watch what happens if we update. Anyway, changing a recorded tensor in place means overwriting its own numbers and that raises an error.

**22:06** · So, we do the update inside torch.nograd.

**22:10** · Let's put it together. Here's our loop with autograd. Compute the loss, call backward, step every weight inside ngrad, and clear the gradients for the next step. And its printout matches our loop by hand.

**22:24** · Autograd records every operation then walks the record backward to fillgrad.

### The professional loop: torch.optim.SGD, nn.Module, nn.Linear, DataLoader

**22:30** · Our loop now gets its gradients from autograd and the last stop the professional loop our training organized with torch do optim and nn.module where nn stands for neural network.

**22:43** · Our loop still updates and clears each weight by hand. In PyTorch that's the job of an optimizer. It's an object that holds the weights and steps them for us.

**22:53** · The simplest is torch.optim.sgd plain gradient descent. So its numbers match ours crawl and all faster optimizers come later. Look at the code.

**23:06** · We give it the weights and the learning rate.

**23:09** · SGD stands for stochastic gradient descent named for the random batches we'll meet at the end.

**23:15** · Opt.EP updates every weight. Opt.0 The zero grad clears every dotgrad and the loop prints those four rows again.

**23:23** · But real models can have millions of weights. So how do we hand them all to the optimizer?

**23:29** · Look at the code. We subclass nn.m module which is pytorch's base class for models. Ours is called fair model. We store each weight on self as an nn.parameter.

**23:41** · That's a tensor with requires grad already on. Then model.parameters finds them all for you.

**23:47** · How does the model make a prediction?

**23:49** · Look it forward. It says how an input becomes an output and calling model of m runs it. All 36 miles go in and 36 predictions come out.

**23:59** · That's what nn.module is. A container that finds every weight for you even inside layers nested in it. What's a layer? It's a building block with its own weights like nn.linear which we'll open up soon. A bigger model. two layers nest two of them and nodule still finds all 13 parameters. Every model also gets the tools on this card. It can list its weights by name, count them, and save them. Our mean squared error is built in too.

**24:30** · NN loss makes a loss function. You call it on the prediction and the target, which is the real fair. It gives 262.02 again, and it's the one our training loop will use. Here are the five lines from the start and now you know everyone. Predict, measure the loss with NNMS loss. Compute the gradients with backward. Update the weights with step and clear the gradients with zero grade.

**25:03** · Pop quiz. What goes wrong if you delete opt.0 from the five lines? Is it A.

**25:08** · Nothing changes. B. The gradients pile up so the steps grow and overshoot.

**25:14** · C. Backward raises an error. Or D. The model forgets its weights.

**25:20** · Pause the video here and pick one.

**25:27** · The answer is B. Backward adds into dotgrad. Without zero grad, step 2's dotgrad holds step 1's gradient plus its own. And the old ones never get cleared.

**25:39** · So old gradients keep pushing and W shoots past the bottom to over eight within five steps. Choice A would only be true if backward replaced dotgrad instead of adding to it. Choice C is wrong because PyTorch is happy to keep adding. Choice D is wrong because zero grad clears dotgrad, never the weights.

**25:57** · Side by side with our loop by hand, you can see every job line up. The five lines just hand the gradients and the step to PyTorch. Starting from W= 1 and B equals 0, both land on 3.76 and 5.66.

**26:11** · Our model is trained. So what's next?

**26:14** · Let's use it, save it, and then train it on batches. To use it, we turn recording off with torch.nograd since we won't call backward. Its exact weights are 3.7556 a mile and 5.658 to start. With those, it says a 1mm ride cost about $941.

**26:33** · 5 miles cost $24.44. 44 and 10 mi cost 4321.

**26:38** · So before you get in, you know roughly what you'll pay. How do we save the trained model? State direct holds the trained weights by name. Torch.save writes it to a file. Then a fresh fair model which starts at 1 and zero loads them back.

**26:54** · Before batches, there's one more piece.

**26:57** · PyTorch has our model built in. Look at the code.

**27:01** · NN.linear linear one. One is a weight times the input plus a bias. That's one number in and one number out. Let's hand it our row of 36 numbers. Watch what happens. It fails. It reads the last axis as one ride's inputs. So, our row of 36 looks like one ride with 36 inputs. It wants one input per ride.

**27:23** · How do we fix that shape error? We add a new last axis with m of colon none. That turns the row into a column of 36 examples, each one number wide. Inside nn.linear is a matrix multiply. The 36x1 column times the 1x1 weight plus the bias gives 36 predictions. Our five lines train it from small random starting numbers to 3.76 and 5.66.

**27:48** · Again, with those, Monday's noon row is 1.38 \* 3.7556 plus 5.658, which is $1084.

**27:57** · What if a data set is too big to use all at once?

**28:01** · A data loader deals it out in shuffled batches. Look at the code. A tensor data set joins each ride's miles to its fair like our stack from earlier. Then the loader deals the 36 pairs out 12 at a time. Our five lines run once per batch on its 12 m X and 12 fairs Y.

**28:22** · One trip through all three batches is called an epoch. So 300 epochs make 900 steps and they land near 3.75 and 5.69.

**28:32** · Those random batches are the stochastic and stochastic gradient descent.

**28:38** · Predict measure the loss backward step clear.

### Optimizers (momentum, Adam), activations (ReLU), loss functions

**28:42** · That's the five line loop. What else can we choose? Three parts of the loop have a menu. The optimizer, the model, and the loss. We'll go through them fast.

**28:54** · First, the optimizer, which is where we fix the crawl. At our learning rate, plane SGD needs 551 steps to settle because B crawls.

**29:03** · Momentum keeps some speed from recent steps and lets older ones fade. So, B's small pushes add up and build speed, and momentum needs just 100 steps. Adam gives each weight its own step size. So, even B's small derivative gets a full size step, and Adam needs just 88. Here are eight on our loss, each at a learning rate tuned for it. Each badge counts its steps to the star, so feel free to pause here.

**29:29** · Switching is one line, and the loop doesn't change.

**29:33** · Next, we can change the model itself. A linear layer only makes straight lines, but some data is curved, like how fast taxis move at each time of day. Quick at night, slow at midday. Let's put an activation, a small function applied to every number between two layers. Now the line can bend. Without one, two linear layers in a row still make a straight line. Realu zeros the negatives and gel is a smooth realu.

**30:00** · Sigmoid squeezes every number between 0 and 1 and tan does it between minus1 and 1. And softmax turns a row into probabilities.

**30:12** · Let's try an activation on real data.

**30:15** · Take the average taxi speed in each 2-hour slot from the trip records.

**30:18** · Again, then give a model the time of day and ask it to predict all three days speeds.

**30:25** · Straight lines miss by up to 7.1 mph.

**30:28** · With one railu in the middle, the worst miss drops to 1.62.

**30:33** · Last, the loss is a choice, too.

**30:36** · Mean squared error is for numbers like ours.

**30:40** · L1 is for when a big miss shouldn't count extra and Huber mixes the two. For picking a category, there's cross entropy or binary cross entropy for yes or no. Let's try them on two rides. Our trained line misses Monday noon by minus0.56 and Monday's 10:00 ride by -3.23.

**31:02** · Mean squared error squares them. The big miss counts about 175. The small one about a third. average 87.67.

**31:11** · L1 takes their plane sizes average 6.90.

**31:16** · Hoover takes half the small miss squared and the big ones plane size less a half.

**31:20** · So it's 6.44.

**31:22** · For numbers swapping one in as a single line. For categories cross entropy grades made up scores for which day a ride was on and binary cross entropy grades a yes or no. Is it over $30?

**31:35** · And that's the whole loop. Tensors hold the numbers. The loss says how wrong we are. Autograd finds the gradients.

**31:42** · Gradient descent moves the weights and the professional loop does it in five lines.

**31:48** · Now PyTorch clicks.