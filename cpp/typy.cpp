/*
 * hello.cpp
 
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    //char imie; // deklaracja zmiennej znakowej
    char imie[10]; // deklaracja tablicy znakowej
    //int wiek; // deklaracja typu całkowitego
    //wiek = 0; // inicjacja zmiennej
    int wiek = 0;
    
	cout << "Witaj w C++!" << endl;
	cout << "Podaj imię";
    //cin >> imie;
    cin.getline(imie, 10);
    cout << "Cześć " << imie << endl;
    cout << "Ile masz lat? ";
    cin >> wiek;
    cout << "Rok urodzenia: " << 2017 - wiek << endl;
    
	return 0;
}

