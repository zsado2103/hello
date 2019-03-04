/*
 * struktury.cpp
 */


#include <iostream>
#include <fstream>
using namespace std;

struct osoba {
    char imie[20];
    char nazwisko[20];
    int wiek;
};

void drukujOsoby(osoba tb[], int ile) {
    for (int i=0; i < ile; i++) {
        cout << "Podano: " << tb[i].imie << " " << tb[i].nazwisko << " " << tb[i].wiek << endl;
    }
    
}

void getOsoby(osoba tb[], int ile) {
    for (int i=0; i < ile; i++) {
        osoba uczen;
        cout << "Podaj imię: ";
        cin.getline(uczen.imie, 20);
        cout << "Podaj nazwisko: ";
        cin.getline(uczen.nazwisko, 20);
        cout << "Podaj wiek: ";
        cin >> uczen.wiek;
        tb[i] = uczen;
        cin.ignore(1);
    }
}

void zapiszOsoby(osoba tb[], int ile) {
    ofstream plik;
    plik.open("osoby.txt");
    for (int i=0; i < ile; i++) {
        plik << tb[i].imie << " " << tb[i].nazwisko << " " << tb[i].wiek << "\n";
    }
    plik.close();
    cout << "Baza zapisana\n";
    
}

int main(int argc, char **argv)
{   
    int ile = 3;
    osoba tb[ile];
    getOsoby(tb, ile);
    drukujOsoby(tb, ile);
    zapiszOsoby(tb, ile);
    
    
	return 0;
}

