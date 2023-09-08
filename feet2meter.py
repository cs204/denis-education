def main():
    v = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v:.2f} метров.")

def feet2meter(v):
    if "ft" in v:
        v1 = v.replace("ft", " ")
        metr = float(v1) / 3.28084
        return float(metr)

main()