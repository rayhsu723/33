#include <iostream>
using namespace std;
double convert( int knot )
{
	return knot*6076.0/5280.0/60.0;
}

int main()
{
	int knot;
	cout << "Enter the number of knots to convert: ";
	cin >> knot;
	cout << convert(knot) << endl;
	return 0;
}