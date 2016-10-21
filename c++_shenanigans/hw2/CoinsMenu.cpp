#include "Coin.h"
#include <iomanip>

void presentMenu()
{
	cout << "----------------------------------------------\n"
		 << "           PIGGY BANK MENU                   -\n"
		 << "-   OPTION                          ENTER    -\n"
		 << "-   Show Balane (in $)              B or b   -\n"
		 << "-   Show Coins in the Bank          C or c   -\n"
		 << "-   Deposit Coins                   D or d   -\n"
		 << "-   Get Coins for Purchase          P or p   -\n"
		 << "-                                            -\n"
		 << "-   Quit                            Q or q   -\n"
		 << "----------------------------------------------\n";
}

char getChoice()
{
	char ch;
	cout << "Enter in a command (followed by enter): ";
	cin >> ch;
	return ch;
}

void evaluateCommand( Coins & piggyBank, char choice )
{
	switch(choice)
	{
		case 'B': case 'b':
			cout << "Balance is $" << setprecision(2) << piggyBank.total()/100.0 << endl;
			break;
		case 'C': case 'c':
			cout << piggyBank << endl;
			break;
		case 'D': case 'd':
		{
			int q, d, n, p;
			cout << "How many quarters?: ";
			cin >> q;
			cout << "How many dimes?: ";
			cin >> d;
			cout << "How many nickels?: ";
			cin >> n;
			cout << "How many pennies?: ";
			cin >> p;
			Coins depositThis(q,d,n,p);
			piggyBank.deposit(depositThis);
			break;
		}
		case 'P': case 'p':
			int cost;
			cout << "How much do you need? (in cents): ";
			cin >> cost;
			piggyBank.extractChange(cost);
			break;
		case 'Q': case 'q':
			cout << "Dont with Piggy Bank\n\n";
			exit(0);
		default:
			cout << "Invalid command " << choice << endl;
			break;
	}
}

int main()
{
	Coins piggyBank(0,0,0,0);
	while( true )
	{
		presentMenu();
		char command = getChoice();
		evaluateCommand( piggyBank, command );
	}
}
// void presentMenu()
// {
// 	cout << "* * * * * * * * * * * * * * * * * * * * * * * *\n"
//     << "   *		 PIGGY BANK MENU					 *\n"
//     << "   *								  			 *\n"
//     << "   * OPTION						    ENTER		 *\n"
//     << "   *											 *\n"
//     << "   *   Show Balance (in $)			B or b		 *\n"
//     << "   *   Show Coins in the Bank		C or c		 *\n"
//     << "   *   Deposit Coins				D or d		 *\n"
//     << "   *   Get Coins for Purchase		P or p		 *\n"
//     << "   *											 *\n"
//     << "   *   Quit							Q or q		 *\n"
//     << "   *											 *\n"
//     << "   * * * * * * * * * * * * * * * * * * * * * * * *\n";
// }

// char getChoice( string prompt )
// {
// 	char ch;
// 	cout << prompt << " (followed by enter): ";
// 	cin >> ch;
// 	return ch;
// }

// void evaluateCommand( Coins & piggyBank, char choice )
// {
// 	switch(choice)
// 	{
// 		case 'B': case 'b':
// 			cout << "Balance is $" << setprecision(2) << piggyBank.total()/100 << endl;
// 			break;
// 		case 'C': case 'c':
// 			cout << piggyBank << endl;
// 			break;
// 		case 'D': case 'd':
// 			int q, d, n ,p;
// 			cout << "How many quarters?: ";
// 			getline(cin, q);
// 			cout << "How many dimes?: ";
// 			getline(cin, d);
// 			cout << "How many nickels?: ";
// 			getline(cin, n);
// 			cout << "How many pennies?: ";
// 			getline(cin, p);
// 			Coins depositThis( q, d, n ,p );
// 			piggyBank.deposit(depositThis);
// 			break;
// 		case 'P': case 'p':
// 			int amount;
// 			cout << "How much do you need?: ";
// 			getline(cin, amount);
// 			if(hasSufficientAmount(amount)
// 			{
// 				Coins item = extractChange(amount);
// 			}
// 			else
// 			{
// 				cout << "You don't have enough coins" << endl;
// 			}
// 			break;
// 		case 'Q': case'q':
// 			cout << "Done with piggy bank. \n\n";
// 			exit(0);
// 		default:
// 			cout << "Invalid command " << choice << endl;
// 			break;
// 	}
// }

// int main()
// {
// 	Coins piggyBank;
// 	while( true )
// 	{
// 		presentMenu();
// 		char command = getChoice("Enter a command character: ");
// 		evaluateCommand(piggyBank, command);
// 	}
// }