import math
import string

def load_data(file="aspell.txt"):
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

def transition_probs(data):
    tr_counts = {}


def viterbi(word, states, start_probs, trans_probs, emit_probs):
    V = [{}]
    path = {}


def main():
    data = load_data("aspell.txt")
    em_probs = emission_probs(data)
    tr_probs = transition_probs(data)
    start_probs =
    states =
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
