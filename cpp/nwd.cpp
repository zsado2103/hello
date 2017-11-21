/*
 * 
 */


#include <iostream>
using namespace std;

int nwd(int a,int b)
{
    while (a!=b) 
    {
        if (a > b)
            a = a - b;
        else 
            b = b - a;
    }
    return a;
}           
 
int main(int argc, char **argv)
{
	int a,b;
    cout << "Podaj liczbe" << endl;
    cin >> a;
    cout << "Podaj liczbe" << endl;
    cin >> b;
    cout <<"Najwiekszy wspólny dzielnik: "<< nwd(a,b) <<endl;
	return 0;
}
