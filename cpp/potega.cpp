/*
 * potega.cpp
 */


#include <iostream>
#include <math.h>

using namespace std;
int potega_rek(int podstawa, int wykladnik)
    {
		if (wykladnik == 0) 
        return 1;
		else
		return potega_rek(podstawa, wykladnik - 1) * podstawa;
	}


int main(int argc, char **argv)
{
	int podstawa = 0;
	int wykladnik = 0;
	int wynik = 1;
	
	cout << "Podaj podstawe : " ;
	cin >> podstawa;
	cout <<"Podaj wykladnik: " ;
	cin >> wykladnik;
	
	for (int i = 0; i < wykladnik; i++)
		wynik*=podstawa;
	if(wykladnik == 0)
		cout << "1" << endl;
	else 
		cout << wynik << endl;
	return 0;
	

}

