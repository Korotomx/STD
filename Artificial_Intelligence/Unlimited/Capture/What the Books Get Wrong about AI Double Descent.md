![](https://www.youtube.com/watch?v=z64a7USuGX0)

Huge thanks to KiwiCo for sponsoring today’s video! Go to https://www.kiwico.com/welchlabs and use code WELCHLABS for 50% off your first monthly crate or for 20% off your first Panda Crate!  
  
New Book Available Now! The Welch Labs Illustrated Guide to AI (30:47):  
https://www.welchlabs.com/resources/ai-book-ezrzm-msrmc  
  
Sections  
0:00 - Intro  
3:43 - AlexNet & Overfitting  
5:19 - Overfitting  
6:45 - Rethinking Generalization  
11:05 - KiwiCo is Awesome  
12:28 - The Double Descent Hypothesis  
13:57 - Double Descent is Real!  
16:01 - Double Descent with Polynomial Curvefitting?!  
20:36 - But why?  
22:35 - Should I throw out my books?  
24:28 - The Bias-Variance Tradeoff  
28:30 - My take  
30:47 - I’ve written a new book on AI!  
  
Books with U-shaped test set error curves:  
Murphy, Kevin P. Probabilistic machine learning: an introduction. MIT press, 2022.  
Goodfellow, Ian, et al. \*Deep learning\*. Vol. 1. No. 2. Cambridge: MIT press, 2016.  
Russell, Stuart Jonathan, and Peter Norvig, eds. \*Prentice Hall series in artificial intelligence\*. Englewood Cliffs, NJ:: Prentice Hall, 1995.  
Bishop, Christopher M., and Nasser M. Nasrabadi. \*Pattern recognition and machine learning\*. Vol. 4. No. 4. New York: springer, 2006.  
Learning, Machine. "Tom mitchell." \*Publisher: McGraw Hill\* (1997): 31.  
Hastie, Trevor, Robert Tibshirani, and Jerome Friedman. "The elements of statistical learning." (2009).  
Hastie, Trevor, Robert Tibshirani, and Jerome Friedman. "An introduction to statistical learning." (2009).  
Abu-Mostafa, Yaser S., Malik Magdon-Ismail, and Hsuan-Tien Lin. \*Learning from data\*. Vol. 4. New York: AMLBook, 2012.  
MacKay, David JC. \*Information theory, inference and learning algorithms\*. Cambridge university press, 2003.  
  
Harvard Team’s code & results:  
https://gitlab.com/harvard-machine-learning/double-descent  
  
Great repo showing polynomial double descent:  
https://github.com/RylanSchaeffer/Stanford-AI-Alignment-Double-Descent-Tutorial  
  
Technical Notes  
\- 26:25 For these linear fits, we’re using N=15 instead of N=5 points. This increases the bias and reduces the variance of these fits, making the bias variance trade-off more clear, but also pushes out the interpolation threshold. Full results are here: https://github.com/stephencwelch/manim\_videos/blob/master/\_2025/generalization/Final Video Polynomial Examples.ipynb  
\- 27:38 It’s tricky to show the full bias-variance results here, as the variance explodes ad Degree=4. Instead we’ve chosen to show qualitative breakdowns, showing which terms dominate the overall error at each degree. Full results can be seen here: https://github.com/stephencwelch/manim\_videos/blob/master/\_2025/generalization/Final%20Video%20Polynomial%20Examples.ipynb  
  
Special Thanks to Patrons https://www.patreon.com/welchlabs  
Juan Benet, Ross Hanson, Yan Babitski, AJ Englehardt, Alvin Khaled, Eduardo Barraza, Hitoshi Yamauchi, Jaewon Jung, Mrgoodlight, Shinichi Hayashi, Sid Sarasvati, Dominic Beaumont, Shannon Prater, Ubiquity Ventures, Matias Forti, Brian Henry, Tim Palade, Petar Vecutin, Nicolas baumann, Jason Singh, Robert Riley, vornska, Barry Silverman, Jake Ehrlich, Mitch Jacobs, Lauren Steely, Jeff Eastman, Rodolfo Ibarra, Clark Barrus, Rob Napier, Andrew White, Richard B Johnston, abhiteja mandava, Burt Humburg, Kevin Mitchell, Daniel Sanchez, Ferdie Wang, Tripp Hill, Richard Harbaugh Jr, Prasad Raje, Kalle Aaltonen, Midori Switch Hound, Zach Wilson, Chris Seltzer, Ven Popov, Hunter Nelson, Amit Bueno, Scott Olsen, Johan Rimez, Shehryar Saroya, Tyler Christensen, Beckett Madden-Woods, Darrell Thomas, Javier Soto, U007D, Caleb Begly, Rick Rubenstein, Brent Hunsaker, Dan Patterson, Tchsurvives, Alex Adai, Walter Reade, Zyansheep, Walter Reade, Duncan Stannett, Reginald Carey, Jean-Manuel Izaret, dh71633, Adrian Rodriguez, Dimitar Stojanovski, Michael Harder, Peter Maldonado, Emily Pesce, David Johnston, Insang Song, FaeTheWolf, Stephen Taylor, KittenKaboodle, EMatter, PATRICKMCCORMACK, John Beahan, Cameron, Cole Jones, Garrett Thornburg, Jeroen W, Rohit Sharma, GlennB, Emmanuel Cortes, Katie Quinn, Karina C, Cakra WW, Mike Ton, Eric Gometz, MacCallister Higgins, Niko Drossos, David Eraso, Tom Zehle, Steve, Brian Lineburg, rjbl, Michael Loh, Perry Vais, Bengal0, Farhad Manjoo, Sara Chipps, Ellis Driscoll, William Taysom, Will Harmon, CK, Abdullah, Peter Cho, Leo Nikora, Griffin Smith, Ash Katnoria, Alex, Markus Hays Nielsen  
  
Special thanks to: Mikhail Belkin, Preetum Nakkiran, Emily Zhang, Varun Reddy  
  
Code for Welch Labs Videos: https://github.com/stephencwelch/manim\_videos  
  
Written by: Stephen Welch  
Produced by: Stephen Welch, Sam Baskin, and Pranav Gundu  
  
Premium Beat IDs  
EEDYZ3FP44YX8OWT  
CFAQJOTYQHT7JYIT

## Transcript

### Intro

**0:00** · This video is sponsored by KiwiCo. More on them later. Also, I've written a whole new book on AI. You can learn more about the book at the end of this video.

**0:10** · When I first learned machine learning, these three books were incredibly helpful. But they're also all wrong.

**0:17** · Each book has a version of the same plot. A core tenant of machine learning theory and practice.

**0:23** · The x-axis shows the size of a learning model. And the y-axis shows the model's performance, measured using some type of error metric.

**0:32** · From here, we plot two curves. The first curve shows the model's performance on its training data.

**0:38** · As our model becomes larger, it's able to learn more complex patterns, better fit its training data, and bring down its error.

**0:46** · Of course, what we really care about here is how well our model will perform on examples outside of its training set.

**0:53** · Our second curve shows the same error metric, but measured on a test set that the model hasn't seen before.

**0:59** · Again and again, in every book, the test set error curve has the same U shape.

**1:05** · Our testing set error starts high for smaller models, comes down to a nice minimum for some medium-size model, and shoots back up as the size of our model continues to grow.

**1:16** · The shooting back up part of the testing curve is due to the model overfitting the data.

**1:22** · Many authors demonstrate the overfitting phenomenon using polynomial curve fitting.

**1:27** · If we take a set of data points, for example, this set of parabola-shaped points, and set aside half of our data for testing, and fit a first-order polynomial, which is just a line, our curve fit will be poor.

**1:41** · We can measure just how bad our fit is by taking the differences between our fit line and our training points.

**1:47** · Squaring and averaging these errors together, we get the mean squared error of our linear model on our training set.

**1:55** · We can repeat this process on our test set points to compute our test set error.

**2:00** · Both our training and testing errors are relatively high because our simple linear model is not powerful enough to fit our parabola shaped data.

**2:09** · Moving to a second order polynomial, our parabolic model is now able to nicely fit our parabolic data.

**2:16** · Bringing down our training and testing error.

**2:21** · Fitting a third order model, our cubic curve is able to get very close to our training points, bringing down the error on our training set.

**2:29** · But starts to fit the noise in our data instead of the underlying parabolic shape.

**2:35** · Resulting in worse performance on our test set.

**2:39** · Moving to a fourth order polynomial, over-fitting becomes even worse.

**2:44** · Our more powerful model is able to now perfectly fit our noisy data with zero training error.

**2:50** · But results in wild curve fits and worse test set performance.

**2:54** · And our resulting errors line up with the characteristic U-shaped testing error curve.

**3:00** · This central idea is often known as the bias-variance tradeoff and is named after a nice piece of statistical theory that supports the idea that our test set curve should be U-shaped.

**3:12** · The takeaway for a whole generation of machine learning practitioners was that we must carefully limit the power of our models to match the complexity of our data to avoid over-fitting.

**3:24** · Our U-shaped test error curve, supported by the bias-variance tradeoff theory, feels disciplined. It feels responsible.

**3:33** · It's telling us that the core of machine learning is about balance, but it's also wrong.

**3:42** · In 2012, Alex Krizhevsky, Ilya Sutskever, and Geoff Hinton successfully trained what was then considered an enormous classification neural network with around 16 million parameters, that today we call AlexNet.

### AlexNet & Overfitting

**3:57** · Overfitting was a significant concern for the AlexNet team.

**4:01** · To reduce overfitting, the team used data augmentation, applying random shifts, flips, and color changes to their images while training.

**4:10** · And used a new technique called dropout, where collections of neurons are randomly turned off during training.

**4:17** · Both data augmentation and dropout forced AlexNet to learn more robust and general ways to classify images that don't depend on exactly how an image appears or a specific pathway through the network.

**4:30** · And the team found that without data augmentation and dropout, the model exhibited substantial overfitting.

**4:38** · The team also used a technique called weight decay, where the model is penalized for having large weight values.

**4:45** · If we apply the same weight decay approach to one of our overfit polynomials from earlier, we see that as we increase the amount of weight decay, our fit becomes smoother, reducing overfitting.

**4:56** · In statistics, this is known as ridge regression.

**4:59** · Data augmentation, dropout, and weight decay are all examples of regularization techniques, where we modify the training process to prevent our model from overfitting the data.

**5:11** · These techniques were seen as critical back in 2012 and remain very common practice in machine learning today.

**5:17** · The takeaway for many machine learning practitioners at the time, myself included, was that large neural networks were clearly in the overfitting region of the bias-variance curve.

### Overfitting

**5:27** · And that without regularization, these models would dramatically overfit, effectively memorizing their training examples without learning the robust pattern recognizers needed to generalize to new examples.

**5:40** · And that through regularization, we could push these models back towards the happy middle of the curve.

**5:46** · A sneakier and more subtle conclusion, one that I certainly internalized at the time, is that in the over-fitting regime, lower training set error is causally linked to higher test set error.

**5:59** · This implication even shows up in the name we've chosen for the phenomenon.

**6:03** · Over-fitting implies that we're doing too much fitting of the training data.

**6:08** · And that doing too much fitting, lowering our training set error too much, is causing something bad. In this case, leading to higher test set error.

**6:19** · AlexNet was a wild success, and deep learning exploded over the next few years, with larger and deeper models delivering more and more impressive results.

**6:29** · We would expect models larger and more complex than AlexNet to require more aggressive regularization to avoid over-fitting.

**6:37** · But this turned out not to be the case, with deep learning continuing to generalize suspiciously well, even without aggressive regularization measures in place.

### Rethinking Generalization

**6:47** · In 2016, a team at Google Brain addressed this apparent contradiction head-on, in a brilliantly insightful paper called "Understanding Deep Learning Requires Rethinking Generalization".

**6:59** · To test the extent to which we can actually control over-fitting in deep models, the Google Brain team devised a clever experiment, where they took the same ImageNet data set that AlexNet was trained on, and the smaller CIFAR image classification data set, and completely randomized all the labels, and trained models to predict these random labels.

**7:21** · So, one cat in the ImageNet data set would be labeled as an aircraft carrier, and the next cat would be labeled as a sea snake, and so on.

**7:29** · The only way for a model to do well in this training data is to dramatically over-fit, or essentially memorize each example.

**7:37** · This exact cat image is an aircraft carrier. This exact cat image is a sea snake, and so on.

**7:44** · Because the labels are randomized, there are no deeper patterns to learn.

**7:48** · All noise, no signal.

**7:52** · Now, if regularization was actually preventing deep models from over-fitting, as was widely believed, we would expect a regularized deep model to not learn these randomly assigned labels, resulting in poor performance on the training set.

**8:08** · Shockingly, the team showed that deep models were able to perfectly memorize all 50,000 training images in the CIFAR data set, and almost all of the 1.3 million training examples in the ImageNet data set, even with regularization in place.

**8:25** · These models, of course, performed terribly on their test sets, performing no better than random guessing.

**8:32** · So, deep models, even with regularization in place, are perfectly capable of just memorizing their training data.

**8:40** · However, when we switch back to the correct labels, the same models with the same training procedures do not memorize, and instead learn robust patterns that do generalize to new data.

**8:52** · The Google Brain team also showed that when learning from the correct labels, contrary to the AlexNet team's findings, regularization was not actually critical to avoid over-fitting.

**9:04** · By 2016, more efficient and flexible deep architectures than AlexNet had been developed.

**9:10** · The Google Brain team trained a newer Inception v3 architecture on the same ImageNet data set that AlexNet was trained on, and observed that when they removed data augmentations, dropout, and weight decay, the model's test set performance did decrease, but only modestly.

**9:28** · And they also found that an Inception v3 model trained without any explicit regularization performed on par with the original AlexNet results.

**9:37** · And even more interesting, when regularization did make these modest improvements to test set accuracy, it had very limited or apparently no impact on training set error.

**9:49** · As we would expect if regularization was moving our model back towards the center of the bias variance curve.

**9:57** · These models trained on the CIFAR data set show an increase in the test set accuracy from around 86% to 89% when adding different types of regularization.

**10:07** · But all four models still perfectly fit the training data with accuracies of 100%.

**10:14** · These results dramatically call into question the fundamental trade-off between training set and test set performance predicted by the typical bias variance curves in the over fitting region.

**10:26** · Returning to our polynomial curve fitting example, this model behavior is analogous to our curve somehow exactly fitting our noisy observations while still effectively learning the underlying parabolic shape and performing well on our testing points.

**10:42** · Exactly fitting the training data is known as the model interpolating the data.

**10:48** · So, what's going on here? Does the bias variance trade-off simply not apply to deep models?

**10:55** · Do we even need to worry about over fitting when training deep neural networks?

**10:59** · And should I throw away all of my statistics and machine learning books?

### KiwiCo is Awesome

**11:05** · Whenever I think about learning versus memorization, I can't help but think about how my own children are learning.

**11:11** · Which is why I was more than happy to partner again with this video sponsor KiwiCo.

**11:16** · KiwiCo makes hands-on project kits that make learning genuinely fun for kids of all ages.

**11:22** · My son just turned two this summer and he's exploding with curiosity.

**11:27** · I love these puzzles that promote spatial reasoning and they're incredibly engaging. Even later that day when we were watching TV, he kept sneaking off to work on the puzzles. I loved this.

**11:39** · The thoughtfulness the KiwiCo team puts into the crates really makes them so much stickier than many of the toys we have.

**11:46** · I was worried that this pirate treasure crate was a little too old for my daughter, but I was delighted when she was able to understand the treasure map that we drew together, and was able to follow the map to the right part of the house. Creating and reading maps like this takes some serious abstract reasoning. It was amazing to see.

**12:04** · KiwiCo makes amazing gifts for the kids and families in your life.

**12:08** · And they make awesome learning experiences for kids of all ages.

**12:12** · Use my code Welch Labs to receive 50% off your first crate for kids three and older, or 20% off your first Panda Crate for kids under three.

**12:20** · Big thanks to KiwiCo for sponsoring this video. Now, back to what's really going on with the bias-variance tradeoff.

### The Double Descent Hypothesis

**12:29** · In 2018, a team of researchers led by Mikhail Belkin proposed an interesting alternative explanation of what's going on here.

**12:37** · What if the traditional bias-variance tradeoff wasn't exactly wrong, but wasn't the full picture?

**12:44** · What would happen to the bias-variance curve if we just kept increasing the size of our models well beyond the overfitting regime?

**12:53** · Are there certain combinations of models and data where we would actually see the testing set error come back down?

**12:59** · Is there something beyond overfitting?

**13:03** · The team showed some compelling small-scale demonstrations of exactly this phenomenon on the MNIST handwritten digit data set.

**13:11** · Using a random Fourier feature model, this is essentially a small two-layer neural network where only the final layer is trained.

**13:19** · The team showed that these models would demonstrate the classical bias-variance tradeoff curve, but then suddenly shift to a new regime as model size increased further.

**13:29** · With test set performance improving dramatically, and actually exceeding the test set performance found in the classical regime.

**13:37** · The team called the phenomenon double descent.

**13:41** · Their hypothesis was compelling, but it remained to be seen if the double descent phenomenon could be replicated in full-scale deep models.

**13:49** · And exactly what underlying mechanisms could be causing this unexpected behavior.

**13:55** · The following year, in 2019, a Harvard and OpenAI team definitively showed that double descent was real.

### Double Descent is Real!

**14:02** · Demonstrating the phenomenon across a variety of model architectures, including transformers, on both vision and language data sets.

**14:11** · Interestingly, the team observed double descent behavior not only as a function of the size of their models, but as a function of how long their models were trained for.

**14:21** · This observation is potentially highly relevant for machine learning practitioners.

**14:26** · It's very common to visualize test set error while training, and stop training when test set error stops coming down.

**14:34** · It's also common to see test set error start to trend up later in training.

**14:39** · This would typically be interpreted as the model beginning to overfit its training data.

**14:44** · But what the Harvard team found, remarkably, was that for certain models and data sets, if you just kept training the model, the testing error would follow a double descent behavior, coming back down. In some cases to an even lower value.

**14:59** · If you were training one of these models and assumed a classical bias-variance tradeoff behavior, you would likely stop training long before you saw the double descent.

**15:09** · I should note here that the plots we've seen so far from the Harvard team's work include a small amount of added label noise on the CIFAR data set.

**15:17** · This makes the model more likely to overfit, and the double descent curve more pronounced.

**15:22** · We still see double descent without the added noise, but it's less dramatic.

**15:27** · CIFAR is a very clean academic data set, so you could argue that adding label noise is a reasonable proxy for larger, noisier data sets.

**15:37** · So, double descent is a real phenomenon, but why would models behave like this?

**15:42** · To me, seeing this behavior while training is especially confounding.

**15:46** · Why would models start overfitting while training only for the trend to reverse after undergoing more of the same training process?

**15:55** · Let's return to our curve fitting example one last time.

**15:59** · Remarkably, it turns out that double descent can also occur with simple polynomial curve fitting.

### Double Descent with Polynomial Curvefitting?!

**16:06** · We saw earlier that a second-order curve nicely fits our noisy parabolic data.

**16:11** · And this puts us nicely at the bottom of our bias-variance curve.

**16:15** · If we increase the order of our polynomial to three, we begin to overfit. With our training error dropping close to zero, but our testing error shooting up.

**16:25** · When we reach a fourth-order polynomial, our test error continues to increase and our training error goes to zero.

**16:33** · Our fourth-order curve has five free parameters that are able to exactly fit our five data points.

**16:40** · This is analogous to our image classification models exactly fitting or interpolating their training data.

**16:47** · This point is known as the interpolation threshold and corresponds to the smallest model that is capable of perfectly fitting our data.

**16:55** · Now, moving to a fifth-order polynomial, our situation changes a little.

**17:01** · Our polynomial is still able to perfectly fit our training data, but because our curve has six free parameters, but we still only have five training points, this means that there will actually be an infinite number of fifth-order polynomials that perfectly fit our five training points.

**17:17** · Here's 100 different fifth-order polynomials that perfectly fit our data.

**17:23** · How does our curve-fitting algorithm choose which curve to go with?

**17:28** · It turns out that there's a fairly natural closed-form matrix inversion solution that extends how we handle the earlier cases.

**17:36** · The solver will effectively choose the curve with the smallest sum of squared coefficients.

**17:42** · For example, this more chaotic curve fit corresponds to this polynomial with these six coefficients.

**17:48** · And the simpler curve corresponds to this polynomial.

**17:53** · If we take each coefficient from our first curve's equation, square these values and add them together, we get 19.13.

**18:01** · This value is known as the L2 norm squared of our coefficients.

**18:06** · Performing the same computation on our second polynomial, we get a smaller norm, 7.04.

**18:13** · So, our solver would choose our second curve over our first.

**18:17** · Out of all the possible fifth-order curve fits, our second curve turns out to be the lowest norm solution.

**18:25** · So, this is the curve our solver would return.

**18:28** · Just like our fourth-order curve, our fifth-order curve perfectly interpolates our training data, resulting in zero training error.

**18:36** · However, our fifth-order curve is a bit less chaotic. And if we measure its test set error, we see that it's actually lower than our fourth-degree polynomial's test set error, starting to create double descent behavior.

**18:51** · Now, there's an important technical point here about how exactly we set up our solver.

**18:56** · Expressing our polynomial as ax to the fifth plus bx to the fourth and so on, turns out to create numeric instability for our solver, especially as the degree of our polynomial grows.

**19:07** · It's common to instead use what's known as a different polynomial basis.

**19:12** · Here, we're are using the Legendre basis.

**19:14** · The curve fitting model is still a fifth order polynomial, but rearranged in a way where our coefficients multiply what are known as the Legendre polynomials.

**19:24** · These polynomials have nice mathematical properties that make curve fitting more stable.

**19:29** · We can rearrange our Legendre polynomial representation into our typical ax to the fifth plus bx to the fourth representation.

**19:36** · But importantly, the coefficients our solver actually uses when fitting our curve are different.

**19:42** · Meaning that the minimum norm solution is different.

**19:45** · And if we use a standard ax to the fifth plus bx to the fourth polynomial representation, and we pick a minimum norm solution, we do not see double descent behavior.

**19:56** · I'll put some links about this in the video description.

**19:59** · So depending on our exact curve fitting procedure, our solver will pick a minimum norm solution in our chosen polynomial basis.

**20:06** · And some common choices of basis do exhibit double descent.

**20:11** · Jumping to a tenth order fit, we have an enormous range of possible solutions.

**20:17** · Here's a hundred of them.

**20:19** · Some of these curves catastrophically overfit our data.

**20:23** · However, again, our smallest norm constraint chooses a smoother curve that actually kind of looks like a squiggly version of our parabola, and again brings down our test set error, giving us more nice double descent behavior.

### But why?

**20:38** · Now, why does our polynomial curve fitting process demonstrate this perhaps surprising double descent behavior?

**20:45** · Our worst generalizing fit is precisely at the interpolation threshold, where our model exactly fits our training data for the first time.

**20:54** · In this case, we have exactly as many constraints as we have variables, meaning there's only one unique curve we can fit. And our model is forced to contort itself exactly to the data, and is more susceptible to noise.

**21:07** · Unlike in our higher order fits, where our solver has many curves to choose from and it can pick a smoother lower norm solution.

**21:15** · The Harvard team lays out a similar line of thinking when reasoning about why double descent occurs in deep neural networks.

**21:22** · For model sizes at the interpolation threshold, there is effectively only one model that fits the training data.

**21:29** · And this interpolating model is very sensitive to noise in the train set.

**21:34** · For over parameterized models, there are many interpolating models that fit the training set.

**21:39** · And SGD is able to find one that memorizes or absorbs the noise while still performing well on the distribution.

**21:46** · SGD here refers to the stochastic gradient descent algorithm used to train deep neural networks.

**21:53** · This algorithm works very differently than the solvers we used in our curve fitting example.

**21:58** · But has interestingly been shown to arrive at norm minimizing solutions under certain constraints.

**22:04** · Just as our curve fitting solvers do.

**22:07** · So, as we train larger models or train models for longer, when these models are near the interpolation threshold, where they're just able to perfectly fit the training data for the first time, the model has less flexibility and is more likely to overfit.

**22:22** · As we move to larger models or train for longer, our model has more flexibility and our training algorithm is able to choose smoother less chaotic solutions that will better generalize to new data.

### Should I throw out my books?

**22:35** · So, should we throw out the bias-variance tradeoff and should I throw away all my books?

**22:41** · The first book we showed at the beginning of the video, The Elements of Statistical Learning, which is a great book by the way, was written by three Stanford statistics professors in the early 2000s.

**22:53** · After double descent gained notoriety in 2018 and 2019, the book's first author, Trevor Hastie, co-authored a massive 70-page paper looking into the phenomenon.

**23:04** · He titled the paper Surprises in High-Dimensional Ridge-less Least Squares Interpolation.

**23:09** · In 2021, Hastie and his co-authors published a new edition of Introduction to Statistical Learning, which is in many ways a successor to his original book.

**23:20** · The familiar U-shaped bias-variance curves are still prominently featured in the opening chapters of the book, but there is a new section on double descent in chapter 10.

**23:29** · In this chapter, Hastie and his present the double descent phenomenon and argue that it does not contradict the bias-variance trade-off.

**23:38** · Their argument centers around the way we're measuring the size or complexity of our learning model.

**23:44** · In our polynomial double descent example, our x-axis corresponds to the degree of our polynomial.

**23:51** · Hastie and his co-authors essentially argue that after we pass the interpolation threshold, the degree of our polynomial is no longer the right measure for model complexity.

**24:01** · They also use a somewhat different nomenclature, calling their measure flexibility.

**24:07** · This is a fair point. As we saw in our polynomial curve fitting example, once we pass the interpolation threshold, we have many possible fits to choose from.

**24:17** · And when our solver picks the lowest norm curve, the result is in many ways simpler than the curve we get at the interpolation threshold, where we only have one choice.

### The Bias-Variance Tradeoff

**24:28** · The variance in the bias-variance trade-off refers to a specific statistical measure of the variability of our fit.

**24:36** · Here's our second-order curve fit from earlier.

**24:39** · Now, if we take a different random sample of our underlying parabola and refit our second-order polynomial, we get a slightly different fit, like this.

**24:49** · Here's a third data sample and fit.

**24:52** · And here's 50 more second-order fits from different random samples.

**24:57** · From here, we can compute the mean and standard deviation across all these fits.

**25:02** · Here the shaded region corresponds to one standard deviation above and below the mean fit.

**25:08** · Our average fit is quite close to our true underlying parabola.

**25:13** · The difference between these two curves is the bias in the bias variance tradeoff.

**25:18** · Note that we need to know the true underlying function to compute bias. And in practice we generally do not know this function.

**25:25** · So as we've seen the bias variance tradeoff and U-shaped testing error curve are typically conceptual tools.

**25:32** · We can't actually compute bias for most of the problems that we care about.

**25:36** · The variance in the bias variance tradeoff is proportional to the yellow shaded region squared and measures the variability of our various fits.

**25:46** · Now returning to our test set error measurements, we can see a really compelling part of bias variance theory.

**25:53** · It turns out that for a given fit, we can decompose our overall test set error into a sum of our bias squared, our variance, and a final irreducible error term.

**26:05** · For our second order fit, our largest error component is our variance.

**26:10** · So our theory is telling us here that the majority of our error is coming from the variability of our fits that result from the randomness of our data.

**26:19** · Shifting to a first order fit, here's a hundred different linear fits based on different samples of our underlying parabola.

**26:27** · Taking our mean and standard deviation as we did before, we see that unlike our second order fit, our average fit is now quite far from our target parabola function, leading to a high bias.

**26:40** · This high bias means that our model is unable to fit the actual underlying function.

**26:46** · Moving to our third order fits, these polynomials are more sensitive to the noise in our data. Here's a hundred different fits based on different random samples of our underlying parabola.

**26:56** · Collapsing these into a mean and standard deviation, we see that our bias isn't too bad, but our variance is enormous.

**27:04** · This means that our test set error in our third-order case is dominated by our variance term.

**27:10** · This classic U-shaped section of our error plot nicely demonstrates the bias-variance tradeoff. Our first-order fit is unable to match our underlying parabola and has a large bias.

**27:21** · As we increase the order of our fit, our bias comes down, but our variance increases as our models become more sensitive to noise.

**27:29** · As we cross the interpolation threshold, our fourth- and fifth-order fits are also very sensitive to the noise in our random samples, meaning variance is our primary source of error.

**27:41** · However, after we pass our interpolation threshold, as we've seen, our solver is able to choose smoother, lower norm solutions.

**27:49** · This brings down the overall variance of our fits, bringing down our average error, and creating the double descent behavior.

**27:57** · So, while it's certainly still possible to decompose our errors into bias and variance components at and beyond the interpolation threshold, the tradeoff between bias and variance is no longer the primary driver of changes in test set error, as it is in the classical U-shaped region of our curve.

**28:17** · So, as Hastie and his co-authors state, technically, the bias-variance tradeoff theory does not mean that our curve has to be U-shaped.

**28:25** · And the shape of our curve will depend on how we measure the flexibility or capacity of our models.

### My take

**28:31** · However, when every presentation of this central theory in all the books and lectures you see presents the same U-shape, it's hard to not internalize this U-shape as what the theory really says.

**28:43** · That was certainly my experience when learning the subject. And overfitting in this fundamentally U-shaped and formed much of my work in machine learning for years.

**28:52** · It's such a nice little mental model.

**28:54** · I was really shocked when I learned that this picture was incomplete in such an important way.

**29:00** · When researching this video, I had a chance to chat with Mikhail Belkin, the lead author of the double descent paper.

**29:06** · Mikhail told me how nerve-racking it was to challenge such a prominent and widely held theory.

**29:12** · And that he and his co-authors sought out some extra opinions before publishing.

**29:17** · It's just so easy to accept and in this case over-generalize theories like this.

**29:22** · Especially when they fit so nicely into a simple mental image.

**29:26** · It's really important to note here that double descent behavior is not universal.

**29:31** · For plenty of data sets and models, testing error will just continue to increase with model size and never come back down.

**29:38** · Double descent depends on a number of factors, including the level of noise in the data set, and critically depends on how a given model handles the over-parameterized case, where many available solutions perfectly fit the data.

**29:51** · This is known as the inductive bias of a given model.

**29:55** · Deep models appear to have an incredibly friendly inductive bias. They're clearly capable of catastrophic over-fitting, but somehow generalize incredibly well in practice.

**30:06** · As Simon Prince says in his great book on deep learning, "If the efficient fitting of neural networks is startling, their generalization to new data is dumbfounding."

**30:17** · Deep learning theory is still very much catching up to practice. It's like we're observing some new phenomenon of nature.

**30:24** · One that is remarkably capable of acting quite intelligently, and we're trying to figure out how it works.

**30:30** · If the bias-variance tradeoff is like Newtonian physics, it feels like we're getting glimpses of Einstein's general relativity with double descent.

**30:38** · I'm really looking forward to seeing how the theories develop in the coming years.

**30:43** · But for now at least, I'm going to hang on to my books.

### I’ve written a new book on AI!

**30:48** · If you're looking for a new book to hang on to, check out the Welch Labs Illustrated Guide to AI. It's coming out later this year.

**30:56** · This is the book I've always wanted to write.

**30:59** · We really leaned into the visuals. The book has hundreds of figures. I especially like these full-page spreads.

**31:06** · This one shows how loss landscapes are computed.

**31:10** · On the next page into this super high-quality overhead contour plot view of our landscape.

**31:16** · And we show how we might expect our model to work its way through valleys to reach its global minimum.

**31:21** · But it instead creates what looks like a wormhole on our loss landscape.

**31:26** · We're putting a huge amount of effort into each chapter to create these kinds of visuals and deep explanations.

**31:33** · Trying to give the most visceral feel we can for how this stuff really works.

**31:38** · Each chapter includes supporting Python code that walks through the key results from that chapter.

**31:43** · And there's also a supporting GitHub repo as well that's a bit more comprehensive.

**31:49** · At the end of each chapter, you'll also find exercises. We've put a ton of thought into these.

**31:55** · Here's an exercise from the chapter on backpropagation.

**31:58** · Where you're given a small complete neural network. And asked to move some data through the network using a few equations.

**32:05** · Then you're asked to compute the network's gradients. And use your computed gradients to fill in steps in the model's real learning process.

**32:13** · These exercises are designed to get you as hands-on as possible with modern AI.

**32:17** · And solutions are in the back of the book.

**32:20** · Most of the exercises are written or programming. But my favorite is probably this spread that gives you instructions for building your own perceptron machine.

**32:29** · The book starts with a fresh take on the fundamentals. The perceptron, gradient descent, backpropagation, deep models, and AlexNet.

**32:37** · And then he uses this foundation to dive into cutting-edge topics, including neural scaling laws, mechanistic interpretability, and AI image and video generation models like Sora.

**32:48** · Each chapter goes along with a Welch Labs video that came out over the last 18 months.

**32:54** · I really think that the book is the best way to get deeper into each video's topic.

**33:00** · The book is great for self-study, AI courses, or just looks great on your coffee table.

**33:05** · You can pre-order a copy today at welchlabs.com, and book ship on or before December 15th.

**33:12** · Last year we shipped the imaginary numbers book around the same date, but completely sold out of our print run in November.

**33:19** · So, if you want to make sure you get a copy in time for the holidays, I do recommend ordering early.

**33:24** · Finally, I know that many of you live outside the US and are interested in Welch Labs products.

**33:29** · We're only accepting pre-orders currently to US addresses. Me, my family, and my tiny team handle all fulfillment. So, we're still very limited on where we can ship.

**33:39** · You can join our international shipping waitlist at the link in the description.

**33:43** · I don't know yet when we'll be able to offer international shipping, but I promise we're working on it.

**33:49** · Thank you so much for your time and support.

**33:52** · Books and education are really near and dear to my heart.

**33:56** · And we've poured a ton of effort into this book. I really think you're going to like it.

**34:01** · Woo!