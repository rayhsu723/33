#include <iostream>
using namespace std;

class String
  {
  public:
    String( const char * s = "");
    String( const String & s );
    String operator = ( const String & s );
    char & operator [] ( int index );
    int size();
    String reverse();
    int indexOf( const char c );
    int indexOf( const String pattern );
    bool operator == ( const String s );
    bool operator != ( const String s );
    bool operator > ( const String s );
    bool operator < ( const String s );
    bool operator <= ( const String s );
    bool operator >= ( const String s );
    String operator + ( const String s );
    String operator += ( const String s );
    void print( ostream & out );
    void read( istream & in );
    ~String();
    static void final_report_on_allocations();
  private:
    bool inBounds( int i )
    {
      return i >= 0 && i < strlen(buf);
    }
    static int strlen(const char *src);
    static char *strcpy(char *dest, char *src);
    static int strcmp(const char *left, const char *right);
    static int strncmp(const char *left, const char *right, int n);
    static char *strdup(const char *src); 
    static const char * strchr(const char * str, int c);
    static char * strstr(char * haystack, char * needle);
    static char * strcat(char * dest, const char * src);
    static int allocations;
    static char * new_char_array(int n_bytes);
    static void delete_char_array(char * p);
    char * buf; 
  };


  ostream & operator << ( ostream & out, String str );
  istream & operator >> ( istream & in, String & str );