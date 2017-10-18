/*
 * petle_dwucyfrowe.cpp
 * program wypisuje wszystkie liczby parzyste podziele przez 3 w zakresie <m,n> podanym przez użytkownika.
 */


#include <iostream>

using namespace std;
int main(int argc, char **argv)
{
	int m, n;
   
cout <<"Podaj przedział <m, n> <10,99> :  " << endl;
cin >> m >> n;

    while (m > n || n < 10 || n > 99 || m <10 || m > 99)
    {
    cout <<"Podaj przedział <m, n> <10,99> :  " << endl;
    cin >> m >> n;
    }
    while (m <= n)
    {
    if (m % 3 == 0)
    {
    cout << m << endl;
    }
    else if ((m+1)% 3 == 0)
    {
    cout << m+1 << endl;
    }
    else if ((m+2) % 3 == 0)
    {
    cout << m+2 << endl;
    }
    
    m += 3;
    }
			
		 

			
		 

   

	return 0;
}

