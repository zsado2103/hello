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
			cout << wynik << endl;
		}	
		return wynik;
	}
int silnia_rek(int n)
{
    if (n < 2)
        return 1;
    else
        return silnia_rek(n- 1) * n;
}

int main(int argc, char **argv)
{
	int n = 1;
	cout << "Podaj liczbe " << endl;
	cin >> n ;
	cout << "Silnia wynosi: " << silnia(int(n)) << endl;
	return 0;
}

