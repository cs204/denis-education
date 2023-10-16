def main():
    check()

def check():
    while True:
        try:
            inp = input("Дробь: ")
            first_num = int(inp.partition('/')[0])
            second_num = int(inp.partition('/')[2])
            res = first_num / second_num
            if res == 0.75:
                print("75%")
                break
            elif res == 0.50:
                print("50%")
                break
            elif res == 0.25:
                print("25%")
                break
            elif res <= 0.1:
                print("E")
                break
            elif res >= 0.99:
                print("F")
                break

        except (ValueError, ZeroDivisionError):
            return check()


main()