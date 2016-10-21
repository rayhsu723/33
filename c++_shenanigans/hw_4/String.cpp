#include "String.h"

String::String( const char * s )
{
	buf = strdup(s);
}

String::String( const String & s )
{
	buf = strdup(s.buf);
}

String String::operator = ( const String & s )
{
	delete[] buf;
	buf = strdup(s.buf);
	return buf;
}

char & String::operator [] ( int index )
{
	return buf[index];
}

int String::size()
{
	return strlen(buf);
}

String String::reverse()
{
	int length = size();
	String s;
	for(int i = 0; length > 0; --length, ++i)
		s.buf[i] = buf[length-1];
	return s;
}

int String::indexOf( const char c )
{
	const char *pointer;
	pointer = strchr(buf, c);
	return pointer - buf;
}

int String::indexOf( const String pattern )
{
	String pat = pattern.buf;
	char *point = &pat[0];
	char *point1;
	point1 = strstr(buf, point);
	return point1 - buf;
}

bool String::operator == ( const String s )
{
	return strcmp(buf, s.buf) == 0;
}

bool String::operator != ( const String s )
{
	return strcmp(buf, s.buf) != 0;
}

bool String::operator > ( const String s )
{
	return strcmp(buf, s.buf) > 0;
}

bool String::operator < ( const String s )
{
	return strcmp(buf, s.buf) < 0;
}

bool String::operator <= ( const String s )
{
	return strcmp(buf, s.buf) <= 0;
}

bool String::operator >= ( const String s )
{
	return strcmp(buf, s.buf) >= 0;
}

String String::operator + ( const String s )
{
	char *temp = strdup(buf);
	delete[] buf;
	buf = strcat(temp, s.buf);
	return buf;
}

String String::operator += ( const String s )
{
	char *temp = strdup(buf);
	delete[] buf;
	buf = strcat(temp, s.buf);
	return buf;
}

void String::print( ostream & out )
{
	out << buf;
}

void String::read( istream & in )
{
	in >> buf;
}

String::~String()
{
	delete[] buf;
}

int String::strlen( const char * src )
{
	int len = 0;
	for (int i = 0; src[i]; ++i)
		++len;
	return len;
}

char * String::strcpy( char *dest, char *src )
{
	int i = 0;
	for(i = 0; src[i]; ++i)
		dest[i] = src[i];
	dest[i] = src[i];
	return dest;
}

char * String::strdup( const char *src )
{
	int length = strlen(src);
	char * new_list = new char[length];
	int i = 0;
	for(i = 0; i < length ; ++i)
		new_list[i] = src[i];
	new_list[i] = src[i];
	return new_list;
}

const char * String::strchr( const char *str, int c )
{
	for(; *str != c; ++str)
		if(*str == 0)
			return nullptr;
	return str;
}

char * String::strstr( char * haystack, char * needle )
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

int String::strcmp( const char * left, const char * right )
{
	int i;
	for(i = 0; left[i] == right[i]; ++i)
		if(left[i] == '\0')
			return 0;
	return left[i] - right[i];
}

char * String::strcat(char * dest, const char * src)
{
	int new_length = strlen(dest) + strlen(src);
	char * new_list = new char[new_length];
	for(int i = 0; dest[i]; ++i)
		new_list[i] = dest[i];
	int dest_length1 = strlen(dest);
	for(int dest_length = strlen(dest); src[dest_length - dest_length1]; ++dest_length)
		new_list[dest_length] = src[dest_length - dest_length1];
	return new_list;
}

int String::allocations = 0;

char * String::new_char_array( int n_bytes )
{
	++allocations;
	return new char(n_bytes);
}

void String::delete_char_array( char * p )
{
	--allocations;
	if(allocations < 0)
		cout << "Error: more delete[] than new[]" << endl;
	delete[] p;
}

void String::final_report_on_allocations()
{
	if(allocations > 0)
		cout << "Memory leak in class String" << endl;
	if(allocations < 0)
		cout << "Too many delete[] in class String" << endl;
	if(allocations == 0)
		cout << "Allocations and deallocations match\n" << endl;
}

std::ostream & operator << ( ostream & out, String str )
{
    str.print(out);
    return out;
}

std::istream & operator >> ( istream & in, String & str )
{
	str.read(in);
	return in;
}