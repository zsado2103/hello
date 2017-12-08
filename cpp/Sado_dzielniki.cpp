/*
 * Sado_dzielniki.cpp
 */


#include <iostream>

using namespace std;


     
int main(int argc, char **argv)
{
    int a = 0;
    
    cout << "Jakiej liczby dzielniki program ma wypisać? " << endl;
    cin >> a;
    
    int i = 0;
    int suma = 0;
    
    while(i != (a + 1))
{
    if (a%i == 0)
    suma = suma + 1 ;
    i = i+1;
    }
    cout << "Ilość dzielników: " << suma << endl;
	return 0;
}

