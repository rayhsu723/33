#include <iostream>
using namespace std;
#include "Coin.h"

int main()
{
	// Create two Coins objects
	Coins pocket( 5, 3, 6, 8 );
	Coins piggyBank( 50, 50, 50, 50 );

	// Buy a bag of chips for 68 cents from coins in pocket. Display how much left
	Coins payForChips = pocket.extractChange(68);
	cout << "I bought a bag of chips for " << 68 << " cents using " << payForChips << endl;
	cout << "I have " << pocket << " left in my pocket" << endl;

	//Transfer a bunch of coins from your piggy bank to your pokcet and display how much in both
	Coins transfer = piggyBank.extractChange(139);
	pocket.deposit(transfer);
	cout << "I transferred " << transfer << " from my piggy bank to my pocket" << endl;
	cout << "I currently have " << pocket << " in my pocket and " << piggyBank << "in my piggy bank" << endl;

	// Found loose change while vaccuming sofa. Put that change in your piggy bank
	Coins looseChange( 2, 3, 4, 5 );
	piggyBank.deposit(looseChange);
	cout << "I found " << looseChange << " while vacuuming my sofa, and I put it in my piggy bank" << endl;
	cout << "I now have " << piggyBank << " in my piggy bank" << endl;

	return 0;
}