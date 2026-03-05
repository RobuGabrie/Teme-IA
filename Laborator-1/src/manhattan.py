from scipy.spatial.distance import cityblock # type: ignore


def read_vectors_from_file(path: str) -> tuple[list[float], list[float]]:
    """Citeste doi vectori dintr-un fisier text.

    Functia citeste liniile ne-goale din fisier, interpreteaza primele doua
    linii ca vectori si verifica daca au aceeasi dimensiune.

    Args:
        path: Calea catre fisierul de intrare.

    Raises:
        ValueError: Daca fisierul are mai putin de doua linii ne-goale.
        ValueError: Daca vectorii parsati nu au aceeasi dimensiune.

    Returns:
        Un tuplu care contine cei doi vectori parsati.
    """
    with open(path, "r", encoding="utf-8") as f:
        lines = []
        for raw_line in f:
            line = raw_line.strip()
            if line:
                lines.append(line)

    if len(lines) < 2:
        raise ValueError("Fisierul trebuie sa contina cel putin doua linii, cate una pentru fiecare vector.")

    vector_1 = _parse_vector_line(lines[0])
    vector_2 = _parse_vector_line(lines[1])

    if len(vector_1) != len(vector_2):
        raise ValueError("Vectorii trebuie sa aiba aceeasi dimensiune.")

    return vector_1, vector_2


def manhattan_manual(v1: list[float], v2: list[float]) -> float:
    """Calculeaza manual distanta Manhattan dintre doi vectori.

    Args:
        v1: Primul vector numeric.
        v2: Al doilea vector numeric.

    Raises:
        ValueError: Daca vectorii nu au aceeasi dimensiune.

    Returns:
        Distanta Manhattan sub forma de numar real.
    """
    if len(v1) != len(v2):
        raise ValueError("Vectorii trebuie sa aiba aceeasi dimensiune.")

    distance = 0.0
    for i in range(len(v1)):
        distance += abs(v1[i] - v2[i])

    return distance


def manhattan_cityblock(v1: list[float], v2: list[float]) -> float:
    """Calculeaza distanta Manhattan folosind ``scipy.spatial.distance.cityblock``.

    Args:
        v1: Primul vector numeric.
        v2: Al doilea vector numeric.

    Raises:
        ValueError: Daca vectorii nu au aceeasi dimensiune.

    Returns:
        Distanta Manhattan sub forma de numar real.
    """
    if len(v1) != len(v2):
        raise ValueError("Vectorii trebuie sa aiba aceeasi dimensiune.")
    return float(cityblock(v1, v2))


def _parse_vector_line(line: str) -> list[float]:
    """Interpreteaza o linie text ca vector numeric.

    Virgulele sunt tratate ca separatori, la fel ca spatiile.

    Args:
        line: O linie de intrare care contine valori numerice.

    Raises:
        ValueError: Daca linia nu contine valori numerice.

    Returns:
        Vectorul parsat ca lista de valori float.
    """
    line = line.replace(",", " ")
    parts = line.split()

    if not parts:
        raise ValueError("Linie invalida pentru vector.")

    vector = []
    for value in parts:
        vector.append(float(value))

    return vector
