/*
 * silnia.cpp
 */


#include <iostream>
using namespace std;

int silnia(int(n))
	{
		int wynik = 1;
		for (int i = 2; i<=n ; i++)
		{
			wynik = wynik * i;	
		}	
		return wynik;
	}

int main(int argc, char **argv)
{
	int n = 1;
	cout << "Podaj liczbe " << endl;
	cin >> n ;
	cout << "Silnia wynosi: " << silnia(int(n)) << endl;
	return 0;
}

