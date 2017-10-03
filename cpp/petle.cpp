/*
 * petle.cpp
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int i;
    
    for (i = 0; i < 101; i++)// i++ wartość zwiększona o 1 (inkrementacja), c-- wartość zmniejszona o 1(dekrementacja), inkrementacja o 2 i +=2
    {

        if (i % 10 == 0)//'!=' różne od
        {
            
        
            cout << i << endl;
            // cout << '*' << endl;
        }
    }
    return 0;
}

