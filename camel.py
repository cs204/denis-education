inp = input("Верблюжий стиль: ")
underline = "_"
result = ""

for i in inp:
    if i.isupper():
        result += underline + i
        result = result.lower()
    else:
        result += i
        result = result.lower()

print(result.lstrip(underline))
