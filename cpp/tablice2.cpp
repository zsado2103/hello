/*
 * tablice2.cpp
 */


#include <iostream>

using namespace std;

void pobierzDane(int tab[], int ile){ // []- adres pierwszorzędny
    int i;
    cout << "Podaj " << ile << "liczb : " << endl;
    for(i = 0; i < ile; i++) {
        cin >> tab[i];
    }
    }
    int sumuj(int tab[], int ile){
        int i;
        int suma = 0;
        cout << "Podane liczby : " << endl;
    for (i = 0; i < ile; i++) {
        suma  += tab[i];
        cout << tab[i] << " " << endl;
    }
    return suma;
    }
    
    float liczSrednia (int tab[], int ile) {
        return sumuj (tab, ile)/float(ile);
        }
    
int main(int argc, char **argv)
{
    //const int ROZMIAR = 5; //wartości zmiennej nie mozna ruszyc,ani zmienic
	int rozmiar =0;
    cout << "Ile ocen: " << endl;
    cin >> rozmiar;
    
    int liczby[rozmiar];
    
    
    
    pobierzDane(liczby, rozmiar);
    
       //cout << "Podane oceny: " << endl;
    //for (i = 0; i < rozmiar; i++) {
       // suma  += liczby [i];
        //cout << liczby [i] << " " << endl;
    //}
    cout << "Suma ocen: " << sumuj(liczby, rozmiar) << endl;
    cout << "Średnia : " << liczSrednia(liczby,rozmiar) << endl;
    
    
    return 0;
}

