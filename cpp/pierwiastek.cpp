/*
 * hello.cpp
 
 */


#include <iostream>
#include <math.h>

using namespace std;

int main(int argc, char **argv)
{
    int r = 0;
    
	//cout << "Witaj w C++!" << endl;
	cout << "Podaj liczbe:";
    //cin >> imie;
    //cin.getline(imie, 10);
    cin >> r;
    cout << "Pierwiastek: " << sqrt(r) << endl;
    
	return 0;
}

