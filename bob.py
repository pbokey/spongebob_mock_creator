from random import randint

inp = input('Enter text: ')
def transform(strt):
    splitter = list(strt)
    for i in range(len(splitter)):
        x = randint(0,1)
        if (x == 1):
            if (not splitter[i].isupper()):
                splitter[i] = splitter[i].upper()
    x = "".join(splitter)
    return x
print(transform(inp))