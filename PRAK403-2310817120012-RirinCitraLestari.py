angka1, angka2 = map(int, input("Input (dua angka dipisahkan spasi): ").split())

if angka1 < angka2:
    for i in range(angka1, angka2 + 1):
        x = angka2
        x = x - (i - angka1)
        print(f"{i} {x}", end="")
        if i == angka2:
            break
        else:
            print(" - ", end="")
else:
    for i in range(angka1, angka2 - 1, -1):
        x = angka2
        x = x + (angka1 - i)
        print(f"{i} {x}", end="")
        if i == angka2:
            break
        else:
            print(" - ", end="")
