def count_vowels(text):
    return sum(c in "aeiouAEIOU" for c in text)
