#include <iostream>
#include <string>
#ifndef _SHAPE_H
#define _SHAPE_H

using namespace std;

class Shape
{
protected:
	string name;
	int centerX;
	int centerY;
public:
	Shape(string n, int cx, int cy)
		: name(n), centerX(cx), centerY(cy){}
	virtual double area() = 0;
	virtual void draw() = 0;
	virtual ~Shape() {}
};

#endif