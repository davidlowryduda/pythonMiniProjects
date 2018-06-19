/*
 * Expected use:
 *
 * c++ -std=c++14 363.cpp
 * cat enable1.txt | ./a.out
 *
 * Background
 * ==========
 *
 * "I before E except after C" is perhaps the most famous English spelling
 * rule. For the purpose of this challenge, the rule says:
 *
 * if "ei" appears in a word, it must immediately follow "c".
 * If "ie" appears in a word, it must not immediately follow "c".
 * A word also follows the rule if neither "ei" nor "ie" appears anywhere in
 * the word. Examples of words that follow this rule are:
 *
 * fiery hierarchy hieroglyphic
 * ceiling inconceivable receipt
 * daily programmer one two three
 *
 * There are many exceptions that don't follow this rule, such as:
 *
 * sleigh stein fahrenheit
 * deifies either nuclei reimburse
 * ancient juicier societies
 *
 * Challenge
 * ---------
 *
 * Write a function that tells you whether or not a given word follows the "I
 * before E except after C" rule.
 *
 * check("a") => true
 * check("zombie") => true
 * check("transceiver") => true
 * check("veil") => false
 * check("icier") => false
 *
 * Optional Bonus 1
 * ----------------
 *
 * How many words in the enable1 word list are exceptions to the rule? (The
 * answer is 4 digits long and the digits add up to 18.)
**/

#include <iostream>
#include <string>
#include <assert.h>

// #define DO_TESTS


bool check(std::string);
void do_tests();

int main()
{
#ifdef DO_TESTS
  do_tests();
#endif
  std::string word;
  int total;
  while (std::cin >> word)
  {
    if (not check(word))
    {
      total++;
    }
  }
  std::cout << total << std::endl;
}

bool check(std::string in_string)
{
  if (in_string.size() < 2) { return true; }
  if (in_string[0] == 'e' and in_string[1] == 'i') { return false; }
  char let1, let2, let3;
  for (int i = 0; i<in_string.size()-2; ++i)
  {
    let1 = in_string[i];
    let2 = in_string[i+1];
    let3 = in_string[i+2];
    if (let2 == 'i' and let3 == 'e')
    {
      if (let1 == 'c') { return false; }
    }
    if (let2 == 'e' and let3 == 'i')
    {
      if (let1 != 'c') { return false; }
    }
  }
  return true;
}

void do_tests()
{
    assert(check("a") == true);
    assert(check("zombie") == true);
    assert(check("transceiver") == true);
    assert(check("thre") == true);
    assert(check("two") == true);
    assert(check("one") == true);
    assert(check("programmer") == true);
    assert(check("daily") == true);
    assert(check("receipt") == true);
    assert(check("inconceivable") == true);
    assert(check("ceiling") == true);
    assert(check("hieroglyphic") == true);
    assert(check("hierarchy") == true);
    assert(check("fiery") == true);
    assert(check("veil") == false);
    assert(check("icier") == false);
    assert(check("societie") == false);
    assert(check("juicier") == false);
    assert(check("ancient") == false);
    assert(check("reimburse") == false);
    assert(check("nuclei") == false);
    assert(check("either") == false);
    assert(check("deifies") == false);
    assert(check("fahrenheit") == false);
    assert(check("stein") == false);
    assert(check("sleigh") == false);
    std::cout << "All checks passed." << std::endl;
}
