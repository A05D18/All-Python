ls = ["hello", "who are you", "I dont know anything", "Why are you here"]


def longest(lst):
    longest_str = ''
    for item in lst:
        word = item.split()
        for words in word:
            if len(words) > len(longest_str):
                longest_str = words

    return longest_str


print(longest(ls))
