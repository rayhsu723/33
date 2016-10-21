#include "String_LL.h"

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

void test_length()
{
	cout << "Testing length()\n" << endl;
	String s("hello");
	cout << s.length() << endl;
	String s1("potato");
	cout << s1.length() << "\n" << endl; 
}


void test_indexOf()
{
	cout << "Testing indexOf()\n" << endl;
	String s("hi there");
	cout << s.indexOf('i') << endl;
	cout << s.indexOf('t') << "\n" << endl;
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

void test_plus()
{
	cout << "Testing +\n" << endl;
	String s = "hello";
	String s1 = "whatup";
	String s2 = s+s1;
	String s3 = s1+s;
	cout << s2 << endl;
	cout << s3 << "\n" << endl;
}

void test_plus_equal()
{
	cout << "Testing +=\n" << endl;
	String s = "hello";
	String s1 = "whatup";
	String s2 = (s+=s1);
	String s3 = (s1+=s);
	cout << s2 << endl;
	cout << s3 << "\n" << endl;
}

void test_print()
{
	cout << "Testing print\n" << endl;
	String s = "hello";
	String s1 = "whatup";
	cout << s << endl;
	cout << s1 << "\n" << endl;
}

void test_read()
{
	cout << "Testing read" << endl;
	cout << "Enter in a string: ";
	String s;
	cin >> s;
	cout << s << endl;
}


int main()
{
	test_constructor_and_print();
	test_assignment();
	test_index();
	test_length();
	test_indexOf();
	test_equality();
	test_less_than();
	test_plus();
	test_plus_equal();
	test_print();
	test_read();
	return 0;
}