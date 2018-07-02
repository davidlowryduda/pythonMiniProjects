#include <iostream>
#include <string>
#include <vector>

int main()
{
  std::string line;
  std::vector<int> hold;
  while (std::getline(std::cin, line))
  {
    std::string val = "";
    for (unsigned i = 0; i < line.size(); ++i)
    {
      if (line[i] == '(' or line[i] == ' ') {}
      else if (line[i] == ',' or line[i] == ')')
      {
        hold.push_back(stoi(val));
        std::cout << stoi(val);
        val = "";
      }
      else
      {
        val.push_back(line[i]);
      }
    }
    std::cout << std::endl << std::endl;
  }
}
