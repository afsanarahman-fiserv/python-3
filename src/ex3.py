def create_files(file):
    # put words in set to avoid repeats
    words = set()
    with open(file, "r") as f:
        while True:
            line = f.readline().split()
            if not line:
                break
            for word in line:
                words.add(word)
    # save number of words to return
    num_words = len(words)

    with open("../files/large-words.txt", "w") as f:
        for word in words:
            if len(word) >= 3:
                f.write(word + '\n')
    
        for word in words:
            if len(word) < 3:
                f.write(word + '\n')

    return num_words

def ex3():
    total_words = create_files("../files/words.txt")
    print(f"Total words: {total_words}.")

ex3()