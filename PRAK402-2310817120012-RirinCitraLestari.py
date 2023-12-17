def main():
    batas = int(input("Input (batas maksimal bilangan): "))

    ganjil = [i for i in range(1, batas + 1) if i % 2 != 0]
    print(" ".join(map(str, ganjil)))

    genap = [i for i in range(batas, 1, -1) if i % 2 == 0]
    print(" ".join(map(str, genap)))

if __name__ == "__main__":
    main()
