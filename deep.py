inp = input("Какой ответ на главный вопрос жизни, вселенной и всего такого? ")
inpToLower = inp.lower()

match inpToLower:
    case "42":
        print("Да")
    case "сорок два":
        print("Да")
    case _:
        print("Нет")