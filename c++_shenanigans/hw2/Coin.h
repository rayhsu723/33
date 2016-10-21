#include <iostream>
#include <cstdlib>
using namespace std;

const int CENTS_PER_QUARTER = 25, CENTS_PER_DIME = 10, CENTS_PER_NICKEL = 5;
class Coins
{
private:
	int quarters, dimes, nickels, pennies;
public:
	Coins( int q, int d, int n, int p )
		: quarters(q), dimes(d), nickels(n), pennies(p)
	{
		if( q < 0 || d < 0 || n < 0 || p < 0 )
		{
			cout << "Coins must be integer greater than equal to 0" << endl;
			exit(1);
		}
	}
	void deposit( Coins & c )
	{
		quarters += c.quarters;
		dimes += c.dimes;
		nickels += c.nickels;
		pennies += c.pennies;
	}
	int total()
	{
		return quarters*CENTS_PER_QUARTER + dimes*CENTS_PER_DIME + nickels*CENTS_PER_NICKEL + pennies;
	}
	bool hasSufficientAmount( int amount )
	{
		return total() >= amount;
	}
	Coins extractChange( int amount )
	{
		int cost = amount;
		if( hasSufficientAmount(amount) )
		{
			Coins item(0,0,0,0);
			while( cost > 0 )
			{
				if( quarters == 0 || cost > 24 )
				{
					quarters--;
					item.quarters++;
					cost -= CENTS_PER_QUARTER;
				}
				else if( dimes == 0 || cost > 9 )
				{
					dimes--;
					item.dimes++;
					cost -= CENTS_PER_DIME;
				}
				else if( nickels == 0 || cost > 4 )
				{
					nickels--;
					item.nickels++;
					cost -= CENTS_PER_NICKEL;
				}
				else if( pennies != 0 )
				{
					pennies--;
					item.pennies++;
					cost -= 1;
				}
			}
			return item;
		}
		else
		{
			cout << "Not enough coins" << endl;
			exit(1);
		}
	}
	void print( ostream & out )
	{
		out << quarters << " quarter(s), " << dimes << " dime(s), "
		<< nickels << " nickel(s), and " << pennies << " penny/pennies";
	}
};
ostream & operator << ( ostream & out, Coins & c )
{
	c.print(out);
	return out;
}
