import java.util.Scanner;

public class RosterManager {
	// private variablea
	private Course[] courseList = new Course[10];
	private int numOfCourses = 0;

	// default constructor for RosterManager
	public RosterManager () {}

	// copy constructor for RosterManager
	public RosterManager (RosterManager rm) {
		courseList = rm.courseList;
		numOfCourses = rm.numOfCourses;
	}





	// commands are:
	// ac : add course
	// dc : drop course
	// as : add student
	// ds : drop student
	// p  : print class roster
	// q  : quit program
	public void run() throws DuplicateCourseException, DuplicateStudentException, EmptyStudentListException, EmptyCourseListException, CourseNotFoundException, CourseLimitException, StudentNotFoundException, StudentLimitException{
		System.out.println("Welcome to the Class Roster Manager!\nSelect an action based on the following menu:");
		ClassRosterUI.printMenu();
		// Scanner sc = new Scanner(System.in);
		while (true) {
			String command = ClassRosterUI.getCommand();

			if (command.equals("ac")) {
				String cc;
				String cn;
				cc = ClassRosterUI.getCourseCode();
				cn = ClassRosterUI.getCourseName();

				Course c = new Course(cc, cn);
				addCourse(c);
			}

			else if (command.equals("dc")) {
				String cc = ClassRosterUI.getCourseCode();
				deleteCourse(cc);
			}

			else if(command.equals("as")) {
				String cc;
				int sID;
				String ln;
				String fn;

				cc = ClassRosterUI.getCourseCode();
				sID = ClassRosterUI.getStudentID();
				ln = ClassRosterUI.getLastName();
				fn = ClassRosterUI.getFirstName();

				Student s = new Student(sID, fn, ln);

				addStudent(cc, s);
			}

			else if (command.equals("ds")) {
				String cc;
				int sID;
				cc = ClassRosterUI.getCourseCode();
				sID = ClassRosterUI.getStudentID();

				deleteStudent(sID, cc);
			}

			else if (command.equals("p")) {
				print_roster();
			}

			else if (command.equals("q")) {
				break;
			}

			ClassRosterUI.printMenu();
		}
	}


	// the addCourse method takes in a course and adds it to the courseList
	// the cases that I check for
	// --------------------------------------------------------------------------------------------------------------------------------------------------
	// CASE 1: if the course code is already in the course list, throw a DuplicateCourseException
	// CASE 2: if the course list already has 10 courses, throw a CourseLimitException
	// --------------------------------------------------------------------------------------------------------------------------------------------------

	public void addCourse(Course c) throws DuplicateCourseException, CourseLimitException{
		try {
			// CASE 2
			if (numOfCourses == 10)
				throw new CourseLimitException();
			// CASE 1
			for (int i = 0; courseList[i] != null; ++i) {
				if (courseList[i].getCourseCode().equalsIgnoreCase(c.getCourseCode()))
					throw new DuplicateCourseException();
			}


			courseList[numOfCourses] = c;
			++numOfCourses;
		}

		catch (DuplicateCourseException ex) {
			System.out.println("DuplicateCourseException : RosterManager.addCourse : course code already added; cannot add duplicate course code");
		}

		catch (CourseLimitException ex) {
			System.out.println("CourseLimitException : RosterManager.addCourse : course list already at maximum (10)");
		}
		// System.out.println(numOfCourses);

	}

	// the deleteCourse method takes in a course code and attempts to delete it from the courseList
	// here are the cases that I check for
	// --------------------------------------------------------------------------------------------------------------------------------------------------
	// CASE 1: if the course list is empty, throw an EmptyCourseListException
	// CASE 2: if the course that we are deleting is the last course in a full course list (index 9, numOfCourses 10) and the course codes match, 
	// simplly change it to null
	// CASE 3: if the course codes are equal, we check to see if the course after it is null or not; if it is null, simply change the current to null
	//		   if it is not null, we need to bump all them back one index
	// CASE 4: if the number of courses didn't change after going through course list, we throw a CourseNotFoundException
	// --------------------------------------------------------------------------------------------------------------------------------------------------

	public void deleteCourse(String cc) throws EmptyCourseListException, CourseNotFoundException {
		try {
			// CASE 1
			if (numOfCourses == 0) 
				throw new EmptyCourseListException();

			int prevNum = numOfCourses;

			for (int i = 0; i < numOfCourses; ++i) {
				if (courseList[i].getCourseCode)
			}
			// for (int i = 0; i < numOfCourses; ++i) {
			// 	// CASE 2
			// 	if (i == 9 && (courseList[i].getCourseCode().equalsIgnoreCase(cc))) {
			// 		// Course to_return = courseList[9];
			// 		courseList[9] = null;
			// 		--numOfCourses;
			// 		break;
			// 	}
			// 	// CASE 3
			// 	else if (courseList[i].getCourseCode().equalsIgnoreCase(cc)) {
			// 		// Course to_return = courseList[i];
			// 		courseList[i] = null;
			// 		int temp = i;
			// 		int next = i+1;
			// 		while (next < 10 && courseList[next] != null) {
			// 			System.out.println(temp + " " + next);
			// 			courseList[temp] = courseList[next];
			// 			++temp; ++next;
			// 		}
			// 		--numOfCourses;
			// 		break;
			// 	}

			// }
			// CASE 4
			if (prevNum == numOfCourses)
				throw new CourseNotFoundException();
		}

		catch (EmptyCourseListException ex) {
			System.out.println("EmptyCourseListException : RosterManager.deleteCourse : cannot delete from empty course list");
		}
		catch (CourseNotFoundException ex) {
			System.out.println("CourseNotFoundException : RosterManager.deleteCourse : couldn't find course in course list");
		}
	}

	// addStudent takes in a course code and a Student, and uses Course.addStudent method to add students
	// if the course code is not found in courseList, we throw a CourseNotFoundException
	public void addStudent(String cc, Student s) throws CourseNotFoundException, StudentLimitException, DuplicateStudentException{
		try {
			int i = 0;
			for (; i < numOfCourses; ++i) {
				if (courseList[i].getCourseCode().equalsIgnoreCase(cc)) {
					courseList[i].addStudent(s);
					break;
				}
			}
			if ((i == numOfCourses) && (!courseList[i-1].getCourseCode().equalsIgnoreCase(cc)))
				throw new CourseNotFoundException();
			
		}

		catch (CourseNotFoundException ex) {
			System.out.println("CourseNotFoundException : RosterManager.addStudent : could not find course code : " + cc);
		}
	}
	// deleteStudent takes in a an ID and a course code, and uses Course.removeStudent method to delete students
	// if the course code is not found in courseList, we throw a CourseNotFoundException
	public void deleteStudent(int id, String cc) throws EmptyStudentListException, StudentNotFoundException, CourseNotFoundException{
		try {
			int i = 0;
			for (; i < numOfCourses; ++i) {
				if (courseList[i].getCourseCode().equalsIgnoreCase(cc)) {
					courseList[i].removeStudent(id);
					break;
				}
			}

			if ((i == numOfCourses) && (!courseList[i-1].getCourseCode().equalsIgnoreCase(cc)))
				throw new CourseNotFoundException();
		}

		catch (CourseNotFoundException ex) {
			System.out.println("CourseNotFoundException : Roster_manager.deleteStudent : could not find course code : " + cc);
		}
	}


	// prints out the Roster Manager in the correct format for UI
	public void print_roster() {
		System.out.println("********************");
		for (int i = 0; i < numOfCourses; ++i) {
			System.out.println(courseList[i].getCourseCode() + ": " + courseList[i].getCourseName() + "\nEnrolled: " + courseList[i].getEnrolled());

			Student[] temp_list = courseList[i].getStudentList();
			for (int j = 0; j < courseList[i].getEnrolled(); ++j) {
				System.out.println("\t" + temp_list[j].getStudentID() + " | " + temp_list[j].getLastName() + ", " + temp_list[j].getFirstName());
			}
		}
		System.out.println("********************");

	}


	public int getNumOfCourses() {
		return numOfCourses;
	}

	public Course[] getCourseList() {
		return courseList;
	}

	public void setNumOfCourses(int noc) {
		numOfCourses = noc;
	}

	public void setCourseList(Course[] cl) {
		courseList = cl;
	}

	// public static void main (String[] args) throws DuplicateCourseException, DuplicateStudentException, EmptyStudentListException, EmptyCourseListException, CourseNotFoundException, CourseLimitException, StudentNotFoundException, StudentLimitException{
	// 	RosterManager rm = new RosterManager();

	// 	Course c1 = new Course("ICS45J", "Programming in Java");
	// 	Course c2 = new Course("CS122A", "Databases");
	// 	Course c3 = new Course("ICS90", "Seminar");

	// 	Student s1 = new Student(10, "A", "A");
	// 	Student s2 = new Student(20, "B", "B");
	// 	Student s3 = new Student(20, "C", "C");

	// 	rm.addCourse(c1);
	// 	rm.addCourse(c2);
	// 	rm.addCourse(c3);

	// 	// System.out.println(rm.get_numOfCourses());

	// 	rm.addStudent("ICS45J", s1);
	// 	rm.addStudent("ICS45J", s2);
	// 	rm.addStudent("rugijkj", s1);
	// 	rm.addStudent("CS122A", s3);
	// 	// rm.addStudent("ICS45J", s3);

	// 	rm.deleteStudent(349, "ICS45J");

	// 	// rm.deleteCourse("CS122A");

	// 	// System.out.println(rm.get_numOfCourses());

	// 	rm.print_roster();

	// 	// rm.run();

	// }




}