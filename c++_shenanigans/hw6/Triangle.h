#include "Shape.h"

class Triangle : public Shape
{
protected:
	double base, height;
public:
	Triangle(string n, int cx, int cy, double newBase, double newHeight)
		: Shape(n, cx, cy), base(newBase), height(newHeight){}

	virtual double area()
	{
		return ((1.0/2.0)*base*height);
	}

	virtual void draw()
	{
		cout << "    *\n   * *\n  *   *\n *     *\n* * * * *\n" << endl;
	}
};