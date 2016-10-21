#include "Shape.h"

class Picture
{
public:
	Picture()
		: head(nullptr) {}

	void add(Shape *sp)
	{
		head = new ShapeNode(sp, head);
	}

	double totalArea()
	{
		double total = 0.0;
		for (ShapeNode *p = head; p; p=p->next)
			total += p->info->area();
		return total;
	}

	void drawAll()
	{
		cout << "-------- DRAWING SHAPES --------" << endl;
		for (ShapeNode *p = head; p; p=p->next)
			p->info->draw();
		cout << "--------- DONE DRAWING ---------" << endl;
	}

	~Picture()
	{
		ShapeNode *temp;
		for (ShapeNode *p = head; p;)
		{
			temp = p;
			p = p->next;
			delete temp;
		}
	}

private:
	struct ShapeNode
	{
		Shape *info;
		ShapeNode *next;
		ShapeNode(Shape *newShape, ShapeNode *newNext)
			: info(newShape), next(newNext) {}
	};
	ShapeNode *head;
};