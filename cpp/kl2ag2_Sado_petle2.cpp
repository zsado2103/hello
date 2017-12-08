/*
 * kl2ag2_Sado_petle1.cpp
 */


#include <iostream>
using namespace std;
int main(int argc, char **argv)
{
    int n;

	cout << "Podaj ilość liczb: " << endl;
    cin >> n;
    int iloczyn = 1;
    int i = 1;
    int parzyste = 0;
    
    while(i != n + 1){
        int a;
        cout << " Podaj liczbę:  " << endl;
        cin >> a;
        iloczyn = iloczyn * a;
        i += 1;
        
        if (a % 2 == 0)
        parzyste += 1;
        } 
     
     
    cout  << "Iloczyn podanych przez Ciebie liczb wynosi : " << iloczyn << endl;
    cout << "Ile liczb jest  parzystych? " << parzyste << endl;
    cout << "Ile liczb jest nieparzystych? " << n - parzyste << endl;
	return 0;
}

