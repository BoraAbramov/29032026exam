from logging import exception


def str_list(words_list):
    while True:
        words_list = []
        word = str(input("Enter a word: "))
        if word == "quit":
            return words_list
        else:
            words_list.append(word)

def duplitector(words_list):
    try:
        for x in words_list:
            x.lower(x.lower())
            print(x, words_list)
    except exception as e:
        print(e)


list1 = []

str_list(list1)
duplitector(list1)


