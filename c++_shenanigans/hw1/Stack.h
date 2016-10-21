#include <iostream>
using namespace std;
#define STACK_CAPACITY 1000

class Stack
{
private:
	int count;
	char stuff[STACK_CAPACITY];
public:
	Stack()
	{
		count = 0;
	}
	void push( char c ) // adds c to top of stack
	{
		if(isFull())
			cout << "ERROR: push() called on full stack";
		else
		{
			stuff[count] = c;
			count++;
		}
	}
	char pop() // removes top element
	{
		if(isEmpty())
		{
			cout << "ERROR: pop() called on empty stack";
			return ' ';
		}
		else
		{
			return stuff[--count];
		}

	}
	char top() // returns top element
	{
		if(isEmpty())
		{
			cout << "ERROR: top() called on empty stack";
			return ' ';
		}
		else
			return stuff[count - 1];
	}
	bool isEmpty() // returns True iff stack is empty
	{
		return count == 0;
	}
	bool isFull() // returns True iff stack is full
	{
		return count == STACK_CAPACITY;
	}
	~Stack() // destructor for a stack
	{

	}
	// void getCount()
	// {
	// 	cout << count;
	// }
	// char getValue( int c )
	// {
	// 	return stuff[c];
	// }
};