def main():
    kelipatan = int(input("Input pertama (bilangan kelipatan): "))
    simbol = input("Input kedua (simbol pengganti): ")

    for i in range(1, 51):
        if i % kelipatan == 0:
            print(simbol, end=" ")
        else:
            print(i, end=" ")
if __name__ == "__main__":
    main()