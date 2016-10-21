#include "Coin.h"
const int CENTS_FOR_CANDYBAR = 482;

int main()
{
	Coins pocket( 100, 10, 10, 100 );
	cout << "I started with " << pocket << " in my pocket." << endl;
	Coins payForCandy = pocket.extractChange( CENTS_FOR_CANDYBAR );
	cout << "I bought a candybar for " << CENTS_FOR_CANDYBAR << " cents using "
	<< payForCandy << endl;
	cout << "I have " << pocket << " left in my pocket." << endl;
	return 0;
}