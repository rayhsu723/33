#include <iostream>
#include <string>
#include "Stack.h"

int main()
{
	string message;
	Stack stack1;
	cout << "Type your message: ";
	getline(cin, message);

	for(int i = 0; i < message.length(); ++i)
		stack1.push(message[i]);
	
	while(!stack1.isEmpty())
		cout << stack1.pop() << endl;

	return 0;
}