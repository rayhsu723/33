#include "String_LL.h"

String::String(const char * s) : head(ListNode::stringToList(s)) {}

String::String(const String & s) : head(ListNode::copy(s.head)) {}

String String::operator = (const String & s)
{
	ListNode::deleteList(head);
	head = ListNode::copy(s.head);
	return String(s);
}

char & String::operator [] (const int index)
{
	ListNode * temp = head;
	if (!inBounds(index))
	{
		return temp->info;
	}

	else
		for (int count = 0; count < index; ++count)
		{
			temp = head->next;
		}
		return temp->info;
}

int String::indexOf(char c) const
{
	int count = 0;
	int size = length();
	for(ListNode * L = head; count < size; ++count, L = L->next)
		if (L->info == c)
			return count;
	return -1;
}

bool String::operator == (const String & s) const
{
	return ListNode::equal(head, s.head);
}

bool String::operator < (const String & s) const
{
	return ListNode::compare(head, s.head) < 0;
}

String String::operator + (const String & s) const
{
	String L;
	L.head = ListNode::concat(head, s.head);
	return L;
}

String String::operator += (const String & s)
{
	String L;
	L.head = ListNode::concat(head, s.head);
	return L;
}

String::~String()
{
	ListNode * temp;
	for (ListNode * p = head; p != nullptr;)
	{
		temp = p;
		p = p->next;
		delete temp;
	}
}

String::ListNode * String::ListNode::stringToList(const char * s)
{
	char temp = *s;
	return *s == '\0' ? nullptr : new ListNode(temp, stringToList(++s));
}

String::ListNode * String::ListNode::copy(ListNode * L)
{
	return !L ? nullptr : new ListNode(L->info, copy(L->next));
}

bool String::ListNode::equal(ListNode * L1, ListNode * L2)
{
	for (; L1 && L2; L1 = L1->next, L2 = L2->next)
		if (L1 != L2)
			return false;
	return L1 == nullptr && L2 == nullptr;
}

String::ListNode * String::ListNode::concat(ListNode * L1, ListNode * L2)
{
	return !L1 ? copy(L2) : new ListNode(L1->info, concat(L1->next, L2));
}

int String::ListNode::compare(ListNode * L1, ListNode * L2)
{
	for (; L1 == L2; L1 = L1->next, L2 = L2->next)
		if (!L1)
			return 0;
	return L1 - L2;
}

void String::ListNode::deleteList(ListNode * L)
{
	if (L)
	{
		deleteList(L->next);
		delete L;
	}
}

int String::ListNode::length(ListNode * L)
{
	int size = 0;
	for(; L; L = L->next)
		++size;
	return size;
}

void String::read(istream & in)
{
	char buffer[256];
	in >> buffer;
	head = ListNode::stringToList(buffer);

}

void String::print(ostream & out)
{
	for (ListNode * p = head; p != nullptr; p = p->next)
		out << p->info;
}

std::ostream & operator << (ostream & out, String str)
{
	str.print(out);
	return out;
}

std::istream & operator >> (istream & in, String & str)
{
	str.read(in);
	return in;
}