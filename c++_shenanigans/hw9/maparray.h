#include <iostream>
#include <map>
#include <string>
#include <algorithm>
#ifndef _MAPARRAY_H
#define _MAPARRAY_H

using namespace std;

template
< typename K  >

class MapArray
{
private:
	pair<K,int> * buf;
	int arraySize;
	int curSize;

public:
	struct iterator
	{
		typedef forward_iterator_tag iterator_category;
		typedef iterator self_type;
		typedef pair<K,int> value_type;
		typedef pair<K,int>& reference;
		typedef pair<K,int>* pointer;
		typedef ptrdiff_t difference_type;
	private:
		pointer ibuf;
	public:
		iterator(pointer ptr) : ibuf(ptr) {}

		self_type operator++ ()
		{
			++ibuf;
			return *this;
		}

		self_type operator++ (int postfix)
		{
			self_type cpy = *this;
			ibuf++;
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

		bool operator== (const self_type rhs) const
		{
			return ibuf == rhs.ibuf;
		}

		bool operator!= (const self_type rhs) const
		{
			return ibuf != rhs.ibuf;
		}
	};




	MapArray(int newSize) : buf(new pair<K,int>[newSize]), arraySize(newSize), curSize(0) {}

	void add(K data)
	{
		if (curSize == 0)
		{
			buf[0] = make_pair(data, 1);
			++curSize;
		}

		else
		{
			int check = 0; // if check == 0, add into buf
			for(int i=0; i < curSize; ++i)
			{
				if (buf[i].first == data)
				{
					buf[i].second++;
					check = 1;
					break;
				}
			}
			if (check == 0)
			{
				buf[curSize] = make_pair(data, 1);
				++curSize;
			}		
		}
	}


	iterator begin()
	{
		return iterator(buf);
	}

	iterator end()
	{
		return iterator(buf + 200);
	}

	~MapArray()
	{
		delete[] buf;
	}




};

#endif