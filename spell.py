import string

#Opens aspell.txt and loads data
def load_data(file = "aspell.txt"):
    data = []
    with open(file) as f:
        for line in f:
            #Skips lines without colons
            if ":" not in line:
                continue
            correct, wrongs = line.strip().split(":", 1)
            correct = correct.strip().lower()
            for wrong in wrongs.strip().split():
                data.append((correct, wrong.lower()))
    return data

#Emission Probabilities
def emission_probs(data):
    em_counts = {}
    for correct, typed in data:
        #Zip allows comparison of letters
        for c, t in zip(correct, typed):
            em_counts.setdefault(c, {})
            em_counts[c][t] = em_counts[c].get(t, 0) + 1

    # Testing Purposes
    # print("Emission counts:")
    # for c, t_counts in em_counts.items():
    #     print(f"{c}: {t_counts}")

    #Convert counts to probabilities
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

#Transition Probabilities
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

    #Possible next letters + counts
    alphabet = list(string.ascii_lowercase) + ["</s>"]
    tr_probs = {}
    for a, b_counts in tr_counts.items():
        total = sum(b_counts.values()) + len(alphabet)
        tr_probs[a] = {}
        for b in alphabet:
            count_b = b_counts.get(b, 0)
            add_count = count_b + 1
            probs = add_count / total
            tr_probs[a][b] = probs

    # Testing Purposes
    # print("Transition probabilities:")
    # for a, b_counts in tr_probs.items():
    #     print(a, {b: round(p, 4) for b, p in b_counts.items()})
    return tr_probs

#Viterbi Algorithm
def viterbi(word, states, start_probs, trans_probs, emit_probs):
    viterbi_ = [{}]
    path = {}
    #First letter probabilities
    for state in states:
        viterbi_[0][state] = start_probs.get(state, 0.01) * emit_probs.get(state, {}).get(word[0], 0.01)
        path[state] = [state]
    #Recursion for subsequent letters
    for t in range(1, len(word)):
        viterbi_.append({})
        new_path = {}
        for curr in states:
            emit_p = emit_probs.get(curr, {}).get(word[t], 0.01)
            best_prev = None
            best_prob = 0
            for prev in states:
                trans_p = trans_probs.get(prev, {}).get(curr, 0.01)
                prob = viterbi_[t-1][prev] * trans_p * emit_p
                if prob > best_prob:
                    best_prob = prob
                    best_prev = prev
            viterbi_[t][curr] = best_prob
            new_path[curr] = path[best_prev] + [curr]
        path = new_path
    #Final best state
    last_state = None
    max_prob = 0
    for state in states:
        if viterbi_[-1][state] > max_prob:
            max_prob = viterbi_[-1][state]
            last_state = state
    return ''.join(path[last_state])

#Computes probabilities
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
