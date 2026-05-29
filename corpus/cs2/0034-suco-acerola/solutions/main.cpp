/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: souca
 *
 * Created on 14 de Janeiro de 2021, 19:45
 */

#include <cstdlib>
#include <stdio.h>
#include <stdlib.h>
#include<math.h>
#include <iomanip>
#include <iostream>

using namespace std;

/*
 * 
 */
int main(int argc) {
    int N = 1, F = 1;
    cout << fixed << setprecision(2);
    while (N != 0 && F != 0) {
        cin >> N;
        while (N < 0 || N > pow(10, 3)) {
            cin >> N;
        }
        cin >> F;
        while (F < 0 || F > pow(10, 3)) {
            cin >> F;
        }
        if (N != 0 && F != 0) {
            cout << ((float) F * 50) / 1000 / (float) N;
        }
    }


    //return 0;
}

