"""
Background
==========

"I before E except after C" is perhaps the most famous English spelling rule.
For the purpose of this challenge, the rule says:

if "ei" appears in a word, it must immediately follow "c".
If "ie" appears in a word, it must not immediately follow "c".
A word also follows the rule if neither "ei" nor "ie" appears anywhere in the
word. Examples of words that follow this rule are:

fiery hierarchy hieroglyphic
ceiling inconceivable receipt
daily programmer one two three

There are many exceptions that don't follow this rule, such as:

sleigh stein fahrenheit
deifies either nuclei reimburse
ancient juicier societies

Challenge
---------

Write a function that tells you whether or not a given word follows the "I
before E except after C" rule.

check("a") => true
check("zombie") => true
check("transceiver") => true
check("veil") => false
check("icier") => false

Optional Bonus 1
----------------

How many words in the enable1 word list are exceptions to the rule? (The answer
is 4 digits long and the digits add up to 18.)
"""

def check(word):
    if len(word) < 2:
        return True
    if word[0] == "e" and word[1] == "i":
        return False
    for let1, let2, let3 in zip(word, word[1:], word[2:]):
        if let2 == "i" and let3 == "e":
            if let1 == "c":
                return False
        if let2 == "e" and let3 == "i":
            if let1 != "c":
                return False
    return True

def test():
    assert check("a") == True
    assert check("zombie") == True
    assert check("transceiver") == True
    assert check("veil") == False
    assert check("icier") == False
    assert check("thre") == True
    assert check("two") == True
    assert check("one") == True
    assert check("programmer") == True
    assert check("daily") == True
    assert check("receipt") == True
    assert check("inconceivable") == True
    assert check("ceiling") == True
    assert check("hieroglyphic") == True
    assert check("hierarchy") == True
    assert check("fiery") == True
    assert check("societie") == False
    assert check("juicier") == False
    assert check("ancient") == False
    assert check("reimburse") == False
    assert check("nuclei") == False
    assert check("either") == False
    assert check("deifies") == False
    assert check("fahrenheit") == False
    assert check("stein") == False
    assert check("sleigh") == False
    return

def main():
    total = 0
    with open("enable1.txt", "r") as inputfile:
        for line in inputfile:
            if not check(line):
                total += 1
    print(total)

if __name__ == "__main__":
    #test()
    main()
