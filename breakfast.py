menu = {
   "кофе": 20.00,
   "чай": 10.00,
   "булочка": 5.00,
   "салат": 30.40,
   "пирожное": 45.50
}
sum = 0

while True:
    try:
        s = input("Блюдо: ")
        inp = s.lower()
        if inp in menu:
            sum += menu[inp]
    except EOFError:
        print(f"\nСумма: {sum:.2f}")
        break