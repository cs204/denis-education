months = ["январь", "февраль", "март", "апрель",
     "май", "июнь", "июль", "август", "сентябрь", "октябрь",
     "ноябрь", "декабрь"]
monthsInt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        31]

def main():
     outdated()

def outdated():
     dot = "."
     space = " "
     while True:
          try:
               s = input("Дата: ")
               if dot in s:
                    inp = s.split(dot)
                    day = days[int(inp[0])-1]
                    month = monthsInt[int(inp[1])-1]
                    year = int(inp[2])
                    print(f"{year}-{month:02}-{day:02}")
                    break
               elif space in s:
                    inp = s.split(space)
                    if inp[1] in months:
                         day = days[int(inp[0])-1]
                         monthInput = months.index(inp[1])
                         month = monthsInt[monthInput]
                         year = int(inp[2])
                         print(f"{year}-{month:02}-{day:02}")
                         break
                    else:
                         day = days[int(inp[0])-1]
                         month = monthsInt[int(inp[1])-1]
                         year = int(inp[2])
                         print(f"{year}-{month:02}-{day:02}")
                         break
          except ValueError:
               return outdated()

main()