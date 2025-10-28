import math

def load_data(file = "aspell.txt"):
    data = []
    with open(file) as f:
        for line in f:
            if ":" not in line:
                continue
            correct, wrongs = line.strip().split()
            correct = correct.strip()
            for wrong in wrongs.strip().split():
                data.append((correct, wrong))
    return data