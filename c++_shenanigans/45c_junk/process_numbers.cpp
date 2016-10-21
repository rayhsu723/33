#include <fstream>
#include <iterator>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	ifstream in("rand_numbers.txt");
	ofstream odd_txt("odd.txt");
	ofstream even_txt("even.txt");

	vector<int> rand_num;
	vector<int> even_num;
	vector<int> odd_num;

	copy(istream_iterator<int>(in), istream_iterator<int>(), back_inserter(rand_num));

	sort(rand_num.begin(), rand_num.end());

	for_each(begin(rand_num), end(rand_num), [&](int i)
	{
		if (i%2 == 0)
			even_txt << i << endl;
		else
			odd_txt << i << endl;
	});


}