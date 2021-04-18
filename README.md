# poetryslam2

Gannon Leech
CSCI 3725 - Computational Creativity
Title: "To Bot or not to Bot"

Set up and Run: To set up and run the code you only have to execute the main.py
file. You will be asked to input a file of your choosing as an inspiring set. I 
have the sonnets.txt file in, which contains Shakespeare's 154 sonnets, so if you enter
sonnets.txt it will use that, or you may include one of your own. Then it will ask for
an n value which you can enter. The output will be played over your system, and the final
poem will be saved to the outputs folder

Description: This program uses n-grams and a genetic algorithm to generate
poetry inspired by the sonnets of shakespeare. The inspirational set is all 
154 of Shakespear's sonnets, which are read in. Then, the program goes through the 
sonnets, creating dictionaries based on what the user entered value for the n-gram
is, mapping sequences of words with the words that come directly after and the number 
of their occurences. Then, the program generates 20 poems using those probabilities as 
an initial population. After the generation is complete, the steps of a genetic algorithm
are followed in order to evolve the original poems that were generated. This was done in order
to make the poems more unique. The crossover process is fairly simple, each poem is represented
as two havles, so crossover just switches the halves between two poems to create two different
offspring. 

For mutation I gave a small probability to swap at each word in the poem with a different word  
using the ngram model. 

The biggest challenge for me was how to measure the fitness of a given poem. To think about this,
I read different scientific papers, and tried to understand what those authors did and how I could
utilize that. This led me to decide that two metrics I would look at for fitness would be the variability/uniqueness
of the poems as well as the realisticness of the poem. To measure variability, I simply looked at the 
number of unique words in a poem, in order to avoid ngram poems that just repeated the same phrase over
and over again. To look at realisticness, I added a fitness measure to reward a poem if the word sequence 
is a high probability sequence, as stored in the n-gram dictionary. This way, it rewards more common sequences over
less common sequences, which would hopefully add make the overall poem more thematically connected throughout.

This project challenged me a lot as a computer scientist. Originallay, I did not intend to use n-grams
to generate my poem, and was going to try to utilize tweepy and the twitter api to make it work. However,
as I was going through, I really struggled with parsing the twitter data and getting enough meaningful 
information from individual accounts to begin the creation process. This led me to consider using different
resources as my inspiring set. Then, when I settled on using the Shakesperean sonnets as inspiration, I 
still struggled with generation, eventually realizing that using n-grams would be a good starting point
for my poem generation. Once I was able to generate basic poems, my biggest challenge was in poem evaluation
and how to measure the fitness of each poem during the evolutionary process. As I read through the different 
papers, I realized good fitness measures would be variability and realisticness, which I was able to implement 
myself in the genetic algorithm.

The three papers I used are cited below, and they were really helpful in giving me ideas for how to evaluate
my poems, as well as for how a genetic algorithm might work for poetry composition. I was able to utilize some
of the starting points and ideas from these papers and implement them myself.

Alice H Oh, Alexander I Rudnicky, "Stochastic natural language generation for spoken dialog systems", Computer Speech & Language, Volume 16, Issues 3–4, 2002, Pages 387-407, ISSN 0885-2308.

Frankel, Richard, et al. “The Metric System: Transforming Prose to Verse.” 2010. 

Langkilde, Irene, and Kevin Knight. “The Practical Value of N-Grams In Generation.” 

The sonnets were retrieved from this website: http://www.shakespeares-sonnets.com/Archive/allsonn.htm