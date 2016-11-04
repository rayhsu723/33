/*
* CrapsSimulation.java
* Lab Section 4
* Partner 1 : Raymond Hsu
*	  email : hsurw@uci.edu
*		 ID : 80042296
* 
* Partner 2 : Shannon Lee
*     email : leest1@uci.edu
*     ID    : 28557039
*/
import java.util.Scanner;

public class CrapsSimulation {
	CrapsMetricMonitor m;
	CrapsGame g;
	String name;
	int balance;
	int bet;
	int curWinStreak = 0;
	int curLoseStreak = 0;

	// constructor
	CrapsSimulation() {
		m = new CrapsMetricMonitor();
		g = new CrapsGame(m);
	}

	// takes in a win/loss, modifies the balance accordingly, and modifies
	// win streak and lose streak accordingly
	public void checkWL (boolean result) {
		if (result) {
			balance += bet;
			++curWinStreak;
			curLoseStreak = 0;
			if (curWinStreak > m.winStreak)
				m.winStreak = curWinStreak;
		}
		else {
			balance -= bet;
			++curLoseStreak;
			curWinStreak = 0;
			if (curLoseStreak > m.loseStreak)
				m.loseStreak = curLoseStreak;
		}
	}

	// takes in the current balance and checks to see if it is greater
	// than the max balance
	public void checkMaxBalance (int money) {
		if (money >= m.maxBalance) {
			m.maxBalance = money;
			m.maxGame = m.gamesPlayed;
		}
	}

	// does all the user prompting stuff and runs game until end
	public void game() {
		Scanner sc = new Scanner(System.in);
		System.out.print("Welcome to SimCraps! Enter your user name: ");
		// prompt the user for their username
		name = sc.nextLine();

		System.out.println("Hello " + this.name + "!");
		
		// this while loop will keep prompting the user until they enter in a valid balance (positive and type int)
		while (true) {
			Scanner s = new Scanner(System.in);
			System.out.print("Enter the amount of money you will bring to the table: ");
			try {
				int value = s.nextInt();
				if (value <= 0) {
					System.out.println("Input value. Please enter an amount greater than 1");
				}
				else {
					balance = value;
					break;
				}
			}
			catch (Exception e) {
				System.out.println("Invalid input type. Please enter an integer greater than 1");
			}
		}

		// this while loop will keep prompting the user until they enter in a valid bet (integer between 1 and balance)
		System.out.print("Enter the bet amount between $1 and $" + balance + ": ");
		while (true) {
			Scanner s = new Scanner(System.in);
			try {
				int b = s.nextInt();
				if (b > balance || b < 1) {
					System.out.print("Invalid bet! Please enter a bet between $1 and $" + balance + ": ");
				}
				else {
					bet = b;
					break;
				}
			}
			catch (Exception e) {
				System.out.print("Invalid bet! Please enter a bet between $1 and $" + balance + ": ");
			}
		}
		System.out.print("\n");


		// do the first game
		boolean firstGame = g.playGame();

		checkWL(firstGame);
		checkMaxBalance(balance);

		int originalBet = bet;

		// this while loop will run until the user prompts 'n' when requesting a new game
		// or when the user runs out of money
		while (true) {
			// check to see if the user even has money
			if (balance == 0) {
				System.out.println("You're out of money!");
				break;
			}
			// the bet will be altered if the original bet is greater than the current balance
			bet = originalBet;
			if (bet > balance)
				bet = balance;
			else
				bet = originalBet;
			// System.out.println("=========THE BET IS " + bet + " ==========");


			System.out.print(name + "'s balance: $" + balance + ". Playing a new game ...\n");
			boolean result = g.playGame();
			checkWL(result);
			checkMaxBalance(balance);

			continue;
		}
		m.printStatistics();
		// prompt user for whether they want to play another game
		// Scanner sca = new Scanner(System.in);
		// System.out.print("Replay? Enter 'y' or 'n': ");
		// String in = sca.next();
		// if("y".equals(in)){
		// 	m.resetStats();
		// 	start();
		// }
		// else if ("n".equals(in)) {

		// }
	}

	public void start() {
		game();
		while (true) {
			Scanner sca = new Scanner(System.in);
			System.out.print("Replay? Enter 'y' or 'n' : ");
			String in = sca.next();
			if ("y".equals(in)) {
				m.resetStats();
				game();
			}
			else if ("n".equals(in)) {
				break;
			}
			else {
				System.out.println("Invalid input");
			}
		}
	}

}