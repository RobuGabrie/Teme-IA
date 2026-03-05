from manhattan import manhattan_cityblock, manhattan_manual, read_vectors_from_file


def main() -> None:
    input_file = "data/input.txt"
    v1, v2 = read_vectors_from_file(input_file)

    d_manual = manhattan_manual(v1, v2)
    d_cityblock = manhattan_cityblock(v1, v2)

    print("Vectorul 1:", v1)
    print("Vectorul 2:", v2)
    print("Distanta Manhattan (manual):", d_manual)
    print("Distanta Manhattan (scipy.cityblock):", d_cityblock)


if __name__ == "__main__":
    main()
