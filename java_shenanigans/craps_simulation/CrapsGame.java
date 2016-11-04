/*
* CrapsGame.java
* Lab Section 4
* Partner 1 : Raymond Hsu
*	  email : hsurw@uci.edu
*		 ID : 80042296
* 
* Partner 2 : 
*     email : 
*     ID    : 
*/
import java.util.Scanner;

public class CrapsGame {
	CrapsMetricMonitor m;
	public int numRolls = 1;

	// constructor
	public CrapsGame (CrapsMetricMonitor monitor) {
		m = monitor;
	}

	// game logic is here
	public boolean playGame() {
		// first we want to do the come out roll
		int rollOne = (int)(6.0 * Math.random()) + 1;
		int rollTwo = (int)(6.0 * Math.random()) + 1;
		// add up the come out roll
		int comeOutSum = rollOne + rollTwo;
		System.out.println("Rolled a " + comeOutSum);
		// check to see if we won (come out = 7 or 11) AKA natural
		if (comeOutSum == 7 || comeOutSum == 11) {
			System.out.println("*****Natural! You win!*****");
			m.naturalRoll();
			return true;
		}
		// if we didn't win, we want to check if we lost (come out = 2, 3, or 12) AKA craps
		else if (comeOutSum == 2 || comeOutSum == 3 || comeOutSum == 12) {
			System.out.println("*****Craps! You lose.*****");
			m.crapsRoll();
			return false;
		}
		// if we didn't win or lose on the come out roll, the come out roll becomes the point number.
		// We keep rolling until we roll 7 (we lose) or until we roll the point number again (we win)
		else {
			int pointNo = comeOutSum;
			while (true) {
				rollOne = (int)(6.0 * Math.random()) + 1;
				rollTwo = (int)(6.0 * Math.random()) + 1;
				int newSum = rollOne + rollTwo;
				System.out.println("Rolled a " + newSum);
				++numRolls;
				// if we roll a 7, we lose
				if (newSum == 7) {
					m.newMaxRolls(numRolls);
					// we want to reset numRolls everytime we end in this part
					numRolls = 1;
					System.out.println("*****Rolled a 7! You lose*****");
					m.sevenRoll();
					return false;
				}
				// if we roll the point number again, we win
				else if (newSum == pointNo) {
					m.newMaxRolls(numRolls);
					numRolls = 1;
					System.out.println("*****Rolled the point! You win!*****");
					m.pointRoll();
					return true;
				}
				// if we didn't roll a 7 or the point number, we keep rolling
				else {
					continue;
				}
			}
		}

	}

}
