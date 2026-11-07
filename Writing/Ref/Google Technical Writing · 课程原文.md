# Google Technical Writing · 课程原文

来源：Google for Developers, Technical Writing courses  
- https://developers.google.com/tech-writing/overview
- https://developers.google.com/tech-writing/one
- https://developers.google.com/tech-writing/two
- https://developers.google.com/tech-writing/error-messages
- https://developers.google.com/tech-writing/accessibility/self-study

> 内容版权归 Google，按 [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) 使用。  
> 本文档是个人学习存档，只读；要改笔记请去 `STDY/Google 技术写作.md`。  
> 抓取日期：2026-11-08。国内镜像：`developers.google.cn`。

## 目录

- [Technical Writing One](#technical-writing-one)
- [Technical Writing Two](#technical-writing-two)
- [Writing Helpful Error Messages](#writing-helpful-error-messages)
- [Tech Writing for Accessibility](#tech-writing-for-accessibility)


# Technical Writing One


## Just enough grammar (optional)

> **Estimated Time:** 10 minutes

This unit provides just enough grammar to understand the remainder of the
course. If you already know some grammar, move on to [Words(https://developers.google.cn/tech-writing/one/words).
Otherwise, read on.

For simplicity's sake, this unit takes a few shortcuts; grammatical topics are
actually wildly more complicated than this unit suggests.

Grammarians don't all agree on the number or types of parts of speech. The
following table focuses on the parts of speech relevant to this course:

| Part of Speech | Definition | Example |
|---|---|---|
| Noun | A person, place, concept, or thing | Sam runs races . |
| Pronoun | A noun that replaces another noun (or larger structure) | Sam runs races. He likes to compete. |
| Adjective | A word or phrase that modifies a noun | Sam wears blue shoes. |
| Verb | An action word or phrase | Sam runs races. |
| Adverb | A word or phrase that modifies a verb, an adjective,
        or another adverb | Sam runs slowly . |
| Preposition | A word or phrase specifying the positional relationship
        of two nouns | Sam's sneakers are seldom on his shelf. |
| Conjunction | A word that connects two nouns or phrases | Sam's trophies and ribbons live only in his imagination. |
| Transition | A word or phrase that connects two sentences | Sam runs races weekly. However , he finishes races weakly. |

### Nouns

Nouns represent people, places, or things. **Judy**, **Antarctica**, and
**hammers** are all nouns, but so are intangible concepts like **robustness**
and **perfection**. In the following example passage, we've formatted the
nouns in bold:

> In the **framework**, an **object** must copy any underlying **values** that
> the **object** wants to change. The **protocol buffers** in the **codebase**
> are huge, so copying the **protocol buffers** is unacceptably expensive.

In programming, you might think of classes and variables as your program's
nouns.

#### Exercise

Identify the six nouns in the following passage:

> C enables programmers to control pointers and memory.
> Great power brings great responsibility.

### Pronouns

Pronouns are an indirection layer—pointers to or substitutions for other nouns
or sentences. For example, consider the following two sentences:

> Janet writes great code. **She** is a senior staff engineer.

In the preceding example, the first sentence establishes **Janet** as a noun.
The second sentence replaces the noun **Janet** with the pronoun **She**.

In the following example, the pronoun **This** replaces an entire sentence:

> Most applications aren't sufficiently tested. **This** is poor engineering.

#### Exercise

Identify the three pronouns in the following passage:

> The cafeteria featured peanut butter and plum jam on rye toast.
> Employees found it awesome and wished they could eat this every day.

### Verbs

A verb is an action word or phrase. When you want to represent the relationship
between two nouns (an actor and a target), the verb does the work. A verb
identifies what the actor does to the target.

Each sentence must contain at least one verb. For example, each of the following
sentences contains a single verb:

- Sakai **prefers** pasta.
- Rick **likes** the ocean.
- Smurfs **are** blue.
- Jess **suffers** from allergies.

Some sentences, such as the following, contain multiple verbs:

- Nala **suffers** from allergies and **sneezes** constantly.
- The program **runs** slowly but **fails** quickly.

Depending on the tense and the conjugation, a verb could consist of one word or
multiple words. For example:

- Tina **was eating** breakfast a few hours ago.
- Tina **is eating** lunch right now.
- Tina **will eat** dinner tonight at 7:00.

#### Exercise

Identify the verbs in the following passage:

> Samantha is coding Operation Bullwinkle in C++. This project
> currently consumes over 80,000 lines of code. She previously
> used Python, but recently gravitated to C++. Samantha leads
> a team of four software engineers, which will grow to six
> software engineers next quarter.

### Adjectives and adverbs

Adjectives modify nouns. For example, in the following passage, notice how the
adjectives modify the subsequent noun:

- Tom likes **red** balloons. He prepares **delicious** food. He fixed **eight** bugs at work.

Most adverbs modify verbs. For example, notice how the adverb
(**efficiently**) in the following sentence modifies the verb (**fixes**):

- Jane **efficiently** fixes bugs.

Adverbs are not necessarily right next to their verb. For example, in the
following sentence, the adverb (**efficiently**) is two words away from the
verb (**fixes**):

- Jane fixes bugs **efficiently**.

Adverbs can also modify adjectives or other adverbs.

#### Exercise

Identify the four adjectives in the following passage:

> Engineering is a great career for a brilliant mind. I know a
> clever engineer who could excel at any intellectual task.

### Prepositions

Prepositions specify the relationship between two things. Some prepositions
answer the question, "*Where* is this thing relative to that other thing?"
For example:

- The submenu lies **under** the menu.
- The definition appears **next to** the term.
- The `print` function falls **within** the main routine.

Other prepositions answer the question, "*When* is this event relative to
that other event?"  For example:

- The program evaluates the addition operation **before** evaluating the subtraction operation.
- The cron daemon executes the script every Tuesday **at** noon.

A few prepositions (for example, **by** and **of**) answer other kinds of
questions about relationships. For example, the following sentence uses
**by** to relate a book to its authors:

- *The C Programming Language* **by** Kernighan and Richie remains popular.

> **Note:** Some English words fall into multiple grammatical categories.  For
> example, although **under** is usually a preposition, **under** can also serve
> as an adverb or adjective depending on context.

#### Exercise

Identify the two prepositions in the following passage:

> Parameters may optionally appear within a URL, after the path.

### Conjunctions and transitions

Conjunctions connect phrases or nouns *within* a sentence; transitions connect
sentences themselves.

The most important conjunctions are as follows:

- And
- But
- Or

For example, in the following sentence, **and** connects "code" with
"documentation," while **but** connects the first half of the sentence
with the second.

> Olivia writes great internal code **and** documentation **but** seldom
> works on open-source projects.

The most important transitions in technical writing are as follows:

- However
- Therefore
- For example

For example, in the following passage, notice how the transitions connect and
contextualize the sentences:

> Juan is a wonderful coder. **However**, he rarely writes sufficient tests.
> **For example**, Juan coded a 5,000 line FFT package that contained only a
> single 10-line unit test.

#### Exercise

Fill in the most appropriate transition:

> Barbara typically studies problems for a long time before writing the first
> line of code. _____________, she spontaneously coded a method the other day
> when she was suddenly inspired.


## Words

> **Estimated Time:** 10 minutes

We researched documentation extensively, and it turns out that the best
sentences in the world consist primarily of words.

### Define new or unfamiliar terms

When writing or editing, learn to recognize terms that might be unfamiliar to
some or all of your target audience. When you spot such a term, take one of the
following two tactics:

- If the term already exists, link to a good existing explanation. (Don't reinvent the wheel.)
- If your document is introducing the term, define the term. If your document is introducing many terms, collect the definitions into a glossary.

### Use terms consistently

If you change the name of a variable midway through a method, your code won’t
compile. Similarly, if you rename a term in the middle of a document, your
ideas won’t compile (in your users’ heads).

The moral: apply the same unambiguous word or term consistently throughout your
document. Once you've named a component **thingy**, don't rename it
**thingamabob**. For example, the following paragraph mistakenly renames
**Protocol Buffers** to **protobufs**:

> Protocol Buffers provide their own definition language. Blah, blah, blah. And
> that's why protobufs have won so many county fairs.

George Fairbanks, a Google software engineer, provides this excellent note about
consistent naming:

| When I encounter two words that seem to be synonyms, I wonder if the author is
trying to signal a subtle distinction that I need to track down and
understand. |

Yes, technical writing is cruel and restrictive, but at least technical writing
provides an excellent workaround. Namely, when introducing a long-winded concept
name or product name, you may also specify a shortened version of that name.
Then, you may use that shortened name throughout the document. For example, the
following paragraph is fine:

> **Protocol Buffers** (or **protobufs** for short) provide their own definition
> language. Blah, blah, blah. And that's why protobufs have won so many county
> fairs.

### Use acronyms properly

On the initial use of an unfamiliar acronym within a document or a section,
spell out the full term, and then put the acronym in parentheses. Put both
the spelled-out version and the acronym in boldface. For example:

> This document is for engineers who are new to the
> **Telekinetic Tactile Network** (**TTN**) or need
> to understand how to order TTN replacement parts
> through finger motions.

You may then use the acronym going forward, as in the following example:

> If no cache entry exists, the Mixer calls the **OttoGroup Server** (**OGS**)
> to fetch Ottos for the request. The OGS is a repository that holds all
> servable Ottos. The OGS is organized in a logical tree structure, with a root
> node and two levels of leaf nodes. The OGS root forwards the request to the
> leaves and collects the responses.

Do not cycle back-and-forth between the acronym and the expanded version in the
same document.

#### Use the acronym or the full term?

Sure, you can introduce and use acronyms properly, but *should* you use
acronyms?  Well, acronyms do reduce sentence size.
For example, *TTN* is two words shorter than *Telekinetic Tactile Network*.
However, acronyms are really just a layer of abstraction; readers must
mentally expand recently learned acronyms to the full term. For example,
readers convert *TTN* to *Telekinetic Tactile Network* in their heads,
so the "shorter" acronym actually takes a little longer to process than
the full term.

Heavily used acronyms develop their own identity. After a number of
occurrences, readers generally stop expanding acronyms into the full term.
Many web developers, for example, have forgotten what *HTML* expands to.

Here are the guidelines for acronyms:

- Don't define acronyms that would only be used a few times.
- Do define acronyms that meet both of the following criteria:  The acronym is significantly shorter than the full term. The acronym appears many times in the document.

#### Exercise

Fix the following passage. Assume that this passage is the initial instance of
the term **MapReduce** in the document and that **MR** is the best abbreviation.

> Jeff Dean invented MapReduce in 1693, implementing the algorithm on a
> silicon-based computer fabricated from beach sand, wax-paper, a quill pen, and
> a toaster oven. This version of MR held several world performance records
> until 2014.

(Please note that the preceding passage is meant to be humorous, not factual.)

### Recognize ambiguous pronouns

Many pronouns point to a previously introduced noun. Such pronouns are analogous
to pointers in programming. Like pointers in programming, pronouns tend to
introduce errors. Using pronouns improperly causes the cognitive equivalent of a
null pointer error in your readers’ heads. In many cases, you should simply
avoid the pronoun and just reuse the noun. However, the utility of a pronoun
sometimes outweighs its risk (as in this sentence).

Consider the following pronoun guidelines:

- Only use a pronoun *after* you've introduced the noun; never use the pronoun before you've introduced the noun.
- Place the pronoun as close as possible to the referring noun. In general, if more than five words separate your noun from your pronoun, consider repeating the noun instead of using the pronoun.
- If you introduce a second noun between your noun and your pronoun, reuse your noun instead of using a pronoun.

#### It and they

The following pronouns cause the most confusion in technical documentation:

- It
- They, them, and their

For example, in the following sentence, does **It** refer to Python or to C++?

> Python is interpreted, while C++ is compiled. **It** has an almost cult-like
> following.

As another example, what does **their** refer to in the following sentence?

> Be careful when using Frambus or Carambola with HoobyScooby or BoiseFram
> because a bug in **their** core may cause accidental mass unfriending.

#### This and that

Consider two additional problem pronouns:

- This
- That

For example, in the following ambiguous sentence, **This** could refer to
the user ID, to running the process, or to all of these:

> Running the process configures permissions and generates a user ID. **This**
> lets users authenticate to the app.

To help readers, avoid using **this** or **that** in ways where it's not clear
what they refer to. Use either of the following tactics to clarify ambiguous
uses of **this** and **that**:

- Replace **this** or **that** with the appropriate noun.
- Place a noun immediately after **this** or **that**.

Substitute or add explicit terms as needed, as in the following rewrites of the
example's second sentence:

> This user ID lets users authenticate.
> The process of configuring permissions lets users authenticate.
> The combination of permissions and a user ID lets users authenticate.

#### Exercise

Identify all possible meanings for the ambiguous pronouns in each of the
following passages:

1. Aparna and Phil share responsibilities with Maysam and Karan and they are next on call.
2. You may import Carambola data via your configuration file or dynamically at run time. This may be a security risk.


## Active voice vs. passive voice

> **Estimated Time:** 15 minutes

The vast majority of sentences in technical writing should be
in active voice. This unit teaches you how to do the following:

- Distinguish passive voice from active voice.
- Convert passive voice to active voice because active voice is usually clearer.

First, watch this video, just to get the ball
rolling[1](#Footnote1):

### Distinguish active voice from passive voice in simple sentences

In an active voice sentence, an actor acts on a target. That is,
an active voice sentence follows this formula:

> Active Voice Sentence = actor + verb + target

A passive voice sentence reverses the formula. That is, a passive
voice sentence typically follows the following formula:

> Passive Voice Sentence = target + verb + actor

#### Active voice example

For example, here’s a short, active voice sentence:

> The cat sat on the mat.

- Actor: The cat
- Verb: sat
- Target: the mat

#### Passive voice examples

By contrast, here's that same sentence in passive voice:

> The mat was sat on by the cat.

- Target: The mat
- Passive verb: was sat
- Actor: the cat

Some passive voice sentences omit an actor. For example:

> The mat was sat on.

- Actor: *unknown*
- Passive verb: was sat
- Target: the mat

Who or what sat on the mat? A cat? A dog? A T-Rex? Readers can only guess.
Good sentences in technical documentation identify who is doing what to whom.

### Recognize passive verbs

Passive verbs typically have the following formula:

Although the preceding formula looks daunting, it is actually pretty simple:

- A **form of *be*** in a passive verb is typically one of the         following words:          is/are was/were
- A **past participle verb** is typically a plain verb plus the suffix         *ed*.  For example, the following are past participle verbs:          interpreted generated formed

Unfortunately, some past participle verbs are irregular; that is, the past
participle form doesn't end with the suffix *ed*. For example:

- sat
- known
- frozen

Putting the form of *be* and the past participle together yields passive
verbs, such as the following:

- was interpreted
- is generated
- was formed
- is frozen

If the phrase contains an actor, a preposition ordinarily follows the
passive verb. (That preposition is often a key clue to help you spot
passive voice.) The following examples combine the passive verb and
the preposition:

- was interpreted as
- is generated by
- was formed by
- is frozen by

#### Imperative verbs are typically active

It is easy to mistakenly classify sentences starting with an imperative
verb as passive.  An **imperative verb** is a command. Many items in
numbered lists start with imperative verbs.  For example, *Open* and
*Set* in the following list are both imperative verbs:

1. Open the configuration file.
2. Set the `Frombus` variable to `False`.

Sentences that start with an imperative verb are typically in active voice,
even though they don't explicitly mention an actor.  Instead, sentences
that start with an imperative verb *imply* an actor. The implied actor
is **you**.

#### Exercise

Mark each of the following sentences as either **Passive** or **Active**:

1. `MutableInput` provides read-only access.
2. Read-only access is provided by `MutableInput`.
3. Performance was measured.
4. Python was invented by Guido van Rossum in the twentieth century.
5. David Korn discovered the KornShell quite by accident.
6. This information is used by the policy enforcement team.
7. Click the Submit button.
8. The orbit was calculated by Katherine Johnson.

### Distinguish active voice from passive voice in more complex sentences

Many sentences contain multiple verbs, some of which are active and
some of which are passive. For example, the following sentence
contains two verbs, both of which are in passive voice:

Here is that same sentence, partially converted to active voice:

And here is that same sentence, now fully converted to active voice:

#### Exercise

Each of the following sentences contains two verbs.
Categorize each of the verbs in the following sentences as either
active or passive.  For example, if the first verb is active and
the second is passive, write **Active, Passive**.

1. The QA team loves ice cream, but the writers prefer sorbet.
2. Performance metrics are required by the team, though I prefer wild guesses.
3. When software engineers attempt something new and innovative, a reward should be given.

### Prefer active voice to passive voice

Use the active voice most of the time. Use the passive voice sparingly.
Active voice provides the following advantages:

- Most readers mentally convert passive voice to active voice. Why subject your readers to extra processing time? By sticking to active voice, you enable readers to skip the preprocessor stage and go straight to compilation.
- Passive voice obfuscates your ideas, turning sentences on their head. Passive voice reports action indirectly.
- Some passive voice sentences omit an actor altogether, which forces the reader to guess the actor's identity.
- Active voice is generally shorter than passive voice.

Be bold—be active.

#### Scientific research reports (optional material)

Passive voice runs rampant through certain scientific research reports.
In those research reports, experimenters and their equipment often
disappear, leading to passive sentences that start off as follows:

- It has been suggested that...
- Data was taken...
- Statistics were calculated...
- Results were evaluated.

Do we know who is doing what to whom? No. Does the passive voice
somehow make the information more objective? No.

Many scientific journals have embraced active voice. We encourage
the remainder to join the quest for clarity.

#### Exercise

Rewrite the following passive voice sentences as active voice. Only part of
certain sentences are in passive voice; ensure that all parts end up as active
voice:

1. The flags weren't parsed by the Mungifier.
2. A wrapper is generated by the Op registration process.
3. Only one experiment per layer is selected by the Frombus system.
4. Quality metrics are identified by asterisks; ampersands identify bad metrics.


1. "Get the ball rolling" is an idiom that
means "to get something started." [↩](#ref1)


## Clear sentences

> **Estimated Time:** 10 minutes

Comedy writers seek the funniest results, horror writers strive for the
scariest, and technical writers aim for the clearest. In technical writing,
clarity takes precedence over all other rules. This unit suggests a few ways
to make your sentences beautifully clear.

### Choose strong verbs

Many technical writers believe that the verb is the most important part of a
sentence. Pick the right verb and the rest of the sentence will take care of
itself. Unfortunately, some writers reuse only a small set of mild verbs,
which is like serving your guests stale crackers and soggy lettuce every day.
Picking the right verb takes a little more time but produces more satisfying
results.

To engage and educate readers, choose precise, strong, specific verbs.
Reduce imprecise, weak, or generic verbs, such as the following:

- Forms of *be*: is, are, am, was, were, etc.
- Occur
- Happen

For example, consider how strengthening the weak verb in the following
sentences ignites a more engaging sentence:

| Weak Verb | Strong Verb |
|---|---|
| The exception occurs when dividing by zero. | Dividing by zero raises the exception. |
| This error message happens when... | The system generates this error message when... |
| We are very careful to ensure... | We carefully ensure ... |

Many writers rely on forms of *be* as if they were the only spices on the rack.
Sprinkle in different verbs and watch your prose become more appetizing. That
said, a form of *be* is sometimes the best choice of verb, so don't feel that
you have to eliminate every form of *be* from your writing.

Note that generic verbs often signal other problems, such as:

- An imprecise or missing actor in a sentence
- A passive voice sentence

#### Exercise

Clarify the following sentences by picking more specific verbs. Along the way,
feel free to rearrange the sentences and to add, modify, or delete words:

1. When a variable declaration doesn't have a datatype, a compiler error happens.
2. Compiler errors occur when you leave off a semicolon at the end of a statement.

### Reduce there is / there are

Sentences that start with **There is** or **There are** marry a generic noun to
a generic verb. Generic weddings bore readers. Show true love for your
readers by providing a real subject and a real verb.

In the best-case scenario, you may simply delete **There is** or **There are**
(and possibly another word or two later in the sentence). For example, consider
the following sentence:

> There is a variable called `met_trick` that stores the current accuracy.

Removing **There is** replaces the generic subject with a better subject.
For example, either of the following sentences is clearer than the original:

> A variable named `met_trick` stores the current accuracy.
> The `met_trick` variable stores the current accuracy.

You can sometimes repair a **There is** or **There are** sentence by moving the
true subject and true verb from the end of the sentence to the beginning. For
example, notice that the pronoun **you** appears towards the end of the
following sentence:

> There are two disturbing facts about Perl you should know.

Replacing **There are** with **You** strengthens the sentence:

> You should know two disturbing facts about Perl.

In other situations, writers start sentences with **There is** or **There
are** to avoid the hassle of creating true subjects or verbs. If no subject
exists, consider creating one. For example, the following **There is** sentence
does not identify the receiving entity:

> There is no guarantee that the updates will be received in sequential order.

Replacing "There is" with a meaningful subject (such as **clients**) creates
a clearer experience for the reader:

> Clients might not receive the updates in sequential order.

#### Exercise

Clarify the following sentences by removing **There is**,
and possibly rearranging, adding, modifying, or deleting other words:

1. There is a lot of overlap between X and Y.
2. There is no creator stack for the main thread.
3. There is a low-level, TensorFlow, Python interface to load a saved model.
4. There is a sharding function named `distribute` that assigns keys.

### Minimize certain adjectives and adverbs (optional)

Adjectives and adverbs perform amazingly well in fiction and poetry. Thanks to
adjectives, plain old grass becomes **prodigal** and **verdant**, while lifeless
hair transforms into something **lustrous** and **exuberant**. Adverbs push
horses to run **madly** and **freely** and dogs to bark **loudly** and
**ferociously**.  Unfortunately, adjectives and adverbs sometimes make technical
readers bark loudly and ferociously. That's because adjectives and adverbs tend
to be too loosely defined and subjective for technical readers. Worse,
adjectives and adverbs can make technical documentation sound dangerously like
marketing material. For example, consider the following passage from a technical
document:

> Setting this flag makes the application run screamingly fast.

Granted, **screamingly fast** gets readers' attention but not necessarily in a
good way. Feed your technical readers factual data instead of marketing speak.
Refactor amorphous adverbs and adjectives into objective numerical information.
For example:

> Setting this flag makes the application run 225-250% faster.

Does the preceding change strip the sentence of some of its charm? Yes, a
little, but the revamped sentence gains accuracy and credibility.

> **Note:** Don't confuse educating your readers (technical writing) with
> publicizing or selling a product (marketing writing). When your readers
> expect education, provide education; don't intersperse publicity or
> sales material inside educational material.


## Short sentences

> **Estimated Time:** 20 minutes

Software engineers generally try to minimize the number of lines of code in an
implementation for the following reasons:

- Shorter code is typically easier for others to read.
- Shorter code is typically easier to maintain than longer code.
- Extra lines of code introduce additional points of failure.

In fact, the same rules apply to technical writing:

- Shorter documentation reads faster than longer documentation.
- Shorter documentation is typically easier to maintain than longer documentation.
- Extra lines of documentation introduce additional points of failure.

Finding the shortest documentation implementation takes time but is
ultimately worthwhile. Short sentences communicate more powerfully
than long sentences, and short sentences are usually easier to understand
than long sentences.

### Focus each sentence on a single idea

Focus each sentence on a single idea, thought, or concept. Just as statements
in a program execute a single task, sentences should execute a single idea.
For example, the following very long sentence contains multiple thoughts:

> The late 1950s was a key era for programming languages because IBM
> introduced Fortran in 1957 and John McCarthy introduced Lisp the following
> year, which gave programmers both an iterative way of solving problems and
> a recursive way.

Breaking the long sentence into a succession of single-idea sentences yields
the following result:

> The late 1950s was a key era for programming languages.
> IBM introduced Fortran in 1957. John McCarthy invented Lisp the following
> year. Consequently, by the late 1950s, programmers could solve problems
> iteratively or recursively.

#### Exercise

Convert the following overly long sentence to a series of shorter sentences.
Don't revise too much; just end up with a few sentences instead of only one.

> In bash, use the if, then, and fi statements to implement a
> simple conditional branching block in which the if statement
> evaluates an expression, the then statement introduces a block of
> statements to run when the if expression is true, and the fi
> statement marks the end of the conditional branching block.

### Convert some long sentences to lists

Inside many long technical sentences is a list yearning to break free. For
example, consider the following sentence:

> To alter the usual flow of a loop, you may use either a **break** statement
> (which hops you out of the current loop) or a **continue** statement (which
> skips past the remainder of the current iteration of the current loop).

When you see the conjunction **or** in a long sentence, consider refactoring
that sentence into a bulleted list. When you see an embedded list of items or
tasks within a long sentence, consider refactoring that sentence into a
bulleted or numbered list. For example, the preceding example contains
the conjunction **or**, so let's convert that long sentence to the following
bulleted list:

To alter the usual flow of a loop, call one of the following statements:

- `break`, which hops you out of the current loop.
- `continue`, which skips past the remainder of the current iteration of the current loop.

#### Exercise

Refactor the following sentences into something shorter and clearer. Make sure
that your answer contains a list:

1. To get started with the Frambus app, you must first find the app at a suitable store, pay for it using a valid credit or debit card, download it, configure it by assigning a value for the `Foo` variable in the `/etc/Frambus` file, and then run it by saying the magic word twice.
2. KornShell was invented by David Korn in 1983, then a computer scientist at Bell Labs, as a superset of features, enhancements, and improvements over the Bourne Shell (which it was backwards compatible with), which was invented by Stephen Bourne in 1977 who was also a computer scientist at Bell Labs.

### Eliminate or reduce extraneous words

Many sentences contain filler—textual junk food that consumes space without
nourishing the reader. For example, see if you can spot the unnecessary words in
the following sentence:

> An input value greater than 100 causes the triggering of logging.

Replacing **causes the triggering of** with the much shorter verb **triggers**
yields a shorter sentence:

> An input value greater than 100 triggers logging.

With practice, you'll spot the extra words and feel enormous happiness in
removing or reducing them. For example, consider the following sentence:

> This design document provides a detailed description of Project Frambus.

The phrase **provides a detailed description of** reduces to the verb
**describes** (or the verb **details**), so the resulting sentence could become:

> This design document describes Project Frambus.

The following table suggests replacements for a few common bloated phrases:

| Wordy | Concise |
|---|---|
| at this point in time | now |
| determine the location of | find |
| is able to | can |

#### Exercise

Shorten the following sentences without changing their meaning:

1. In spite of the fact that Arnold writes buggy code, he writes error-free documentation.
2. Changing the sentence from passive voice to active voice enhances the clarification of the key points.
3. Determine whether Rikona is able to write code in COBOL.
4. Frambus causes the production of bugs, which will be chronicled in logs by the LogGenerator method.

### Reduce subordinate clauses (optional)

A **clause** is an independent logical fragment of a sentence, which contains an
actor and an action. Every sentence contains the following:

- A main clause
- Zero or more subordinate clauses

Subordinate clauses modify the idea in the main clause. As the name
implies, subordinate clauses are less important than the main clause. For
example, consider the following sentence:

> Python is an interpreted programming language, which was invented in 1991.
> Main clause: Python is an interpreted programming language
> Subordinate clause: which was invented in 1991

You can usually identify subordinate clauses by the words that introduce them.
The following list (by no means complete) shows common words that introduce
subordinate clauses:

- which
- that
- because
- whose
- until
- unless
- since

Some subordinate clauses begin with a comma and some don't. The highlighted
subordinate clause in the following sentence, for example, begins with the
word **because** and does not contain a comma:

> I prefer to code in C++ because I like
> strong data typing.

When editing, scrutinize subordinate clauses. Keep the `one sentence = one idea`,
[single-responsibility principle](https://en.wikipedia.org/wiki/Single-responsibility_principle) 
in mind. Do the subordinate clauses in a sentence *extend* the single idea or
do they *branch off* into a separate idea? If the latter, consider dividing the
offending subordinate clause(s) into separate sentences.

#### Exercise

Determine which of the sentences contain subordinate clauses that should be
branched off into separate sentences. (Don't rewrite the sentences, just
identify the sentences that should be rewritten.)

1. Python is an interpreted language, which means that the language can execute source code directly.
2. Bash is a modern shell scripting language that takes many of its features from KornShell 88, which was developed at Bell Labs.
3. Lisp is a programming language that relies on Polish prefix notation, which is one of the systems invented by the Polish logician Jan Łukasiewicz.
4. I don't want to say that Fortran is old, but only radiocarbon dating can determine its true age.

### Distinguish that from which

**That** and **which** both introduce subordinate clauses.  What's the
difference between them? Well, in some countries, the two words are
pretty much interchangeable. Inevitably though, alert readers
from the United States will angrily announce that you confused the
two words again.

In the United States, reserve **which** for nonessential
subordinate clauses, and use **that** for an
essential subordinate clause that the sentence can't live without.
For example, the key message in the following sentence is that
Python is an interpreted language; the sentence can survive without
*Guido van Rossum invented*:

> Python is an interpreted language, **which** Guido van Rossum invented.

By contrast, the following sentence requires *don't involve linear
algebra*:

> Fortran is perfect for mathematical calculations **that** don't involve
> linear algebra.

If you read a sentence aloud and hear a pause just before the
subordinate clause, then use **which**. If you don't hear a pause,
use **that**.  Go back and read the preceding two example sentences. Do you
hear the pause in the first sentence?

Place a comma before **which**; do not place a comma before **that**.


## Lists and tables

> **Estimated Time:** 15 minutes

Good lists can transform technical chaos into something orderly.
Technical readers generally love lists.  Therefore, when writing,
seek opportunities to convert prose into lists.

### Choose the correct type of list

The following types of lists dominate technical writing:

- Bulleted lists
- Numbered lists
- Embedded lists

Use a **bulleted list** for *unordered* items; use a
**numbered list** for *ordered* items. In other words:

- If you rearrange the items in a *bulleted* list, the list's meaning does not change.
- If you rearrange the items in a *numbered* list, the list's meaning *changes*.

For example, we've made the following a bulleted list because rearranging its
items does not change the list's meaning:

> Bash provides the following string manipulation mechanisms:
> Deleting a substring from the start of a string
> Reading an entire file into one string variable

The following list, by contrast, must be a numbered list because rearranging its
items would change the list's meaning:

> Take the following steps to reconfigure the server:
> Stop the server.
> Edit the configuration file.
> Restart the server.

An **embedded list** (sometimes called a **run-in** list) contains items
stuffed within a sentence. For example, the following sentence contains
an embedded list with four items.

> The llamacatcher API enables callers to create and query llamas, analyze
> alpacas, delete vicunas, and track dromedaries.

Generally speaking, embedded lists are a poor way to present technical
information. Try to transform embedded lists into either bulleted lists or
numbered lists. For example, you should convert the sentence containing
the embedded list into the following passage:

> The llamacatcher API enables callers to do the following:
> Create and query llamas.
> Analyze alpacas.
> Delete vicunas.
> Track dromedaries.

#### Exercise

Convert the following paragraph into one or more lists:

> Today at work, I have to code three unit tests, write a design document, and
> review Janet's latest document. After work, I have to wash my car without
> using any water and then dry it without using any towels.

Don't forget to introduce your list(s).

### Keep list items parallel

What separates effective lists from defective lists?  Effective lists
are parallel; defective lists tend to be nonparallel.  All items in a
**parallel** list look like they "belong" together.  That is, all
items in a parallel list match along the following parameters:

- Grammar
- Logical category
- Capitalization
- Punctuation

Conversely, at least one item in a **nonparallel** list fails at least
one of the preceding consistency checks.

For example, the following list is parallel
because all the items are plural nouns (grammar),
edible (logical category), in title case (capitalization),
and without periods or commas (punctuation).

- Carrots
- Potatoes
- Cabbages

By contrast, the following list is painfully nonparallel along
all parameters:

- Carrots
- Potatoes
- The summer light obscures all memories of winter.

The following list is parallel because all the items are complete
sentences with complete sentence capitalization and punctuation:

- Carrots contain lots of Vitamin A.
- Potatoes taste delicious.
- Cabbages provide oodles of Vitamin K.

The first item in a list establishes a pattern that readers expect
to see repeated in subsequent items.

#### Exercise

Is the following list parallel or nonparallel?

- Broccoli inspires feelings of love or hate.
- Potatoes taste delicious.
- Cabbages.

#### Exercise

Is the following list parallel or nonparallel?

- The red dots represent sick trees.
- Immature trees are represented by the blue dots.
- The green dots represent healthy trees.

### Start numbered list items with imperative verbs

Consider starting all items in a numbered list with an imperative verb. An
**imperative verb** is a command, such as **open** or **start**. For example,
notice how all of the items in the following parallel numbered list begin with
an imperative verb:

1. Download the Frambus app from Google Play or iTunes.
2. Configure the Frambus app's settings.
3. Start the Frambus app.

The following numbered list is nonparallel because two of the sentences start
with an imperative verb, but the third item does not:

1. Instantiate the Froobus class.
2. Invoke the Froobus.Salmonella() method.
3. The process stalls.

#### Exercise

Make the following list parallel. Ensure that each element in the result list
begins with an imperative verb:

1. Stop Frambus
2. The key configuration file is `/etc/frambus`. Open this file with an ASCII text editor.
3. In this file, you will see a parameter named Carambola, which is currently set to the default value (32). Change this value to 64.
4. When you are finished setting this parameter, save and close the configuration file
5. now, start Frambus again.

### Punctuate items appropriately

Though different style guides offer conflicting advice about punctuating
list items, the [Google developer documentation style
guide](https://developers.google.cn/style/lists#capitalization-and-end-punctuation)
recommends (with some exceptions) starting each list item with a capital
letter. For example:

- Loops
- Conditionals
- Variable declarations

If a list item is a sentence, use appropriate sentence-ending punctuation.
For example:

1. Open the program.
2. Click the settings icon.

### Create useful tables

Analytic minds tend to love tables. Given a page containing multiple
paragraphs and a single table, engineers' eyes zoom towards the table.

Consider the following guidelines when creating tables:

- Label each column with a meaningful header. Don't make readers guess what each column holds.
- Avoid putting too much text into a table cell. If a table cell holds more than two sentences, ask yourself whether that information belongs in some other format.
- Although different columns can hold different types of data, strive for parallelism *within* individual columns. For instance, the cells within a particular table column should not be a mixture of numerical data and famous circus performers.

> **Note:** Some tables don't render well across all form factors. For example,
> a table that looks great on your laptop may look awful on your phone.

### Introduce each list and table

We recommend introducing each list and table with a sentence that tells readers
what the list or table represents. In other words, give the list or table
context. Terminate the introductory sentence with a colon rather than a period.

Although not a requirement, we recommend putting the word **following** into
the introductory sentence.  For example, consider the following introductory
sentences:

> The following list identifies key performance parameters:
> Take the following steps to install the Frambus package:
> The following table summarizes our product's features against our key
> competitors' features:

#### Exercise

Write an introductory sentence for the following table:

| Language | Inventor | Year Introduced | Key Feature |
|---|---|---|---|
| Lisp | John McCarthy | 1958 | recursion |
| C++ | Bjarne Stroustrup | 1979 | OOP |
| Python | Guido van Rossum | 1994 | simplicity |


## Paragraphs

> **Estimated Time:** 10 minutes

This unit provides some guidelines on building cohesive paragraphs.
But first, here is an inspirational message:

> The work of writing is *simply* this: untangling the dependencies
> among the parts of a topic, and presenting those parts in a logical
> stream that enables the reader to understand you.

### Write a great opening sentence

The opening sentence is the most important sentence of any paragraph.
Busy readers focus on opening sentences and sometimes skip over subsequent
sentences. Therefore, focus your writing energy on opening sentences.

Good opening sentences establish the paragraph's central point.
For example, the following paragraph features an effective opening sentence:

> A loop runs the same block of code multiple times. For example,
> suppose you wrote a block of code that detected whether an input line
> ended with a period. To evaluate a million input lines, create a loop
> that runs a million times.

The preceding opening sentence establishes the theme of the paragraph as
an introduction to loops.  By contrast, the following opening sentence
sends readers in the wrong direction:

> A block of code is any set of contiguous code within the same function.
> For example, suppose you wrote a block of code that detected whether
> an input line ended with a period. To evaluate a million input lines,
> create a loop that runs a million times.

#### Exercise

Is the opening sentence of the following paragraph effective
or defective?

> The Pythagorean Theorem states that the sum of the squares
> of both legs of a right triangle is equal to the square of the
> hypotenuse.  The k-means clustering algorithm relies on the
> Pythagorean Theorem to measure distances. By contrast, the
> k-median clustering algorithm relies on the Manhattan Distance.

> **Note:** Effective opening sentences can take many forms. That is,
> not all great paragraphs start with a sentence that states the
> theme. Starting a paragraph with a rhetorical question, for example,
> can engage readers.

### Focus each paragraph on a single topic

A paragraph should represent an independent unit of logic. Restrict
each paragraph to the current topic. Don't describe what will happen
in a future topic or what happened in a past topic. When revising,
ruthlessly delete (or move to another paragraph) any sentence that
doesn't directly relate to the current topic.

For example, assume that the opening sentence of the following paragraph
does focus on the correct topic. Can you spot the
sentences that should be removed from the following paragraph?

> The Pythagorean Theorem states that the sum of the squares
> of both legs of a right triangle is equal to the square of the
> hypotenuse. The perimeter of a triangle is equal to the sum of
> the three sides.  You can use the Pythagorean Theorem to measure
> diagonal distances. For example, if you know the length and width
> of a ping-pong table, you can use the Pythagorean Theorem to
> determine the diagonal distance. To calculate the perimeter of the
> ping-pong table, sum the length and the width, and then multiply
> that sum by 2.

We've crossed out the second and fifth sentences to yield a
paragraph focused exclusively on the Pythagorean Theorem:

> The Pythagorean Theorem states that the sum of the squares
> of both legs of a right triangle is equal to the square of the
> hypotenuse. The perimeter of a triangle is equal to the sum of
> the three sides. You can use the Pythagorean Theorem to measure
> diagonal distances. For example, if you know the length and width
> of a ping-pong table, you can use the Pythagorean Theorem to
> determine the diagonal distance. To calculate the perimeter of the
> ping-pong table, sum the length and the width, and then multiply
> that sum by 2.

#### Exercise

Remove the extraneous sentence(s) from the following paragraph.
Assume that the opening sentence does establish the desired theme
for the paragraph:

> **Spreadsheets** provide a great way to organize data. Think of a
> spreadsheet as a table with rows and columns. Spreadsheets also
> provide mathematical functions, such as means and standard deviations.
> Each row holds details about one entity. Each column holds details
> about a particular parameter. For example, you can
> create a spreadsheet to organize data about different trees. Each row would
> represent a different type of tree. Each column would represent a different
> characteristic, such as the tree's height or the tree's spread.

### Don't make paragraphs too long or too short

Long paragraphs are visually intimidating. *Very* long paragraphs form
a dreaded "wall of text" that readers ignore. Readers generally welcome
paragraphs containing three to five sentences, but will avoid paragraphs
containing more than about seven sentences. When revising, consider dividing
very long paragraphs into two separate paragraphs.

Conversely, don't make paragraphs too short. If your document contains
plenty of one-sentence paragraphs, your organization is faulty. Seek ways to
combine those one-sentence paragraphs into cohesive multi-sentence paragraphs
or possibly into lists.

### Answer what, why, and how

Good paragraphs answer the following three questions:

1. **What** are you trying to tell your reader?
2. **Why** is it important for the reader to know this?
3. **How** should the reader use this knowledge? Alternatively, how should the reader know your point to be true?

For example, the following paragraph answers what, why, and how:

> The garp() function returns the
> delta between a dataset's mean and median.
> Many people believe unquestioningly that
> a mean always holds the truth. However, a mean is easily influenced by a
> few very large or very small data points.
> Call garp() to help determine
> whether a few very large or very small data points are influencing the mean
> too much. A relatively small garp() value suggests that the mean is
> more meaningful than when the garp() value is relatively high.


## Audience

> **Estimated Time:** 10 minutes

The course designers believe that you are probably comfortable with mathematics.
Therefore, this unit begins with an equation:

> good documentation = knowledge and skills your audience needs to do a task −
>                      your audience's current knowledge and skills

In other words, make sure your document provides the information that your
audience needs but doesn't already have. Therefore, this unit explains how to do
the following:

- Define your audience.
- Determine what your audience needs to learn.
- Fit documentation to your audience.

As the following video suggests, targeting the *wrong* audience can be messy:

### Define your audience

Serious documentation efforts spend considerable time and energy on
defining their audience. These efforts might involve surveys,
user experience studies, focus groups, and documentation testing.
You probably don't have that much time, so this unit takes a simpler
approach.

Begin by identifying your audience's **role**(s). Sample roles include:

- Software engineers
- Technical, non-engineer roles (such as technical program managers)
- Scientists
- Professionals in scientific fields (for example, physicians)
- Undergraduate engineering students
- Graduate engineering students
- Non-technical positions

We happily appreciate that many people in non-technical roles have great
technical and mathematical skills. However, roles remain an essential
first-order approximation in defining your audience. People within the same role
*generally* share certain base skills and knowledge. For example:

- Most software engineers know popular sorting algorithms, [big O notation](https://en.wikipedia.org/wiki/Big_O_notation), and at least one programming language.  Therefore, you can depend on software engineers knowing what O(n) means, but you can't depend on non-technical roles knowing O(n).
- A research report targeted at physicians should look very different from a newspaper article about the same research aimed at a lay audience.
- A professor's explanation of a new machine learning approach to graduate students should differ from the explanation to first-year undergraduate students.

Writing would be so much easier if everyone in the same role shared exactly
the same knowledge. Unfortunately, knowledge within the same role quickly
diverges.  Amal is an expert in Python, Sharon's expertise is C++,
and Micah's is in Java.  Kara loves Linux, but David only knows iOS.

Roles, by themselves, are insufficient for defining an audience.
That is, you must also consider your audience's *proximity* to the knowledge.
The software engineers in Project Frombus know something about related
Project Dingus but nothing about unrelated Project Carambola.
The average heart specialist knows more about ear problems than the
average software engineer but far less than an audiologist.

Time also affects proximity. Almost all software engineers,
for example, studied calculus. However, most software engineers don't use
calculus in their jobs, so their knowledge of calculus gradually fades.
Conversely, experienced engineers typically know vastly more about their current
project than new engineers on the same project.

#### Sample audience analysis

The following is a sample audience analysis for fictitious Project Zylmon:

> The target audience for Project Zylmon falls into the following roles:
> Software engineers
> Technical product managers
> The target audience has the following proximity to the knowledge:
> My target audience already knows the Zyljeune APIs, which are somewhat
> similar to the Zylmon APIs.
> My target audience knows C++, but has not typically built C++
> programs in the new Winged Victory development environment.
> My target audience took linear algebra in university, but many
> members of the team need a refresher on matrix multiplication.

### Determine what your audience needs to learn

Write down a list of everything your target audience needs to learn
to accomplish goals.  In some cases, the list should hold tasks
that the target audience needs to *perform*. For example:

> After reading the documentation, the audience will know how to do
> the following tasks:

> Use the Zylmon API to list hotels by price.
> Use the Zylmon API to list hotels by location.
> Use the Zylmon API to list hotels by user ratings.

Note that your audience must sometimes master tasks in a certain order.
For example, your audience might need to learn how to build and
execute programs in a new development environment *before* learning
how to write particular kinds of programs.

If you are writing a design spec, then your list should focus on
information your target audience should learn rather than on mastering
specific tasks. For example:

> After reading the design spec, the audience will learn the following:

> Three reasons why Zylmon outperforms Zyljeune.
> Five reasons why Zylmon consumed 5.25 engineering years to develop.

### Fit documentation to your audience

Writing to meet your audience's needs requires unselfish empathy.
You must create explanations that satisfy your audience's curiosity
rather than your own.  How do you step out of yourself in order to fit
documentation to the audience?  Unfortunately, we can offer no
easy answers. We can, however, offer a few parameters to focus on.

#### Vocabulary and concepts

Match your vocabulary to your audience. See [Words(https://developers.google.cn/tech-writing/one/words) for help.

Be mindful of proximity. The people on your team
probably understand your team's abbreviations, but do
people on other teams understand those same abbreviations?
As your target audience widens, assume that you must explain more.

Similarly, experienced people on your software team probably
understand the implementation details and data structures of your
team's project, but nearly everyone else (including new members
of your team) does not. Unless you are writing specifically for
other experienced members of your team, you typically must
explain more than you expect.

#### Curse of knowledge

Experts often suffer from **the curse of knowledge**, which means that
their expert understanding of a topic ruins their explanations to newcomers.
As experts, it is easy to forget that novices don’t know what you
already know. Novices might not understand explanations that make
passing reference to subtle interactions and deep systems that the
expert doesn’t stop to explain.

From the novice's point of view, the curse of knowledge is a "File not found"
linker error due to a module not yet compiled.

#### Exercise

1. Assume that the following paragraph is the start of a paper aimed at physicians who have never programmed before.  Identify the aspects of the paragraph that suffer from the curse of knowledge:  C is a mid-level language, higher than assembly language but lower than Python and Java. The C language provides programmers fine-grained control over all aspects of a program.  For example, using the C Standard Library, it is easy to allocate and free blocks of memory.  In C, manipulating pointers directly is mundane.
2. Suppose the preceding paragraph was aimed at undergraduate computer science students new to C but comfortable with Python. Does the paragraph still suffer from the curse of knowledge?

#### Simple words

English has become the dominant language for technical communication worldwide.
However, a significant percentage of technical readers are more comfortable
in languages other than English. Therefore, prefer simple words over complex
words; avoid obsolete or overly-complex English words.
[Sesquipedalian](https://www.google.com/search?q=sesquipedalian)
and rare words repel some readers.

#### Cultural neutrality and idioms

Keep your writing culturally neutral. Do not require readers to understand the
intricacies of NASCAR, cricket, or sumo in order to understand how a piece of
software works. For example, the following sentence—packed with baseball
metaphors as American as apple pie—might puzzle some Parisian readers:

> If Frambus 5.0 was a solid single, Frambus 6.0 is a stand-up double.

**Idioms** are phrases whose overall meaning differs from the literal
meaning of the individual words in that phrase.  For example, the
following phrases are idioms:

- a piece of cake
- Bob's your uncle

Cake? Bob? Most readers from the United States recognize the first idiom; most
British readers recognize the second idiom.
If you are writing strictly for a British audience, then
*Bob's your uncle* can be fine. However, if you are writing for
an international audience, then replace that idiom with *this task is done*.

Idioms are so deeply ingrained in our speech that the special nonliteral
meaning of idioms becomes invisible to us. That is, idioms are another
form of the curse of knowledge.

Note that some people in your audience use translation software to read
your documentation.  Translation software tends to struggle more with
cultural references and idioms than with plain, simple English.

#### Exercise

Identify the problems with the following sentences:

1. As of Version 3.0, it was still kosher to call the Frambus method.
2. Deciding which BlogResource constraints are combinable is a sticky wicket.
3. Be that as it may, you still have to write unit tests.


## Documents

> **Estimated Time:** 10 minutes

You can write sentences. You can write paragraphs. Can you organize
all those paragraphs into a coherent document?

### State your document's scope

A good document begins by defining its scope. For example:

> This document describes the design of Project Frambus.

A better document additionally defines its non-scope—the topics not
covered that the target audience might reasonably expect your document
to cover. For example:

> This document does not describe the design for the related technology,
> Project Froobus.

Scope and non-scope statements benefit not only the reader but also the
writer (you). While writing, if the contents of your document veer away from the
scope statement (or venture *into* the non-scope statement), then you must
either refocus your document or modify your scope statement. When reviewing
your first draft, delete any sections that don't help satisfy the scope
statement.

#### Exercise

What problem do you see in the following paragraph?

> This document explains how to use the Frambus API to create, update, and
> publish Fwidgets. This document does not explain how to use the Frambus
> API to delete Fwidgets or cover the history of the Linux operating system.

### State your audience

A good document explicitly specifies its audience. For example:

> This document is aimed at the following audiences:
> software engineers
> program managers

Beyond the audience's role, a good audience declaration might also
specify any prerequisite knowledge or experience. For example:

> This document assumes that you understand matrix multiplication
> and the fundamentals of backpropagation.

In some cases, the audience declaration should also specify prerequisite
reading or coursework. For example:

> You must read "Project Froobus: A New Hope" prior to reading this document.

### Summarize key points at the start

Engineers and scientists are busy people who won't necessarily read all
76 pages of your document. Imagine that your peers might only read
the first paragraph of your document. Therefore, ensure that the start of your
document answers your readers' essential questions.

Professional writers focus considerable energy on page one to increase the
odds of readers making it to page two. However, the start of any long document
is the hardest page to write. Be prepared to revise page one many times.

#### Compare and contrast

In your career, no matter how creative you are, you will author precious few
documents containing truly revolutionary ideas.  Most of your work will be
evolutionary, building on existing technologies and concepts. Therefore, compare
and contrast your ideas with concepts that your audience already understands.
For example:

> This new app is similar to the Frambus app, except with much better graphics.

Or:

> The Froobus API handles the same use cases as the Frambus API, except that the
> Froobus API is much easier to use.

#### Exercise

What problem do you see in the following introduction?

> Frambus Weather app v2 introduces ten features not available in Frambus
> Weather app v1. Most importantly, v2 offers two-week forecasts, v1 offered
> only one-week forecasts. Tidal information won't change.

### Write for your audience

This course repeatedly emphasizes the importance of defining your audience.
In this section, we focus on audience definition as a means of organizing
your document.

#### Define your audience's needs

Answering the following questions helps you determine what your document
should contain:

- Who is your target audience?
- What is your target audience's goal? Why are they reading this document?
- What do your readers already know *before* they read your document?
- What should your readers know or be able to do *after* they read your document?

For example, suppose you have invented a new sorting algorithm, which is
similar to quicksort. The following list contains some potential answers
to the preceding questions:

- **Who is your target audience?** The target audience consists of all the software engineers in my organization.
- **What is your target audience's goal?** My target audience wants to find more efficient ways to sort data. They are reading this document to determine whether this new algorithm is worth implementing.
- **What do your readers already know *before* they read your document?** My target audience knows how to write code and has previously studied sorting algorithms, including quicksort.  However, most people in my target audience haven't implemented or evaluated a sorting algorithm in several years.
- **What should your readers know or be able to do *after* they read your document?** My target audience will be able to do all of the following:  Understand how the algorithm compares and contrasts with quicksort. Identify the two kinds of datasets for which the algorithm outperforms the quicksort algorithm. Implement the algorithm in their choice of programming language. Identify the two edge cases in which the algorithm performs poorly.

#### Organize the document to meet your audience's needs

After defining the audience's needs, organize the document to help readers
get the information they need. For example, based on the answers in the
previous section, the outline for the document could look as follows:

1. Overview of the algorithm  Compare and contrast with quicksort, including Big O comparisons  Link to Wikipedia article on quicksort  Optimal datasets for the algorithm
2. Implementing the algorithm  Implementation in pseudocode Implementation tips, including common mistakes
3. Deeper analysis of algorithm  Edge cases Known unknowns


## Punctuation (optional)

> **Estimated Time:** 5 minutes

This optional unit provides a quick refresher on punctuation marks.

### Commas

Programming languages enforce clear rules about punctuation. In English,
by contrast, the rules regarding commas are somewhat hazier. As a guideline,
insert a comma wherever a reader would naturally pause somewhere within
a sentence. For the musically inclined, if a period is a whole note (semibreve)
rest, then a comma is perhaps a half-note (minim) or quarter-note (crotchet)
rest. In other words, the pause for a comma is shorter than that for a period.
For example, if you read the following sentence aloud, you probably rest briefly
before the word *just*:

> C behaves as a mid-level language, just a couple of steps up in abstraction
> from assembly language.

Some situations *require* a comma. For example, use commas to separate
items in an embedded list like the following:

> Our company uses C++, Python, Java, and JavaScript.

You might be wondering about a list's final comma, the one inserted between
items N-1 and N. This comma—known as the **serial comma** or **Oxford
comma**—is controversial. We recommend supplying that final comma simply
because technical writing requires picking the least ambiguous solution.
That said, we actually prefer circumventing the controversy by converting
embedded lists into bulleted lists.

In sentences that express a condition, place a comma between the condition and
the consequence. For example, both of the following sentences supply the comma
in the correct place:

> If the program runs slowly, try the `--perf` flag.
> If the program runs slowly, then try the `--perf` flag.

You can also wedge a quick definition or digression between a pair of commas as
in the following example:

> Python, an easy-to-use language, has gained significant momentum in recent
> years.

Finally, avoid using a comma to paste together two independent thoughts.
For example, the comma in the following sentence is guilty of a punctuation
felony called a **comma splice**:

Not recommended

> Samantha is a wonderful coder, she writes abundant tests.

Use a period rather than a comma to separate two independent thoughts.
For example:

Recommended

> Samantha is a wonderful coder. She writes abundant tests.

#### Exercise

Add commas where appropriate to the following passage:

> Protocol Buffers sometimes known as protobufs are our team's
> main structured data format. Use Protocol Buffers to
> represent store and transfer structured data. Unlike XML
> Protocol Buffers are compiled. Consequently clients
> transmit Protocol Buffers efficiently which has led to
> rapid adoption.

Hint: Read the passage aloud and put a comma everywhere you hear a short pause.

### Semicolons

A period separates distinct thoughts; a semicolon unites highly related
thoughts. For example, notice how the semicolon in the following
sentence unites the first and second thoughts:

Recommended

> Rerun Frambus after updating your configuration file; don't rerun
> Frambus after updating existing source code.

Before using a semicolon, ask yourself whether the sentence would still make
sense if you flipped the thoughts to opposite sides of the semicolon. For
example, reversing the earlier example still yields a *valid* sentence:

> Don't rerun Frambus after updating existing source code; rerun Frambus
> after updating your configuration file.

The thoughts preceding and following the semicolon must each be grammatically
complete sentences. For example, the following semicolon is *incorrect* because
the passage following the semicolon is a
[clause(https://developers.google.cn/tech-writing/one/short-sentences#reduce_subordinate_clauses_optional),
not a complete sentence:

Not recommended

> Rerun Frambus after updating your configuration file; not after updating
> existing source code.

Recommended

> Rerun Frambus after updating your configuration file, not after updating
> existing source code.

You should almost always use commas, not semicolons, to separate items in
an embedded list. For example, the following use of semicolons is *incorrect*:

Not recommended

> Style guides are bigger than the moon; more essential than oxygen; and
> completely inscrutable.

As mentioned earlier in this lesson, technical writing usually prefers bulleted
lists to embedded lists. However, if you truly prefer an embedded list, use
commas rather than semicolons to separate the items, as in the following
example:

Recommended

> Style guides are bigger than the moon, more essential than oxygen, and
> completely inscrutable.

Many sentences place a transition word or phrase immediately after the
semicolon. In this situation, place a comma after the transition. Note
the comma after the transition in the following two examples:

> Frambus provides no official open source package for string manipulation;
> however**,** subsets of string manipulation packages are available from
> other open source projects.

> Even seemingly trivial code changes can cause bugs; therefore**,** write
> abundant unit tests.

#### Exercise

Which of the following periods or commas could you replace with a semicolon?

1. Python is a popular programming language. The C language was developed long before Python.
2. Model learning for a low value of X appears in the top illustration. Model learning for a high value of X appears in the bottom illustration.
3. I'm thankful for my large monitor, powerful CPU, and blazing bandwidth.

### Em dashes

Em dashes are compelling punctuation marks, rich with punctuation possibilities.
An em dash represents a longer pause—a bigger break—than a comma. For the
musically fluent, think of a comma as a quarter note (crotchet) rest and an
em dash as a half-note (minim) rest. For example:

> C++ is a rich language—one requiring extensive experience to fully understand.

Writers sometimes use a pair of em dashes to block off a digression,
as in the following example:

> **Protocol Buffers**—often nicknamed **protobufs**—encode structured
> data in an efficient yet extensible format.

Could we have used commas instead of em dashes in the preceding examples?
Sure. Why did we choose an em dash instead of a comma? Feel. Art. Experience.

#### En dashes and hyphens

Consider the horizontal punctuation marks shown in the following table:

| Name | Mark | Relative width |
|---|---|---|
| em dash | — | widest (usually, the length of the letter m ) |
| en dash | – | medium (usually, the length of the letter n ) |
| hyphen | - | narrowest |

Some style guides recommend the **en dash** for certain uses. The
[Google Style Guide](https://developers.google.cn/style/dashes#en-dashes),
however, offers the following blunt advice about en dashes:

> Don't use.

**Hyphens** are tricky. Within technical writing, hyphens connect words in
certain compound terms, such as:

- Self-attention
- N-gram

Confusingly, three-word compound terms often contain a hyphen between the
first and second word but not between the second and third word. For example:

- Decision-making system
- Floating-point feature

When in doubt about hyphens, consult a dictionary, glossary, or style guide.

> **Note:** If you consult *more than one* dictionary, glossary, or style guide
> about hyphens, you may encounter inconsistencies.

### Colons

In technical writing, use a colon to alert readers that a list or table will
follow. In other words, terminate the [sentence that introduces a list or
table(https://developers.google.cn/tech-writing/one/lists-and-tables#introduce_each_list_and_table)
with a colon. In the following example, notice the colon at the end of the
sentence that introduces the list:

> Consider the following important programming languages:
> Python
> Java
> C++

Technical writing prefers bulleted lists or numbered lists to embedded
lists. That said, you can use a colon to introduce an embedded list as
in the following example:

> Consider the following important programming languages: Python, Java,
> and C++.

Not all embedded lists require a colon. For example:

> My three favorite programming languages are Python, Java, and anything
> other than C++.

### Parentheses

Use parentheses to hold minor points and digressions. Parentheses inform readers
that the enclosed text isn't critical. Because the enclosed text isn't critical,
some editors feel that text that deserves parentheses doesn't deserve to be
in the document. As a compromise, keep parentheses to a minimum in technical
writing.

The rules regarding periods and parentheses aren't always clear. Here
are the standard rules:

- If a pair of parentheses holds an entire sentence, the period goes inside the closing parenthesis.
- If a pair of parentheses ends a sentence but does not hold the entire sentence, the period goes just outside the closing parenthesis.

For example:

> (Incidentally, Protocol Buffers make great birthday gifts.)
> Binary mode relies on the more compact native form (described later in this
> document).


## Markdown (optional)

> **Estimated Time:** 10 minutes

**Markdown** is a lightweight markup language that many technical professionals
use to create and edit technical documents.  With Markdown, you write text
in a plain text editor (such as vi or Emacs), inserting special characters
to create headers, boldface, bullets, and so on.  For example, the following
example shows a simple technical document formatted with Markdown:

The rendered version of the preceding technical document looks as follows:

> bash and ksh
> **bash** closely resembles an older shell named **ksh**.  The key
> *practical* difference between the two shells is as follows:
> More people know bash than ksh, so it is easier to get help for bash
> problems than ksh problems.

A Markdown parser converts Markdown files into HTML. Browsers can then
display the resulting HTML to readers.

We recommend becoming comfortable with Markdown by taking one of the following
tutorials:

- [www.markdowntutorial.com](https://www.markdowntutorial.com/)
- [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)

### What's next?

Congratulations: you've completed the pre-class work for Technical Writing One.

If the in-class portion of Technical Writing One is available in your
organization, please take it. If you'd like to facilitate the in-class portion
of Technical Writing One, see the
[facilitator's guide(https://developers.google.cn/tech-writing/for-instructors/one/instructors-guide).

A quick compilation of the topics covered in Technical Writing One
is available on the [Summary(https://developers.google.cn/tech-writing/one/summary) page.


## Summary of Technical Writing One pre-class

> **Estimated Time:** 2 minutes

Congratulations! You've completed the pre-class portion of Technical Writing
One, which covered the following fundamental principles of technical writing:

| Section | Lesson |
|---|---|
| Words |
| Define new or unfamiliar terms. |
| Use terms consistently. |
| Avoid ambiguous pronouns. |
| Active voice |
| Prefer active voice to passive voice. |
| Clear sentences |
| Pick specific verbs over vague ones. |
| Reduce there is and there are . |
| Short sentences |
| Focus each sentence on a single idea. |
| Convert some long sentences to lists. |
| Eliminate unneeded words. |
| Lists and tables |
| Use a numbered list when ordering is important and a bulleted list
          when ordering is irrelevant. |
| Keep list items parallel. |
| Start numbered list items with imperative words. |
| Paragraphs |
| Establish a paragraph's central point in the first sentence. |
| Focus each paragraph on a single topic. |
| Audience |
| Determine what your audience needs to learn. |
| Fit documentation to your audience. |
| Documents |
| Begin a document by stating its scope, audience, and
          key points. |
| Aim the document at your audience. |
| Punctuation |
| Use commas to force short pauses within a sentence or
          to separate items in a list. |
| Use a period to separate distinct thoughts; use a semicolon
          to unite highly related thoughts. |
| Use a colon instead of a period in a sentence that introduces
          a list. |

If your organization offers the instructor-led portion of Technical Writing One,
you're now ready for that class. If your organization doesn't offer the
instructor-led portion of Technical Writing One, note that Google occasionally
offers the course. See the [Announcements page(https://developers.google.cn/tech-writing/announcements) for
details.


# Technical Writing Two


## Self-editing

> **Estimated Time:** 10 minutes

Imagine that you just wrote the first draft of a document. How do you make it
better? In most cases, working towards a final published document is an
iterative process. Transforming a blank page into a first draft is often the
hardest step. After you write a first draft, make sure you set aside plenty of
time to refine your document.

The editing tips in this unit can help turn your first draft into a document
that more clearly communicates the information your audience needs. Use one tip
or use them all; the important thing is to find a strategy that works for you,
and then make that strategy part of your writing routine.

> **Note:** The tips in this unit build on the basic writing and editing skills
> from Technical Writing One. This unit includes a summary of useful editing
> techniques from that course. For a more detailed refresher, visit the
> [self-study units(https://developers.google.cn/tech-writing/one) from Technical Writing One.

### Adopt a style guide

Companies, organizations, and large open source projects frequently either adopt
an existing style guide for their documentation or write their own. Many of
the documentation projects on the [Google Developers(https://developers.google.cn/) site follow the
[Google Developer Documentation Style Guide(https://developers.google.cn/style). If you've never relied on
a style guide before, at first glance the Google Developer Documentation Style
Guide might seem a little intimidating, offering detailed guidance on topics
such as grammar, punctuation, formatting, and documenting computer interfaces.
You might prefer to start by adopting the
[style-guide highlights(https://developers.google.cn/style/highlights).

> **Note:** For smaller projects, such as team documentation or a small open source
> project, you might find the highlights are all you need.

Some of the guidelines listed in the highlights are covered in Technical Writing
One. You might recall some of the following techniques:

- Use [active voice(https://developers.google.cn/tech-writing/one/active-voice) to make clear who's performing the action.
- Format sequential steps as [numbered lists(https://developers.google.cn/tech-writing/one/lists-and-tables).
- Format most other lists as bulleted lists.

The highlights introduce many other techniques that can be useful when writing
technical documentation, such as:

- [Write in the second person(https://developers.google.cn/style/person). Refer to your audience as "you", not "we".
- [Place conditions before instructions(https://developers.google.cn/style/sentence-structure), not after.
- Format [code-related text as code font(https://developers.google.cn/style/code-in-text).

### Think like your audience

Who is your audience? Step back and try to read your draft from their point of
view. Make sure the purpose of your document is clear, and provide definitions
for any terms or concepts that might be unfamiliar to your readers.

It can be helpful to outline a persona for your audience. A persona can consist
of any of the following attributes:

- A role, such as *Systems Engineer* or *QA Tester*.
- An end goal, such as *Restore the database*.
- A set of assumptions about the persona and their knowledge and experience. For example, you might assume that your persona is:  Familiar with Python. Running a Linux operating system. Comfortable following instructions for the command line.

You can then review your draft with your persona in mind. It can be especially
useful to tell your audience about any assumptions you've made. You can also
provide links to resources where they can learn more if they need to brush up on
a specific topic.

Note that relying too heavily on a persona (or two) can result in a document
that is too narrowly focused to be useful to the majority of your readers.

For a refresher and more information on this topic from Technical Writing One,
see the [Audience(https://developers.google.cn/tech-writing/one/audience) self-study unit.

### Read it out loud

Depending on the context, the style of your writing can alienate, engage, or
even bore your audience. The desired style of a given document depends to an
extent on the audience. For example, the contributor guide for a new open source
project aimed at recruiting volunteers might adopt a more informal and
conversational style, while the developer guide for a commercial enterprise
application might adopt a more formal style.

To check if your writing is conversational, read it out loud. Listen for awkward
phrasing, too-long sentences, or anything else that doesn't feel natural.
Alternatively, consider using a [screen
reader](https://en.wikipedia.org/wiki/Screen_reader) to voice the content for
you.

For more information on adjusting the style of your writing to suit your
audience, see [Style and authorial tone(https://developers.google.cn/style/tone).

### Come back to it later

After you write your first draft (or second or third), set it aside. Come back
to it after an hour (or two or three) and try to read it with fresh eyes.
You'll almost always notice something that you could improve.

### Change the context

Some writers like to print their documentation and review a paper
copy, red pencil in hand. A change of context when reviewing your own work can
help you find things to improve. For a modern take on this classic tip, copy
your draft into a different document and change the font, size, and color.

### Find a peer editor

Just as engineers need peers to review their code, writers need editors to give
them feedback on docs. Ask someone to review your document and give you
specific, constructive comments. Your peer editor doesn't need to be a subject
matter expert on the technical topic of your document, but they do need to be
familiar with the style guide you follow.

### Exercise

If you have a document that you're working on, use one or more of the tips on
this page to make it better. If you don't have a document in progress, edit the
paragraph below.

> Determine whether or not you can simplify your document through the use of
> terminology that is equivalent but relatively shorter in length and therefore
> more easily comprehensible by your audience. It's important to make sure your
> document is edited before it is seen by your audience, which might include
> people that are less or more familiar with the matter covered by your document.
> The first thing you need is a rough draft. Some things that can help make your
> document easier to read are making sure you have links to background
> information, and also checking for active voice instead of passive voice. If
> you have long sentences you can consider shortening them or implementing the
> use of a list to make the information easier to scan.


## Organizing large documents

> **Estimated Time:** 20 minutes

How do you organize a large collection of information into a cohesive document
or website?  Alternatively, how do you reorganize an existing messy document or
website into something approachable and useful? The following tactics can help:

- Choosing to write a single, large document or a set of documents
- Organizing a document
- Adding navigation
- Disclosing information progressively

### When to write large documents

You can organize a collection of information into longer standalone documents
or a set of shorter interconnected documents. A set of shorter interconnected
documents is often published as a website, wiki, or similar structured
format.

Some readers respond more positively than others to longer documents. Consider
the following perspectives from two hypothetical readers you're writing
documentation for:

- Hong finds reading long documents difficult and disorientating. He prefers to use site search to find answers to his questions.
- Rose is comfortable navigating large documents. She often uses the built-in page search feature in her web browser to find useful information on the current page.

So, should you organize your material into a single document or into a set of
documents in a website? Consider the following guidelines:

- How-to guides, introductory overviews, and conceptual guides often work better as shorter documents when aimed at readers who are new to the subject matter. For example, a reader who is completely new to your subject matter might struggle to remember lots of new terms, concepts, and facts. Remember that your audience might be reading your documentation to gain a quick and general overview of the topic.
- In-depth tutorials, best practice guides, and command-line reference pages can work well as lengthier documents, especially when aimed at readers who already have some experience with the tools and subject matter.
- A great tutorial can rely on a narrative to lead the reader through a series of related tasks in a longer document. However, even large tutorials can sometimes benefit from being broken up into smaller parts.
- Many longer documents aren't designed to be read in one sitting. For example, users typically scan through a reference page to search for an explanation of a command or flag.

The remainder of this unit covers techniques that can be useful for writing
longer documents, such as tutorials and some conceptual guides.

### Organize a document

This section suggests some techniques for planning a longer document, including
creating an outline and drafting an introduction. After you've completed the
first draft of a document, you can review it against your outline and
introduction to make sure you haven't missed anything you originally intended
to cover.

#### Outline a document

Starting with a structured, high-level outline can help you group topics and
determine where more detail is needed. The outline helps you move topics around
before you get down to writing.

You might find it useful to think of an outline as the narrative for your
document. There is no standard approach to writing an outline, but the following
guidelines provide practical tips you might find useful:

- Before you ask your reader to perform a task, explain to them why they are doing it. For example, the following bullet points illustrate a section of an outline from a tutorial about auditing and improving the accessibility of web pages:  Introduce a browser plugin that audits the accessibility of web pages; explain that the reader will use the results of the audit report to fix several bugs. List the steps to run the plugin and audit the accessibility of a web page.
- Limit each step of your outline to describing a concept or completing a specific task.
- Structure your outline so that your document introduces information when it's most relevant to your reader. For example, your reader probably doesn't need to know (or want to know) about the history of the project in the introductory sections of your document when they're just getting started with the basics. If you feel the history of the project is useful, then include a link to this type of information at the end of your document.
- Consider explaining a concept and then demonstrating how the reader can apply it either in a sample project or in their own work. Documents that alternate between conceptual information and practical steps can be a particularly engaging way to learn.
- Before you start drafting, share the outline with your contributors. Outlines are especially useful if you're working with a team of contributors who are going to review and test your document.

#### Outline exercise

Review and update the following high-level outline of an introduction to a long
tutorial. To solve this exercise, you can do any of the following:

- Rearrange the existing topics.
- Add any missing topics you feel should be in an introduction.
- Remove any topics you feel are irrelevant for an introduction.

#### Introduce a document

If readers of your documentation can't find relevance in the subject, they are
likely to ignore it. To set the ground rules for your users, we recommend
providing an introduction that includes the following information:

- What the document covers.
- What prior knowledge you expect readers to have.
- What the document doesn't cover.

Remember that you want to keep your documentation easy to maintain, so don't
try to cover everything in the introduction.

The following paragraph demonstrates the ideas from the preceding list
as an overview for a hypothetical document publishing platform called Froobus:

After you've completed the first draft, check your entire document against
the expectations you set in your overview. Does your introduction provide
an accurate overview of the topics you cover? You might find it useful to
think of this review as a form of documentation quality assurance (QA).

#### Introduction exercise

For this exercise, review and revise the following introduction for a best
practices guide for a hypothetical programming language called F@. Remove any
information you feel is irrelevant in this context and add any information you
feel is missing.

### Add navigation

Providing navigation and signposting for your readers ensures they can find what
they are looking for and the information they need to get unstuck.

Clear navigation includes:

- introduction and summary sections
- a clear, logical development of the subject
- headings and subheadings that help users understand the subject
- a table of contents menu that shows users where they are in the document
- links to related resources or more in-depth information
- links to what to learn next

The tips in the following sections can help you plan the headings in your
documentation.

#### Prefer task-based headings

Choose a heading that describes the task your reader is working on. Avoid
headings that rely on unfamiliar terminology or tools. For example, suppose you
are documenting the process for creating a new website. To create the site, the
reader must initialize the Froobus framework. To initialize the Froobus
framework, the reader must run the `carambola` command-line tool. At first
glance, it might seem logical to add either of the following headings to the
instructions:

- Running the carambola command
- Initializing the Froobus framework

Unless your readers are already very experienced with the terminology and
concepts for this topic, a more familiar heading might be preferable, such as
*Creating the site*.

#### Provide text under each heading

Most readers appreciate at least a brief introduction under each heading to
provide some context. Avoid placing a level three heading immediately after a
level two heading, as in the following example:

In this example, a brief introduction can help orient the reader:

#### Heading exercise

Helping readers navigate through your documentation helps them find the
information they need to successfully use your tool. Often, a clear and
well-organized table of contents or outline acts like a map that helps your
users navigate the functionality of your tool.

For this exercise, improve the following outline. You can rearrange,
add, and delete topics and create secondary entries too.

### Disclose information progressively

Learning new concepts, ideas, and techniques can be a rewarding experience for
many readers who are comfortable reading through documentation at their own
pace. However, being confronted with too many new concepts and instructions too
quickly can be overwhelming. Readers are more likely to be receptive to longer
documents that progressively disclose new information to them when they need it.
The following techniques can help you incorporate progressive disclosure in your
documents:

- Where possible, try introducing new terminology and concepts near the instructions that rely on them.
- Break up large walls of text. To avoid multiple large paragraphs on a single page, aim to introduce tables, diagrams, lists, and headings where appropriate.
- Break up large series of steps. If you have a particularly long list of complicated steps, try to re-arrange them into shorter lists that explain how to complete sub-tasks.
- Start with simple examples and instructions, and add progressively more interesting and complicated techniques. For example, in a tutorial for creating forms, start by explaining how to handle text responses, and then introduce other techniques to handle multiple choice, images, and other response types.


## Illustrating

> **Estimated Time:** 10 minutes

Remember when your teacher assigned you a hefty chapter to read?
You flipped through the assigned section of the textbook, desperately
hoping for...yes, pictures! Viewing illustrations was so much
more fun than reading text. In fact, when it comes to reading
technical material, the vast majority of adults are still little
kids—still yearning for pictures rather than text.

**Figure 1. Good graphics engage readers in ways that text cannot.**
[
Nirmal Dulal [CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0)]](https://commons.wikimedia.org/wiki/File:Nepalese_Children.JPG)

According to research by [Sung and Mayer
(2012)](https://www.sciencedirect.com/science/article/pii/S0747563212000921),
providing any graphics—good or bad—makes readers like the document more;
however, only *instructive* graphics help readers learn. This unit suggests
a few ways to help you create figures truly worth a thousand words.

### Write the caption first

It is often helpful to write the caption *before* creating the
illustration. Then, create the illustration that best represents the caption.
This process helps you to check that the illustration matches the goal.

Good captions have the following characteristics:

- They are **brief**. Typically, a caption is just a few words.
- They explain the **takeaway**. *After viewing this graphic, what should the reader remember?*
- They **focus** the reader's attention. Focus is particularly important when a photograph or diagram contains a lot of detail.

> **Note:** By convention, the caption always follows the diagram.

#### Exercise

Target Audience: CS undergraduate students taking an "Introduction to Data
Structures" class.

Consider the following three figures, each of which uses the
same caption.

**Caption A. A singly linked list node stores content and a reference to the
next node.**

**Caption B. A singly linked list node stores content and a reference to the
next node.**

**Caption C. A singly linked list node stores content and a reference to the
next node.**

Which of the three preceding figures best illustrates its caption?

### Constrain the amount of information in a single drawing

Few intellectual tasks can be quite as rewarding as studying a fine painting,
gradually uncovering layers of insight and meaning. People pay good money to
do exactly that in the world's art museums.

**Figure 2. You'd happily study this Van Gogh painting.**

[Portrait of Pere Tanguy By Vincent van Gogh - Musée Rodin [Public domain]](https://commons.wikimedia.org/wiki/File:Van_Gogh_-_Portrait_of_Pere_Tanguy_1887-8.JPG)

By contrast, highly complex technical illustrations like the following tend
to discourage most readers:

**Figure 3. Complex block diagrams overwhelm readers.**

Just as you avoid overly-long sentences, strive to avoid visual run-ons. As a
rule of thumb, don't put more than one paragraph's worth of information in a
single diagram. (An alternative rule of thumb is to avoid illustrations that
require more than five bulleted items to explain.) I can hear you saying,
"But real-life technical systems can be vastly more complex than the one
shown in Figure 3." You are correct, but you probably don't feel compelled to
explain real-life complex systems in a single paragraph.

The trick to reducing visual clutter into something coherent and helpful
is to organize complex systems into subsystems, like those shown in the
following figure:

**Figure 4. A complex system organized into three subsystems.**

After showing the "big picture," provide separate illustrations of each
subsystem.

**Figure 5. Expanded detail for one subsystem of a complex system.**

Alternatively, start with a simple "big picture" and then gradually expand
detail in each subsequent illustration.

### Focus the reader's attention

When confronted with a complex screenshot like the following, readers
struggle to determine what's relevant:

**Figure 6. Readers don't know what to focus on.**

Adding a visual cue, for example, the red oval in the following
figure, helps readers focus on the relevant section of the screenshot:

**Figure 7. Readers focus on a shape that breaks the pattern.**

**Callouts** provide another way to focus the reader's attention. For pictures
and line art, a callout helps our eyes find just the right spot to land on.
Callouts in pictures are often better than paragraph long explanations of the
pictures because callouts focus the reader's attention on the most important
aspects of the picture. Then, in your explanation, you can focus directly on the
relevant part of the diagram, rather than spending time describing what part of
the image you are talking about.

In the example image, the callout and arrow quickly direct the reader to the
purpose.

**Figure 8. A callout directs readers' eyes.**

[NASA / JPL-Caltech / University of Arizona [Public domain]](https://commons.wikimedia.org/wiki/File:Phobos_colour_2008.jpg)

### Illustrating is re-illustrating

As with writing, the first draft of an illustration is seldom good
enough.  Revise your illustrations to clarify the content.
As you revise, ask yourself the following questions:

- How can I simplify the illustration?
- Should I split this illustration into two or more simpler illustrations?
- Is the text in the illustration easy to read? Does the text contrast sufficiently with its background?
- What's the takeaway?

For instance, consider the
[evolution of the London Tube
map](https://wikipedia.org/wiki/Tube_map#History).
Prior to 1931, the Tube map was drawn to scale, complete with above ground
roads and tube lines that curved as the tracks did.

**Figure 9. 1908 to scale map of the London Tube with above ground roads.**

[[Public domain]](https://commons.wikimedia.org/wiki/File:Tube_map_1908.jpg)

In 1931, Harry Beck pioneered a new type of public transit map that
simplified the older map by removing above ground markers and removing scale.
His design instead focused on what people using the maps really cared about:
getting from station A to station B. Even with the success of his 1931 map,
Beck still iterated on the diagram for many years to simplify and clarify the
map.  Consider now the [modern tube
map](https://www.google.com/search?tbm=isch&q=london+tube+map), although new
lines and stations have appeared, they still remain close to Beck's design.

#### Exercise

Consider the following original illustration:

**Figure 10. A complex diagram.**

The takeaway of the preceding diagram is supposed to be:

> For a recursive solution, call the function itself in the return statement
>   until you reach a base case solution.

In what ways does the complexity of the diagram hide the takeaway? How
might you address these problems?

Here is an improved illustration:

**Figure 11. A simplified version of the preceding diagram.**

What flaws do you see in the improved illustration?

### Illustration tools

There are many options available for creating diagrams. Three options that are
free or have free options include:

- [Google Drawings](https://drawings.google.com)
- [diagrams.net](https://diagrams.net)
- [LucidChart](https://www.lucidchart.com/pages/)

When exporting diagrams from these tools to use in documentation, it is usually
best to export the files as [Scalable Vector
Graphics](https://wikipedia.org/wiki/Scalable_Vector_Graphics) (SVG).
The SVG format easily scales diagrams based on space constraints so
that no matter the size, you end up with a high quality image.


## Creating sample code

> **Estimated Time:** 10 minutes

Good sample code is often the best documentation.  Even if your paragraphs and
lists are as clear as blue water, programmers still prefer good sample code.
After all, text and code are different languages, and it is code that the
reader ultimately cares about.  Trying to describe code with text is like
trying to explain an Italian poem in English.

Good samples are **correct** and **concise** code that your readers can
**quickly understand** and **easily reuse** with **minimal side effects**.

### Correct

Sample code should meet the following criteria:

- Build without errors.
- Perform the task it claims to perform.
- Be as production-ready as possible. For example, the code shouldn't contain any security vulnerabilities.
- Follow language-specific conventions.

Sample code is an opportunity to directly influence how your users write code.
Therefore, sample code should set the best way to use your product. If
there is more than one way to code the task, code it in the manner
that your team has decided is best. If your team hasn't considered
the pros and cons of each approach, take time to do so.

Always test your sample code. Over time, systems change and your sample
code may break. Be prepared to test and maintain sample code as you would
any other code.

Many teams reuse their unit tests as sample programs, which is sometimes a
bad idea.  The primary goal of a unit test is to test; the only goal of a
sample program is to educate.

A **snippet** is a piece of a sample program, possibly only one or a few
lines long.  Snippet-heavy documentation often degrades over time because
teams tend not to test snippets as rigorously as full sample programs.

#### Running sample code

Good documents explain how to run sample code.  For example, your document might
need to tell users to perform activities such as the following prior to running
the samples:

- Install a certain library.
- Adjust the values assigned to certain environment variables.
- Adjust something in the integrated development environment (IDE).

Users don't always perform the preceding activities properly.  In some
situations, users prefer to run or (experiment with) sample code directly
in the documentation. ("Click here to run this code.")

Writers should consider describing the expected output or result of sample code,
especially for sample code that is difficult to run.

### Concise

Sample code should be short, including only essential components.  When
a novice C programmer wants to learn how to call the `malloc` function,
give that programmer a brief snippet, not the entire Linux source tree.
Irrelevant code can distract and confuse your audience.  That said, never
use bad practices to shorten your code; always prefer correctness over
conciseness.

### Understandable

Follow these recommendations to create clear sample code:

- Pick descriptive class, method, and variable names.
- Avoid confusing your readers with hard-to-decipher programming tricks.
- Avoid deeply nested code.
- Optional: Use bold or colored font to draw the reader's attention to a specific section of your sample code. However, use highlighting judiciously—too much highlighting means the reader won't focus on anything in particular.

#### Exercise

Which of the following would be a more helpful line of code in a
sample program? Assume that the target audience consists of
software engineers new to the `go.so` API.

1. `MyLevel = go.so.Level(5, 28, 48)`
2. `MyLevel = go.so.Level(rank=5, 28, 48)`
3. `MyLevel = go.so.Level(rank=5, dimension=28, opacity=48)`

### Commented

Consider the following recommendations about comments in sample code:

- Keep comments short, but always prefer clarity over brevity.
- Avoid writing comments about *obvious* code, but remember that what is obvious to you (the expert) might not be obvious to newcomers.
- Focus your commenting energy on anything non-intuitive in the code.
- When your readers are very experienced with a technology, don't explain *what* the code is doing, explain *why* the code is doing it.

Should you place descriptions of code inside code comments or in
text (paragraphs or lists) outside of the sample code?  Note that readers
who copy-and-paste a snippet gather not only the code but also any embedded
comments. So, put any descriptions that belong in the pasted code into the code
comments.  By contrast, when you must explain a lengthy or tricky concept,
you should typically place the text before the sample program.

> **Note:** If you must sacrifice production readiness in order to make the
> code shorter and easier to understand, explain your decisions in the comments.

#### Exercise

What problems do you see in the comments within the following snippet?
Assume that the code is aimed at programmers who are new to the `br` API
but who have some experience with the concept of streams:

### Reusable

For your reader to easily reuse your sample code, provide the following:

- All information necessary to run the sample code, including any dependencies and setup.
- Code that can be extended or customized in useful ways.

Having easy-to-understand sample code that's concise and compiles is
a great start. If it blows up your reader's app, though, they won't
be happy. Therefore, when writing sample code, consider any potential
side effects caused by your code being integrated into another program.
Nobody wants insecure or grossly inefficient code.

### The example and the anti-example

In addition to showing readers *what to do*, it is sometimes wise to show
readers *what not to do*.  For example, many programming languages
permit programmers to place white space on either side of the equals sign.
Now suppose that you were writing a tutorial on a language (such as bash)
that does not permit white space on either side of the equals sign. In this
case, showing both a good example and an anti-example will benefit the reader.
For example:

### Sequenced

A good sample code set demonstrates **a range of complexity**.

Readers completely unfamiliar with a certain technology typically
crave simple examples to get started.  The first and most basic
example in a sample code set is usually termed a
[Hello World program](https://wikipedia.org/wiki/%22Hello,_World!%22_program).  After mastering the basics, engineers
want more complex programs. A good set of sample code provides a healthy
range of simple, moderate, and complex sample programs.

#### Exercise

Which of the following would be a good set of sample functions to support
a tutorial introducing newcomers to the concept of functions?

1. The following set of functions:  A function that takes no parameters and doesn't return anything. A function that takes one parameter but doesn't return anything. A function that takes one parameter and returns one value. A function that takes three parameters and returns one value.
2. The following set of functions:  A function that takes three parameters and returns one value.
3. The following set of functions:  A function that takes one parameter and returns one value. A function that takes three parameters and returns one value.


## Using large language models (LLMs) in technical writing

> **Estimated Time:** 20 minutes

[**Large language models**(https://developers.google.cn/machine-learning/glossary#large-language-model)
(**LLMs**) such as [Gemini](https://gemini.google.com) can help you improve
your documents. On the other hand, careless use of LLMs can inject mistakes
into your documents. This section focuses on responsible use of LLMs to
help you do the following:

- Generate a first draft.
- Revise a document.
- Format a document.
- Summarize a document.

The requests you make to an LLM are called
[**prompts**(https://developers.google.cn/machine-learning/glossary#prompt). An LLM reacts to prompts
by generating [**responses**(https://developers.google.cn/machine-learning/glossary#response). This module
explains how to write prompts that generate useful responses.

In general, writing good prompts requires following good technical writing
principles.

> **Caution:** Responses sometimes contain errors. Always check responses carefully,
>          not only for factual errors but also for instances where the response
>          doesn't "feel" right.

### Generate a first draft

An LLM can help you write that dreaded, bang-your-head-against-the-screen
first draft. To get a good first draft, you'll need to supply good prompts.

LLMs generate the best responses for topics they "know" about. LLMs know
the following:

- The information the LLM was [**pre-trained**(https://developers.google.cn/machine-learning/glossary#pre-training) on.
- Any additional information the LLM was subsequently [**fine-tuned**(https://developers.google.cn/machine-learning/glossary#fine-tuning) on.
- Information traditionally available through a search engine (if the LLM is enhanced with [Retrieval-Augmented Generation (RAG)(https://developers.google.cn/machine-learning/glossary#retrieval-augmented_generation)).
- Any additional information you provide in prompts or attachments.

For example, most LLMs are pre-trained on a lot of information about the
Python programming language. Therefore, most LLMs can generate a first draft
of text about any standard Python function. However, an LLM doesn't know about
the Python function that you wrote this morning unless you pass that source
code within a prompt.

The rest of this section explores specific ways to write effective prompts
for generating a first draft.

#### Take on a role

LLMs tend to generate better responses when the prompt tells the LLM to
impersonate a role. For example:

Recommended

> You are an expert technical writer...

> You are a patient senior software engineer talking to a junior software
> engineer...

> You are a computer science professor writing slides for your first-year
> students...

To choose a role, imagine who could best explain or teach a certain topic
to the target audience.

#### Identify your target audience

Prompts should specify the target audience.
For example, the following prompt does *not* identify a target audience,
so the LLM's response may or may not be helpful:

Not recommended

> Describe the Carambola app.

In contrast, the following prompts are far more specific and will likely yield
better responses:

Recommended

> Describe the Carambola app to new hires on my team responsible for
> maintaining the app.

> Describe the Carambola app to a software engineer on another team...

> Describe the Carambola app to the vice-president of marketing...

#### Specify the document type

What *type* of document do you want the LLM to generate?
The following prompt, for example, doesn't answer the preceding question:

Not recommended

> Generate a document...

In contrast, the following prompts are more specific:

Recommended

> Generate an FAQ...

> Generate an email...

Consider prompting for a subset of a lengthy document rather than the entire
document. For example, if a programmer's guide needs to be hundreds of pages
long, then the following prompt might yield a poor response:

Not recommended

> Generate a complete programmer's guide on...

In contrast, prompting for specific chapters might yield better responses:

Recommended

> Generate the section of the programmer's guide that explains how to
> book a reservation.

> Generate the section of the programmer's guide that explains how to
> change a reservation.

#### Define the goal of the document

People read technical documentation in order to learn something or do
something. A good prompt tells the LLM what the reader intends to with
the information. For example, the following prompts provide practical
goals:

Recommended

> After reading the FAQ, readers should be able to debug common
> problems themselves.

> After reading this tutorial, the reader should know the difference between
> regular functions and lambda functions in Python.

#### Choose the style

LLM responses are typically a lot of bulleted lists connected by short
paragraphs. That's usually an appropriate style for technical writing.
However, your prompt can suggest a different style or a format. For example:

Recommended

> ... Organize the release notes in the following order:
> An introductory paragraph
> A table containing one-line summaries of each bug
> Subsections for each bug, detailing the problem and any workarounds

Alternatively, if you like the style of another document, you can attach
that document to the prompt and tell the LLM to mimic its style (or selected
aspects of its style). You can even specify a style guide to mimic.
For example:

Recommended

> Write comments for the following Python function that conform to the
> Google Python Style Guide.

LLM responses tend to be too long. Consider telling the LLM to
abbreviate a response. For example:

Recommended

> ... Limit the bulleted list to the most important three items.

> **Note:** LLMs sometimes make math mistakes, so the resulting bulleted list
>       might not contain exactly three items.

#### Add prompt constraints

You can reduce [hallucinations(https://developers.google.cn/machine-learning/glossary#hallucination)
in the LLM response by adding specific constraints to your prompt. For
example, you can constrain the LLM to only use information that you provide
in the prompt:

Recommended

> Only use information from the following text in your response:

You can also constrain the LLM to only use information from a specific
set of files.

#### Iterate and refine

Your initial prompt generally won't produce a perfect response.
You'll probably need to prompt multiple times, making adjustments each time.
If the responses still aren't very good, consider the following questions:

- Do your prompts identify a role, a target audience, and a document type?
- Are your prompts sufficiently specific? Are you asking for exactly what you want?
- Is your prompt clear? Would your prompt conform to the technical writing lessons in [Technical Writing One(https://developers.google.cn/tech-writing/one)? If you gave the same prompt to a human, would that person know what you are requesting?

Sometimes, the perfect is the enemy of the good. If a response is very good,
but not quite perfect, it is tempting to continue refining the prompt. However,
it can be more efficient to edit the very good response yourself rather than
endlessly refine the prompt.

> **Note:** LLMs often produce different responses to the *same* prompt. So, even
>       re-issuing the same prompt can sometimes be a form of iteration.

#### Set the context

As mentioned earlier, LLMs can only use the sources available to them.
Providing additional information to establish context helps LLMs generate
better responses. The additional information could include just about any
information relevant to the topic, including:

- Documents
- Meeting transcripts
- Source code
- Emails
- Diagrams

For example, attaching the relevant source code to a prompt can help an LLM
generate a first draft of documentation:

Recommended

> Base the documentation on the attached source code.

An LLM generally assumes that information in attachments is factual, and this
can cause problems. For example, an LLM might mistakenly assume that the bugs
in attached source code are actually features.

Consider this counterpoint
When you rely on an LLM to create a first draft, you lose the *benefits* of the
writing process.

"One writes to know what one is thinking" - Abraham Verghese

Writing is a struggle, but that struggle crystallizes ideas, turning vague
notions into focused plans. Until you write a design document, you haven't
fully worked through all the issues and their solutions. Clear technical
writing is the byproduct of clear technical thought.
Exercise
A design team recorded a brainstorming session aimed at designing a new app.
We captured
[the transcript(https://developers.google.cn/tech-writing/two/artifacts/design-meeting-transcript) of
that highly creative session. Prompt an LLM to create an email based on the
transcript. The email should aim to convince the vice-president of engineering
to fund development of the pet translator app. The vice-president is busy, so
keep the email short and focused.

Click the icon to see a possible answer.

Prompting almost never has a single right answer. That said, here is
one possible prompt:

You are a senior engineer. Based on the transcript, write an email to convince
the vice-president of engineering to fund development of the pet translator app.
Make the tone serious and formal. The vice-president of engineering is busy, so
keep the email short. Start the email with an opening paragraph summarizing the
proposal. Then, provide a three-item bulleted list. Finish with a one-sentence
call to action.

Revise a document
LLMs excel at critical analysis. LLMs are such good critics that they can even
find mistakes in the text that *they* generated.
Reorganize
We recommend fixing organizational issues before editing grammar and style
issues. When prompting an LLM to reorganize documents, a clear detailed prompt
will outperform a vague prompt. For example, the following prompt forces the
LLM to guess at your intentions:
Not recommended

Reorganize the attached course.

In contrast, the following prompt provides context and specificity to help
guide the LLM to reorganize more effectively.
Recommended

The attached course is an introduction to logistic regression in machine
learning. The course is aimed at second-year computer science students
who know how to program in Python but know little to nothing about machine
learning fundamentals. Can you recommend a better organization of the
course modules? For example, what material should I move to a different
module? Should the course discuss classification threshold earlier?

Copy edit
LLMs "know" a tremendous amount about grammar, punctuation, and spelling.
So, a general prompt like the following usually detects embarrassing problems:
Recommended

Find grammatical, punctuation, and spelling issues in the attached passage.

Find style problems
LLMs can spot stylistic issues. For example:
Recommended

Identify any passive voice in the following passage:

Going a step further, you can ask an LLM to suggest edits. For example:
Recommended

Replace any passive voice sentences in the following passage with their
active voice equivalents.

You can ask an LLM to perform a general hunt for style issues:
Recommended

How does the attached document deviate from the writing principles in Google's
Technical Writing One course? Assume that the document is aimed at expert
software engineers seeking to get better at testing automation.

Find other issues
LLMs also excel at finding logical inconsistencies or outright mistakes in
documentation. Providing a role within the prompt can help put the LLM in
the proper "mindset." For example:
Recommended

You are a computer science professor reviewing the attached first draft of
a paper that describes research on a new machine translation paradigm.
Examine the Introduction section for any mistakes in the description of
prior algorithms. Then, assess the rest of the paper for any possible
logical flaws.

Format a document
LLMs can convert a document from one format to another. For example, you can
ask an LLM to convert a Word document to HTML or Markdown. To do so, you'll
need to provide the following:

The document to convert.
The target format.
Any specific formatting requirements.

For example:
Recommended

Convert the attached Word document to Markdown, making all headings
either level 2 or level 3.

You can also ask an LLM to reformat a document to conform to a specific
style guide. For example:
Recommended

Reformat the attached HTML document to conform to the Google developer
documentation style guide.

Summarize a document
Condensing lengthy writing down to 50 or 100 words is so challenging that most
technical professionals struggle to write abstracts, executive summaries,
and overviews. Fortunately, LLMs generally excel at summarization.
Prompts to summarize text should typically identify the following:

Style
Target audience
Purpose
Optionally, tone

For example, here is a good summarization prompt:
Recommended

Write a one-sentence summary of the attached course.
Aim the summary at software engineers who will use the summary
to determine whether to take the course. Make the summary engaging,
yet professional; the summary shouldn't look like marketing literature.

Ironically, a good summarization prompt might be longer than the
generated summary.
In some cases, summaries must match a specific style. Therefore, your
prompt should identify or attach the relevant style guide.
In other cases, although the style isn't codified in a style guide,
your summary should still resemble certain summaries. You can pass those
exemplar summaries as part of the prompt. (This technique is called
[few-shot prompting](https://developers.google.cn/machine-learning/glossary/#few-shot-prompting).)
For example:
Recommended

Write a tldr-style summary for the attached design doc that matches
the style of the following tldr summaries:

This fun four-hour course gives software engineers a solid grounding
in Python.

This hands-on two-hour course guides software engineers through building
better prompts for generating Python code.

Alternate media for summaries
If the medium you are working in *requires* a textual summary, then you'll
need to provide text. Sometimes though, technical people default to producing
textual summaries when a non-text summary (for example, an image or a video)
might be more memorable or engaging.
Or, viewing the problem in a different way, you could ask an LLM to write
a textual summary of an image.
Exercise
We've captured [the
transcript(https://developers.google.cn/tech-writing/two/artifacts/design-meeting-transcript) of
an overly creative brainstorming session to design a new app.
**Task 1:** Prompt your favorite LLM to generate a one-sentence summary of the
pet translation app discussed in the brainstorming meeting. (Copy-and-paste the
transcript along with the prompt.) This summary should get other engineers
interested in working on the project.

Click the icon to see a possible answer.

As always, many different prompts will produce a good response.
Here is one possible prompt:

You are a respected senior engineer. Generate a one-sentence summary of
the attached app discussed in the attached transcript. Aim the summary
at junior engineers. The summary should get those junior engineers interested
in working on the project.

**Task 2:** Prompt your favorite LLM to create an image representing the app.
The image should help non-technical people understand the app.

Click the icon to see a possible answer.

Here is one possibility:

Create an image that helps non-technical people understand the app.

What's next?
Congratulations: you've completed the pre-class work for Technical Writing Two.
If your organization is offering the in-class portion of Technical Writing Two,
do take it. If you'd like to facilitate the in-class portion
of Technical Writing Two, see the
[facilitator's guide(https://developers.google.cn/tech-writing/for-instructors/two/instructors-guide).
A quick compilation of the topics covered in Technical Writing Two
is available on the [Summary(https://developers.google.cn/tech-writing/two/summary) page.


## Summary of Technical Writing Two

> **Estimated Time:** 1 minute

Congratulations! You've completed the pre-class portion of Technical Writing
Two, which covered the following intermediate principles of technical writing:

| Section | Lesson |
|---|---|
| Self-editing |
| Adopt a style guide. |
| Think like your audience. |
| Read documents out loud to yourself. |
| Organizing large docs |
| Determine whether to organize a large amount of information
          into a single long document or a collection of shorter
          documents. |
| Outline first. Alternatively, write free form and then
          reorganize. |
| Introduce a large document by explaining what it covers. |
| Choose headings that describe the task your reader is
          working on. |
| Illustrating |
| Consider writing the caption before creating the
          illustration. |
| Constrain the amount of information in a single drawing. |
| Focus the reader's attention on the relevant part of a picture or
          diagram by describing the takeaway in the caption or by adding a
          visual cue to the picture. |
| Creating sample code |
| Create sample code that is accurate, clear, short, easy to understand,
          and well-commented. |
| Consider providing not only examples but also anti-examples. |
| In tutorials, provide code samples that demonstrate a range of
          complexity. |
| Using LLMs in tech writing |
| Construct detailed prompts by defining a role for the LLM, a
          target audience, a document type, and a specific goal. |
| Revise documents by prompting an LLM to reorganize content,
          copy edit for errors, and identify stylistic or logical
          issues. |
| Generate concise summaries by identifying the summary's purpose,
          target audience, and style. |

The *in-class component* of Technical Writing Two helps you practice
intermediate technical writing principles.

If your organization offers the instructor-led portion of Technical Writing Two,
you're now ready for that class. If your organization doesn't offer the
instructor-led portion of Technical Writing Two, note that Google occasionally
offers the course. See the [Announcements page(https://developers.google.cn/tech-writing/announcements) for
details.


# Writing Helpful Error Messages


## error-handling

- [                Error Messages            ](https://developers.google.cn/tech-writing/error-messages)

# General error handling rules

Before we get to the fun part of the course—wording error messages—let's
discuss a few general error handling rules.

### Don't fail silently

Failure is inevitable; failing to report failures is inexcusable.
Failing silently causes the following problems:

- Users wonder whether something has gone wrong. (*"Why did my order not go through?"*)
- Customer support wonders what caused a problem. (*"The log file gave no indication of a problem."*)

Embrace your software's fallibility. Assume that humans will make mistakes
using your software. Try to minimize ways for people to misuse your software,
but assume that you can't completely eliminate misuse. Therefore, plan error
messages as you design software.

### Follow the programming language guides

Follow the guidelines on error handling in Google's programming language guides,
including:

- [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html)
- [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html), particularly the [Error Messages section](https://google.github.io/styleguide/pyguide.html#3102-error-messages)
- [Google JavaScript Style Guide](https://google.github.io/styleguide/jsguide.html)
- [Google Go Style Guide](https://google.github.io/styleguide/go), particularly the [Error handling section](https://google.github.io/styleguide/go/best-practices#error-handling)

### Implement the full error model

Implement the full error model described in the [Errors page of the Google
AIP.](https://google.aip.dev/193) 
For instance, note the following quote
about implementing error messages in services:

> Services must return a
> [google.rpc.Status](https://github.com/googleapis/api-common-protos/blob/master/google/rpc/status.proto)
> message when an API error occurs, and must use the
> canonical error codes defined in
> [google.rpc.Code](https://github.com/googleapis/api-common-protos/blob/master/google/rpc/code.proto).

The [Errors page of the Google Cloud API design
guide](https://cloud.google.com/apis/design/errors) provides helpful information about implementing the full error
model for Google APIs.

### Avoid swallowing the root cause

API implementations should not swallow the root cause of issues occurring in
the back end. For example, many different situations can cause a
"Server error" problem, including:

- service failure
- network connection drop
- mismatching status
- permission issues

"Server error" is too general an error message to
help users understand and fix the problem. If the server logs contain
identification information about the in-session user and operation, we recommend
providing additional context on the particular failure case.

### Log the error codes

Numeric **error codes** help customer support monitor and diagnose errors.
Consequently, specifying numeric error codes along with textual error messages is often
quite valuable.

You can specify error codes for both internal and external errors.
For internal errors, provide a proper error code for easy lookup/debugging
by internal support personnel and engineers.

Document all error codes.

### Raise errors immediately

Raise errors as early as useful. Holding on to errors and then raising them
later increases debugging costs dramatically.


## identify-the-cause

- [                Error Messages            ](https://developers.google.cn/tech-writing/error-messages)

# Identify the error's cause

Tell users exactly what went wrong. Be specific—vague error messages
frustrate users.

Not recommended

> Bad directory.

Recommended

> The *[Name of directory]* directory exists but is not writable. To add
> files to this directory, the directory must be writable. *[Explanation of
> how to make this directory writable.]*

Not recommended

> Invalid field 'picture'.

Recommended

> The 'picture' field can only appear once on the command line; this command
> line contains the 'picture' field *<N>* times.
> Note: Prior to version 2.1, you could specify the 'picture' field more than
> once, but more recent versions no longer support this.


## invalid-inputs

- [                Error Messages            ](https://developers.google.cn/tech-writing/error-messages)

# Identify the user's invalid inputs

If the error involves values that the user can enter or modify (for example,
text, settings, command-line parameters), then the error message should
identify the offending value(s).

Not recommended

> Funds can only be transferred to an account in the same country.

Recommended

> You can only transfer funds to an account within the same country.
> Sender account's country (UK) does not match the recipient account's
> country (Canada).

Not recommended

> Invalid postal code.

Recommended

> The postal code for the US must consist of either five or nine digits.
> The specified postal code (4872953) contained seven digits.

If the invalid input is a very long value that spans many lines,
consider doing one of the following:

- Disclose the bad input progressively; that is, provide one or more clickable  ellipses to enable users to control how much additional error information  they want to see.
- Truncate the bad input, keeping only its essential parts.

#### Multiple choice exercise


## specify-requirements

- [                Error Messages            ](https://developers.google.cn/tech-writing/error-messages)

# Specify requirements and constraints

Help users understand requirements and constraints. Be specific.
Don't assume that users know the limitations of your system.

Not recommended

> The combined size of the attachments is too big.

Recommended

> The combined size of the attachments (14MB) exceeds the allowed limit (10MB).
> *[Details about possible solution.]*

Not recommended

> Permission denied.

Recommended

> Permission denied.  Only users in <group name> have access.
> *[Details about adding users to the group.]*

Not recommended

> Time-out period exceeded.

Recommended

> Time-out period (30s) exceeded.  *[Details about possible solution.]*


## show-fix

- [                Error Messages            ](https://developers.google.cn/tech-writing/error-messages)

# Explain how to fix the problem

Create **actionable error messages**. That is, after explaining the cause of
the problem, explain how to fix the problem.

Not recommended

> The client app on your device is no longer supported.

Recommended

> The client app on your device is no longer supported. To update the client app,
> click the **Update app** button.

Here's a second example:

Not recommended

> Could not fetch resource:
>   - Quota 'CPUS' exceeded. Limit: 1.0 in region us-central-1.

Recommended

> You requested 2.0 CPUs, which exceeds your quota of 1.0 CPUs in the
> us-central-1 region. To fix the problem, take either of the following
> actions:
>   - Increase your CPU quota in the us-central-1 region.
>   - Make your request in a region where you have more CPU quota.
> See *[URL of documentation]* for details.


## provide-examples

- [                Error Messages            ](https://developers.google.cn/tech-writing/error-messages)

# Provide examples

Supplement explanations with examples that illustrate how to correct the
problem.

Not recommended

> Invalid email address.

Recommended

> The specified email address (robin) is missing an @ sign and a
> domain name. For example: robin@example.com.

Not recommended

> Invalid input.

Recommended

> Enter the pathname of a Windows executable file. An executable file
> ordinarily ends with the .exe suffix. For example:
> C:\Program Files\Custom Utilities\StringFinder.exe

Not recommended

> Do not declare types in the initialization list.

Recommended

> Do not declare types in the initialization list.
> Use calls instead, such as 'BankAccount(owner, IdNum, openDate)' rather than
> 'BankAccount(string owner, string IdNum, Date openDate)'

Not recommended

> Syntax error on token "||", "if" expected.

Recommended

> Syntax error in the "if" condition.
> The condition is missing an outer pair of parentheses.
> Add a pair of bounding opening and closing parentheses to the
> condition.  For example:
> if   (a > 10) || (b == 0)  # Incorrect
> if ((a > 10) || (b == 0)) # Correct

#### Multiple choice exercise


## be-concise

- [                Error Messages            ](https://developers.google.cn/tech-writing/error-messages)

# Be concise

Write concise error messages. Emphasize what's important. Cut unnecessary text.
See the
[Short sentences unit
of Tech Writing One(https://developers.google.cn/tech-writing/one/short-sentences)
for tips on reducing sentence length.

Not recommended

> Unable to establish connection to the SQL database. *[Explanation of how to
> fix the issue.]*

Recommended

> Can't connect to the SQL database. *[Explanation of how to fix the issue.]*

Not recommended

> The resource was not found and cannot be differentiated. What you selected
> doesn't exist in the cluster.
> *[Explanation of how to find valid resources in the cluster.]*

Recommended

> Resource <name> isn't in cluster <name>.
> *[Explanation of how to find valid resources in the cluster.]*

Converting from [passive voice to active voice(https://developers.google.cn/tech-writing/one/active-voice)
often makes sentences conciser and easier to understand:

Not recommended

> The Froobus operation is no longer supported by the Frambus app.

Recommended

> The Frambus app no longer supports the Froobus operation.

In your enthusiasm to be concise, don't remove so many words that the
resulting error message becomes cryptic. For example, don't reduce the
preceding error message down to the following:

Not recommended

> Unsupported.

#### Multiple choice exercise


## avoid-double-negatives

- [                Error Messages            ](https://developers.google.cn/tech-writing/error-messages)

# Avoid double negatives

A **double negative** is a sentence or phrase that contains two negative words,
such as:

- *not*, including contractions like *can't*, *won't*
- *no*

Readers find double negatives hard to parse. ("Wait, do two negatives make a
positive or is the author of the error message using two negatives to emphasize
something I shouldn't do?")

Some double negatives in error messages are blatant:

Not recommended

> You cannot not invoke this flag.

Recommended

> You must invoke this flag.

Other double negatives are more subtle. For example, the words *prevents* and
*forbidding* in the following error message are both negatives, leading to
a confusing message:

Not recommended

> The universal read permission on *pathname* prevents the operating
> system from forbidding access.

Recommended

> The universal read permission on *pathname* enables anyone to read
> this file. Giving access to everyone is a security flaw. See *hyperlink*
> for details on how to restrict readers.

Similarly, avoid exceptions to exceptions.

Not recommended

> The App Engine service account must have permissions on the image, except the
> Storage Object Viewer role, unless the Storage Object Admin role is available.

Recommended

> The App Engine service account must have one of the following roles:
> Storage Object Admin
> Storage Object Creator


## target-audience

- [                Error Messages            ](https://developers.google.cn/tech-writing/error-messages)

# Write for the target audience

Tailor the error message to the target audience. That is:

- Use appropriate terminology for that target audience.
- Be mindful of what the target audience knows and doesn't know.

Beware of the
[ curse
of knowledge(https://developers.google.cn/tech-writing/one/audience#curse_of_knowledge) when writing error messages. A term familiar to you might
not be familiar to your target audience.
For example, the following error message contains terminology
appropriate for a target audience of ML experts. If the target audience
includes a significant number of people who aren't ML experts, then the
error message is mystifying:

Recommended for ML experts only

> Exploding gradient problem. To fix this problem, consider gradient clipping.

Now compare the following two error messages. The first error message contains
technical truth, but terms like *server*, *client*, *farm*, and *CPU* are
not going to help most consumers:

Inappropriate for shoppers

> A server dropped your client's request because the server farm is running
> at 92% CPU capacity. Retry in five minutes.

The second error message is more suitable (and comforting) for a
non-technical audience:

Appropriate for shoppers

> So many people are shopping right now that our system can't complete your
> purchase. Don't worry--we won't lose your shopping cart.  Please retry your
> purchase in five minutes.

#### Multiple choice exercise


## use-terminology-consistently

- [                Error Messages            ](https://developers.google.cn/tech-writing/error-messages)

# Use terminology consistently

Use terminology consistently for all error messages within a single
product area. If you call something a "datastore" in one error message,
then call the same thing a "datastore" in all the other error messages.

Not recommended

> Can't connect to cluster at 127.0.0.1:56. Check whether minikube is running.

Recommended

> Can't connect to minikube at 127.0.0.1:56. Check whether minikube is running.

> **Note:** Some authoring systems automatically recommend synonyms to ensure that
> you don't keep repeating the same word. Yes, variety spices up paragraphs.
> However, variety in error messages can confuse users.

Error messages must appear consistently with similar formats and
non-contradictory content; that is, the same problem must generate the same
error message. For example, if different parts of an app each detect problems
with internet connection, both parts should emit the same error message.

readability(https://developers.google.cn/tech-writing/error-messages/format-for-readability)


## format-for-readability

- [                Error Messages            ](https://developers.google.cn/tech-writing/error-messages)

# Format error messages to enhance readability

A few simple techniques help error messages stand out from the
surrounding text and code.

#### Link to more detailed documentation

When an error requires a lengthy explanation (for example, multiple sentences)
and appropriate documentation is available, use links to redirect users to
more detailed documentation.

Not recommended

> Post contains unsafe information.

Recommended

> Post contains unsafe information. Learn more about safety
> at <link to documentation>.

#### Use progressive disclosure

Some error messages are long, requiring a lot of text to explain the problem
and solution. Unfortunately, users sometimes ignore long error messages,
intimidated by the "wall of text." A good compromise is to display a briefer
version of the error message and then give users the option to click something
to get the full context.

Not recommended

> TextField widgets require a Material widget ancestor, but none were located.
> In material design, most widgets are conceptually “printed” on a sheet of
> material. To introduce a Material widget, either directly include one or use
> a widget that contains a material itself.

Recommended

> TextField widgets require a Material widget ancestor, but none were located.
> **...**(Click to see more.)
>   In material design, most widgets are conceptually "printed" on a
> sheet of material. To introduce a Material widget, either directly include
> one or use a widget that contains a material itself.

#### Place error messages close to the error

For coding errors, place error messages as close as possible to the place
where the error occurred.

Not recommended

> 1: program figure_1;
> 2: Grade = integer;
> 3: var
> 4. print("Hello")
> Use ':' instead of '=' when declaring a variable.

Recommended

> 1: program figure_1;
> 2: Grade = integer; 
> ---------^ Syntax Error
> Use ':' instead of '=' when declaring a variable.
> 3: var
> 4. print("Hello")

#### Handle font colors carefully

A surprising percentage of readers are color blind, so be careful with
colors in error messages. For example, the following error message will
mystify some readers:

Not recommended

> The argument expects only digits. Therefore, the supplied value is
> only partially correct:
> 3728LJ947

Many forms of color blindness exist, so just avoiding a red/green
combination isn't sufficient. Because you can't depend on all your
users being comfortable with color, we recommend pairing color with
another visual cue. For example, the following error message pairs
color with boldface:

Recommended

> The argument expects only digits. Therefore, the highlighted part of the
> supplied value is incorrect:
> 3728**LJ**947

The following example pairs color with extra spaces:

Recommended

> The argument expects only digits. Therefore, the highlighted part of the
> supplied value is incorrect:
> 3728  LJ  947

Alternatively, you could skip color completely:

Recommended

> The argument expects only digits. Therefore, the highlighted characters
> in the supplied value are incorrect:
> 3728LJ947
>     ^^


## set-tone

- [                Error Messages            ](https://developers.google.cn/tech-writing/error-messages)

# Set the right tone

The tone of your error messages can have a significant effect on how your users
interpret them.

#### Be positive

Instead of telling the user what they did wrong, tell the user how to get
it right.

Not recommended

> You didn't enter a name.

Recommended

> Enter a name.

Not recommended

> You entered an invalid postal code.

Recommended

> Enter a valid postal code. *[Explanation of valid postal code.]*

Not recommended

> ANSI C++ forbids declaration 'ostream' with no type 'ostream'.

Recommended

> ANSI C++ requires a type for declaration 'ostream' with type 'ostream'.

#### Don't be overly apologetic

While maintaining positivity, avoid the words "sorry" or "please."
Focus instead on clearly describing the problem and solution.

> **Note:** Different cultures interpret apologies differently. Some cultures expect
> apologies in certain situations; other cultures find apologies from software
> corporations somewhat insincere. Although this lesson suggests avoiding
> apologies, be aware of your target audience's expectations.

Not recommended

> We're sorry, a server error occurred and we're temporarily unable
> to load your spreadsheet.
> We apologize for the inconvenience. Please wait a while and try again.

Recommended

> Google Docs is temporarily unable to open your spreadsheet. In the meantime,
> try right-clicking the spreadsheet in the doc list to download it.

#### Avoid humor

Don't attempt to make error messages humorous.  Humor in error messages can
fail for the following reasons:

- Errors frustrate users. Angry users are generally not receptive to humor.
- Users can misinterpret humor. (Jokes don't always cross borders well.)
- Humor can detract from the goal of the error message.

Not recommended

> Is the server running? Better go catch it :D.

Recommended

> The server is temporarily unavailable. Try again in a few minutes.

#### Don't blame the user

If possible, focus the error message on what went wrong rather than assigning blame.

Not recommended

> You specified a printer that's offline.

Recommended

> The specified printer is offline.

#### Multiple choice exercise


## want-to-play-a-game

- [                Error Messages            ](https://developers.google.cn/tech-writing/error-messages)

# Want to play a game?

Challenge yourself by answering these five questions.

### Question 1

### Question 2

### Question 3

### Question 4

### Question 5


## summary

- [                Error Messages            ](https://developers.google.cn/tech-writing/error-messages)

# Course summary

This course recommended the following best practices when writing
error messages:

- Identify the cause of the error.  If the user entered an invalid value, specify the invalid value. Specify requirements and constraints, such as required permissions or minimum RAM.
- Explain how to fix the problem.  When appropriate, provide an example to help demonstrate the fix.
- Write clearly.  Be concise, not wordy. However, don't be so concise that the resulting error message becomes cryptic. Avoid double negatives and exceptions to exceptions. Aim the message at the appropriate target audience. Words appropriate for software engineers are often inappropriate for non-technical users. Use terminology consistently. For example, don't use the term *directory* in one part of an error message and a *folder* in another part. Format long error messages carefully, possibly using progressive disclosure or links to expanded documentation. Set a positive tone. Don't be overly apologetic.


## back-end

- [                Error Messages            ](https://developers.google.cn/tech-writing/error-messages)

# Additional guidelines for back-end engineers

This lesson contains recommendations specifically for back-end
software engineers.

### Supply error codes

If an error code exists, include it as part of the error message.
Error codes help technical users identify the error and find more
information from an error index or error catalog.

Not recommended

> Error: You already own this bucket. Select another name from the
> dropdown list.

Recommended

> Error 409: You already own this bucket. Select another name from the
> dropdown list.

### Include an Error Identifier

Engineers parse logs to learn how and why errors occurred; therefore, include
an Error Identifier to help engineers find particular errors more easily.
The Error Identifier should stay constant, even if the textual error message
changes.

For more information, see the [Errors unit of
AIP-193.](https://google.aip.dev/193)

Not recommended

> { "error" : "Bad Request - Request is missing a required
> parameter: -collection_name.  Update parameter  and resubmit.

Recommended

> { "error" : "Bad Request - Request is missing a required
> parameter: -collection_name.  Update parameter and resubmit.
> Issue Reference Number BR0x0071" }


# Tech Writing for Accessibility


## inclusive-design

- [                Accessibility            ](https://developers.google.cn/tech-writing/accessibility)

# Design for everyone

This overview introduces key concepts of writing for everyone.

Types of disability
Disability can be visible or invisible, and it can be situational, temporary, or
permanent. The following table includes some examples.

**Vision**
**Hearing**
**Speech**
**Mobility**
**Cognition**

**Situational**
Driving
Dark room
Noisy environment
In a library
At a lecture
In bed
Arms/hands full
Forgetting information
Time demands

**Temporary**
Dilated pupils
Cataracts
Ear infection
Laryngitis
Arm or hand injury
No prior training
Multi-tasking

**Permanent**
Blindness
Vision impairment
Deaf
Hard-of-hearing
Dysarthria
Stuttering
Amputation
Parkinson's disease
Dementia

According to the [World Health Organization](https://www.who.int/news-room/fact-sheets/detail/disability-and-health),
about 16% of the world's population experiences significant disability. However,
as the preceding table illustrates, disability shows up in various ways and can
affect anyone at different times in life. Designing for everyone does indeed
benefit everyone.
The curb cut effect
Designing for everyone often results in benefits beyond the intended
use cases.
The *curb cut effect* is a common example of beneficial design in the physical
world. Originally, curb cuts (sidewalk ramps) were designed for people in
wheelchairs. However, many people benefit from curb cuts, such as anyone with a
stroller, suitcase, or delivery cart.
Here are some other examples of the curb cut effect in digital technology:

**Contrast ratios**: Color contrast requirements were originally designed to
help people who have low vision or color blindness. Color contrast
requirements also ended up helping people who are trying to see the phone
screen on a sunny day, or who had their pupils dilated at the eye doctor.
**Text to speech and voice commands**: These tools assist people who are blind
or have low vision. They also turned out to be useful for hands-free
use while driving, cooking, or holding a baby.
**Keyboard access**: Improving keyboard navigability improves accessibility
for screen reader users and people with motor impairments. Keyboard access
also improves productivity for power users.
**Clear language**: Simplifying language makes documentation easier to
understand, and it also eases translation and localization.


## write-alt-text

- [                Accessibility            ](https://developers.google.cn/tech-writing/accessibility)

# Write helpful alt text

*Alternative text* (alt text) is short, descriptive text that acts as a
substitute for visual items on a page. The most common use is for describing
images.

Alt text supports readers in the following ways:

- Screen readers read alt text for people who are blind or who have low vision.
- Descriptive alt text also helps to [improve search results for images](https://developers.google.cn/search/docs/appearance/google-images).

### Write useful alt text

Alt text acts as a functional equivalent of an image for readers who can't
view the image. The following subsections describe best practices for writing
helpful alt text.

#### Explain the image in context

Explain images in the context of the text. For example, the following
photograph shows a black-capped chickadee perched on a snowy branch:

In the context of the surrounding text, you might choose to emphasize or
omit aspects of an image in your description. Consider the following snippets
of text:

Snippet 1:

> A mixed-species flock is a flock of different bird species that travel
> together. In northern temperate zones, chickadees and titmice typically lead
> mixed flocks with other small songbirds. The calls of the chickadees and
> titmice alert the other species to nearby food or threats.

In the context of this snippet, the purpose of the image is to show an example
of a bird species that leads the mixed flock. The time of year, the specific
type of chickadee, or details about the appearance of the chickadee are not
important for that purpose. Alt text that identifies the bird species is
sufficient.

Snippet 2:

> Black-capped chickadees cache food and can remember the locations where they
> stored it for up to 28 days. In winter, they lower their body temperature
> during the night to conserve energy. They also fluff their feathers to trap
> warm air, and the layers of warm air provide insulation from the cold.

This snippet specifically mentions the black-capped chickadee and its fluffed
feathers in cold weather. In this context, the type of chickadee and its
appearance in winter are relevant, so the alt text description should
include those aspects of the image:

The following Google Chrome Developers video explores other examples of how
context affects the way you describe an image:

#### Briefly summarize the image's purpose

Use a short phrase or one or two sentences. Long descriptions interrupt the
reading flow for screen reader users.

- Don't include extra words like "Image of" or "Photo of."
- Capitalize the first word and include a final period.
- Use other punctuation as necessary.

Screen readers generally pause for periods and some other types of
punctuation. Although a final period is not technically required, it
provides auditory separation between the image description and the body
text that follows the image.

The Web Accessibility in Mind site provides guidelines for designing content
that is compatible with screen readers, including a summary of
[how screen readers read content](https://webaim.org/techniques/screenreader/#how).

If you can't capture the meaning of the image in a sentence or two, describe the
meaning of your image in the text of your document. See [Describe complex images
in your document](#complex-images).

#### Avoid duplicating the surrounding text

If the meaning of your document would be the same without the image, add
an empty alt text attribute to the image (`alt=""`). Assistive technologies
ignore the empty attribute.

Use empty alt text in the following situations:

- The image is decorative (not informative), such as an image of a horizontal line that is meant to be a visual border at the end of a page. Consider making a decorative image a CSS background image, since background images are always ignored by screen readers.
- The image duplicates information that is already expressed in text on the page.

If you don't include alt text for an image, then screen readers read the
filename aloud instead of ignoring the image. A user of a screen reader has
no information to indicate whether the image contains useful information.

#### Describe complex images in your document

The information in a complex image such as a flowchart, graph, or map can be
difficult to describe in a few short sentences. In this situation, provide
a short description of the image in the alt text and a longer textual
description in the main text of your document or on a separate page that you
link to.

- For graphs, you can provide a data table on the same page or on a separate page.
- For flowcharts and diagrams, explain the process or parts of your image in the text of your document.

For example, the [Software supply chain threats](https://cloud.google.com/software-supply-chain-security/docs/attack-vectors) page
has a diagram with phases of software development and potential entry points for
vulnerabilities and software attacks.

- The alt text for the diagram is `A diagram that shows entry points for software supply chain attacks.`
- The body text introduces the image, explains the use of the image legend, and then explains each section of the diagram in context.

In situations where the image and the detailed description aren't close
together, specify the location of the detailed description in the alt text. The
following alt text example includes the section heading for the detailed
description.

> **Note:** Avoid using the `longdesc` attribute to describe complex images. The
> `longdesc` attribute is not well supported by screen readers. The attribute is
> also an [obsolete feature](https://html.spec.whatwg.org/multipage/obsolete.html) in the HTML Living
> Standard.

#### Include demographic information only when necessary

When you describe people, include demographic information only if it is critical
to the main point of the image. Otherwise, use *person* or another term that
provides key context about the person's activity or role in the image, such as
*musician*, *basketball player*, *teacher*, or *doctor*.

For information about using appropriate language to describe people, see
[Inclusive language](https://developers.google.cn/style/inclusive-documentation) in the Google developer
documentation style guide.

#### Other considerations

- For repeated images, use consistent alt text.
- Avoid all caps.  Words in all caps always have a rectangular shape, whereas words in regular case have distinct shapes. Some people with visual or cognitive disabilities rely more on the shape of words to read them. Screen readers might misread words in all caps as acronyms.
- Introduce diagrams in the body text, not in the alt text.

### Examples

The following examples apply the principles of writing helpful alt text.

Review the alt text options for each example. The most appropriate option
provides concise and relevant context for the image.

#### Example 1

Consider these alt text options:

- Too concise: `alt="Waffles."`
- Too wordy: `alt="Photo of a round white plate with 17 slices of red strawberries surrounding a stack of three golden-brown waffles with two whole red strawberries on top, with leaves."`
- Just right: `alt="A stack of waffles on a plate with strawberries."`

#### Example 2

The Go gopher is the mascot of the Go programming language.

Consider these alt text options:

- Too concise: `alt="Gopher."`
- Too wordy: `alt="Drawing of blue Go gopher with large round eyes, small yellow paws, single white tooth, and pink hat with small tassel, blowing noisemaker with orange and yellow stripes."`
- Just right: `alt="Go gopher with noisemaker and 10th anniversary party hat."`

### Exercises

Practice what you have learned by writing some alt text.

For each image:

1. Imagine a context for the image.
2. Write alt text that's appropriate for the context you chose.

#### Exercise 1

Your alt text

#### Exercise 2

Image source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:United_States_per_capita_energy_use_1650-2010.png)

Your alt text

#### Learn more

- Read the Google developer documentation style guidelines on [Accessibility](https://developers.google.cn/style/accessibility) and [Alt text](https://developers.google.cn/style/images#alt-text)
- Read the [W3C tutorial for images](https://www.w3.org/WAI/tutorials/images/)
- Read the [Web Accessibility in Mind alt text guidelines](https://webaim.org/techniques/alttext/)


## sufficient-contrast

- [                Accessibility            ](https://developers.google.cn/tech-writing/accessibility)

# Use sufficient contrast

Higher contrast makes it easier for everyone to read text and images. When there
is low contrast, everyone has difficulty viewing content.

Color blindness affects over 300 million people worldwide: 1 in 12 men and 1 in
200 women.

Higher contrast helps people with color blindness and low vision, or anyone that views a screen in
bright sunlight.

Visit [Colour Blind Awareness](https://www.colourblindawareness.org/colour-blindness/types-of-colour-blindness/) to learn more about the effects of color blindness.

[WCAG](https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-contrast.html) suggests these minimum contrast ratios:

- 4.5:1 for small text
- 3:1 for large text (at least 14 pt bold/18 pt regular)

Consider the following contrast examples:

- Poor contrast
- Better contrast
- Best contrast

### Exercise: Choose colors with sufficient contrast

Complete the following exercise to practice measuring sufficient color contrast:

1. In a separate browser window, open the [Contrast Checker](http://webaim.org/resources/contrastchecker) by Web Accessibility In Mind (WebAIM).
2. In the contrast checker, enter the following Hex colors to find out which foreground-background ratios meet contrast requirements. Record the contrast ratios on a notepad or separate document to compare your answers with the [possible answers](#answers).

1. First rectangle:
2. Second rectangle:
3. Third rectangle:

**Click the icon to see the expected answers.**

First rectangle: FAIL

Foreground: #148695
Background: #FD9C32

Second rectangle: FAIL

Foreground: #EBFF33
Background: #667E8B

Third rectangle: FAIL

Foreground: #128697
Background: #EAEAEA

Even though some of the pairs may *look* higher contrast, none of them actually meets WCAG standards.
Unfortunately,  "eyeballing it isn't enough"—it's best to use a contrast checker.

Use minimum contrast guidelines to ensure that everyone can see your content.


## inclusive-language

- [                Accessibility            ](https://developers.google.cn/tech-writing/accessibility)

# Choose language that benefits everyone

When writing about people with disabilities or about accessibility, be mindful
about using unintentionally biased language that may cause harm.

### Write thoughtfully about disability

Don't use euphemisms or patronizing terms:

- **Avoid** describing people without disabilities as *normal* or *healthy*.
- **Better**: *nondisabled person, sighted person, hearing person, person without disabilities, neurotypical person*.
- **Avoid** terms that reflect or project feelings and judgements about a person's disability, such as *victim of, suffering from, wheelchair-bound*.
- **Better**: *experiencing, living with, uses a wheelchair*

### Person-first and identity-first language

When writing about accessibility and people with disabilities, be sure to
center the person or community, and avoid terms that remove personhood.

- **Avoid** language like *the disabled*
- **Better**: *people with disabilities*

**Note**: While person-first language is generally preferred (person with a
cognitive impairment, person with low vision), some people prefer identity-first
language; for example, this preference is common in Deaf and neurodivergent
communities (Deaf person, neurodivergent person).

Before writing about a community, take time to educate yourself about how the
community prefers to be identified and described. Some helpful resources include
the following:

- [Write documentation for all](https://developers.google.cn/style/inclusive-documentation): General guidelines and examples that illustrate some best practices for writing documentation for everyone.


## visual-cues

- [                Accessibility            ](https://developers.google.cn/tech-writing/accessibility)

# Add accessible visuals to writing

In this unit, you learn how to create accessible visuals that use a mix of text
and visual elements, rather than relying on visual cues to convey information.

### Why visual indicators are insufficient

Visual cues like color, shape, and pattern can be effective tools for
communicating information. However, to ensure that content is accessible to a
wide audience, don't rely exclusively on the visual elements, such as the
following:

- colors
- patterns
- images
- font styling
- directional words (for example, "top-right corner")

Instead, use a mix of these visual elements and accompany them with descriptive
text to convey information. It is also important to provide text descriptions or
alternative text when using images, diagrams, or other diagrams.

Users with visual impairments, including color blindness, may not fully perceive
certain visual cues. Incorporating a mix of visual elements with accompanying
descriptive text helps ensure that the intended meaning is conveyed to everyone,
regardless of their ability to perceive the visuals. This approach can also help
eliminate ambiguity that might arise if the meaning or purpose of a color or
shape is not clear to everyone.

### Examples

The following examples help illustrate why it's important not to rely only on
color to communicate information, and how you can use text, color, and symbols
to enhance the accessibility of your visuals.

#### Don't rely on color alone

The following example of comma usage, adapted from the [Google
developer documentation style
guide](https://developers.google.cn/style/commas#commas-separating-two-independent-clauses), relies only on color (red and green) to communicate important
information, thus excluding anyone who is color blind or otherwise visually
impaired.

Some color-blind users can't distinguish between the red text and the green
text, so they'd be unable to tell from the previous example alone which example
is correct. The only distinguishing factor in this example is the color, so
people who either can't see the text or can't distinguish between the colors
wouldn't be able to tell which is the correct example.

#### Use text, color, and symbols for better accessibility

The following example uses the red "thumbs down" and the green "thumbs up"
symbols in addition to text. This change makes it so the text would be clear
even if you removed all color and other visual indicators.

The use of color with the thumbs up and thumbs down symbols could be a useful
visual reference for people who can see them. For people who can't see or
distinguish between the visual cues, providing descriptive text (in this case,
"Not recommended" and "Recommended") is helpful.

### Exercise: Fix a diagram

Next, think about how you could edit the following diagram to make it more
accessible.

This diagram uses rectangles of different colors to represent categories.
Because the diagram relies solely on color to differentiate categories, it
presents accessibility challenges. To make the diagram more accessible, consider
incorporating design elements such as different shapes, line weights, patterns, or
text labels to clearly differentiate the categories.


## editing-accessibility

- [                Accessibility            ](https://developers.google.cn/tech-writing/accessibility)

# Edit for accessibility

In this unit, you learn how to edit your own and others' writing to make it more
accessible to all users. The unit focuses on ways to write—and
edit—your documentation to make it accessible to everyone. This unit is not meant
as an exhaustive reference, but it does describe some general best practices for
editing documentation to focus on accessibility.

### Cultivate an accessibility mindset for doc editing

When you are aware of and focus on the fundamentals of good writing, you also
make your documentation more accessible.

With practice, self-editing can help you catch accessibility pitfalls, such as
these:

- poor or missing headings
- uninformative link text
- dense, complex text

### Create helpful headings

Headings help your audience understand what's in your document. Clear,
well-structured document headings simplify navigation for people with
cognitive disabilities and those who use screen readers.

- Tag headings with heading elements.  HTML: `<h1>`, `<h2>`, `<h3>` ... Markdown: `#`, `##`, `###` ...
- Use a level-1 heading for the page title or main content heading.
- Don't skip levels of the heading hierarchy. For example, don't jump from an `<h1>` to an `<h3>`.

References:

- [Headings and titles](https://developers.google.cn/style/headings)
- [Cognitive accessibility design pattern:  Make the site hierarchy easy to understand and navigate](https://www.w3.org/WAI/WCAG2/supplemental/patterns/o2p02-site-structure/)
- [Making content usable for people with cognitive and learning disabilities](https://www.w3.org/TR/coga-usable/#summary-find)

### Include informative link text

People who use screen readers often use them to scan a page to hear just the
links. Use informative link text to ensure that your audience hears meaningful
information, not just "Learn more, learn more, learn more."

- Avoid:  [Learn more](https://developers.google.cn/style/tables) [Click here](https://developers.google.cn/style/tables) [This document](https://developers.google.cn/style/tables)
- Good:  Learn how to [format tables](https://developers.google.cn/style/tables). Read about [machine learning](https://developers.google.cn/machine-learning).

> **Bonus:** Informative link text also improves search engine optimization.

Reference: [Link text](https://developers.google.cn/style/link-text)

### Use straightforward language and short sentences

Other units in this course talk about making visual images accessible to
everyone. Remember that abstract and unfamiliar *written* representations
can also be particularly challenging for users with cognitive or visual
impairments.

Avoid unfamiliar jargon, US-based slang, pop-cultural references, and
complicated linguistic constructions. Use active voice and short sentences,
and define your technical terms on first use if they are not commonly
understood.

References:

- [Active voice](https://developers.google.cn/style/voice)
- [Jargon](https://developers.google.cn/style/jargon)
- [Designs that make use of abstract imagery and metaphors](https://www.w3.org/TR/coga-usable/#amy-scenario-3-designs-that-make-use-of-abstract-imagery-and-metaphors)

### Exercise: Edit a document

In this exercise, you edit a short document to make it more accessible.

Focus on the order in which the information is presented; place writing tips
first. Simplify the wording where possible. You can change anything, but
especially look for accessibility pitfalls such as missing or unnecessary
headings, uninformative link text, and dense, complex text.

Whenever possible, streamline and simplify the wording. This suggestion isn't
accessibility-specific; however, as with many writing tips, good writing is good
for accessibility.

Now, make a copy of the following exercise and edit it for
accessibility.

> A list of reasons why simplifying a document through editing is good
> Determine whether or not you can simplify your document through the use of
> terminology that is equivalent but relatively shorter in length and therefore
> more easily comprehensible by your audience. It's important to make sure your
> document is edited before it is seen by your audience, which might include
> people that are less or more familiar with the matter covered by your
> document.
> Step 1
> The first thing you need is a rough draft. Some things
> that can help make your document easier to read are making sure you have links
> to background information, and also checking for active voice instead of
> passive voice. If you have long sentences you can consider shortening them or
> implementing the use of a list to make the information easier to scan.
> Step 2
> The second thing you need is a list of resources that will help you edit, like
> [this page](https://developers.google.cn/style/).
> Also [this other one is
> good,too](https://learn.microsoft.com/en-us/style-guide/accessibility/writing-all-abilities).
> Once you have editing resources to use as you edit, you can use them to edit
> your document.

#### Tips for getting started

The title of the exercise is *A list of reasons why simplifying a
document through editing is good*; one approach might be to look for language
that could be presented in a bulleted list or lists.

Highlight or otherwise identify phrases that could work as bulleted items. Start to build your bulleted list (or lists). As you do so, look for ways to make complex text simpler by using active voice and short phrases. Revise link text to be informative. Keep list items parallel.

##### Build your bulleted list

The following table shows how you might begin to break down the longer paragraphs into concise bulleted lists.

| Existing text | Possible list items | Edited list items |
| Paragraph 1: Determine whether or not you can simplify your document through the use of terminology that is equivalent but relatively shorter in length and therefore more easily comprehensible by your audience . | Determine whether or not you can simplify your document . Use terminology that is equivalent but relatively shorter in length. Make sure your material is comprehensible to your audience . | Simplify : Use short sentences. Check terminology : If you use words that might be unfamiliar to your audience, include definitions. Note: The second bullet covers this already. |
| Paragraph 2: It's important to make sure your document is edited before it is seen by your audience , which might include people that are less or more familiar with the matter covered by your document. | Make sure your document is edited . Note: You've already addressed the need to know your audience . You can cut this repetitive information. | Edit : Request a review or peer edit from someone who is
familiar with your subject matter. |

> **Note:** Learn more about creating lists in [Tech Writing One](https://developers.google.cn/tech-writing/one/lists-and-tables).

If you continue breaking down the existing text into possible bulleted items,
you can organize and order the items logically, which will make the information
easier for your readers to understand and act on.

### Test your content for accessibility

Finally, to get a feel for some different ways your users might access and
consume your document, try these testing tips:

- Change the zoom level to help accommodate readers on small screens or full-size monitors.
- Use only the keyboard to navigate your document. For example, see [Keyboard shortcuts in Chrome](https://support.google.com/chrome/answer/157179).
- Use a screen reader:  ChromeVox for ChromeOS VoiceOver for Mac

These methods can help you assess the usability of your document for different
audiences as you edit your own and others' documents for accessibility.


## conclusion

- [                Accessibility            ](https://developers.google.cn/tech-writing/accessibility)

# Course summary

Technical Writing for Accessibility focused on the following ideas:

- Accessibility in documentation benefits people with permanent, temporary, or situational disabilities.
- Every image requires an alt text element. Alt text acts as a functional equivalent for an image by providing a concise summary of the image's purpose and context.
- Sufficient color contrast helps readers with color blindness or low vision.
- Write for a broad spectrum of readers.
- Avoid relying only on visual indicators, such as colors or patterns, to communicate important information.
- Practice editing for accessibility to ensure proper heading structure, descriptive link text, and clear language.

### Continue learning

- [Write accessible documentation](https://developers.google.cn/style/accessibility): Accessibility guidelines
