/*
 * petle_switch.cpp
 * Program pobiera numer miesiąca i wyświetla jego nazwę
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)

{
	int m = 0;
    
    
    //while (true) {
        //cout << "Podaj miesiac " << endl;
        //cin >> m;
        //if (m < 13 && m > 0)
            //break;
    //};
    
        // pętla zaporowa
        
    while (m > 12 || m < 1 ) { // || - lub
        cout << "Podaj miesiąc (1-12): " << endl;
        cin >> m;
        };
        
    //if (m == 1)
    //cout << "Styczeń " << endl;
    //else if (m == 2)
    //cout << "Luty " << endl;
    //else if (m == 3)
    //cout << "Marzec " << endl;
    
    //switch - sprawdz, case-wartosc
    
    switch(m) 
    {
        case 1:
            cout << "Styczeń";
        break;
        case 2:
            cout << "Luty";
        break;
        case 3:
            cout << "Marzec";
        break;
        case 4:
            cout << "Kwieceń";
        break;
    }
    
    
	return 0;
}

