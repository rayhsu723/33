/*
* CrapsMetricMonitor.java
* Lab Section 4
* Partner 1 : Raymond Hsu
*	  email : hsurw@uci.edu
*		 ID : 80042296
* 
* Partner 2 : Shannon Lee
*     email : leest1@uci.edu
*     ID    : 28557039
*/

public class CrapsMetricMonitor {
	public int gamesPlayed;
	public int gamesWon;
	public int gamesLost;
	public int maxRolls = 1;
	public int natCount;
	public int crapsCount;
	public int winStreak = 0;
	public int loseStreak = 0;
	public int maxBalance;
	public int maxGame;

	// default contstructor
	public CrapsMetricMonitor () {}

	// resets all of the player's statistics
	public void resetStats () {
		this.gamesPlayed = 0;
		this.gamesWon = 0;
		this.gamesLost = 0;
		this.maxRolls = 1;
		this.natCount = 0;
		this.crapsCount = 0;
		this.winStreak = 0;
		this.loseStreak = 0;
		this.maxBalance = 0;
		this.maxGame = 0;
	}
	
	// increments the right stuff when a natural roll occurs
	public void naturalRoll () {
		++this.gamesPlayed;
		++this.gamesWon;
		++this.natCount;

	}

	// increments the right stuff when a craps roll occurs
	public void crapsRoll () {
		++this.gamesPlayed;
		++this.gamesLost;
		++crapsCount;
	}

	// increments the right stuff when a point roll occurs
	public void pointRoll () {
		++this.gamesPlayed;
		++this.gamesWon;
	}

	// increments the right stuff when a seven roll occurs
	public void sevenRoll () {
		++this.gamesPlayed;
		++this.gamesLost;
	}

	// takes in the currrent number of rolls and compares it to the max rolls currently. If it is greater
	// than the max rolls, it will replace max rolls
	public void newMaxRolls (int rolls) {
		if (rolls > this.maxRolls) {
			this.maxRolls = rolls;
		}
	}

	// prints out statistics at the end of the simulation
	public void printStatistics () {
		System.out.println("*****************************\n*** SIMULATION STATISTICS ***\n*****************************");
		System.out.println("Games played: " + gamesPlayed + "\nGames won: " + gamesWon + "\nGames lost: " + gamesLost 
							+ "\nMaximum Rolls in a single game: " + maxRolls + "\nNatural Count: " + natCount
						    + "\nCraps Count: " + crapsCount + "\nMaximum Win Streak: " + winStreak + "\nMaximum Losing Streak: " + loseStreak
							+ "\nMaximum Balance: " +  maxBalance + " during game " + maxGame);
	}

}