def hitung_kelipatan(baris, kelipatan):
    total_per_baris = []

    for i in range(1, baris + 1):
        row_total = 0
        row_calculation = []

        for j in range(i, 0, -1):
            nilai = j * kelipatan
            row_calculation.append(f"({j} * {kelipatan})")
            row_total += nilai
        
        print(f"{' + '.join(row_calculation)} = {row_total}")
        total_per_baris.append(row_total)

    return total_per_baris

def main():
    baris, kelipatan = map(int, input("Input: ").split())
    total_per_baris = hitung_kelipatan(baris, kelipatan)

    print(sum(total_per_baris))

if __name__ == "__main__":
    main()