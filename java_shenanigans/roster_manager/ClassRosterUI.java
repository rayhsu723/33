import java.util.Scanner;

public class ClassRosterUI {

	static void print_menu() {
		System.out.println("----------\nac: Add Course\ndc: Drop Course\nas: Add Student\nds: Drop Student\n p: Print ClassRoster\n q: Quit Program\n----------");
	}
	// commands are:
	// ac : add course
	// dc : drop course
	// as : add student
	// ds : drop student
	// p  : print class roster
	// q  : quit program
	static String get_command() {
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

	static String get_course_code() {
		Scanner s = new Scanner(System.in);
		System.out.print("Enter course code: ");
		String cc = s.nextLine();
		return cc;
	}

	static String get_course_name() {
		Scanner s = new Scanner(System.in);
		System.out.print("Enter course name: ");
		String cn = s.nextLine();
		return cn;
	}

	static String get_first_name() {
		Scanner s = new Scanner(System.in);
		System.out.print("Enter first name: ");
		String fn = s.nextLine();
		return fn;
	}

	static String get_last_name() {
		Scanner s = new Scanner(System.in);
		System.out.print("Enter last name: ");
		String ln = s.nextLine();
		return ln;
	}

	static int get_student_id() {
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


	public static void main(String[] args) {
		ClassRosterUI.get_command();
	}
}