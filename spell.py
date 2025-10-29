import math
import string

def load_data(file = "aspell.txt"):
    data = []
    with open(file) as f:
        for line in f:
            if ":" not in line:
                continue
            correct, wrongs = line.strip().split(":", 1)
            correct = correct.strip().lower()
            for wrong in wrongs.strip().split():
                data.append((correct, wrong.lower()))
    return data

def emission_probs(data):
    em_counts = {}
    for correct, typed in data:
        for c, t in zip(correct, typed):
            em_counts.setdefault(c, {})
            em_counts[c][t] = em_counts[c].get(t, 0) + 1
    # Testing Purposes
    # print("Emission counts:")
    # for c, t_counts in em_counts.items():
    #     print(f"{c}: {t_counts}")
    em_probs = {}
    for c, t_counts in em_counts.items():
        total = sum(t_counts.values())
        em_probs[c] = {}
        for t, v in t_counts.items():
            em_probs[c][t] = v / total
    # Testing Purposes
    # print("Emission probabilities:")
    # for c, t_counts in em_probs.items():
    #     print(f"{c}: {t_counts}")
    return em_probs


def transition_probs(data):
    tr_counts = {}
    for correct, _ in data:
        letters = ["<s>"] + list(correct) + ["</s>"]
        for a, b in zip(letters, letters[1:]):
            tr_counts.setdefault(a, {})
            tr_counts[a][b] = tr_counts[a].get(b, 0) + 1
    # Testing Purposes
    # print("Transition counts:")
    # for a, b_counts in tr_counts.items():
    #     print(a, b_counts)
    alphabet = list(string.ascii_lowercase) + ["</s>"]
    tr_probs = {}
    for a, b_counts in tr_counts.items():
        total = sum(b_counts.values()) + len(alphabet)
        tr_probs[a] = {}
        for b in alphabet:
            count_b = b_counts.get(b, 0)
            smoothed_count = count_b + 1
            probability = smoothed_count / total
            tr_probs[a][b] = probability
    # Testing Purposes
    # print("Transition probabilities:")
    # for a, b_counts in tr_probs.items():
    #     print(a, {b: round(p, 4) for b, p in b_counts.items()})
    return tr_probs

def viterbi(word, states, start_probs, trans_probs, emit_probs):
    V = [{}]
    path = {}

def main():
    data = load_data("aspell.txt")
    em_probs = emission_probs(data)
    tr_probs = transition_probs(data)
    start_counts = tr_probs.get("<s>", {})
    total_starts = sum(start_counts.values())
    start_probs = {}
    for k, v in start_counts.items():
        probs = v / total_starts
        start_probs[k] = probs
    states = set(string.ascii_lowercase)
    while True:
        user_input = input("Please enter a word to decode ('quit' to exit): ").strip().lower()
        if user_input == 'quit':
            break
        words = user_input.split()
        corrected_words = []
        for word in words:
                corrected_word = viterbi(word, states, start_probs, tr_probs, em_probs)
                corrected_words.append(corrected_word)
        print("Correct text: " + ' '.join(corrected_words))


if __name__ == "__main__":
    main()
