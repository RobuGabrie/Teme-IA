from scipy.spatial.distance import cityblock


def read_vectors_from_file(path: str) -> tuple[list[float], list[float]]:
    with open(path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    if len(lines) < 2:
        raise ValueError("Fisierul trebuie sa contina cel putin doua linii, cate una pentru fiecare vector.")

    v1 = _parse_vector_line(lines[0])
    v2 = _parse_vector_line(lines[1])

    if len(v1) != len(v2):
        raise ValueError("Vectorii trebuie sa aiba aceeasi dimensiune.")

    return v1, v2


def manhattan_manual(v1: list[float], v2: list[float]) -> float:
    if len(v1) != len(v2):
        raise ValueError("Vectorii trebuie sa aiba aceeasi dimensiune.")
    return sum(abs(a - b) for a, b in zip(v1, v2))


def manhattan_cityblock(v1: list[float], v2: list[float]) -> float:
    if len(v1) != len(v2):
        raise ValueError("Vectorii trebuie sa aiba aceeasi dimensiune.")
    return float(cityblock(v1, v2))


def _parse_vector_line(line: str) -> list[float]:
    cleaned = line.replace(",", " ")
    parts = cleaned.split()
    if not parts:
        raise ValueError("Linie invalida pentru vector.")
    return [float(x) for x in parts]
