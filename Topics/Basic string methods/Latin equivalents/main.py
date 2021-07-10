in_name = input()


def normalize(name):
    new_name = name.replace("é", "e").replace("ë", "e").replace("á", "a").replace("å", "a")\
        .replace("œ", "oe").replace("æ", "ae")
    return new_name


print(normalize(in_name))
