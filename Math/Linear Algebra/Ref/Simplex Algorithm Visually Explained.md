![](https://www.youtube.com/watch?v=aQav5HQMGNY)

This video provides a visual explanation of the Simplex Algorithm. We demonstrate how to define a linear program, visualize its feasible region and objective function geometrically, and explain why optimal solutions are found at corners. We then detail Dantzig's corner-to-corner search strategy and elucidate why this method reliably identifies the global optimum, concluding with a discussion of its diverse applications.  
  
Socials:  
\======  
Patreon: https://www.patreon.com/thesyntheticmind  
BuyMeACoffee: https://buymeacoffee.com/thesyntheticmind  
TikTok: https://www.tiktok.com/@the.synthetic.mind  
  
Chapters:  
\========  
0:00 Introducing Linear Programs  
1:37 Worked Example: The Geometry  
5:11 The Challenge: High Dimensions  
6:46 The Simplex Walk Explained  
9:58 Why Simplex Always Works  
12:20 Simplex: Applications & Limits

## Transcript

### Introducing Linear Programs

**0:00** · Every morning an airline has to decide which crews will fly which planes. There might be thousands of pilots and thousands of flights along with rules about rest periods, qualifications, scheduling, and where each crew needs to end up at the end of the day.

**0:17** · The airline has to put together a schedule that satisfies all of those requirements without spending more than it needs to.

**0:26** · A refinery faces a different version of the same problem. It has to decide how much of each crude oil to turn into which fuel when every fuel sells for a different price and uses up a different mix of what's in the tanks.

**0:41** · These problems come from completely different industries, but mathematically, they can be written in much the same way. There's some quantity you want to maximize or minimize such as profit or cost, and a set of constraints that the solution has to satisfy. When both can be written using linear relationships, you get what's called a linear program.

**1:05** · And problems like this show up everywhere from transportation and manufacturing to scheduling, hospital staffing, and supply chains.

**1:14** · In 1947, mathematician George Dantzig developed a method for solving these problems called the simplex algorithm.

**1:23** · Since then, it's become one of the foundational algorithms in optimization and is still widely used today.

**1:31** · To see how it works, let's start by building the idea up from a simple example.

### Worked Example: The Geometry

**1:37** · Picture a small workshop that makes chairs and tables. A chair brings in $40 of profit and a table brings in 60. Each week the workshop has 40 planks of wood and 60 hours of labor. A chair uses one plank and three hours, while a table uses two planks and two hours. The question is, how many of each to build to make the most money? That's a linear program. And it has the three parts every linear program has.

**2:08** · The numbers you get to choose are the variables, which here are the number of chairs and tables. So, we'll call them X and Y. The quantity we're trying to maximize is the objective, which in this case is profit, $40 for every chair plus 60 for every table. And the constraints are the rules the solution has to satisfy. One chair uses one plank of wood and one table uses two. So, together they can't use more than the 40 planks available.

**2:40** · A chair also takes three hours of labor and a table takes two. And together they can't use more than 60 hours. And neither X nor Y can be negative. It's linear because those relationships don't change as production increases. Every additional chair always uses one more plank and three more hours of labor. And every additional table always uses two more planks and two more hours.

**3:07** · Because there's only two variables, we can draw the whole problem on a graph with chairs on one axis and tables on the other.

**3:16** · The wood constraint gives us one straight line. Everything on one side of that line uses no more than the 40 planks we have, while everything on the other side requires more wood than is available.

**3:30** · The labor constraint gives us another line.

**3:33** · And the conditions that X and Y can't be negative keep us in the first quadrant.

**3:38** · Put those constraints together and you get the set of all combinations of chairs and tables that are actually possible.

**3:45** · This is the feasible region. We can draw the objective on the same graph. Every combination of chairs and tables that gives the same profit lies on a straight line. Increase the profit and that line moves outward until eventually it reaches the furthest point in the feasible region. For a linear program like this, there will always be an optimal solution at one of the corners of that region. And this region only has four corners, so we can check each of them easily. First, if we build nothing, then the profit is zero.

**4:17** · Alternatively, if we build 20 chairs and no tables, which uses all 60 hours of labor, the profit is $800.

**4:27** · If we build 20 tables and no chairs, which uses all 40 planks of wood, then the profit is 1200. Finally, if we build 10 chairs and 15 tables, where the wood and labor constraints meet, then the profit is $1300.

**4:43** · So, the best solution is 10 chairs and 15 tables.

**4:48** · Although a table makes more profit than a chair, producing only tables isn't the best use of the resources we have.

**4:56** · Here, we could solve the problem by checking four corners by hand, but that only works because the problem is tiny.

**5:04** · What happens when there are hundreds or thousands of variables and far more corners than we could ever check one by one?

### The Challenge: High Dimensions

**5:12** · Now, let's try adding one more product, such as a stool. That's a third number to choose. So, instead of a two-dimensional graph, the problem now lives in three dimensions. The constraints are no longer lines, they're planes, and together they define a three-dimensional region containing every combination of chairs, tables, and stools that we could actually produce.

**5:35** · The objective works the same way, too.

**5:37** · Instead of a profit line moving across the graph, we now have a profit plane moving through this region, and there will still be an optimal solution at one of its corners.

**5:48** · But now there are more corners, and that becomes the real problem. A workshop might have 50 products and 30 different constraints. Mathematically, that's a problem living in 50 dimensions with no way for us to draw or visualize the feasible region.

**6:05** · The same result still holds.

**6:07** · An optimal solution can still be found at a corner, but the number of possible corners can grow enormously as the problem gets larger.

**6:16** · With enough variables and constraints, there can be far too many to check one by one. And simply picking whatever looks most profitable doesn't work, either.

**6:26** · In the previous example, tables made more money per unit than chairs, but producing only tables still wasn't the best solution.

**6:35** · So now we have a feasible region we can't see, potentially an enormous number of corners, and no obvious way to know which one is best.

**6:43** · The question then becomes how to find that corner without checking everyone.

### The Simplex Walk Explained

**6:47** · Dantzig's idea was to move from corner to corner instead of checking every corner in the entire region. Start at one corner, look at the edges leaving it, and see whether any of them lead to a better objective value.

**7:01** · If one does, follow that edge until you reach the next corner, then repeat. You can write the basic idea as three steps.

**7:09** · First, start at a corner.

**7:11** · For this problem, zero chairs and zero tables is the obvious place to begin.

**7:15** · Second, look at the edges leaving that corner and determine what happens to profit along each one.

**7:22** · Third, if none of those edges improves the objective, you're done. Otherwise, choose one that does, follow it until another constraint becomes tight, and repeat from the new corner.

**7:34** · For the workshop problem, we start at zero chairs and zero tables. From there, we can move in two directions, increasing chairs or increasing tables.

**7:44** · A chair adds $40 of profit and a table adds 60. So, either direction improves the objective. Suppose we choose tables.

**7:52** · We keep increasing the number of tables until one of the constraints stops us.

**7:57** · The wood constraint is the first one we hit at 20 tables and zero chairs, giving us a profit of $1,200. And now we're at a new corner. Going back toward zero tables would reduce profit, so there's no reason to move that way. The other edge runs along the wood constraint. If we want to add a chair while keeping all 40 planks in use, we have to give up half a table because a chair uses one plank and a table uses two. Adding that chair gives us $40 while losing half a table costs 30.

**8:28** · So, moving in that direction increases profit by $10.

**8:33** · We follow that edge until the labor constraint becomes tight, which happens at 10 chairs and 15 tables.

**8:42** · Profit is now $1,300.

**8:45** · From this corner, we check the possible directions again. One takes us back toward the corner we just came from, which would lower profit. Along the other edge, the labor constraint stays tight.

**8:58** · Adding one chair uses three hours of labor, so we'd have to give up one and a half tables to make room for it.

**9:06** · The chair adds $40, but those tables would have been worth 90. So, profit falls by $50. There are no directions left from this corner that improve the objective, so the algorithm stops.

**9:20** · We visited three of the four corners and found the same $1,300 solution we got by checking them manually. The calculation we're doing at each step, comparing what we gain from bringing one variable in against what we have to give up elsewhere, leads to a quantity called the reduced cost. That's what tells the simplex method whether moving in a particular direction can improve the objective.

**9:48** · But there's still an important question.

**9:50** · We never visited the fourth corner. So how can the algorithm be sure that there isn't a better solution somewhere it never checked? That raises a reasonable concern because in most search problems, stopping as soon as every nearby move is worse can get you stuck at a local optimum. Imagine climbing through a hilly landscape in fog. You reach a point where every direction around you goes downhill, so you stop. But there could still be a much taller mountain somewhere else. So why doesn't the same thing happen with simplex?

### Why Simplex Always Works

**10:23** · The answer comes from the shape of a linear program. Every constraint is linear.

**10:30** · And when you put those constraints together, the feasible region is convex.

**10:35** · That means if you take any two points inside the region and draw a straight line between them, that entire line stays inside the region. There are no gaps or dents where the line can leave the feasible region and then come back in. The objective is linear as well. So imagine we're standing at a corner where every edge leading away from it makes the objective worse. Now suppose there were some other corner somewhere else in the region with a higher profit.

**11:03** · Because the region is convex, we could draw a straight path from our current corner to that better one without ever leaving the feasible region. And because the objective is linear, profit would increase steadily as we moved along that path. If the other corner really were better, then even the first small move in its direction would have to improve profit. But at a corner, any direction we can move while staying inside the feasible region is built from the edges leaving that corner.

**11:35** · If every one of those edges makes profit worse, there can't be some other feasible direction that secretly makes it better. So, one simplex reaches a corner with no improving edge, it isn't just the best corner nearby, it's a global optimum.

**11:53** · That's why simplex can move through the problem one corner at a time without having to check every corner. At each step, it only needs information about the current solution and the directions available from there. But, the geometry of a linear program guarantees that when there are no improving moves left, there's no better solution hiding somewhere else. And that same geometric structure shows up in far more problems than just our little workshop.

**12:19** · Linear programs show up any place where the objective and the constraints can be written as linear relationships, and that covers a surprisingly large range of problems. The airline example from the beginning is one of them. You can represent possible assignments with variables, use constraints to enforce things like flight coverage and crew rules, and then minimize the total cost.

### Simplex: Applications & Limits

**12:46** · The real version may have thousands or even millions of variables, but mathematically it's still the same kind of problem we just solved with chairs and tables. They also appear in problems that don't immediately look like scheduling or planning.

**13:01** · Suppose you want to match one distribution to another as cheaply as possible, like figuring out the minimum amount of work needed to move one pile of material into the shape of another.

**13:11** · That can be written as a linear program, too. The same idea appears in optimal transport and in ways of measuring the distance between probability distributions. Linear programming also sits inside harder optimization problems. If some of the variables have to be whole numbers, like the number of planes to buy or factories to open, solvers will often begin by ignoring that requirement and solving the corresponding linear program.

**13:39** · That solution gives them information they can use while searching for the best integer solution. And solving the linear program can tell you more than just what to produce. The constraints can have values associated with them that tell you how much the objective would improve if you had a little more of a limited resource. In our workshop, for example, that could tell us what one additional plank of wood or one additional hour of labor is worth. Those values are usually called shadow prices.

**14:10** · So, if a problem gives you something to maximize or minimize and a set of linear constraints, you already know quite a bit about its structure.

**14:20** · An optimum can be found at a corner of the feasible region. And Simplex gives you a way to search those corners without checking all of them one by one.

**14:30** · Thank you for watching. If you enjoyed this video, please consider subscribing to our channel.