#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
using namespace std;

template
    <typename T>
class Array
{
    T* buf;
    int sz;
public:
    struct iterator
    {
        // Iterator traits
        typedef std::forward_iterator_tag iterator_category;
        typedef iterator self_type;
        typedef T value_type;
        typedef T& reference;
        typedef T* pointer;
        typedef ptrdiff_t difference_type;
    private:
        pointer ibuf;
    public:
        iterator(pointer ptr) : ibuf(ptr) { }
        self_type operator++() { ++ibuf; return *this; }
        self_type operator++(int postfix) { self_type cpy = *this; ibuf++; return cpy; }
        reference operator*() { return *ibuf; }
        pointer operator->() { return ibuf; }
        bool operator==(const self_type& rhs) const { return ibuf == rhs.ibuf; }
        bool operator!=(const self_type& rhs) const { return ibuf != rhs.ibuf; }
    };

    struct const_iterator
    {
        typedef std::forward_iterator_tag iterator_category;
        typedef const_iterator self_type;
        typedef T value_type;
        typedef T& reference;
        typedef T* pointer;
        typedef ptrdiff_t difference_type;
    private:
        pointer buf;
    public:
        const_iterator(pointer ptr) : buf(ptr) { }
        self_type operator++() { ++buf; return *this; }
        self_type operator++(int postfix) { self_type cpy = *this; buf++; return cpy; }
        const reference operator*() { return *buf; }
        const pointer operator->() { return buf; }
        bool operator==(const self_type& rhs) const { return buf == rhs.buf; }
        bool operator!=(const self_type& rhs) const { return buf != rhs.buf; }
    };

    Array(int size) : sz(size), buf(new T[sz]) { }
    Array(initializer_list<T> s): sz(s.size()), buf(new T[sz]) { uninitialized_copy(s.begin(), s.end(), buf);}
    int size() const { return sz; }
    T& operator[](int index) { return buf[index]; }
    const T& operator[](int index) const { return buf[index]; }
    iterator begin() { return iterator(buf); }
    iterator end() { return iterator(buf + sz); }
    const_iterator begin() const { return const_iterator(buf); }
    const_iterator end() const { return const_iterator(buf + sz); }
    ~Array() { delete[] buf; }
};


int main()
{
    Array<double> A { 2.1, 3.2, 4.3 };       // construct from an initializer_list<double>
    int count = 0; // to be captured by reference in lambda below...

    // using lambda with for_each()

    for_each ( A.begin(), A.end(), [&](double x){ count++; cout << x << “ “;}  ); // capturing “count”
    cout << “Looped “ << count << “ times.“ << endl;

    for_each ( A.begin(), A.end(), [](double & x) { x += 10; } );   // modifying elements

    for ( Array<double>::iterator i = A.begin(); i != A.end(); ++i ) // low level for loop 
        cout << *i << " ";
    cout << endl;

    for_each ( A.begin(), A.end(), [](double & x) { x += 10; } );   // modifying elements

    for ( auto i : A ) // using range-based loop
        cout << i << " ";
    cout << endl;

    vector<double> V;
    copy( A.begin(), A.end(), back_inserter(V) );  // copying objects from one container to another

    for_each ( V.begin(), V.end(), [](double & x) {x += 10;} ); // using for_each

    for ( vector<double>::iterator i = V.begin(); i != V.end(); ++i ) // low-level loop using iterator
        cout << *i << " ";
    cout << endl;
}