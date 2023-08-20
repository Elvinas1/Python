import json

words={}

def save_data():
    with open("students.json", "w") as f:
        json.dump(words,f)

def read_data():
    global words
    with open("students.json", "r") as f:
        words = json.load(f)

def add_word():
    new_word = input("Type a new word.")
    words[new_word] = {"meanings": [],
                       "examples": []}
    while True:
        print("""
    1 Add meaning
    2 Add example
    3 Exit""")
        choce = int(input("What do you want to do?"))
        if choce == 1:
            meaning = input("Type the meaning")
            words[new_word]["meanings"].append(meaning)
        elif choce == 2:
            example = input("Type the example")
            words[new_word]["examples"].append(example)
        elif choce == 3:
            break
        else:
            pass

    print(words)
    save_data()

def show_words():
    for word in words:
        print(f"Word :{word}")
        print()
        print("Meanings:")
        for meaning in words[word]["meanings"]:
            print(meaning)
        print()
        print("Examples:")
        for example in words[word]["examples"]:
            print(example)

def research():
    word = input("Which word do you want to search?")
    print()
    print("Meanings:")
    for meaning in words[word]["meanings"]:
        print(meaning)
    print()
    print("Examples:")
    for example in words[word]["examples"]:
        print(example)

def main():
    read_data()
    while True:
        print("""
        1 Add a new word.
        2 Show the word list
        3 Search a word
        """)
        choce = int(input("What do you want to do?"))
        if choce ==1:
            add_word()

        elif choce == 2:
            show_words()

        elif choce == 3:
            research()
        else:
            pass

main()