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
    
    while(i != n + 1){
        int a;
        cout << " Podaj liczbę:  " << endl;
        cin >> a;
        iloczyn = iloczyn * a;
        i += 1;
        } 
     
     
    cout  << "Iloczyn podanych przez Ciebie liczb wynosi : " << iloczyn << endl;
	return 0;
}

