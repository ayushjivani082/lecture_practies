def count_vowel(text):

    vowel = "aeiouAEIOU"

    count = 0

    for ch in text:
        if ch in vowel:
            count += 1
            print(ch)

    return count