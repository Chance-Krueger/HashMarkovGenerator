# HashMarkovGenerator
## Description
Python program that generates random text resembling a given source file using a Markov chain algorithm. It uses a custom hash table ADT to efficiently map prefixes to suffixes, reads input text, builds the Markov chain, and generates probabilistic text with input error checking.

## What I learned:
    - How to implement a hash table with collision handling using linear probing in Python
    - How to build and use a Markov chain for text generation
    - Techniques for mapping prefixes to suffixes efficiently with a hash table
    - How to read and process input files to generate meaningful data structures
    - Managing randomness and probabilities to produce varied yet coherent text output
    - Error checking and validating user input parameters
    - Applying data structures and algorithms to a practical natural language processing task

## How to run the program:
    Make sure you have Python 3 installed on your system.
    Open a terminal or command prompt.

### Run the script by typing:
    python writer_bot_ht.py

### When prompted, enter the following inputs one by one:
    The filename of the source text file (e.g., source.txt)
    The size of the hash table (an integer, e.g., 5000)
    The prefix length n (an integer, e.g., 3)
    The number of words to generate (an integer, e.g., 100)

### Notes:
    The program will then generate and print the random Markov chain text based on your inputs.
    Make sure the source text file is in the same directory or provide the full path when prompted.

## Future Improvements
    - Support for punctuation handling
    - GUI interface
    - Better collision resolution
    - Performance profiling
    - File output option
    - Command-line arguments
    - Support for different seed values
