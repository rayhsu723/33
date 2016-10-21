#include <iostream>
#include <string>
#include <algorithm>
#include <fstream>
#ifndef _SETLIST_H
#define _SETLIST_H

using namespace std;

template
< typename T >

class SetList
{

public:
	struct Node
	{
		T info;
		Node * next;
		Node(T newInfo, Node * newNext) : info(newInfo), next(newNext) {}

		static int length(Node * L)
		{
			int size = 0;
			for(; L; L = L->next)
				++size;
			return size;
		}
	};

	Node * head;
	struct iterator
	{
		typedef forward_iterator_tag iterator_category;
		typedef iterator self_type;
		typedef Node value_type;
		typedef Node& reference;
		typedef Node* pointer;
		typedef ptrdiff_t difference_type;

	private:
		pointer ibuf;
	public:
		iterator(pointer ptr) : ibuf(ptr) {}

		self_type operator++ ()
		{
			ibuf = ibuf->next;
			return *this;
		}

		self_type operator++ (int postfix)
		{
			self_type cpy = *this;
			ibuf = ibuf->next;
			return cpy;
		}

		reference operator* ()
		{
			return *ibuf;
		}

		pointer operator-> ()
		{
			return ibuf;
		}

		bool operator== (const self_type & rhs) const
		{
			return ibuf == rhs.ibuf;
		}

		bool operator!= (const self_type & rhs) const
		{
			return ibuf != rhs.ibuf;
		}
	};

	SetList() : head(nullptr) {}

	void add(T newT)
	{
		int temp = 0; // if temp is 1, do not add into list;
		for (Node * p = head; p != nullptr; p = p->next)
		{
			if (p->info == newT)
			{
				temp = 1;
			}
		}
		if (temp == 0)
			head = new Node(newT, head);
	}

	int size()
	{
		int count = 0;
		for (Node * p = head; p != nullptr; p = p->next)
		{
			++count;
		}
		return count;
	}

	iterator begin()
	{
		return iterator(head);
	}

	iterator end()
	{
		// int size = Node::length(head);
		// Node * temp = head;
		// for (int i = 0; i < size; ++i)
		// 	temp = temp->next;
		// return iterator(temp);
		while (head)
		{
			head = head->next;
		}
		return iterator(head);
	}

	~SetList()
	{
		Node * temp;
		for (Node * p = head; p != nullptr; )
		{
			temp = p;
			p = p->next;
			delete temp;
		}
	}


};

#endif

// int main()
// {
// 	SetArray<int> s;
// 	s.add(1);
// 	s.add(2);
// 	// for(SetArray<int>::iterator i = s.begin(); i != s.end(); i++)
// 	// {
// 	// 	cout << i->info << endl;
// 	// }

// 	cout << s.size() << endl;
// 	// for_each(s.begin(), s.end(), [&](SetArray<int>::Node N)
// 	// {
// 	// 	cout << N.info << endl;
// 	// });
// }