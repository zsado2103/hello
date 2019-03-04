/*
 * struktury.cpp
 */


#include <iostream>
#include <fstream>
using namespace std;

struct punkt {
    int x;
    int y;
};

struct wektor {
    punkt pp;
    punkt pk;
};
punkt wylicz_srodek(wektor w) {
    punkt ps;
    ps.x = (w.pp.x + w.pk.x)/2;
    ps.y = (w.pk.y + w.pk.y)/2;
    
    return ps;
}

wektor getWektor() {
    
        wektor w1;
        cout << "Podaj współrzędne początkowego punktu: ";
        cin >> w1.pp.x;
        cin >> w1.pp.y;
        cout << "Podaj współrzędne końcowego punktu ";
        cin >> w1.pk.x;
        cin >> w1.pk.y;
        
        return w1;
      
       
}

int main(int argc, char **argv)
{   
    wektor w;
    w = getWektor();
    cout << w.pp.x << " " << w.pp.y << endl;
    cout << w.pk.x << " " << w.pk.y << endl;
    
    punkt ps;
    ps = wylicz_srodek(w);
    cout << "Współrzędne środka wektora: " << ps.x << " " << ps.y << endl; 
    
    
    
    
	return 0;
}

