


def snake_to_camel(word: str) -> str:
    word_list = list(word)
    for x in word_list:
        print(x)
        if x == "_":
            word_list.remove(x)
    else:
        return "".join(word_list)






print(snake_to_camel("hello_world"))