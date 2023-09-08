def main():
    print("Нужная сумма: 50")
    coin = input("Вставьте монету: ")
    coffee_machine(coin)

def coffee_machine(coin, amount_due=50, change_owed=0):
    while amount_due != 0:
        if int(coin) == 50 or int(coin) == 20 or int(coin) == 10 or int(coin) == 5:
            if int(coin) < amount_due:
                amount_due = amount_due - int(coin)
                print(f"Нужная сумма: {amount_due}")
                coin = input("Вставьте монету: ")
            elif int(coin) > amount_due:
                change_owed = int(coin) - amount_due
                print(f"Ваша сдача: {change_owed}")
                break
            else:
                print(f"Ваша сдача: {change_owed}")
                break
        else:
            print("Нужная сумма: " + str(amount_due))
            coin = input("Вставьте монету: ")

main()
