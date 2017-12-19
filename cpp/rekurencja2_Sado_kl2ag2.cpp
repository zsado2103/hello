/*
 * rekurencja3_Sado_kl2ag2.cpp
 */


#include <iostream>
using namespace std;

int horner_rek(int k, int tablica [], int x)
{
    if (k == 0)
        return tablica[0] 
    else return horner_rek(k - 1, tablica, x) * x + tbwsp[k];
    }

int main(int argc, char **argv)
{
	int k = 0;
    int x = 0;
    int tablica[];
    
    cout << "Podaj stopień wielomianu: "
    cin >> k;
    for(int i=1; i=k; i++)
    {
        cout << "Podaj współczynniki ";
        cin >> tablica[];
    }

    cout << "Podaj wartość argumentu ";
    cin >> x;
    cout << "Miejsce zerowe: " << horner_rek(k - 1, tablica, x) * x + tbwsp[k];
    
	return 0;
}

