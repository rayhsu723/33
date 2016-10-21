#include "Shape.h"
#include <cmath>

class Circle : public Shape
{
protected:
	int radius;
public:
	Circle(string n, int cx, int cy, int newRadius)
		: Shape(n, cx, cy), radius(newRadius){}
	virtual double area()
	{
		return (radius*radius*M_PI);
	}
	virtual void draw()
	{
		cout << "  * * * *\n *       *\n*         *\n*         *\n *       *\n  * * * *\n" << endl;
	}

};


   