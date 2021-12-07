//
// Created by Kevin on 12/1/2021.
//

#include "Day2part2.h"
#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main(){
    ifstream myfile ("C:\\Users\\Kevin\\AdventOfCode2021\\inputs\\day2.txt");
    int depth = 0;
    int horz = 0;
    int aim = 0;
    for( string line; getline( myfile, line ); )
    {
        cout << line << endl;
        int a = line.back() -'0';
        if (line[0] == 'f'){
            horz += a;
            depth += a*aim;
        } else if (line[0] == 'u'){
            aim -= a;
        } else if (line[0] == 'd'){
            aim += a;
        }


    }
    cout << depth*horz;
    //1997106066
}
