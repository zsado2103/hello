/*
 * funkcje.cpp
 */


#include <iostream>

using namespace std;

void dodaj(int a, int b) // void -nie zwraca wyniku; całość - deklaracja funkji
{
    cout << "Suma: " << a + b << endl;
}
int odejmij (int l1, int l2)
{
    return l1 - l2; //zwraca wynik. RETURN NIE WYSTĘPUJE Z VOID!
}
void mnoz(int x, int y)
{
    cout << "Iloczyn: " << x * y << endl;
}
int dziel (int c, int d)
{
    if(d == 0)
    {
        cout << "Nie dziel przez 0!" << endl;
        return 0;
    }
    return c / d;
}

int main(int argc, char **argv)
{
    int a,b;
    a = b = 0;
    
    cout << "Podaj 2 liczby: " << endl;
    cin >> a >> b;
    
    dodaj(a, b);  //wywołanie funkcji, używanie
    cout << "Różnica: " << odejmij(a, b) << endl;
    mnoz(a,b);
    cout << "Iloraz: " << dziel (a, b) << endl;
    
    
    return 0;
}

