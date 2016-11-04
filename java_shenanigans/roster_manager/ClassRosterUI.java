import java.util.Scanner;

public class ClassRosterUI {

	static void printMenu() {
		System.out.println("----------\nac: Add Course\ndc: Drop Course\nas: Add Student\nds: Drop Student\n p: Print ClassRoster\n q: Quit Program\n----------");
	}
	// commands are:
	// ac : add course
	// dc : drop course
	// as : add student
	// ds : drop student
	// p  : print class roster
	// q  : quit program
	static String getCommand() {
		String command;
		while (true) {
			Scanner sca = new Scanner(System.in);
			System.out.print("Enter Command: ");
			command = sca.next();
			if (command.equals("ac") || command.equals("dc") || command.equals("as") || command.equals("ds") || command.equals("p") || command.equals("q"))
				break;
			else {
				System.out.println("Invalid command: " + command);
				continue;
			}
		}
		// System.out.println(command);
		return command;
	}

	// promp,ts user for course code
	static String getCourseCode() {
		Scanner s = new Scanner(System.in);
		System.out.print("Enter course code: ");
		String cc = s.nextLine();
		return cc;
	}

	// prompts user for course name
	static String getCourseName() {
		Scanner s = new Scanner(System.in);
		System.out.print("Enter course name: ");
		String cn = s.nextLine();
		return cn;
	}

	// prompts user for first name
	static String getFirstName() {
		Scanner s = new Scanner(System.in);
		System.out.print("Enter first name: ");
		String fn = s.nextLine();
		return fn;
	}

	// prompts user for last name
	static String getLastName() {
		Scanner s = new Scanner(System.in);
		System.out.print("Enter last name: ");
		String ln = s.nextLine();
		return ln;
	}

	// prompts user for student ID. will make sure that the ID is an int
	static int getStudentID() {
		while(true) {
			try {
				Scanner s = new Scanner(System.in);
				System.out.print("Enter in student ID: ");
				int sID = s.nextInt();
				return sID;
			}
			catch (Exception e) {
				System.out.println("Please enter in an integer for student ID");
			}
		}
	}

}