/*
 * Sado_lokata.cpp
 */


#include <iostream>

using namespace std; 
int licz(int n){
    int i = 0;
    int w = 100;
    while (i != n)
    {
    w += 10;
    i += 1;
    }
    return w;
}

int main(int argc, char **argv)
{
    int n =0;
    cout << "Podaj ilość miesięcy : ";
    cin >> n;
    
    cout << "Stan konta po tylu miesiącach: " << licz(n);
	return 0;
}

