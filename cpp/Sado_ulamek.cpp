/*
 * Sado_ulamek.cpp
 * 
 */


#include <iostream>
#include <math.h>
using namespace std;

int nwd(int a,int b)
{
    while (a!=b) 
    {
        if (a > b)
            a = a - b;
        else 
            b = b - a;
    }
    return a;
}           

int main(int argc, char **argv)
{   
    int a = 0; // licznik
    int b = 0; // mianownik
    
    cout << "Podaj licznik" << endl;
    cin >> a;
    cout << "Podaj mianownik " << endl; 
	cin >> b;
    
    a /= nwd(a, b);
    b /= nwd(a, b);
    
    cout << "Ułamek po skróceniu wynosi: " << a << "/" << b;
    
    
    
	return 0;
}

