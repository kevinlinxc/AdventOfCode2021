//
// Created by Kevin on 12/4/2021.
//

#include "Day5.h"

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <boost/algorithm/string_regex.hpp>

using namespace std;

int main() {
    ifstream myfile("C:\\Users\\Kevin\\AdventOfCode2021\\inputs\\day5.txt");
    for (string line; getline(myfile, line);) {
        cout << line << endl;
        vector<string> results;
        boost::algorithm::split_regex( results, line, boost::regex( " -> " ) ) ;
        vector<string> left;
        vector<string> right;
        boost::algorithm::split_regex(left, results[0], boost::regex(","));
        boost::algorithm::split_regex(right, results[1], boost::regex(","));
        cout << "x1: " << left[0]  << " y1: " << left[1] << " x2: " << right[0] << " y2: " << right[1] << endl;

    }
}
