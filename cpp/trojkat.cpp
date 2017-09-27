/*
 * trojkat.cpp
 *Program pobiera trzy boki trójkąta,
 * Sprawdza, czy da się z nich zbudować trójkąt,
 * oblicza obwód  pole (ze wzoru Herona)
 * i drukuje na  ekranie odpowiedni komunikat
 */



#include <iostream>
using namespace std;
int main(int argc, char **argv)
{
    int a, b, c;
    a = b = c = 0;
    cout << "Podaj 3 liczby: ";
    cin >> a >> b >> c;
    
    if ( a + b > c && a + c > b && b + c > a )
    {
        cout <<"Trójkąt można zbudować." << endl;
        cout <<"Obwód trójkąta" << a + b + c;
    }
	return 0;
}

