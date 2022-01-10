# Day 13 Exercise

def bad_hashfunction(s, size):
    '''
    Returns the ordinal value of the first character modulo size of hash table
    :param s: The string to be hashed
    :param size The size of the hash table
    :return: The ordinal value of the first character modulo size
    '''
    #string.self = s #i made
    #size.self = size #i made
    return ord(s[0]) % size

def average_collisions(table):
    '''
    Given a hash table, compute an average size of each non-empty bin
    :param table: The hash table
    :return: The average size of non-empty bins
    '''
    sum = 0
    count = 0
    for value in table:
        if value > 0:
            sum += value
            count += 1

    if count == 0:
        return 0
    else:
        return sum / count
# ---------------------------------------------------Add two hash functions here below:-----------------------
def noicHash (s,size):
    #what type to do?
    h=0
    for i in s:
        h += ord(i)
    return h % size

def thirdHash (s,size):
    h=0
    count = 1
    for i in s:
        h += count*(ord(i))
        count+=1
    return h % size

englishWordFile = open("wordsEn.txt", "r")
words = []
# read in each word and add it to list.
for word in englishWordFile:
    words.append(word)
print("There are ", len(words), " words in the file.")

# experiment # 1
# make a table with size 100
table = 100 * [0]
# run through the words, hashing each one and then incrementing the appropriate counter
for w in words:
    h = bad_hashfunction(w, len(table))
    table[h] += 1

print(table) # just for debugging purposes

print("Average collisions (Experiment 1)", average_collisions(table))
englishWordFile.close()

# experiment # 2
englishWordFile = open("wordsEn.txt", "r")
words = []
# read in each word and add it to list.
for word in englishWordFile:
    words.append(word)
print("There are ", len(words), " words in the file.")

# make a table with size 100
table = 100 * [0]
# run through the words, hashing each one and then incrementing the appropriate counter
for w in words:
    h = noicHash(w, len(table))
    table[h] += 1

print(table) # just for debugging purposes

print("Average collisions (Experiment 2)", average_collisions(table))
englishWordFile.close()


# experiment # 3

englishWordFile = open("wordsEn.txt", "r")
words = []
# read in each word and add it to list.
for word in englishWordFile:
    words.append(word)
print("There are ", len(words), " words in the file.")

# make a table with size 100
table = 100 * [0]
# run through the words, hashing each one and then incrementing the appropriate counter
for w in words:
    h = thirdHash(w, len(table))
    table[h] += 1

print(table) # just for debugging purposes

print("Average collisions (Experiment 3)", average_collisions(table))
englishWordFile.close()
