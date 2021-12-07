//
// Created by Kevin on 12/1/2021.
//

#include "Day2.h"
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    ifstream myfile("C:\\Users\\Kevin\\AdventOfCode2021\\inputs\\day2.txt");
    int depth = 0;
    int horz = 0;
    for (string line; getline(myfile, line);) {
        cout << line << endl;
        int a = line.back() - '0';
        if (line[0] == 'f') {
            horz += a;
        } else if (line[0] == 'u') {
            depth -= a;
        } else if (line[0] == 'd') {
            depth += a;
        }
        cout << "depth is: " << depth << " horz is: " << horz << endl;

    }
    cout << depth * horz;
}

//1936494
