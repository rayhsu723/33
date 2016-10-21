#include <iostream>
#include <fstream>
#include <iterator>
#include <map>
#include <string>
#include <vector>
#include <set>
#include <functional>
#include <algorithm>
#include <cctype>
#include "test.cpp"
#include "map.cpp"

using namespace std;

int main()
{
	ifstream doc("sample_doc.txt");
	ifstream stopwords("stopwords.txt");
	ofstream out("frequency.txt");

	vector<string> stop;
	set<string> words;

	copy(istream_iterator<string>(stopwords), istream_iterator<string>(), back_inserter(stop));

	for_each(istream_iterator<string>(doc), istream_iterator<string>(), [&](string s)
	{
		transform(s.begin(), s.end(), s.begin(), :: tolower);

		int check = 0;
		for_each(begin(stop), end(stop), [&](string s1)
		{
			if (s == s1)
			{
				check = 1;
			}
		});

		if (check == 0)
		{
			words.insert(s);
		}

	});

	map<string, int> m;

	for_each(istream_iterator<string>(doc), istream_iterator<string>(), [&](string s)
	{
		transform(s.begin(), s.end(), s.begin(), :: tolower);

		int check = 0;
		for_each(words.begin(), words.end(), [&](string s1)
		{
			if (s1 == s)
			{
				check = 1;
			}
		});

		if (check == 1)
		{
			if (m[s])
				m[s]++;
			else
				m[s] = 1;
		}

	});

	for_each(m.begin(), m.end(), [&](pair<string, int> p)
	{
		cout << p.first << " : " << p.second << endl;
	});

	// SetList<string> words;
	// vector<string> stop;

	// copy(istream_iterator<string>(stopwords), istream_iterator<string>(), back_inserter(stop));

	// for_each(istream_iterator<string>(doc), istream_iterator<string>(), [&](string s)
	// {
	// 	transform(s.begin(), s.end(), s.begin(), :: tolower);
	// 	int check = 0;

	// 	for_each(begin(stop), end(stop), [&](string s1)
	// 	{
	// 		if (s == s1)
	// 		{
	// 			check = 1;
	// 		}
	// 	});

	// 	if (check == 0)
	// 	{
	// 		words.add(s);
	// 	}
	// });


	// int map_size = words.size();
	// MapArray<string> freq(map_size);

	// for_each(istream_iterator<string>(doc), istream_iterator<string>(), [&](string s)
	// {
	// 	transform(s.begin(), s.end(), s.begin(), ::tolower);

	// 	for_each(words.begin(), words.end(), [&](SetList<string>::Node N)
	// 	{
	// 		cout << N.info << ' ' << s << endl;
	// 		if (N.info == s)
	// 		{
	// 			cout << "here" << endl;
	// 			freq.add(s);
	// 		}
			
	// 	});

	// });

	// for_each(freq.begin(), freq.end(), [&](pair<string,int> p)
	// {
	// 	cout << p.first << " : " << p.second << endl;
	// });

}