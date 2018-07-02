/*
 * Description
 * ===========
 *
 * A Ducci sequence is a sequence of n-tuples of integers, sometimes known as
 * "the Diffy game", because it is based on sequences. Given an n-tuple of
 * integers (a_1, a_2, ... a_n) the next n-tuple in the sequence is formed by
 * taking the absolute differences of neighboring integers. Ducci sequences are
 * named after Enrico Ducci (1864-1940), the Italian mathematician credited
 * with their discovery.
 *
 * Some Ducci sequences descend to all zeroes or a repeating sequence. An
 * example is (1,2,1,2,1,0) -> (1,1,1,1,1,1) -> (0,0,0,0,0,0).
 *
 * Additional information about the Ducci sequence can be found in this writeup
 * from Greg Brockman, a mathematics student.
 *
 * It's kind of fun to play with the code once you get it working and to try and
 * find sequences that never collapse and repeat. One I found was (2, 4126087,
 * 4126085), it just goes on and on.
 *
 * It's also kind of fun to plot these in 3 dimensions. Here is an example of
 * the sequence "(129,12,155,772,63,4)" turned into 2 sets of lines (x1, y1,
 * z1, x2, y2, z2).
 *
 * Input Description
 * -----------------
 *
 * You'll be given an n-tuple, one per line. Example:
 *
 * (0, 653, 1854, 4063)
 *
 * Output Description
 * ------------------
 *
 * Your program should emit the number of steps taken to get to either an all 0
 * tuple or when it enters a stable repeating pattern. Example:
 *
 * [0; 653; 1854; 4063]
 * [653; 1201; 2209; 4063]
 * [548; 1008; 1854; 3410]
 * [460; 846; 1556; 2862]
 * [386; 710; 1306; 2402]
 * [324; 596; 1096; 2016]
 * [272; 500; 920; 1692]
 * [228; 420; 772; 1420]
 * [192; 352; 648; 1192]
 * [160; 296; 544; 1000]
 * [136; 248; 456; 840]
 * [112; 208; 384; 704]
 * [96; 176; 320; 592]
 * [80; 144; 272; 496]
 * [64; 128; 224; 416]
 * [64; 96; 192; 352]
 * [32; 96; 160; 288]
 * [64; 64; 128; 256]
 * [0; 64; 128; 192]
 * [64; 64; 64; 192]
 * [0; 0; 128; 128]
 * [0; 128; 0; 128]
 * [128; 128; 128; 128]
 * [0; 0; 0; 0]
 * 24 steps
 *
 * Challenge Input
 * ---------------
 *
 * (1, 5, 7, 9, 9)
 * (1, 2, 1, 2, 1, 0)
 * (10, 12, 41, 62, 31, 50)
 * (10, 12, 41, 62, 31)
*/

#include <iostream>
#include <assert.h>
#include <vector>
#include <map>
#include <string>

bool VERBOSE = false;

void ducci_step(std::vector<int> &);
int count_iters(std::vector<int>);
void do_tests();
void print_vector(std::vector<int>);
bool not_zero_vector(std::vector<int>);
int parse_input(std::vector<int> &);


int main(){
  do_tests();
  std::vector<int> seq;
  while (parse_input(seq))
  {
    std::cout << count_iters(seq) << " steps" << std::endl;
  }
}


// Replace `seq` with the next Ducci sequence, where the ith entry is replaced
// by the absolute value of the difference between the ith entry and the
// (i+1)st entry.
void ducci_step(std::vector<int> & seq)
{
  int first = seq[0];
  for (unsigned int i = 0; i < seq.size() - 1; ++i)
  {
    seq[i] = abs(seq[i] - seq[i+1]);
  }
  seq[seq.size()-1] = abs(seq[seq.size()-1] - first);
  return;
}


void print_vector(std::vector<int> seq)
{
  for (auto i = seq.begin(); i != seq.end(); ++i)
  {
    std::cout << *i << ' ';
  }
  std::cout << std::endl;
  return;
}


// Count the number of Ducci iterations necessary before repeating or before
// hitting the zero sequence. If the VERBOSE bool flag is set, then this
// prints each Ducci sequence along the way.
//
// The bound for the length of the sequences tested is 1000.
int count_iters(std::vector<int> seq)
{
  std::map< std::vector<int>, int> seen;
  while (seen.count(seq) == 0 and seen.size() < 1000 and not_zero_vector(seq))
  {
    seen[seq] = 1;
    if (VERBOSE) {print_vector(seq);}
    ducci_step(seq);
  }
  return seen.size()+1;
}


// Returns true if the vector is not all zeroes.
bool not_zero_vector(std::vector<int> seq)
{
  for (auto i = seq.begin(); i != seq.end(); ++i)
  {
    if (*i != 0) { return true; }
  }
  return false;
}


void do_tests()
{
  assert(count_iters(std::vector<int> {0, 653, 1854, 4063}) == 24);
  return;
}


// Given input like
//
// (1, 2, 3, 4, 5)
// (5, 16)
//
// This parses a line at a time, strips the parentheses, and gathers the
// integers into a vector of ints. If a nontrivial line of input is identified,
// this replaces `seq` with the vector of ints from the line and returns 1.
// If there is no input, this returns 0.
int parse_input(std::vector<int> & seq)
{
  std::string line;
  seq = {};
  if (std::getline(std::cin, line))
  {
    std::string val = "";
    for (unsigned i = 0; i < line.size(); ++i)
    {
      if (line[i] == '(' or line[i] == ' ') {}
      else if (line[i] == ',' or line[i] == ')')
      {
        seq.push_back(stoi(val));
        val = "";
      }
      else
      {
        val.push_back(line[i]);
      }
    }
    return 1;
  }
  else {return 0;}
}
