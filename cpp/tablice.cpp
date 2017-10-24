/*
 * tablice.cpp
 */


#include <iostream>

using namespace std;




int main(int argc, char **argv)
{
	int liczby[5];
    int i;
    int suma = 0;
    
    cout << "Podaj 5 ocen (0-6): " << endl;
    for(i = 0; i < 5; i++) {
        cin >> liczby[i];
    }
    
    cout << "Podane oceny: " << endl;
    for (i = 0; i < 5; i++) {
        suma  += liczby [i];
        cout << liczby [i] << " " << endl;
    }
    cout << "Suma ocen: " << suma << endl;
    cout << "Średnia arytmetyczna liczb: " << float(suma)/float(5) << endl;
    
    
    return 0;
}

