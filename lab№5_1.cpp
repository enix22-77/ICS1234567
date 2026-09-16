#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    double x, y;
   cout << "x = ";
   cin >> x;
    if (x > 1)
 {
    y = log10(abs(x + 1)) + 2.9 * exp(0.1 * x);
 }
  else if (x > -1.1)
     {
        y = sqrt(abs(x)) + cbrt(x) - sin(x);
    }
    else
    {
         y = 4 * x + exp(x) - 4 * sqrt(abs(x));
    }
    cout << "y = " << y;
     return 0;
}   
 
