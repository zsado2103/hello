/*
 * Horner.cpp
 */


#include <iostream>

using namespace std;

// W(x) = 2x^3 + 3x^2 + 5x + 4 (8)
// W(x) = x (2x^2 + 3x + 5) + 4
// W(x) = x (x(2x + 3) + 5) + 4 (3 mnożenia)

float horner_rek(int k, float tbwsp[],float x)
{
    if (k == 0)
        return tbwsp[0] * x;
    return horner_rek(k - 1, tbwsp, x) * x + tbwsp[k];
    
    }

float horner_it(int k, float tbwsp[], float x){
    float wynik = tbwsp[0];
    for (int i = 1; i < k + 1; i++){
        wynik = wynik * x + tbwsp[i];
    
    return wynik;
}  



int main(int argc, char **argv)
  
    float x = 0;
    float wspolczynniki[4];
    int stopien = 3;
    cout << "Podaj x: " << endl;
    cin >> x;
    
    for(int i = 0; i < 4 ; i ++){
        cout << "Podaj współczynnik: ";
        cin >> wspolczynniki[i];
    }
        
    cout << "Wartość wielomianu: " << horner_it(stopien, wspolczynniki, x) << endl;
        
    
	
	return 0;
}

