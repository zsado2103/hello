/*
 * rekurencja6_Sado_kl2ag2.cpp
 * 
 */


#include <iostream>
using namespace std;

int euk_rek(int a, int b)
{
    if (b == 0)
        return a;
    else 
        return euk_rek(b, a % b);

    }

int main(int argc, char **argv)
{
	int a = 0;
    int b = 0;
    
    cout << "Wskaż dowolną liczbę: " << endl;
    cin >> a;
    cout <<"Wskaż kolejną liczbę: " << endl;
    cin >> b;
    cout << "Wynik to: " << euk_rek(b, a % b);
	return 0;
}

