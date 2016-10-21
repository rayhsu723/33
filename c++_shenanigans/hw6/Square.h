#include "Shape.h"
#ifndef _SQUARE_H
#define _SQUARE_H

class Square : public Shape
{
protected:
	double length;
public:
	Square(string n, int cx, int cy, double newLength)
		: Shape(n, cx, cy), length(newLength){}
	virtual double area()
	{
		return (length*length);
	}
	virtual void draw()
	{
		cout << "* * * * *\n*       *\n*       *\n*       *\n* * * * *\n" << endl;
	}
};

#endif