/**
 * Sample Use
 * ==========
 *
 * g++ -std=c++14 384.cpp
 * echo -e "3d6\n10d13\n2d5" | a.out
 *
 *
 * Description
 * ===========
 *
 * I love playing D&D with my friends, and my favorite part is creating
 * character sheets (my DM is notorious for killing us all off by level 3 or
 * so). One major part of making character sheets is rolling the character's
 * stats. Sadly, I have lost all my dice, so I'm asking for your help to make a
 * dice roller for me to use!
 *
 * Formal Inputs & Outputs
 * =======================
 *
 * Input description
 * -----------------
 *
 * Your input will contain one or more lines, where each line will be in the
 * form of "NdM"; for example:
 *
 * 3d6
 * 4d12
 * 1d10
 * 5d4
 *
 * If you've ever played D&D you probably recognize those, but
 * for the rest of you, this is what those mean:
 *
 * The first number is the number of dice to roll, the d just means "dice",
 * it's just used to split up the two numbers, and the second number is how
 * many sides the dice have. So the above example of "3d6" means "roll 3
 * 6-sided dice". Also, just in case you didn't know, in D&D, not all the dice
 * we roll are the normal cubes. A d6 is a cube, because it's a 6-sided die,
 * but a d20 has twenty sides, so it looks a lot closer to a ball than a cube.
 *
 * The first number, the number of dice to roll, can be any integer between 1
 * and 100, inclusive.
 *
 * The second number, the number of sides of the dice, can be any integer
 * between 2 and 100, inclusive.
 *
 * Output description
 * ------------------
 *
 * You should output the sum of all the rolls of that specified die, each on
 * their own line. so if your input is "3d6", the output should look something
 * like
 *
 * 14 Just a single number, you rolled 3 6-sided dice, and they added up to 14.
 *
 * Challenge Input
 * 5d12
 * 6d4
 * 1d2
 * 1d8
 * 3d6
 * 4d20
 * 100d100
 *
 * Challenge Output
 * [some number between 5 and 60, probably closer to 32 or 33]
 * [some number between 6 and 24, probably around 15]
 * [you get the idea]
 * [...]
 *
 * Notes/Hints
 * ===========
 *
 * A dice roll is basically the same as picking a random number between 1 and 6
 * (or 12, or 20, or however many sides the die has). You should use some way
 * of randomly selecting a number within a range based off of your input. Many
 * common languages have random number generators available, but at least a few
 * of them will give the same "random" numbers every time you use the program.
 * In my opinion that's not very random. If you run your code 3+ times with the
 * same inputs and it gives the same outputs, that wouldn't be super useful for
 * a game of D&D, would it? If that happens with your code, try to find a way
 * around that. I'm guessing for some of the newer folks, this might be one of
 * the trickier parts to get correct.
 *
 * Don't just multiply your roll by the number of dice, please. I don't know if
 * any of you were thinking about doing that, but I was. The problem is that if
 * you do that, it eliminates a lot of possible values. For example, there's no
 * way to roll 14 from 3d6 if you just roll it once and multiply by 3. Setting
 * up a loop to roll each die is probably your best bet here.
 *
 * Bonus =====
 *
 * In addition to the sum of all dice rolls for your output, print out the
 * result of each roll on the same line, using a format that looks something
 * like
 *
 * 14: 6 3 5
 * 22: 10 7 1 4
 * 9: 9
 * 11: 3 2 2 1 3
 *
 * You could also try setting it up so that you can manually input more rolls.
 * that way you can just leave the program open and every time you want to roll
 * more dice, you just type it in and hit enter.
**/

#include <iostream>
#include <random>
#include <vector>

std::random_device rd;
bool get_input(unsigned&, unsigned&, char&);
int roll_die(unsigned);
void roll_dice(std::vector<unsigned> &, unsigned);
void print_results(std::vector<unsigned>);


int main() {
  char c;
  unsigned num_rolls, num_sides;
  while (get_input(num_rolls, num_sides, c))
  {
    std::vector<unsigned> results(num_rolls, 0);
    roll_dice(results, num_sides);
    print_results(results);
  }
}


// Input is assumed to be of the form "rds", where "r" is the number of
// dice to roll and "s" is the number of sides of the dice.
// For example, an input may be "4d6".
bool get_input(unsigned& num_rolls, unsigned& num_sides, char& c)
{
  return bool(std::cin >> num_rolls >> c >> num_sides);
}


// Mimic rolling die: generate random number from 1 to `sides`.
int roll_die(unsigned sides)
{
  std::uniform_int_distribution<unsigned> dist(1, sides);
  return dist(rd);
}

// Roll enough dice with `num_sides` sides to fill up the `results`
// vector with dice rolls.
void roll_dice(std::vector<unsigned> & results, unsigned num_sides)
{
  for (int i=0; i< results.size(); ++i)
  {
    results[i] = roll_die(num_sides);
  }
}


void print_results(std::vector<unsigned> results)
{
  std::cout << std::accumulate(results.begin(), results.end(), 0) << ": ";
  for (int i=0; i<results.size(); ++i)
  {
    std::cout << results[i] << ' ';
  }
  std::cout << std::endl;
}
