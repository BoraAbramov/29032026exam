

def story_split(tuple: str):
    split_tuple = tuple.split(" ")
    return split_tuple

def counter(list1):

    sorter = dict()
    for x in list1:
        sorter[x] = sorter.get(x, 0) + 1

    for k, v in sorter.items():
        freq = max(v, key=sorter.get)
        print(f"{k}: {freq}")