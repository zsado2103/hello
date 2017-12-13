/*
 * fibonacci.cpp
 */


#include <iostream>
#include <math.h>
using namespace std;
int fib_iter(int n)
{
    int a = 0;
    int b = 1;
	if (n == 0)
	{	
		cout << 0;
		return 0;
	}
	cout << a;
    for(int i=2; i < n; i++)
    {
	cout << b << " ";
		b += a;
        a = b-a;
	}
}
int fib_rek(int n)
{
	if (n < 2)
		return 1;
	else
		return fib_rek((n - 2) + (n - 1));
	}

int main(int argc, char **argv)
{
	int n;
	cout << "Podaj liczbe " << endl;
	cin >> n;
    cout << fib_rek(n) << endl;
	return 0;
}
