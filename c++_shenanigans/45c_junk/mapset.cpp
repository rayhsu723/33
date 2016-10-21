#include <iostream>
#include <fstream>
#include <iterator>
#include <map>
#include <string>
#include <vector>
#include <functional>
#include <algorithm>
#include <cctype>
#include "maparray.h"
#include "setlist.h"


using namespace std;

int main()
{
	map<string,int> freq;
	vector<string> V;
	vector<string> stop;

	ifstream in("sample_doc.txt");
	ifstream stop_in("stopwords.txt");
	ofstream out("frequency.txt");

	copy(istream_iterator<string>(in), istream_iterator<string>(), back_inserter(V));
	copy(istream_iterator<string>(stop_in), istream_iterator<string>(), back_inserter(stop));

	for_each(begin(V), end(V), [&](string s) 
		{
			transform(s.begin(), s.end(), s.begin(), :: tolower);
			freq[s] ? freq[s]++ : freq[s] = 1;
		});

	for_each(begin(stop), end(stop), [&](string s)
		{
			if (freq.find(s) != freq.end())
				freq.erase(freq.find(s));
		});

	for_each(freq.begin(), freq.end(), [&](pair<string,int> p)
		{
			out<< p.first << " : " << p.second << endl;
		});

	return 0;
}