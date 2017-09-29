/*
* kalkulator.cpp
*/


#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
    char znak; // +, -, *, /
    int a, b;
    a = b  = 0;
    cout << "Podaj dwie liczby" << endl ;
    cin >> a >> b;
    cout <<"Podaj znak " << endl ; 
    cin >> znak;
    
    if (znak == '+')
        cout << " a + b = " << a + b << endl;
    else if (znak == '-')
        cout << " a - b = " << a - b << endl;
    else if (znak == '*')
        cout << " a * b = " << a * b << endl;
        else if (znak == '/')
    cout << " a / b = " << a / b << endl;
    return 0;
}

