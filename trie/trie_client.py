from trie import Trie 

if __name__ == "__main__":
    tongue_twister = Trie() 

    words = ["she", "sells", "sea", "shells", "by", "the", "sea", "shore"]

    for i in range(len(words)):
        tongue_twister.put(words[i], i)

    print tongue_twister.get(words[2]) # Retrieve "sea"
    print tongue_twister.contains(words[3]) # Contains "shells"?
    print tongue_twister.contains("shElls") # Non-existent word "shElls"?

    print tongue_twister.keys() # Iterate all keys in order

    print tongue_twister.keyWithPrefix("sh") # Find all words starting with the letters "sh"

    print tongue_twister.longestPrefixOf("shellsort") # Key that is longest prefix of given word