![](https://www.youtube.com/watch?v=ptbj2nynsMg)

In this video, we build the Metropolis–Hastings algorithm from scratch using a single concrete problem: locating an earthquake off a coastline from arrival-time recordings. We show how a random walker that only compares two candidate spots at a time recovers exact probabilities without ever computing the intractable normalizing constant. We then explore step-size tuning and examine how multimodal geometry can quietly trap a Markov chain on the wrong side of the coast.  
  
Socials:  
\======  
Patreon: https://www.patreon.com/thesyntheticmind  
TikTok: https://www.tiktok.com/@the.synthetic.mind  
Instagram: https://www.instagram.com/the.synthetic.mind/  
X: https://x.com/yyz\_arash  
  
Chapters:  
\========  
0:00 The Earthquake Location Problem  
1:50 Computing Probabilities by Hand  
3:46 The Curse of Dimensionality  
5:35 Walking Without Normalization  
7:23 Detailed Balance and Hastings  
9:33 Tuning the Step Size  
11:10 The Mirror-Image Trap  
12:52 Origins and Practical Limits  
  
#MetropolisHastings #MarkovChainMonteCarlo #BayesianInference #Statistics #AppliedMathematics

## Transcript

### The Earthquake Location Problem

**0:00** · A few seconds after an earthquake starts, its waves reach the nearest seismometers, and each station records the exact moment the ground under it began to move. For a quake near a coastline, the first thing anyone needs from those recordings is where it happened, and in particular, whether it happened under the sea, because only a quake under the sea can lift the seabed and push up a tsunami. The recordings don't tell you that directly. What they give you is a handful of arrival times.

**0:28** · A little earlier at stations close to the quake and a little later at stations farther away. And to turn those times into a location, you have to work backwards. You guess a spot, work out when the waves from that spot would have reached each station, and compare those predictions with the times the stations actually recorded. A guess that matches all of them closely is plausible, and a guess that misses them badly isn't. The trouble is that one best guess isn't enough.

**0:53** · Every arrival time is measured with a small error and the speed of the waves through the rock is only known roughly. So a whole region of places can fit the times about equally well. What a seismologist actually wants is a probability for every possible location.

**1:09** · So they can say whether the quake was almost certainly offshore or whether it could have been on either side of the coast. The same problem turns up in places that have nothing to do with earthquakes. Cosmologists measure faint ripples in the oldest light in the universe and want to know how much ordinary matter and dark matter would have produced them. And biologists compare the genes of a virus collected in different cities and want to know which family tree of infections best explains the differences. In each case, it's easy to check how well one particular answer fits the data. And it takes a computer a fraction of a second.

**1:43** · What's needed, though, is a probability for every answer. And it isn't obvious how to get from the first thing to the second.

### Computing Probabilities by Hand

**1:50** · To see what that probability looks like when you can actually calculate it, start with the smallest version of the problem. Suppose seismologists already know the quake happened on the fault that runs along the seabed offshore. And to keep things simple, the fault is split into five sections. The question is now which of those five sections the quake came from. For each section, you do exactly what we did with a single guess. You put the quake there, work out when its waves would have reached each station, and compare those predicted times with the recorded ones.

**2:21** · Then you turn that comparison into one number called a weight, which is large when the predictions line up with the recordings and small when they don't. The usual choice treats every timing error like a draw from a bell curve. So the weight falls off very quickly as the mismatch grows. In the language of Baze rule, the weight is the likelihood of the recorded times multiplied by how plausible the section was beforehand. And here, every section starts out equally plausible.

**2:50** · Working that out for the five sections from west to east gives weights of 1 3 6 3 and 2. Those numbers only mean something relative to each other.

**3:00** · Section 3 has twice the weight of section 2, so it's twice as plausible.

**3:05** · But a weight of six isn't a probability of anything yet. To turn weights into probabilities, you add them all up and divide each one by the total. Here, the total is 15. So, section 3 gets 6 15, which is 40%. Sections 2 and 4 get 20% each. Section 5 gets about 13% and section 1 gets just under seven. That total, the sum of the weights over every possible answer, is called the normalizing constant. And it's usually written as a capital Z. Notice what made this easy.

**3:36** · Every possible answer was on a list short enough to write down. So, we could check each one and add up the results. And a real earthquake doesn't come with a list like that. A real quake isn't confined to five sections of one fault. It could have started anywhere on the map at any depth down to tens of kilome and at any moment in the seconds before the first station recorded it.

### The Curse of Dimensionality

**3:59** · The waves also travel faster through some layers of rock than others. And those speeds are only known roughly. So a careful model treats them as unknowns too. Put all of that together and a realistic location problem can easily have 30 unknown numbers. A grid of possibilities is hopeless at that size.

**4:17** · With just 100 values for each of 30 numbers, there are 100 to the^ 30 combinations, which is a 1 followed by 60 zeros. And a computer checking a billion of them every second would need vastly longer than the age of the universe to add up Z. Guessing at random doesn't rescue you either. The places that fit the arrival times well form a small patch around the true answer and every extra unknown shrinks that patch further. If the good range of each unknown covers a tenth of its possible values, then only one random guess in 10^ the 30 lands somewhere useful.

**4:49** · That suggests a different plan. Rather than guessing from scratch every time, you start from somewhere that fits reasonably well. Take a small step, check the new spot, and decide whether to move there. A sequence of points where each one depends only on the one before is called a marov chain. And using a chain like that to generate samples is called marov chain Monte Carlo or MCMC. If the chain spends time in each region in proportion to its probability, its list of visited points is all you need.

**5:19** · The fraction of them that lie offshore estimates the chance the quake was offshore and the error in that estimate shrinks like one over the square root of the number of points, however many unknowns there are. What's left is choosing the steps so the chain spends the right amount of time everywhere. Go back to the five sections of the fault where we already know the right answer and pretend we've never seen the total of 15. A walker starts in one of the sections and every step it takes has two parts. First, it proposes a move left or right with equal chance.

### Walking Without Normalization

**5:52** · Then it decides whether to accept that move by comparing weights. If the proposed section has a larger weight than the current one, the walker always moves. If it has a smaller weight, the walker moves with probability equal to the new weight divided by the old one.

**6:06** · And otherwise, it stays where it is. Say the walker starts in section two with weight three and proposes section 3 with weight six. That's uphill, so it moves.

**6:16** · From section 3, it proposes section 4 whose weight of three is half of six.

**6:21** · So, it accepts with a 50% chance.

**6:23** · Suppose the coin says no. The walker stays in section 3 and records section 3 again as its next sample. That repeat matters because if you skipped rejected steps instead of counting them, the walker would get too little credit for the places it's reluctant to leave and every fraction would come out wrong. And if a proposal points past either end of the fault, that spot has weight zero, so the move is always rejected. After 100 steps, the counts are still rough, although section 3 is already ahead.

**6:52** · After 10,000, the fractions settle at about 6.7, 20, 40, 20, and 13.3%. Which is the same answer we got by adding everything up. The walker never used the 15. Every decision it made depended only on the ratio of two weights, and that ratio is exactly the ratio of the two probabilities because the total Z sits underneath both of them and cancels.

**7:15** · That's why the chain never needs the one number we couldn't calculate. What it doesn't explain yet is why this particular rule lands on the right fractions and not some other ones. To see why it works, imagine a million walkers running at once, already spread out in the right proportions. That puts 400,000 in section 3, 200,000 in each of its neighbors, and the rest across the two ends. If every walker takes one step, and the crowd ends up in the same proportions as before, the distribution is called stationary, and the chain keeps it from then on.

### Detailed Balance and Hastings

**7:46** · Look at the boundary between sections 3 and 4. Of the 400,000 walkers in section 3, half propose moving right. And because section 4 has half the weight, half of those moves are accepted. That sends a 100,000 walkers from 3 to 4. In the other direction, half of the 200,000 walkers in section 4 propose moving left. And because that move is uphill, every one of them is accepted, which sends 100,000 walkers back from 4 to 3.

**8:15** · the traffic across that boundary cancels exactly and the same thing happens at every boundary on the fault. This is called detailed balance and the acceptance rule guarantees it for any set of weights because the flow in either direction always works out to the chance of proposing the move times the smaller of the two weights. As long as the chain can eventually reach every section and isn't trapped going around a fixed cycle, it forgets where it started and settles into these proportions. That argument assumed a move is proposed just as often as the move back.

**8:45** · Suppose instead that a walker at the western end always proposes section two rather than wasting steps proposing the edge, while a walker in section two only proposes section one half the time. Walkers would then drift into section two faster than they come back. In 1970, Keith Hastings fixed this by multiplying the acceptance ratio by the chance of proposing the reverse move divided by the chance of proposing the forward one. For the move from section 2 down to section 1, that turns 1/3 into 2/3 and the flows balance again.

**9:18** · That version is the Metropolis Hastings algorithm. Walking instead of guessing has a price, though. Each sample depends on the one before it. So 10,000 steps carry less information than 10,000 independent guesses, and how much less depends on how far each step gets.

### Tuning the Step Size

**9:35** · On the real map, the walker isn't limited to neighboring sections. At each step, it proposes a new spot drawn from a bell curve centered on where it is and nudges the depth, the start time, and the wave speeds the same way. The width of that bell curve is the step size, and the accept rule doesn't change at all.

**9:53** · The step size matters enormously. With tiny steps of a couple of hundred meters, almost every proposal fits about as well as the current spot. So, nearly every move is accepted. That sounds healthy, but the walker hardly goes anywhere because a random walk only covers distance in proportion to the square root of the number of steps. And traveling a 100 step lengths takes about 10,000 steps. With huge steps of 30 km, most proposals land where the times fit terribly and get rejected. So, the walker sits on one spot for dozens of steps, recording it again and again.

**10:24** · For targets shaped roughly like a bell curve in many dimensions, the best balance accepts about 23% of proposals, rising to about 44% in one dimension. The starting point matters, too. This chain starts at the station that recorded the quake first on land, and its early steps are just the walker finding its way to the region that fits. So, those first samples are thrown away as burn-in.

**10:49** · After that, the samples form a tight cloud, and you can read off whatever you need from it. The fraction of samples on each side of the coast gives the chance of each side and the depths of the samples give the probability of every depth without calculating any extra integrals. Here almost every sample sits inland under the hills a few km behind the coast and the chains averages have stopped changing. That answer is wrong and nothing in the chain says so. Look at where the seismometers are.

### The Mirror-Image Trap

**11:15** · All five sit on land just behind the coast almost on a straight line and a spot out at sea and its mirror image the same distance inland are almost exactly the same distance from every station. The waves from either one would arrive at nearly the same times. So the arrival times can't tell the two apart and the weight has two peaks, one offshore and one inland. Between those peaks, right under the coastline, the times fit badly. A quake there would sit almost on top of the nearest station.

**11:45** · So its waves would reach that station far too early compared with the others. That leaves a valley of almost zero weight between the two peaks. Every proposal from the inland peak toward the sea lands in that valley and is almost always rejected. So the chain can run for millions of steps without crossing. While its trace, its averages, and its acceptance rate all look perfectly healthy.

**12:07** · The true picture, the one we saw at the start, puts about 58% of the probability offshore because the coast bends slightly and the stations aren't quite on one line. Anyone trusting this chain would have said inland with near certainty and missed the one case that could send a tsunami toward the coast.

**12:26** · The standard defense is to run several chains from starting points spread across the map. Here, the chains started at sea settle offshore, and the chains started on land settle inland. And that disagreement exposes the problem. It only works if some chain happens to start near each peak, though, and no test can prove that a chain has found every peak. The real fix is better data, such as a seismometer on the sea floor, which breaks the mirror symmetry and leaves a single peak.

### Origins and Practical Limits

**12:52** · With the sealoor station included, the evidence now points strongly to an offshore earthquake on the fault about 10 km below the surface. That's exactly the kind of event that can lift the seabed and generate a tsunami. Reaching that conclusion never required adding up the weights over every possible location. At each step, the chain only needed to compare the weight of one possibility with another. Which is why the same idea can still work when the problem has dozens, hundreds, or even thousands of unknowns.

**13:24** · There is one important limitation, though. A chain can only tell you about the regions it has actually explored. A trace that looks stable tells you the chain has settled somewhere, but it doesn't prove that there isn't another important peak somewhere else. That's why a practical check is to start several chains far apart and see whether they eventually converge on the same distribution. Thank you for watching. If you enjoyed the video, please consider subscribing.

**13:48** · And if you'd like to support the channel and help us keep making videos like this, you can become a YouTube member for early access to videos, the ability to request future video topics, and other perks, or support us on Patreon. Thanks again for watching and for supporting the