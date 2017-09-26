/*
 * hello.cpp
 
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int bok = 0;
    
	//cout << "Witaj w C++!" << endl;
	cout << "Podaj bok kwadratu:";
    //cin >> imie;
    //cin.getline(imie, 10);
    cin >> bok;
    cout << "Obwód kwadratu: " << 4 * bok  << endl;
    cout << "Pole kwadratu: " << bok * bok  << endl;
    
	return 0;
}

