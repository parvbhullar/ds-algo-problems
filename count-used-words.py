# Program will display a welcome message to the user
print("Welcome! This program will analyze your file to provide a word count, the top 30 words and remove the following stopwords.")

s = open('Obama 2009.txt','r').read()  # Open the input file

# Program will count the characters in text file
num_chars = len(s)

# Program will count the lines in the text file
num_lines = s.count('\n')

# Program will call split with no arguments
words = s.split()
d = {}
for w in words:
    if w in d:
        d[w] += 1
    else:
        d[w] = 1

num_words = sum(d[w] for w in d)

lst = [(d[w],w) for w in d]
lst.sort()
lst.reverse()

# Program assumes user has downloaded an imported stopwords from NLTK
from nltk.corpus import stopwords # Import the stop word list
from nltk.tokenize import wordpunct_tokenize

stop_words = set(stopwords.words('english')) # creating a set makes the searching faster
print ([word for word in lst if word not in stop_words])

# Program will print the results
print('Your input file has characters = '+str(num_chars))
print('Your input file has lines = '+str(num_lines))
print('Your input file has the following words = '+str(num_words))

print('\n The 30 most frequent words are /n')

i = 1
for count, word in lst[:50]:
    print('%2s. %4s %s' %(i,count,word))
    i+= 1


print("Thank You! Goodbye.")




class TrieNode:

    # Trie node class
    def __init__(self):
        self.children = [None] * 26

        # isEndOfWord is True if node represent the end of the word
        self.count  = 0
        self.isEndOfWord = False

    def increaseCount(self):
        self.count += 1
        print 'Count - %d - %s' % (self.count, ('T' if self.isEndOfWord else 'F'))


class Trie:
    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        # Returns new trie node (initialized to NULLs)
        return TrieNode()

    def _charToIndex(self, ch):
        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case

        return ord(ch) - ord('a')

    def insert(self, key):

        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            else:
                print key[level]
                pCrawl.children[index].increaseCount()
            pCrawl = pCrawl.children[index]

        # mark last node as leaf
        pCrawl.isEndOfWord = True

    def search(self, key):
        # Search key in the trie
        # Returns true if key presents
        # in trie, else false
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]

        return pCrawl != None and pCrawl.isEndOfWord

    def countOfWords(self, key):
        pCrawl = self.root
        

'''wordCount(TrieNode root)
    {
        int result = 0;

        // Leaf denotes end of a word
        if (root.isLeaf)
            result++;

        for (int i = 0; i < ALPHABET_SIZE; i++)
          if (root.children[i] != null )
             result += wordCount(root.children[i]);

        return result;
    }'''


