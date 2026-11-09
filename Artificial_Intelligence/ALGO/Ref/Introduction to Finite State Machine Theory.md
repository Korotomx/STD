![](https://www.youtube.com/watch?v=05zp5vbYXSQ)

After studying digraphs and regular expressions, we have a pretty good foundation for our next topic – finite state machines. A finite state machine, or FSM, can be used to represent the flow of just about any system. It's directed edges transition us from state to state to state until we reach completion. In this episode, we introduce FSM and use regular expressions to show how they are used.  
  
Timestamps  
00:00 | Intro  
03:27 | Components of a finite state machine  
06:08 | Review of basic RegEx forms  
08:26 | Finite state machines for basic RegEx forms  
13:11 | Finite state machines for more complex RegEx forms  
16:34 | Finite state machines for Ethernet preamble and SFD  
19:30 | Representing FSMs with a state transition table  
  
Hashtags  
#fsm #finite #automata

## Transcript

### Intro

**0:00** · now that we have studied digraphs and regular Expressions we're ready to do finite State \[Music\] machines let's say we want to figure out when we finished capturing four binary bits ones and zeros it's usually referred to as a nibble and so what you do is you start out you've got you've received no digits at all and then you receive the first digit and then the second digit and then the third digit and the fourth digit you've received the fourth digit we did it okay now now how

**0:30** · many conditions do we have to this particular system these are called States and so I've got the first state no digits at all I've got the second state one digit and then two digits and then three digits and four digits so I have five states now I can represent these using well kind of a notation similar to what we've been using with our diagraphs I can have one two 3 four

**0:54** · five states I'm going to label these Q Sub 0 Q sub 1 Q2 Q3 Q4 all right now which is our starting State the initial State the one where we're we've got no digits at all well that would be q0 and so I'm going to put a little arrow there to identify it as the reset State the starting State now if I receive a zero or a one that

**1:19** · takes me to the next state so I know I've got one digit and then I receive another Z or01 and I go to the next state and I receive another Zer or one and I go to the next state and then I receive another Z 1 and I get to the last state now there is a way to identify this as the last state instead of being a single Circle I make this

**1:38** · double circle this these two circles that are embedded in each other now what I need to know also that takes me from state to state to state well with this system it's kind of silly because I don't really have anything but a one or a zero coming in I should also on each

**1:54** · one of these lines these arrows say a zero or a one will take me to the next state a z or a one will take me to the next state a zero or a one to the next a zero or a one to the next state and so we just go ch ch ch to this next state next state After we receive each bit let me change this just a little bit What If instead I want to see if this binary

**2:18** · number this nibble is an odd number or an even number what makes it an odd number or an even number well remember that the least significant bit of a binary number gives the the two to the zero or the one power or not a one power in other words if I've got a zero as the last digit that comes in that will say that it's an even number if I've got a one that's the last digit that comes in that'll be an odd number so I've got actually two final States here I'm going to label one of them Q4 the other one

**2:52** · Q5 this top one that'll be our even State this is this will be the final place we get to if we received an even number and the bottom one that's going to be the state the condition if we received an odd number so I receive a bit a bit a bit and then from Q3 if I receive a zero I go to even from Q3 if I

**3:15** · receive a one I go to odd and you can actually tell by which one of these places we stopped at which one which number we received did we receive an odd number or an even number well this diagram here is something that represents a finite State machine otherwise known as an FSM all right and an FSM or a finite

### Components of a finite state machine

**3:44** · State machine consists of five things the first thing is a set of States all right and these are represented with in graph Theory with these vertices and that set of States we'll call capital Q all right and so in the case of this one we've got q q1 and

**4:06** · so on all right now the second thing that we have is a set of directed edges all right and that's these edges right here we'll just call this e and I'll just identify it with a state e subz E1 and so on now I didn't actually identify names or give each one of those uh edges and identifier but you get the idea each one of these edges is contained in some sort of a set then we also have an

**4:39** · alphabet to identify or label the Transitions and here's a new word I used transitions so this set of directed edges these are actually referred to as

**4:58** · transitions they allow us to transition from one state to the next state from one condition to the next condition now the next thing is we have a single state and I'm going to call this q0 that is our

**5:22** · initial State and so q0 is an element inside of of the set Q now just one we can only start in one place this is our initial and in the case of this diagram right here it's q0 now it is possible however

**5:41** · to have multiple final States so a set of final States we'll call this F which is a subset of Q and notice that it doesn't have to be a proper subset all the states could end up being f fin States in some of the diagrams in this case we just have Q4 and Q5 those are our final

### Review of basic RegEx forms

**6:08** · States now I mentioned this idea of our regular expressions or the reg X remember now to give you kind of a refresher course on regular Expressions regular Expressions were built up from a set of characters in an alphabet and so

**6:26** · let's see one of one of them remember was the empty string so the empty string and we refer to it as Lambda some people refer to it as lamb as Epsilon but we're going to use Lambda as our symbol for the empty string so an empty string that's a regular expression in itself and then we could also have a simple character from our alphabet and so for

**6:52** · my example here my alphabet is going to be equal to the set of letters lowercase letters all the way up from A to Z right all right now we also had

**7:08** · concatenation and that was whenever we could put two letters together no space they had to come in that sequence um and then we had Union right and the union was we used the little symbol for the or so we had a or b so that meant in order to satisfy that regular expression it

**7:29** · could just be a or it could just be B but it couldn't be both and it couldn't be any other letter then we also used star if you remember star just allowed us to put this little star this little asterisk up next to whatever regular expression we were trying to represent and then we also had the cross and the cross looked like that now these two were very closely related for example a star if you remember was we could have no A's we

**7:58** · could have the empty string we could have one a or a A or a a a or a a a a and any number of A's repeated from zero up to you know however many you wanted the Plus or the cross that one said we can't have the empty string it's exactly the same as star but we don't include the empty string so this one is a or a A

**8:22** · or a AA or A AAA and so on now what we want to do now is show how finite state maches those graphs with the directed edges how they can be used to represent any regular expression that we may have remember the regular Expressions build upon these so for example A or B could actually be concatenated with something else so you're actually using all of these components in order to build your regular your regular expression the

### Finite state machines for basic RegEx forms

**8:51** · question is is let's just start with these guys in order to figure out what sort of a finite State machine we can represent with this now empty string empty string is nothing right and so as soon as you get into your initial State bam you're in your final State because you don't get any characters at all that need to move you along the transitions so our final state is also our initial

**9:16** · state so believe it or not that is the finite State machine the diaph that represents the um Regular expression for the empty string initialize it to the final State there you are all right right but now for a character let's start out with some sort of an initial State now in that initial State we haven't received anything yet we're waiting to receive something just like the string of ones and zeros we were talking about in the previous example well what's the thing that that's going to take us to our final State well is a

**9:48** · transition with the character a and so this is our initial State this is our final state to get that transition is just a single character of a now if that made sense then the concatenation should probably also make sense because what we're looking at here is we need to have a followed by B and so we're going to have an initial State we're going to get taken to the next state with an A and then we're going to takeen get taken to a final state with a

**10:22** · b and so in order to get from the initial state to the final State you have to get an A and then a b that's the only way to get from one end to the other what about the union that one's a little different because an a could get us to the final state or a B could get us to the final state so we're going to start off with an initial state if I get

**10:46** · an A that's going to take me to one final State that's one way but I could also get a B that takes me to another final State and that's kind of like the previous example where it was odd or it was even an odd took us one way an even took us the other way both of these guys are fig are refer or they terminal States their final States so a receiving

**11:11** · an A or a B will show the completion of that particular regular expression now these two get a little bit more complicated let's start out with the star I remember an empty string that's fine so believe it or not it starts out looking a lot like the empty string so we've got this empty string the initial State and the final state are the same thing so it turns out that if I get no A's at all nothing I'm still

**11:41** · in the final state but what if I receive an a a single a well a single a I should still be in a final State what if I receive two A's I should still be in a final State Three A's and so on so what we're going to do is we are going to make a loop if you remember from our discussion about directed graphs a loop

**12:01** · is an edge that just simply exits a state or exits a vertex and comes back into that same vertex and so this particular diagram that's enough to show us that as many A's as we get from zero all the way up to you know a thousand that is going to keep us in the final State what about a cross well a cross

**12:23** · remember was different than the star in that we had to receive at least one a first and so that's kind of almost a combination of receiving this Single Character this single element and the star It's a combination of those two so what we're going to do is we're going to start out with an initial State this initial state is not going to be a final state that initial state says I have to get at least one a before I can get to a

**12:54** · final State now once I've gotten to the final State then I can get as many A's as I want and so something like AC cross that actually would be a finite State machine that would represent a

**13:10** · cross now remember regular Expressions can be made up of regular expressions and so any of those different Expressions that I showed you on the board just a moment ago they can be combined to make new more complex regular Expressions so we might have something like the concatenation of A and B but then do a star now remember the star

### Finite state machines for more complex RegEx forms

**13:33** · said we can start out with an empty string no no characters at all so it turns out that our initial State can also be our final State all right so we're just going to go ahead we'll label this guy q0 now what do we do in order to figure out if we've received one of the sequences or two of the sequences remember that this guy defines the set we've got the empty string and then AB and then ABAB and then ab ab a and so on

**14:05** · so that set consists of a lot of elements but what is the key thing of to see here is that we've got a followed by B always so if an a occurs we have to get a B well what we want to do is come back to the final State we could generate another final State you know we could have a going to a new Final going

**14:26** · to an intermediate State and then B going to another final state but then that would only take care of this guy and then in order to get this one you'd have to go AB to another final State and then to get this guy you'd have to go to AB again there's an easier way what we're going to do is we're going to have some sort of an intermediate state that we get to by going through the transition a and by going through the transition a what we're going to have is a non-final state that is waiting for a b if we receive a b we go back to the

**14:58** · final state and so does this does this finite State machine does this diaph that represents a finite State machine handle all of these cases well it handles the empty string by starting out in the final State then if we get AB we come back to the final State and then AB a back to the final State and so forth so it looks like this one does handle our uh our

**15:23** · requirements from this regular expression but what if we've got a regular expression Like A or B star now remember A or B star actually said well I could have a or I could have B we're going to start out because this is a star we're going to start out with our initial State as also being a final state so that we can just empty string we're right there but what happens what

**15:50** · does this set look like well the set that's generated by this guy is the empty string and it's a could be B it could be a a it could be BB it could be a any number of things right so basically any sequence that including the empty string that we can generate with the letters A and B and since it's any sequence then if I get an A I can

**16:16** · come back in here and if I get a B I can come back in here notice this notation I've taken this directed Edge and I've put both A and B separated by commas in order to identify that particular particular um that particular transition back into the final State now in previous lessons we've talked about something called the ethernet Preamble and start a frame

### Finite state machines for Ethernet preamble and SFD

**16:41** · delimiter um basically in order to when you're receiving a message on a on an Ethernet Network every one of the frames starts out with one zero one 0o one0 and a whole bunch of one zeros ending with a one one now this one one that those two one in a row identify the fact that the message itself specifically the addressing is going to start right after that point so what we're looking for is to identify that as a final State all

**17:11** · right now really what this looks like is just one Z Plus because we need to hit get EX at least one of them um because what you're looking to do is you're looking to use those one zeros to synchronize everybody so that they know exactly the the rate at which the bits are coming at them and so we need to get at least one one zero recognize that one zero at least once followed by a 1 one

**17:39** · so what does that look like with a regular expression well let's start out with the one zero so we have an initial State we're going to call this q0 and what's going to happen is we need to get a one followed by a zero all right and

**17:59** · that one Z or one Zer that's going to give us show us that we've received at least one of those guys let's assume that we're just looking at this case where it's the last one one1 so we've got 1 0 and then I'm going to come down here we'll get a one going to Q3

**18:20** · followed by another one going to Q4 now the one11 that's the minimum number of one zeros we can have one one one would take us actually to a final State being Q4 but what if we're actually receiving more one zeros what if it goes one Z one0 well in that case uh we're not quite where we should be right well it turns out that if I go from

**18:54** · 1 1 1 If instead of re receiving this second one I receive a zero what we can do is actually come back here with a zero drawing sort of filled up my space a little too much here and what we're looking at here is we can get 1 0 1 0 1 0 1 0 one one okay and and it's this one

**19:22** · zero it's this Loop right here which allows us to get a sequence of more than just one 1 Z now we have shown how we can use diagraphs in order to represent these finite State machines but it turns out there is another way to do it and that is some with something called a state

### Representing FSMs with a state transition table

**19:44** · transition table this table serves as a summary to show us which condition or state we go to based on the state we're currently in and the value of the input to our system let me go ahead and do an example up here it may be a lot easier to show with an example um I'm going to have my current states listed and let's just say I have how about q0 q1 Q2 so there are

**20:13** · all my States and now what I want to do is have over here columns representing what the the destination State what we're transitioning to based on the the the input to our system so let's say that our Al alphabet consists of a b and c we can have a b or c as the input and

**20:36** · so for each one of these rows we're going to identify exactly where we're going to based on our different values of a b and c so let's go ahead and ah let's just fill something out how about Q2 q1 q1 q1 Q2 q1 q0 0 q0 Q2 just making some

**21:02** · stuff up all right and let's see if we can't come up with the state diagram that represents this and by the way there's something missing from this table in this table I also have to tell you what the initial state is we'll just call the initial State we'll just make it q0 and we'll talk about the final

**21:23** · States remember you can have more than one final State we're just going to have one in this case well call it Q2 so let's go ahead and draw this out we'll have q0 and how about q1 and Q2 and remember Q2 is our final

**21:43** · state q0 is our initial State now all we need to do is do is add the Transitions and this table shows us what our transitions are so in q0 if we get an A we're going to Q2 so a a brings us from q0 to Q2 if we're in q0 a b brings us to

**22:08** · q1 if we're in q0 a c also brings us to q1 so this will show us all the transitions from q0 that are going to occur based on our alphabet of a b and c now what if we're in q1 well if we're in q1 and we get an A we come back to q1 if we're in q1 and we get a B we go to Q2 if we're in q1 and we get a c we also

**22:41** · go to q1 and that takes care of all of our transitions for a b and c out of q1 how about Q2 where do we go out of this final State well if we get an A we go back an a brings us back to Q Z so it looks like if we started in our initial State and just go a a a a a back and forth that'll be what happens if we're in Q2 and we get a B we also go to q0 so we've got a B there if we're in Q2

**23:16** · and we get a c we stay in Q2 and so there is our state die our directed graph B based on the finite State machine that is defined by that state transition table now please understand finite State machines are used for so much more than just regular Expressions turns out regular Expressions were just a really easy way for me to demonstrate how finite State machines work and the diagrams work but for example this this state transition table and the resulting uh State diagram

**23:49** · probably not a regular expression right the idea is that a finite State machine and these directed graphs that represent them are great great ways to model our Computing systems because our Computing systems naturally go from state to state to state from condition to condition to condition and these diagrams will really help us see the overall picture of how they're working