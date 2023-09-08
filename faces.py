def main():
    inp = str(input())
    convert(inp)

def convert(inp):
    if ":)" in inp:
        inp1 = inp.replace(":)", "🙂")
        if ":(" in inp1:
            inp2 = inp1.replace(":(", "🙁")
            print(inp2)
        else:
            print(inp1)
    elif ":(" in inp:
        inp1 = inp.replace(":(", "🙁")
        if ":)" in inp1:
            inp2 = inp1.replace(":)", "🙂")
            print(inp2)
        else:
            print(inp1)
    else:
        print(inp)

main()