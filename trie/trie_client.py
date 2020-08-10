from trie import Trie 

if __name__ == "__main__":
    tongue_twister = Trie() 

    words = ["she", "sells", "sea", "shells", "by", "the", "sea", "shore"]

    for i in range(len(words)):
        tongue_twister.put(words[i], i)

    print tongue_twister.get("sea")
    print tongue_twister.contains(words[3]) # Contains shells
    print tongue_twister.contains("shElls") # Non-existent word

    print tongue_twister.keys()
