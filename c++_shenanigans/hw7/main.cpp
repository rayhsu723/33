#include "matrix.h"

template
	< typename T >

void fillMatrix(Matrix<T> & m)
{
	int i, j;
	for (i = 0; i < m.numRows(); i++)
		m[i][0] = T();
	for (j = 0; j < m.numCols(); j++)
		m[0][j] = T();
	for (i = 1; i < m.numRows(); i++)
		for (j = 1; j < m.numCols(); j++)
		{
			m[i][j] = T(i * j);
		}
}

class IndexOutOfBoundsException
{
public:
	IndexOutOfBoundsException(int r, int c) : rows(r), cols(c) {}
	int getRow()
	{
		return rows;
	}
	int getCol()
	{
		return cols;
	}
private:
	int rows, cols;
};

void test_int_matrix()
{
	Matrix<int> m(10,5);
	fillMatrix(m);
	cout << m;
	int r, c;
	try
	{
		cout << "Enter in a row: \n";
		cin >> r;
		cout << "Enter in a column: \n";
		cin >> c;

		if (c < 0 || r < 0 || r > m.numRows() || c > m.numCols())
			throw IndexOutOfBoundsException(r,c);

		cout << "Value at row " << r << ", column " << c << " is " << m[r][c] << endl;; 
	}
	catch(IndexOutOfBoundsException e)
	{
		cout << "Error: Index is out of bounds" << endl;
		cout << "End" << endl;
	}

}

void test_double_matrix()
{
	Matrix<double> m(8,10);
	fillMatrix(m);
	cout << m;

	int r, c;
	try
	{
		cout << "Enter in a row: \n";
		cin >> r;
		cout << "Enter in a column: \n";
		cin >> c;

		if (c < 0 || r < 0 || r > m.numRows() || c > m.numCols())
			throw IndexOutOfBoundsException(r,c);

		cout << "Value at row " << r << ", column " << c << " is " << m[r][c] << endl; 
	}
	catch(IndexOutOfBoundsException e)
	{
		cout << "Error: Index is out of bounds" << endl;
		cout << "End" << endl;
	}
}




int main()
{
	test_int_matrix();
	test_double_matrix();
}