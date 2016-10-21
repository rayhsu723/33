#include <iostream>

using namespace std;


int main()
{
	int a[4];
	int *p = a;
	a[0] = 1;
	*p = 10;

	cout << a[0] << endl;

	return 0;
}