/*
 * rekurencja1_Sado_kl2ag2.cpp
 */


#include <iostream>
using namespace std;

int ciag_rek(int n){
    if (n == 1)
        return 1;
    if (n == 2)
        return 2;
    return ciag_rek(n - 1) + (2 * n) + (ciag_rek(n - 2));
    }

int main(int argc, char **argv)
{
    int n = 0;
    cout << "Wskaż numer wyrazu: " << endl;
    cin >> n;
    
    cout << "Wynik wynosi: " << ciag_rek(n);
	
	return 0;
}

