

def str_list(words_list):
    """

    :param words_list: empty list or list of words
    :return: add strings to list till 'quit'
    """
    words_list = []
    while True:
        word = str(input("Enter a word: "))
        if word == "quit":
            return words_list
        else:
            words_list.append(word)


def duplitector(words_list):
    """

    :param words_list: list of words
    :return: check duplicates
    """
    sorter = dict()
    for x in words_list:
        sorter[x] = sorter.get(x, 0) + 1

    for value in sorter.values():
        if value > 1:
            print("there were duplicates")
            return

    print("there were no duplicates")





list1 = []

str_list(list1)
duplitector(list1)


