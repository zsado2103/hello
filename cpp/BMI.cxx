/*
 * BMI.cpp
 * 
 */


#include <iostream>
#include <math.h>
using namespace std;



int main(int argc, char **argv)

{
    float b, m, w;
    m = w = b =0;
	cout << "Podaj swoją masę" << endl;
    cin >> m;
    cout << "Podaj swój wzrost w metrach" << endl;
    cin >> w;
    b = m /(w*w);
    cout << "Twoje BMI  wynosi: " << b << endl;

    if (b < 18.5){
        cout << "NIEDOWAGA" << endl;
        }
    else if ((b > 18.5) && (b < 24.9)){
        cout << "NORMA" << endl;
        }
    else if ((b >= 25) && (b < 30)){
        cout << "NADWAGA" << endl;
        }
    else if (b >= 30){
        cout << "OTYŁOŚĆ" << endl;
        }
	return 0;
}

