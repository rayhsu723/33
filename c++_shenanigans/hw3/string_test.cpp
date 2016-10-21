#include "String.h"

void test_constructor_and_print()
{
	cout << "Testing constructor and print\n" << endl;
	String s("hello world");
	cout << s << endl;
	String s1 = "I am the best";
	cout << s1 << "\n" << endl;

}

void test_assignment()
{
	cout << "Testing  =\n" << endl;
	String s("hello");
	String s1("hi");
	String s2 = ("whatup");
	s = s1;
	cout << s << endl;
	s1 = s2;
	cout << s1 << "\n" << endl;
}

void test_index()
{
	cout << "Testing [] \n" << endl;
	String s("hello");
	cout << s[0] << ' ' << s[3] << "\n" << endl;
}

void test_size()
{
	cout << "Testing size()\n" << endl;
	String s("hello");
	cout << s.size() << endl;
	String s1("potato");
	cout << s1.size() << "\n" << endl; 
}

void test_reverse()
{
	cout << "Testing reverse()\n" << endl;
	String x("I am the best");
	cout << x.reverse() << endl;
	String s1("c++ is so fun");
	cout << s1.reverse() << endl;
}

void test_indexOf()
{
	cout << "Testing indexOf()\n" << endl;
	String s("Raymond Hsu is the best c++ coder in the world");
	cout << s.indexOf('i') << endl;
	cout << s.indexOf("best") << "\n" << endl;
}

void test_equality()
{
	cout << "Testing ==\n" << endl;
	String s = "hello";
	String s1 = "hello";
	String s2 = "sup";
	int tf = (s==s1);
	int tf1 = (s==s2);
	cout << tf << endl;
	cout << tf1 << "\n" << endl;
}

void test_not_equal()
{
	cout << "Testing !=\n" << endl;
	String s = "hello";
	String s1 = "hello";
	String s2 = "sup";
	int tf = (s!=s1);
	int tf1 = (s1!=s2);
	cout << tf << endl;
	cout << tf1 << "\n" << endl;
}

void test_greater_than()
{
	cout << "Testing >\n" << endl;
	String s = "hello";
	String s1 = "hallo";
	String s2 = "aloha";
	int tf = (s>s1);
	int tf1 = (s>s2);
	cout << tf << endl;
	cout << tf1 << "\n" << endl;
}

void test_less_than()
{
	cout << "Testing <\n" << endl;
	String s = "hello";
	String s1 = "hallo";
	String s2 = "aloha";
	int tf = (s<s1);
	int tf1 = (s<s2);
	cout << tf << endl;
	cout << tf1 << "\n" << endl;
}

void test_less_than_equal()
{
	cout << "Testing <=\n" << endl;
	String s = "hello";
	String s1 = "hallo";
	String s2 = "aloha";
	int tf = (s<=s1);
	int tf1 = (s<=s2);
	cout << tf << endl;
	cout << tf1 << "\n" << endl;
}

void test_greater_than_equal()
{
	cout << "Testing >=\n" << endl;
	String s = "hello";
	String s1 = "hallo";
	String s2 = "aloha";
	int tf = (s>=s1);
	int tf1 = (s1>=s2);
	cout << tf << endl;
	cout << tf1 << "\n" << endl;
}

int main()
{
	test_constructor_and_print();
	test_assignment();
	test_index();
	test_size();
	test_reverse();
	test_indexOf();
	test_equality();
	test_not_equal();
	test_greater_than();
	test_less_than();
	test_less_than_equal();
	test_greater_than_equal();
	return 0;
}