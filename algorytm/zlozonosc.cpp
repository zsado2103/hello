/*
 * zlozonosc.cpp
 */


#include <iostream>
using namespace std;
int main(int argc, char **argv)
{
	int n = 0;
    cout << "Podaj n: " << endl;
    cin >> n;
    
    int i = 1;
    while (i < n){
        i += 2;
        cout << i << endl;
    }
	
	return 0;
}

