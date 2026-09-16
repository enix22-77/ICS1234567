#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    double xA, yA;
    double xB, yB;
    double xC, yC;
    cout << "Enter A: ";
    cin >> xA >> yA;
    cout << "Enter B: ";
    cin >> xB >> yB;
    cout << "Enter C: ";
    cin >> xC >> yC;
    double A = sqrt(xA * xA + yA * yA);
    double B = sqrt(xB * xB + yB * yB);
    double C = sqrt(xC * xC + yC * yC);
    if (A < B && A < C)
    {
        cout << "Nearest point: A";
    }
    else if (B < A && B < C)
    {
        cout << "Nearest point: B";
    }
    else
    {
        cout << "Nearest point: C";
    }
    return 0;
}