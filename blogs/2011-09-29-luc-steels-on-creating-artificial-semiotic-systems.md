---
title: "Luc Steels on creating artificial semiotic systems"
date: "2011-09-29"
categories: 
  - "justblogging"
tags: 
  - "ai"
  - "embodied"
  - "linguistics"
  - "nlp"
  - "representation"
  - "symbol"
---

In this post I'm just presenting an organized version of the notes I've taken after reading a beautiufl paper by Luc Steels, titled: "[The Symbol Grounding Problem has been solved. So What's Next?](https://homepage.univie.ac.at/nicole.rossmanith/concepts/papers/steels2008symbol.pdf)".

Who is Luc Steels? [Steels is a Belgian scientist](https://en.wikipedia.org/wiki/Luc_Steels) working in area of embodied cognition and robotics.

The post is organized as follows: 1. Preface: the symbol grouding problem and Peirce's inheritance 2. Semiotic systems 3. Re-conceiving the symbol grounding problem 4. Clarifying the notion of ‘symbol’ 5. Clarifying the notion of ‘representation’ 6. The debate around symbols and representations 7. Clarifying the notion of ‘embodiment’ 8. Creating robots capable of performing semiotic processes 9. Is the symbol grounding problem solved? Yes!

 

### 1\. Preface: the symbol grouding problem and Peirce's inheritance:

 

- THE QUESTION OF SYMBOL GROUNDING; SEARLE’S CHINESE ROOM THEORY (SEARLE 1980)

> Searle's article had the advantage of stirring up discussion about when and how symbols could be about things in the world, whether intelligence involves representations or not, what embodiment means, and under what conditions cognition is embodied.

 

- THE SEMIOTIC TRIANGLE: SYMBOL - OBJECT - CONCEPT

> Let us start from Peirce and the (much longer) semiotic tradition which makes a distinction between a symbol, the objects in the world with which the symbol is associated (for example, for purposes of reference), and the concept associated with the symbol. For example, we could have the symbol ‘ball’, a concrete round spherical object in the world with which a child is playing, and the concept ball which applies to this spherical object so that we can refer to the object using the symbol ‘ball’.

 

- GROUNDED SYMBOLS; NOTION OF METHOD

> In some cases, there is a method that constrains the use of a symbol for the objects with which it is associated. The method could, for example, be a classifier - a perceptual/pattern recognition process that operates over sensorimotor data to decide whether the object 'fits' with the concept. If such an effective method is available, then we call the symbol grounded. \[...\] In this chapter I focus on groundable symbols. \[...\] The method is a procedure to decide whether the concept applies or not.

 

- DEBATE AROUND GROUNDED SYMBOLS

> There is apparently a debate in cognitive psychology between those emphasizing the grounded use of symbols (e.g. Barsalou 1999) and those emphasizing extraction and navigation across nongrounded semantic networks, and the current book reflects some of this debate. However, I think the opposition is a bit of a red herring. Both aspects of semantic processing are clearly extremely important and they interact with each other in normal human cognition. In this chapter I focus on grounded symbols not because I think other kinds of semantic processing are not relevant or important, but because in the Chinese room debate it is accepted that semantic processing can be done by computational systems whereas symbol grounding cannot.

 

### 2\. Semiotic systems

 

- TAGGING SYSTEMS REFLECT REAL SEMIOTIC RELATIONSHIPS

> Tagging sites compute and display the various semantic relations between tags and objects: they display the co-occurrence relations between tags so that users can navigate between the most widely used tags, as well as the contexts in which objects occur, for example, all pictures taken by the same user. The enormous success of these sites shows that this kind of system resonates strongly with large numbers of people, and I believe this is the case because it reflects and externalizes the same sort of semiotic relationships and navigation strategies that our brains are using in episodic memory or language.

 

- NOTION OF A SEMIOTIC NETWORK

> I will call the huge set of links between objects, symbols, concepts, and their methods, a semiotic network .

 

- HUMAN INTERACTION = NAVIGATING, NEGOTIATING AND ADAPTING SEMANTIC NETWORKS

> This semiotic network gets dynamically expanded and reshuffled every time you experience, think, or interact with the world or with others. Individuals navigate through this network for purposes of communication: when a speaker wants to draw the attention of an addressee to an object, he can use a concept whose method applies to the object, then choose the symbol associated with this concept and render it in speech or some other medium. The listener gets the symbol, uses his own vocabulary to retrieve the concept, and hence the method, and applies the method to decide which object might be intended. \[...\] The semiotic networks that each individual builds up and maintains are therefore coupled to those of others and they get progressively coordinated in a group, based on feedback about their usage. \[...\] Psychological evidence for this progressive and continuous adaptation of semiotic networks is now beginning to come from many sources. First of all there are the studies of natural dialogue (Pickering and Garrod 2004; Clark and Brennan 1991) which show convincingly that speakers and hearers adopt and align their communication systems at all levels within the course of a single conversation. Their sound systems and gestures become similar , they adopt and negotiate new word meanings, they settle on certain grammatical constructions, and align their conceptualizations of the world

 

- NOTION OF SEMIOTIC LANDSCAPE

> I call the set of all semiotic networks of a population of interacting individuals a semiotic landscape. Such a landscape is undergoing continuous change as every interaction may introduce, expand, or enforce certain relationships in the networks of individuals. Nevertheless there are general tendencies in the semiotic networks of a population, otherwise communication would not be possible

 

### 3\. Re-conceiving the symbol grounding problem

 

- SEARLE VERSION OF THE SYMBOL GROUNDING PROBLEM

> the question originally posed by Searle (1980): can a robot deal with grounded symbols? More precisely , is it possible to build an artificial system that has a body, sensors and actuators, signal and image processing, pattern recognition processes, and information structures to store and use semiotic networks, and uses all that for communicating about the world or representing information about the world. My first reaction is to say yes. As far back as the early 1970s, AI experiments like Shakey the robot achieved this (Nilsson 1984).

 

- PREPROGRAMMED SEMIOTIC RELATIONS vs EMERGENT SEMIOTIC RELATIONS

> It has always been popular to bash AI because that puts one in the glorious position of defending humanity. But one part of the criticism was justified: all was programmed by human designers. The semiotic relations were not autonomously established by the artificial agent but carefully mapped out and then coded by human programmers. The semantics therefore came from us, humans. \[...\] Nils Nilsson and the other designers of Shakey carved up the world, they thought deeply how the semantics of 'pyramid' and 'big' could be operationalized, and they programmed the mechanisms associating words and sentences with their meanings. So the Chinese room argument, if it is to make sense at all, needs to be taken differently , namely that computational system cannot generate their own semantics whereas natural systems (e.g., human brains) can. Indeed the mind/brain is capable to develop autonomously an enormous repertoire of concepts to deal with the environment and to associate them with symbols that are invented, adopted, and negotiated with others.

 

- A CLEARER VERSION OF THE SYMBOL GROUNDING PROBLEM: FROM GROUNDED SYMBOLS TO SEMIOTIC NETWORKS

> So the key question for symbol grounding is not whether a robot can be programmed to engage in some interaction which involves the use of symbols grounded in reality through his sensorimotor embodiment: that question has been solved. It is actually another question, well formulated by Harnad (1990): if someone claims that a robot can deal with grounded symbols, we expect that this robot autonomously establishes the semiotic networks that it is going to use to relate symbols with the world.

 

- GROUNDING SYMBOLS IN AI RESEARCH: FROM PROGRAMMED GROUNDING TO AUTONOMOUS, SUPERVISED LEARNING

> AI researchers had independently already come to the conclusion that autonomous grounding was necessary . \[...\] Continuing to program these methods by hand was therefore out of the question and that route was more or less abandoned. Instead, all effort was put into the machine learning of concepts, partly building further on the rapidly expanding field of pattern recognition, and partly by using 'neural network'-like structures such as perceptrons. The main approach is based on supervised learning:

 

- HUMANS STILL SET UP THE WORLD FOR THE MACHINE

> So does this mean that the symbol grounding problem is solved? I do not believe so. Even though these artificial systems now autonomously acquire their own methods for grounding concepts (and hence also symbols), it is still the human who sets up the world for the robot, carefully selects the examples and counterexamples

 

### 4\. Clarifying the notion of 'symbol'

 

- NOTION OF SYMBOL 1: SYMBOLIC PROGRAMMING; C-SYMBOLS

> The notion of a symbol in so-called symbolic programming languages like LISP or Prolog is quite precise: it is a pointer (i.e., an address in computer memory) to a list structure containing a string known as the 'print name', which is used to read and write the symbol, \[...\] Almost all sophisticated AI technology , as well as a lot of web technology , rests on the elegant but enormously powerful concept of symbolic programming.

 

- NOTION OF SYMBOL 2: MEANING-ORIENTED SYMBOLS

> Clearly this notion of symbol is not related to anything I discussed in the previous paragraphs, so I propose to make a distinction between c-symbols (the symbols of computer science) and m-symbols (meaning-oriented symbols in the tradition of the arts, humanities, and social and cognitive sciences).

 

- THE SYMBOL GROUNDING DEBATE IS RELATED TO M-SYMBOLS, NOT C-SYMBOLS

> all this has given rise to what is probably the greatest terminological confusion in the history of science. The debate about the role of symbols in cognition or intelligence must be totally decoupled to whether one uses a symbolic programming language or not. The rejection of traditional AI by some cognitive scientists or philosophers seems mostly based on this misunderstanding.

 

### 5\. Clarifying the notion of 'representation'

 

- ANOTHER SOURCE OF LINGUISTIC CONFUSION: THE NOTION OF REPRESENTATION

> The debate on symbol grounding is tied up with another discussion concerning the nature and importance of representations for cognition, and the relation between representations and meanings. The notion of representation also has a venerable history in philosophy , art history , etc., before it was hijacked by computer scientists to become much more narrow in scope. Since then, however, the computational notion of representation has returned to cognitive science through the back door of AI

 

- A REPRESENTATION IS BY CONVENTION OR SELF-WILL; M-SYMBOLS ARE A PARTICULAR TYPE OF REPRESENTATIONS; REPRESENTATIONS ARE DIVIDED BY PEIRCE IN THREE KINDS

> In traditional usage, a representation is a stand-in for something else, so that it can be made present again (i.e. re-present-ed). Anything can be a representation of anything. For example, a pen can be a representation of a boat, a person, or an upward movement; a broomstrick can be a representation of a hobby horse. The magic of representations happens because one person decides to establish that x is a representation for y , and others either agree with this or accept that this representational relation holds. There is nothing in the nature of an object that makes it a representation or not; it is rather the role the object plays in subsequent interaction. Of course, it helps a lot if the representation has some properties that help others to guess what it might be a representation of. But a representation is seldom a picture-like copy of what is represented. \[...\] It is clear that m-symbols are a particular type of representations, one where the physical object being used has a rather arbitrary relation to what is represented. It follows that all the remarks made earlier about m-symbols are also valid for representations. However, the notion of representation is broader. Following Peirce, we can make a distinction between an icon, an index, and a symbol. An icon looks like the thing it signifies, so meaning arises by perceptual processes and assocations, the same way we perceive the objects themselves. An example of an icon is a statue of a saint which looks like the saint, or how people imagine the saint to be. An index does not look like the thing it signifies, but there is nevertheless some causal or associative relation. For example, smoke is an index of fire. A symbol on the other hand has no direct or indirect relation to the thing it signifies. The meaning of a symbol is established purely by convention, and hence you have to know the convention in order to figure out what the symbol is about.

 

- HUMAN REPRESENTATIONS REPRESENT MEANINGS; MEANINGS ARE DIFFERENT FROM REPRESENTATIONS; CONCEIVING A REPRESENTATION

> Human representations have some additional features. First of all they seldom represent physical things, but rather meanings. A meaning is a feature that is relevant in the interaction between the person and the thing being represented \[...\] There is a tendency to confuse meanings and representations. A representation 're-presents' meaning but should not be equated with meaning, just like an ambassador may represent a country but is not equal to that country . Something is meaningful if it is important in one way or another: for survival, maintaining a job, social relations, navigating in the world, etc.. \[...\] Conceiving a representation requires selecting a number of relevant meanings and deciding how these meanings can be invoked in ourselves or others. The invocation process is always indirect and most often requires inference. Without knowing the context, personal history , prior use of representations, etc., it is often very difficult, if not impossible, to decipher representations. Second, human representations typically involve perspective. Things are seen and represented from particular points of view and these perspectives are intermixed.

 

- REFORMULATION OF THE SYMBOL-GROUNDING PROBLEM IN TERMS OF SYMBOLIC REPRESENTATIONS CREATION SKILLS

> Human representations are clearly incredibly rich and serve multiple purposes. They help us to engage with the world and share world views and feelings with others. Symbols or symbolic representations traditionally have this rich connotation. And I believe the symbol grounding problem can only be said to be solved if we understand, at least in principle, how individuals originate and choose the meanings that they find worthwhile to use as basis for their (symbolic) representations, how perspective may arise, and how the expression of different meanings can be combined to create compositional representations.

 

- NOTION OF REPRESENTATION IN COMPUTER SCIENCE: C-REPRESENTATIONS VS M-REPRESENTATIONS

> In the 1950s, when higher-level computer programming started to develop, computer scientists began to adopt the term 'representation' for data structures that held information for an ongoing computational process. For example, in order to calculate the amount of water left in a tank with a hole in it, you have to represent the initial amount of water, the flow rate, the amount of water after a certain time, etc., so that calculations can be done over these representations. Information processing came to be understood as designing representations and orchestrating the processes for the creation and manipulation of these representations. \[...\] computer scientists (and ipso facto AI researchers) are clearly adopting only one aspect of representations: the creation of a 'stand-in' for something into the physical world of the computer so that it could be transformed, stored, transmitted, etc. They are not trying to operationalize the much more complex process of meaning selection, representational choice, composition, perspective taking, inferential interpretation, etc., all of which are an important part of human representation making. I will use the term c-representations to mean representations as used in computer science and m-representations for the original, meaning-oriented use of representations in social science and humanities. \[...\] Mirror neuron networks are a clear example of c-representations. \[...\] the question today is no longer whether or not c-representations are necessary but rather what their nature might be.

 

### 6\. The debate around symbols and representations

 

- SYMBOLIC VS NON-SYMBOLIC C-REPRESENTATIONS

> a debate arose between advocates of symbolic c-representations and nonsymbolic c-representations. Simplified, symbolic c-representations are representations for categories, classes, individual objects, events, or anything else that is relevant for reasoning, planning, language, or memory . Nonsymbolic c-representations, on the other hand, use continuous values and are therefore much closer to the sensory and motor streams. They have also been called analogue c-representations because their values change by analogy with a state of the world, like a temperature measure which goes up and down when it is hotter or colder . Thus, we could have on the one hand a sensory channel for the wavelength of light with numerical values (a nonsymbolic c-representation), and on the other hand (symbolic) c-representations for colour categories like red, green, etc. Similarly , we could have an infrared or sonar channel that numerically reflects the distance of the robot to obstacles (a nonsymbolic c-representation), or we could have a c-symbol representing 'obstacle seen' (a symbolic c-representation)

 

- NEURAL NETWORK MOVEMENT; INTELLIGENCE WITHOUT REPRESENTATION

> When the neural network movement became more prominent again in the 1980s, they de-emphasized symbolic c-representations in favour of the propagation of (continuous) activation values in neural networks (although some researchers used these networks later in an entirely symbolic way , as pointed out in the discussion of Rogers et al . in Chapter 2). When Brooks wrote a paper on 'Intelligence without representation' (Brooks 1991), he argued that real-time robotic behaviour could often be better achieved without symbolic c-representations. For example, instead of having a rule that says 'if obstacle then move back and turn away from obstacle', we could have a dynamical system that directly couples the change in sensory values to a change on the actuators. The more infrared reflection from obstacles is picked up by the right infrared sensor on a robot, the slower its left motor is made to move, and hence the robot starts to veer away from the obstacle.

 

- A FALSE DEBATE?

> The debate between symbolic or nonsymbolic representations seems to be based on an unnecessary opposition, just as the debate between grounded and non-grounded symbols. The truth is that we need both.

 

- ANY TYPE OF REPRESENTATION CANNOT GUARANTEE PER SE THE EMERGENCE OF MEANING

> At the same time, the simple fact of using a c-representation (symbolic or otherwise) does not yet mean that an artificial system is able to come up or interpret the meanings that are represented by the representation. Meaning and representation are different things. In order to see the emergence of meaning, we need a minimum of a task, an environment, and an interaction between the agent and the environment that works towards an achievement of the task.

 

### 7\. Clarifying the notion of 'embodiment'

 

- EMBODIMENT AS IMPLEMENTATION

> In the technical literature (e.g., in patents), the term embodiment refers to implementation (i.e., the physical realization) of a method or idea. Computer scientists more commonly use the word implementation . An implementation of an algorithm is a definition of that algorithm in a form such that it can be physically instantiated on a computer and actually run (i.e., that the various steps of the algorithm find their analogue in physical operations). It is absolute dogma in computer science that an algorithm can be implemented in many different physical media, on many different types of computer architectures, and in different programming languages,

 

- SYSTEMS PERSPECTIVE VS MATERIAL PERSPECTIVE IN EXPLANATIONS

> Computer scientists naturally take a systems perspective when they try to understand a phenomenon. In contrast, most physical natural scientists seek material explanations, they seek an explanation in the materials and material properties involved in a phenomenon. For example, their explanation of why oil floats on top of water is in terms of the attraction properties of molecules, the density of oil and water , and the upward buoyancy forces. System explanations, on the other hand, are in terms of elements and processes between the elements.

 

- SYSTEMS PERSPECTIVE VS MATERIAL PERSPECTIVE IN PHILOSOPHY OF MIND

> It is therefore natural that computer scientists apply system thinking to cognition and the brain. Their goal is to identify the algorithms (in other words the systems) underlying cognitive activities like symbol grounding and study them through various kinds of implementations which may not at all be brain-like. They might also talk about neural implementation or neural embodiment, meaning the physical instantiation of a particular algorithm with the hardware components and processes available to the brain. \[...\] There has been considerable resistance both from biologists and philosophers alike for accepting the systems perspective, i.e., the idea that the same process (or algorithm) can be instantiated (embodied) in many different media. They seem to believe that the (bio-)physics of the brain must have unique characteristics with unique causal powers.

 

- THE MATERIAL PERSPECTIVE IN SEARLE

> his turns out to be also the fundamental criticism of Searle. The reason why he argues that artificial systems, even if they are housed in robotic bodies, cannot deal with symbols is because they will for ever lack intentionality . \[...\] According to Searle, an adequate explanation for intentionality can only be a material one: 'Whatever else intentionality is, it is a biological phenomenon, and it is as likely to be as causally dependent on the specific biochemistry of its origins as lactation, photosynthesis, or any other biological phenomena.' \[...\] Searle invokes biology , but most biologists today accept that the critical features of living systems point to the need to adopt a system perspective instead of a material one; even photosynthesis can be done through many different materials. For example, leading evolutionary biologist John Maynard Smith (2000) has been arguing clearly that the genetic system is best understood in information processing terms and not (just) in molecular terms.

 

- EMBODIMENT AS HAVING A BODY

> There is another notion of embodiment that is also relevant in this discussion. This refers quite literally to 'having a body' for interacting with the world, i.e. having a physical structure, dotted with sensors and actuators, and the necessary signal processing and pattern recognition to bridge the gap from reality to symbol use. Embodiment in this sense is a clear precondition to symbol grounding. As soon as we step outside the realm of computer simulations and embed computers in physical robotic systems, we achieve some form of embodiment (even if the embodiment is not the same as human embodiment) \[...\] it only means that embodied AI is necessarily of a different nature due to the differences in embodiment, not that embodying AI is impossible.

 

### 8\. Creating robots capable of performing semiotic processes

 

- EXPERIMENTS IN LANGUAGE EMERGENCE

> experiments in language emergence (Steels 2003). They take place in the context of a broader field of study concerned with modelling language evolution \[...\] We have been using progressively more complex embodiments, \[...\] The robots have been programmed using a behaviour-based approach (Brooks 1991) so that obstacle avoidance, locomotion, tracking, grasping, etc., are all available as solid smooth behaviours to build upon. \[...\] By using these robots, we achieve the first prerequisite for embodied cognition and symbol grounding, namely that there is a rich embodiment. Often we use the same robot bodies for different agents by uploading and downloading the complete state of an agent after and before a game. This way we can do experiments with larger population sizes.

 

- SETTING UP AN ENVIRONMENT FOR AGENTS TO INTRODUCE NEW RELEVANT DISTINCTIONS

> If we want to solve the symbol grounding problem, we next need a mechanism by which an (artificial) agent can autonomously generate its own meanings. This means that there must be distinctions that are relevant to the agent in its agent-environment interaction. The agent must therefore have a way to introduce new distinctions based on the needs of the task. As also argued by Cangelosi et al . (2000), this implies that there must be a task setting in which some distinctions become relevant and others do not.

 

- LANGUAGE GAMES: COOPERATIVE GOALS + SYMBOLIC INTERACTIONS

> One could imagine a variety of activities that generate meaning, but we have focused on language games. A language game is a routinized situated interaction between two embodied agents who have a cooperative goal (e.g., one agent wants to draw the atten- tion of another agent to an object in the environment, or one agent wants the other one to perform a particular action) and who use some form of symbolic interaction to achieve that goal (e.g., by exchanging language-like symbols or sentences, augmented with nonverbal interactions such as pointing or bodily movement towards objects).

 

- NOTION OF SCRIPT

> In order to play a language game the agents need a script with which they can establish a joint attention frame, in the sense that the context becomes restricted and it is possible to guess meaning and interpret feedback about the outcome of a game.

 

- PROCESS OF MEANINGS GENERATION AND GROUNDING

> Next we need a mechanism by which agents can internally represent and ground their relevant meanings. In the experiment, agents start with no prior inventory of categories and no inventory of methods (classifiers) that apply categories to the features (sensory experience) they extracted from the visual sensation they received through their cameras. In the experiments, the classifiers use a prototype-based approach implemented with radial basis function networks \[...\] The next requirement is that agents autonomously can establish and negotiate symbols to express the meanings that they need to express. In the experiment, agents generate new symbols by combining randomly a number of syllables into a word, like 'wabado' or 'bolima' . The meaning of a word is a perceptually grounded category . No prior lexicon is given to the agents, and there is no central control that will determine by remote control how each agent has to use a word.

 

- PROCESS OF COORDINATION

> If every agent generates his own meanings, perceptually grounded categories, and symbols, then no communication is possible, so we need a process of coordination that creates the right kind of semiotic dynamics so that the semiotic networks of the individual agents become sufficiently coordinated to form a relatively organized semiotic landscape. \[...\] This is achieved in two ways. Firstly , speakers and hearers continue to adjust the score of form-meaning associations in their lexicon based on the outcome of a game: When the game is a success they increase the score and dampen the score of competing associations; when the game is a failure the score is diminished. The net effect of this update mechanism is that a positive feedback arises: \[...\] Speakers and hearers also maintain scores about the success of perceptually grounded categories in the language game, and adjust these scores based on the outcome. As a consequence, the perceptually grounded categories also get coordinated in the sense that they become more similar , even though they will never be absolutely identical.

 

### 9\. Is the symbol grounding problem solved? Yes!

 

- CONCLUSION: THE SYMBOL GROUNDING PROBLEM IS SOLVED

> I argue that these experiments show that we have an effective solution to the symbol grounding problem, if there is ever going to be one: we have identified the right mechanisms and interaction patterns so that the agents autonomously generate meaning, autonomously ground meaning in the world through a sensorimotor embodiment and perceptually grounded categorization methods, and autonomously introduce and negotiate symbols for invoking these meanings. \[...\] The explanatory power of these experiments does not come from the identification of some biochemical substance for intentionality of the sort Searle is looking for, but it is a system explanation in terms of semiotic networks and semiotic dynamics operating over these networks. Each agent builds up a semiotic network relating sensations and sensory experiences to perceptually grounded categories and symbols for these categories \[...\] All the links in these networks have a continuously valued strength or score that is continually adjusted as part of the interactions of the agent with the environment and with other agents \[...\] Although each agent does this locally , an overall coordinated semiotic landscape arises \[...\] I now boldly state that the symbol grounding problem is solved, by that I mean we now understand enough to create experiments in which groups of agents self-organize symbolic system that are grounded in their interactions with the world and others.

 

- FUTURE WORK: GENERATING SEMIOSIS FOR TENSE, MOOD, MODALITY ETC

> we can do many more experiments with artificial robotic agents to progressively understand many more aspects of meaning, conceptualization, symbolization, and the dynamical interactions between them. These experiments might focus, for example, on issues of time and its conceptualization in terms of tense, mood, modality , and the roles of objects in events, as well as its expression in case grammars, the categorization of physical actions and their expression, raising issues in the mirror neuron debate, etc. I see this as the job of AI researchers and (computational) linguists. \[...\] All too often psychological experiments have focused on the single individual in isolated circumstances, whereas enormously exciting new discoveries can be expected if we track the semiotic dynamics in populations, something that is becoming more feasi- ble thanks to internet technologies. Psychological experiments have often assumed as well that symbol use and categorization is static, whereas the interesting feature is precisely in its dynamics.