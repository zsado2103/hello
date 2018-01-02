/*
 * sort_wst.cpp
 */


#include <iostream>

using namespace std;


void sort_wstaw(int t[], int n)
{
    int el= 0; 
    int k= 0;
    
    for(int i = 0; i < n; i++)
    {
        el = t[i];
        k = i - 1;
        
        while(k>=0 && (t[k] > el))
        {
            t[k+1] = t[k];
            k = k - 1;
        }
        t[k+1] = el;
    }
}


int main(int argc, char **argv)
{
	int ile = 8; // [4,3,7,0,2,3,1,9]
    int lista[ile];
    
    lista[0]= 4; 
    lista[1]= 3; 
    lista[2]= 7; 
    lista[3]= 0; 
    lista[4]= 2; 
    lista[5]= 3; 
    lista[6]= 1; 
    lista[7]= 9; 
    
  
	sort_wstaw(lista, ile);

	return 0;
}

