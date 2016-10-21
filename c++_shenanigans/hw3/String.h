#include <iostream>
#define MAXLEN 128
using namespace std;

class String
{
public:
	String(const char * s = "")
	{
		strcpy(buf, s);
	}

	String(const String & s)
	{
		strcpy(buf, s.buf);
	}

	String operator = (const String & s)
	{
		strcpy(buf, s.buf);
		return buf;
	}

	char & operator [] (int index)
	{
		return buf[index];
	}

	int size()
	{
		char *pointer = buf;
		return strlen(pointer);
	}

	String reverse()
	{
		int length = size();
		String s;
		for(int i = 0; length > 0; --length, ++i)
		{
			s.buf[i] = buf[length-1];
		}
		return s;

	}

	int indexOf(const char c)
	{
		const char *pointer;
		pointer = strchr(buf, c);
		return pointer - buf;
	}

	int indexOf(const String pattern)
	{
		
		String pat = pattern.buf;
		char *point = &pat[0];
		char *point1;
		point1 = strstr(buf, point);
		return point1 - buf;
	}

	bool operator == (const String s)
	{
		String s1 = s.buf;
		char *point = &s1[0];
		return strcmp(buf, point) == 0;
	}

	bool operator != (const String s)
	{
		String s1 = s.buf;
		char *point = &s1[0];
		return strcmp(buf, point) != 0;
	}

	bool operator > (const String s)
	{
		String s1 = s.buf;
		char *point = &s1[0];
		return strcmp(buf, point) > 0;
	}

	bool operator < (const String s)
	{
		String s1 = s.buf;
		char *point = &s1[0];
		return strcmp(buf, point) < 0;
	}

	bool operator <= (const String s)
	{
		String s1 = s.buf;
		char *point = &s1[0];
		return strcmp(buf, point) <= 0;
	}

	bool operator >= (const String s)
	{
		String s1 = s.buf;
		char *point = &s1[0];
		return strcmp(buf, point) >= 0;
	}

	String operator + (const String s)
	{
		String s1 = s.buf;
		char *point = &s1[0];
		return strcat(buf, point);
	}

	String operator += (const String s)
	{
		String s1 = s.buf;
		char *point = &s1[0];
		return strcat(buf, point);
	}

	void print(ostream & out)
	{
		out << buf;
	}

	void read(istream & in)
	{
		in >> buf;
	}

	~String()
	{
	}

private:
	char buf[MAXLEN];

	bool inBounds(int i)
	{
		return i >= 0 && i < strlen(buf);
	}

	static int strlen(const char *s)
	{
		int len = 0;
		for(int i = 0; s[i] != '\0'; ++i)
			++len;
		return len;
	}

	static char * strcpy(char *dest, const char *src)
	{
		int i;
		for(i = 0; src[i]; ++i)
			dest[i] = src[i];
		dest[i] = src[i];
		return dest;
	}

	static char * strcat(char *dest, const char *src)
	{
		strcpy(dest + strlen(dest), src);
		return dest;
	}

	static int strcmp(const char *left, const char *right)
	{
		int i;
		for(i = 0; left[i] == right[i]; ++i)
			if(left[i] == '\0')
				return 0;
		return left[i] - right[i];
	}

	static int strncmp(const char *left, const char *right, int n)
	{
		int i = 0;
		for(i = 0; left[i] == right[i] && i < n; ++i)
			if(left[i] == '\0')
				return 0;
		return left[i] - right[i];
	}

	static const char * strchr(const char *str, int c)
	{
		for(; *str != c; ++str)
			if(*str == 0)
				return nullptr;
		return str;
	}

	static char* strstr(char *haystack, char *needle)
	{
	  while (*haystack) 
	  {
		    char *start = haystack;
		    char *pattern = needle;
		    
		    while (*haystack && *pattern && *haystack == *pattern) 
			{
			      haystack++;
			      pattern++;
		    }
		    if (!*pattern)
		    	  return start;
		    	  
		    haystack = start + 1;
	  }
	  return nullptr;
	}
};
ostream & operator << (ostream & out, String str)
{
	str.print(out);
	return out;
}

istream & operator << (istream & in, String & str)
{
	str.read(in);
	return in;
}
