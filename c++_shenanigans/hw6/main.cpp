#include "Triangle.h"
#include "Circle.h"
#include "Square.h"
#include "Rectangle.h"
#include "Picture.h"
using namespace std;

int main()
{
	Picture p;

	p.add(new Triangle("firstTriangle",1,1,5.0,5.0));
	p.add(new Triangle("secondTriangle",1,1,4.0,3.0));

	p.add(new Circle("firstCircle",1,1,5));
	p.add(new Circle("secondCircle",1,1,10));

	p.add(new Square("firstSquare",1,1,5.0));
	p.add(new Square("secondCircle",1,1,10));

	p.add(new Rectangle("firstRectangle",1,1,4.0,8.0));
	p.add(new Rectangle("secondRectangle",1,1,8.0,4.0));

	p.drawAll();
	cout << "Total Area: " << p.totalArea() << endl;

}