class TrieNode(object):
    
    def __init__(self):
        self.children = {}  #HashMap - easier than array
        self.endOfWord = False #checkpoint -- not storing the actual value in the TrieNode


#Initailzie the trie 
class Trie(object):

    def __init__(self):
        #will search everythig from root (milestone)
        self.root = TrieNode()
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root

        for c in word: 

            #create nodes
            if c not in cur.children: #if the character is not in the hashMap yet 
                cur.children[c] = TrieNode() #creating a node for this value
            
            #update position
            cur = cur.children[c] #node already exists (set to the last word)
        cur.endOfWord = True 


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cur = self.root

        for c in word: 

            #create nodes
            if c not in cur.children: #if the character is not in the hashMap yet 
                return False
            
            #update position
            cur = cur.children[c] #node already exists (set to the last word)
        return cur.endOfWord # being set

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        cur = self.root 
        for c in prefix: 

            #create nodes
            if c not in cur.children: #if the character is not in the hashMap yet 
                return False
            
            #update position
            cur = cur.children[c] #node already exists (set to the last word)
        return True 


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)