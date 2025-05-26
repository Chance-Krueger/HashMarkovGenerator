'''
    File: HashMarkovGenerator.py
    Author: Chance Krueger
    Purpose: To generates random text resembling a given source file using a 
    Markov chain algorithm. It employs a hash table ADT to map prefixes to 
    suffixes efficiently. The program reads the source file, constructs a 
    Markov chain table, and generates text by selecting words based on 
    probabilities from the input.Error checking is performed for input values.
'''



import sys

import random

SEED = 8

NONWORD = '@' 



class Hashtable:

    '''The Hashtable class provides a hash table data structure with methods 
    for inserting key-value pairs, retrieving values by keys, and checking key
    existence. It employs linear probing to handle collisions and uses 
    polynomial hashing for computing hash values.'''

    def __init__(self,size):

        '''This method is to initialize a Hashtable object with a specified 
        size, creating a list named _pairs filled with None values, and 
        storing the size information in the _size attribute.
        
        Args: size is an integer representing the size of the hash table to be
            initialized.
        
        Returns: Nothing.'''

        self._pairs = [None] * int(size)
        self._size = size

    def __str__(self):

        '''This method provides a string representation of the Hashtable 
        object by returning the string representation of its _pairs 
        attribute, allowing for easy visualization of the hash table's 
        contents.
        
        Args: None.
        
        Returns: A string representation of the Hashtable, in a 2D list.'''

        return str(self._pairs)
    
    def put(self, key, value):

        '''This method inserts a key-value pair into the Hashtable object by 
        calculating the index for the key using the _hash method. If the 
        calculated index is empty, it stores the key-value pair there; 
        otherwise, it handles collisions by searching backward in the 
        list until it finds an empty slot to insert the pair.
        
        Args: key: The identifier used to access the associated data within 
            the hash table. 
        value: The data associated with the given key, which is stored within 
            the hash table.
        
        Returns: Nothing.'''

        index = self._hash(key)

        if self._pairs[index] == None:
            self._pairs[index] = [key, value]

        else: 
            index -=1
            # Handle collisions by searching backward in the 
            # list until finding an empty slot.
            while self._pairs[index] != None:
                index = (index - 1) % len(self._pairs)

            self._pairs[index] = [key, value]
    
    def get(self,key):

        '''This method retrieves the value associated with a given key from 
        the hash table. It calculates the index for the key using the _hash 
        method, then searches for the key starting from that index. If the key
        is found, it returns the corresponding value; otherwise, it returns 
        None.
        
        Args: key: The identifier used to access the associated data within 
            the hash table. 
        
        Returns: The value associated with the given key if the key is found 
            in the hash table. If the key is not found, it returns None.'''

        index = self._hash(key)

        if self._pairs[index] == None:
            return None
        
        elif self._pairs[index][0] == key:
            return self._pairs[index][1]
        
        else:

            index = (index - 1) % len(self._pairs)
            hash_index = self._hash(key)

            while self._pairs[index] != None and index != hash_index:

                # Check if the current key matches the target key.
                if self._pairs[index][0] == key:
                    return self._pairs[index][1]
                
                index = (index - 1) % len(self._pairs)

            return None
    
    def __contains__(self,key):

        '''This method checks whether a given key exists in the hash table. It
        utilizes the get method to check if the key is present in the table. 
        If the key is found, it returns True; otherwise, it returns False.
        
        Args: key: The identifier used to access the associated data within 
            the hash table. 
        
        Returns: A boolean value: True if the key exists in the hash table, 
            and False otherwise.'''
        
        if self.get(key) == None:
            return False
        else:
            return True
    
    # Hashes the given key to an integer value for placement in the Hashtable.
    # source: University of Arizona, 
    # Department of Computer Science - CSc 120: Writer Bot Hash Table
    def _hash(self, key):

        '''This method is to compute a hash value for a given key using the 
        polynomial hashing method. This hash value is used to determine the 
        index where the key-value pair should be stored in the hash table, 
        aiding in efficient retrieval and storage operations.
        
        Args: key: The identifier used to access the associated data within 
            the hash table.
        
        Returns: An integer value representing the hash code computed for the 
        given key. This hash code is used to determine the index in the hash 
        table where the key-value pair should be stored.'''

        p = 0
        for c in key:
            p = 31*p + ord(c)
        return p % self._size
    


def open_file(sfile):

    '''This function reads the content of a text file specified by the sfile 
    parameter. It opens the file in read mode, reads the lines one by one, 
    splits each line into words, and appends the words to a list named 
    list_of_words. Finally, it closes the file and returns the list of words 
    extracted from the file.
    
    Args: sfile is A string representing the name or path of the text file to
        be opened and read.
    
    Returns: A list containing the words extracted from the text file 
        specified by the sfile parameter.'''

    in_file = open(sfile,'r')
    list_of_words = []

    for line in in_file:
        words = line.split()
        list_of_words += words

    in_file.close()

    return list_of_words



def generate_text(nonword_list, hashtable, num_words):

    '''This function is to create random text by iteratively selecting words 
    based on a Markov chain algorithm using a hashtable. It constructs the 
    text by randomly choosing words that follow the given prefix, ensuring 
    that the generated text resembles the style of the input text used to 
    build the hashtable.
    
    Args: nonword_list is a list representing the initial prefix used for 
        generating text.
    hashtable is the hashtable containing prefix-suffix mappings for 
        generating text.
    num_words is an integer specifying the desired number of words in the 
        generated text.
    
    Returns: a string containing the generated text of the Hashmap table based
        on the Markov chain algorithm.'''

    final_string = ''
    new_str = ''
    index = 0
    list_of_words = []

    # Generate text until the desired number of words is reached.
    while len(list_of_words) != num_words:
        key = ' '.join(nonword_list)
        value = hashtable.get(key)

        # If there are multiple suffixes, choose one randomly.
        if len(value) > 1:
            list_of_words.append(value[random.randint(0, len(value) - 1)])

        # If only one suffix, append it directly.
        elif len(value) == 1:
            list_of_words.append(value[0])

        # Update the nonword list for the next iteration.
        nonword_list.append(list_of_words[index])
        nonword_list = nonword_list[1:]
        index += 1

    # Format the generated text into lines of ten words each.
    while len(list_of_words) > 10:
        new_str = ' '.join(list_of_words[0:10])
        final_string += new_str + '\n'
        list_of_words = list_of_words[10:]
    
    final_string += ' '.join(list_of_words)

    return final_string



def make_hashtable(list_of_words, hashtable, nonword_list):

    '''This function is to populate or update a hashtable with prefix-suffix 
    mappings based on the provided list of words. It iterates through the list
    of words, constructs keys using the nonword_list as prefixes, and adds or 
    appends suffixes to the hashtable accordingly. This process prepares the 
    hashtable for generating text using a Markov chain algorithm.
    
    Args: list_of_words is a list containing words extracted from the input 
        text.
    hashtable is the hashtable containing prefix-suffix mappings for 
        generating text.
    nonword_list is a list representing the initial prefix used for generating 
        text.
    
    Returns: Nothing.'''

    for word in range(len(list_of_words)):

        # Construct a key from the nonword list.
        key = ' '.join(nonword_list)

        if key in hashtable:
            hashtable.get(key).append(list_of_words[word])

        else:
            hashtable.put(key, [list_of_words[word]])

        nonword_list.append(list_of_words[word])
        nonword_list = nonword_list[1:]



def main():

    '''This function orchestrates the generation of random text by reading 
    input parameters, initializing a hashtable, and utilizing helper functions 
    to construct the text. It ensures error-free execution by validating input 
    values and controls the flow of the program, ultimately producing and 
    printing the generated text.
    
    Args: None.
    
    Returns: Nothing.'''

    random.seed(SEED)
    
    sfile = input()
    M = int(input())
    n = int(input())
    num_of_words = int(input())

    if num_of_words < 1:
        print("ERROR: specified size of the generated text is less than one")
        return sys.exit(0)
    
    elif n < 1:
        print("ERROR: specified prefix size is less than one")
        return sys.exit(0)

    list_of_words = open_file(sfile)

    hashtable = Hashtable(M)
    nonword_list = [NONWORD] * n
    make_hashtable(list_of_words, hashtable, nonword_list)

    nonword_list = [NONWORD] * n
    generated_list = generate_text(nonword_list, hashtable, num_of_words)

    print(generated_list)

main()