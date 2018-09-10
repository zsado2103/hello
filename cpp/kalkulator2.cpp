/*
 * kalkulator2.cpp
 * 
 * 
 */


#include <iostream>
using namespace std;

float dodaj(float a, float b) 
{
   return a + b;
}
float odejmij (float a, float b)
{
    return a - b; 
}
float mnoz(float a, float b)
{
    return a * b;
    }
float dziel (float a, float b)
{
    if(b == 0)
    {
        cout << "Nie dziel przez 0!" << endl;
        return 0;
    }
    return a / b;
}

int main(int argc, char **argv)
{
    char znak;
    int a, b;
    a = b  = 0;
    cout << "Podaj dwie liczby" << endl ;
    cin >> a >> b;
    cout <<"Podaj znak " << endl ; 
    cin >> znak;
    
    
	
        if (znak == '+')
        cout << "  " << dodaj(a , b) << endl;
    else if (znak == '-')
        cout << " " << odejmij (a, b) << endl;
    else if (znak == '*')
        cout << " " << mnoz(a,b)<< endl;
        else if (znak == '/')
    cout << "  " << dziel(a,b) << endl;
	return 0;
}

