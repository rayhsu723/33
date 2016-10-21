#include "Square.h"

class Rectangle : public Square
{
protected:
	double width;
public:
	Rectangle(string n, int cx, int cy, double newLength, double newWidth)
		: Square(n, cx, cy, newLength), width(newWidth){}
	virtual double area()
	{
		return (width*length);
	}
	virtual void draw()
	{
		cout << "* * * * * * * *\n*             *\n*             *\n* * * * * * * *\n" << endl;
	}
};
