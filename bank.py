inp = input("Приветствие: ")

if "здравствуйте" in inp:
    print("$0")
elif "з" in inp:
    if "здравствуйте" not in inp:
        print("$20")
else:
    print("100$")
