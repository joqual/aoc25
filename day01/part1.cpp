#include <iostream>
#include <vector>

using std::cout;
using std::endl;
using std::vector;

vector<std::string> parseInput() {
  std::vector<std::string> inputValues;
  auto input = std::string();

  while (std::getline(std::cin, input)) {
    inputValues.push_back(input);
  }

  return inputValues;
}

int main(void) {
  vector<std::string> input = parseInput();

  int dial = 50;
  int maxValue = 100;
  int count = 0;

  for (auto i : input) {
    char direction = i[0];
    int rotate = std::stoi(i.substr(1));

    if (direction == 'L') {
      dial -= rotate;
      count += std::abs(rotate) / 100;
      while (dial < 0) {
        dial = maxValue - std::abs(dial);
      }
    } else {
      dial += rotate;
      dial = dial % maxValue;
    }
    if (dial == 0) {
      count += 1;
    }
    // cout << dial << endl;
  }

  cout << "password: " << count << std::endl;

  return 0;
}