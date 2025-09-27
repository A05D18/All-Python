"""Q.3.In English, present participle is formed by adding
suffix -ing to infinite form: go -> going. A simple set of rules can be given as follows:
 a. If the verb ends in e, drop the e and add ing
 b. If the verb ends in ie, change ie to y and add ing
Write a function make_ing_form() which accepts a list of verbs and
 returns a dictionary with verb : present participle"""

def make_ing_form(words:list) -> dict:
    dict1 = {}
    for word in words:
        if word[-2:] == 'ie':
            dict1[word] = word[:-2] + "ying"
        elif word[-1] == 'e':
            dict1[word] = word[:-1] + "ing"
        else:
            dict1[word] = word + "ing"
    return dict1

"""def make_ing_form(words: list) -> dict:
    dict1 = {}
    for word in words:
        # Skip empty strings or non-string inputs
        if not isinstance(word, str) or not word:
            continue
        # Handle words ending in 'ie'
        if word.endswith('ie'):
            dict1[word] = word[:-2] + "ying"
        # Handle words ending in 'e' (but not 'ie')
        elif word.endswith('e'):
            dict1[word] = word[:-1] + "ing"
        # Handle all other cases
        else:
            dict1[word] = word + "ing"
    return dict1"""


print(make_ing_form(["go", "lie", "fill", "take", "make"]))





