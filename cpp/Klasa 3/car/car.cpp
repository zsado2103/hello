/*
 * car.cpp
 */
#include <iostream>
#include <cstdlib>
#include "car.h"
#include <string>

using namespace std;

car::Car(){
    marka=model=""; //"" - obiekt typu string
    rocznik=przebieg=0;
}
car::Car(string mr, string ml, int r, int p){
    if (r <= 1900) r = 1990;
    marka=mr;
    model = ml;
    rocznik = r;
    przebieg = p;
}

Car::dodaj() {
    cout << "Dodaj samochód " << endl;
    cout << "Marka: " ; cin >> marka;
    cout << "Model: " ; cin >> model;
    cout << "Rocznik: " ; cin >> rocznik;
    cout << "Przebieg: " ; cin >> przebieg;
}

Car::dane() {
    cout << "\nTwoje piękne auto: " << endl;
    cout << "Marka: " << marka << endl;
    cout << "Model: " << model << endl;
    cout << "Rocznik: " << rocznik << endl;
    cout << "Przebieg: "<< przebieg << endl;
}

