Reflection

1.Give an example of a word which was correctly spelled by the user, but which was incorrectly
“corrected” by the algorithm. Why did this happen?

    ●  Example: Tyranny
        - "Corrected" to: tyranty
        - Reason: 
            The algorithm relies on letter-level transition and emission probabilities rather than full-wprd understanding
            or dictionary validation. Since it does not know what a real English word looks like, it only tries to maximize
            the probability of each letter following another. The training data was alos small and uneven, meaning there
            was not a lot of good examples and it was very limited in comparison to the whole of English language.
            Examples of redundancy: 
                - "nn" or "nt"
        - This highlights one of the main weaknesses of small-scale Hidden Markov Models. They rely entirely on statistical
          patterns, not meaning.


2.Give an example of a word which was incorrectly spelled by the user, but which was still
incorrectly “corrected” by the algorithm. Why did this happen?

    ● Example: Abouy
        - "Corrected" to: aboul
        - Reason:
            The algorithm failed because the emission and transition probabilities were estimated from a limited dataset.
            Not only that, but the dataset did not cotain exmaples that reflected real spelling errors or realistic letter 
            substitutions. As a result of this, the algorithm predicted a letter sequence being aboul that is not a valid 
            English word. Also, it is not able to verify the output against vocabulary in the English Language, since its
            limited to the dataset given. Meaning the alogrithm can determine weird combinations as valid, even though they
            are not. Overall, this shows that it lacks contextual awareness and depends on character-level patterns, therefore
            it cannot accurately correct or recognize misspellings.

3.Give an example of a word which was incorrectly spelled by the user, and was correctly corrected
by the algorithm. Why was this one correctly corrected, while the previous two were not?

    ● Example: None
        - Reason: 
            In testing, no words were successfully corrected. This likely due to several factors such as:
                -Limited training data:
                    The aspell.txt datatset does not represent the variety of real-world typos or the standard patterns of
                    charavter patterns in the English langauge.
                -Character-level modeling:
                    The algorithm treats each letter independently, ignoring word structure, prefixes, and suffixes that 
                    influence spelling
                -Probabilities:
                    Due to the limited training data, certain probabilities are patterns are diluted and are unlikely to
                    be picked up by the algorithm. This causes there to be unrealistic sequences and wrong corrections.
                -No dictionary constraint:
                    Without checking outputs against known English words, even high probabilities sequences can be incorrect. 


4.How might the overall algorithm’s performance differ in the “real world” if that training dataset is
taken from real typos collected from the internet, versus synthetic typos (programmatically
generated)?

    ● In real-world conditions, training the algorithm on authentic typo data would significantly improve the accuracy.
      Real typos capture the true patterns of human error, such as pressing nearby keys on the keyboard, forgetting letters,
      doubling letters accidently, or using the wrong word. 
      
      Another point to make is that typos that happen because of autocorrect or other factors can also affect how the 
      algorithm is trained. This is because these synthetic typos do not reflect real errors. This can cause unrealistic
      error distributions, leading to poor accuracy in real-world applications.

      However, the point is that large datasets for typos would be very helpful for algorithms that deal with statistical 
      patterns. Especially for both transition probabilities and emission probabilities.