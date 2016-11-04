import java.util.Scanner;

public class Roster_Manager {
	// private variablea
	private Course[] course_list = new Course[10];
	private int num_of_courses = 0;

	// default constructor for Roster_Manager
	public Roster_Manager () {}

	// copy constructor for Roster_Manager
	public Roster_Manager (Roster_Manager rm) {
		course_list = rm.course_list;
		num_of_courses = rm.num_of_courses;
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
		ClassRosterUI.print_menu();
		// Scanner sc = new Scanner(System.in);
		while (true) {
			String command = ClassRosterUI.get_command();

			if (command.equals("ac")) {
				String cc;
				String cn;
				cc = ClassRosterUI.get_course_code();
				cn = ClassRosterUI.get_course_name();

				Course c = new Course(cc, cn);
				add_course(c);
			}

			else if (command.equals("dc")) {
				String cc = ClassRosterUI.get_course_code();
				delete_course(cc);
			}

			else if(command.equals("as")) {
				String cc;
				int sID;
				String ln;
				String fn;

				cc = ClassRosterUI.get_course_code();
				sID = ClassRosterUI.get_student_id();
				ln = ClassRosterUI.get_last_name();
				fn = ClassRosterUI.get_first_name();

				Student s = new Student(sID, fn, ln);

				add_student(cc, s);
			}

			else if (command.equals("ds")) {
				String cc;
				int sID;
				cc = ClassRosterUI.get_course_code();
				sID = ClassRosterUI.get_student_id();

				delete_student(sID, cc);
			}

			else if (command.equals("p")) {
				print_roster();
			}

			else if (command.equals("q")) {
				break;
			}

			ClassRosterUI.print_menu();
		}
	}








	// the add_course method takes in a course and adds it to the course_list
	// the cases that I check for
	// --------------------------------------------------------------------------------------------------------------------------------------------------
	// CASE 1: if the course code is already in the course list, throw a DuplicateCourseException
	// CASE 2: if the course list already has 10 courses, throw a CourseLimitException
	// --------------------------------------------------------------------------------------------------------------------------------------------------

	public void add_course(Course c) throws DuplicateCourseException, CourseLimitException{
		try {
			// CASE 1
			for (int i = 0; course_list[i] != null; ++i) {
				if (course_list[i].get_course_code().equalsIgnoreCase(c.get_course_code()))
					throw new DuplicateCourseException();
			}
			// CASE 2
			if (num_of_courses == 10)
				throw new CourseLimitException();

			course_list[num_of_courses] = c;
			++num_of_courses;
		}

		catch (DuplicateCourseException ex) {
			System.out.println("DuplicateCourseException : Roster_Manager.add_course : course code already added; cannot add duplicate course code");
		}

		catch (CourseLimitException ex) {
			System.out.println("CourseLimitException : Roster_Manager.add_course : course list already at maximum (10)");
		}

	}

	// the delete_course method takes in a course code and attempts to delete it from the course_list
	// here are the cases that I check for
	// --------------------------------------------------------------------------------------------------------------------------------------------------
	// CASE 1: if the course list is empty, throw an EmptyCourseListException
	// CASE 2: if the course that we are deleting is the last course in a full course list (index 9, num_of_courses 10) and the course codes match, 
	// simplly change it to null
	// CASE 3: if the course codes are equal, we check to see if the course after it is null or not; if it is null, simply change the current to null
	//		   if it is not null, we need to bump all them back one index
	// CASE 4: if the number of courses didn't change after going through course list, we throw a CourseNotFoundException
	// --------------------------------------------------------------------------------------------------------------------------------------------------

	public void delete_course(String cc) throws EmptyCourseListException, CourseNotFoundException {
		try {
			// CASE 1
			if (num_of_courses == 0) 
				throw new EmptyCourseListException();

			int prev_num = num_of_courses;

			for (int i = 0; i < num_of_courses; ++i) {
				// CASE 2
				if (i == 9 && (course_list[i].get_course_code().equalsIgnoreCase(cc))) {
					// Course to_return = course_list[9];
					course_list[9] = null;
					--num_of_courses;
					break;
				}
				// CASE 3
				else if (course_list[i].get_course_code().equalsIgnoreCase(cc)) {
					// Course to_return = course_list[i];
					course_list[i] = null;
					int temp = i;
					int next = i+1;
					while (course_list[next] != null) {
						course_list[temp] = course_list[next];
						++temp; ++next;
					}
					course_list[i+1] = null;
					--num_of_courses;
					break;
				}

			}
			// CASE 4
			if (prev_num == num_of_courses)
				throw new CourseNotFoundException();
		}

		catch (EmptyCourseListException ex) {
			System.out.println("EmptyCourseListException : Roster_Manager.delete_course : cannot delete from empty course list");
		}
		catch (CourseNotFoundException ex) {
			System.out.println("CourseNotFoundException : Roster_Manager.delete_course : couldn't find course in course list");
		}
	}

	// add_student takes in a course code and a Student, and uses Course.add_student method to add students
	// if the course code is not found in course_list, we throw a CourseNotFoundException
	public void add_student(String cc, Student s) throws CourseNotFoundException, StudentLimitException, DuplicateStudentException{
		try {
			int i = 0;
			for (; i < num_of_courses; ++i) {
				if (course_list[i].get_course_code().equalsIgnoreCase(cc)) {
					course_list[i].add_student(s);
					break;
				}
			}
			if ((i == num_of_courses) && (!course_list[i-1].get_course_code().equalsIgnoreCase(cc)))
				throw new CourseNotFoundException();
			
		}

		catch (CourseNotFoundException ex) {
			System.out.println("CourseNotFoundException : Roster_Manager.add_student : could not find course code : " + cc);
		}
	}
	// delete_student takes in a an ID and a course code, and uses Course.remove_student method to delete students
	// if the course code is not found in course_list, we throw a CourseNotFoundException
	public void delete_student(int id, String cc) throws EmptyStudentListException, StudentNotFoundException, CourseNotFoundException{
		try {
			int i = 0;
			for (; i < num_of_courses; ++i) {
				if (course_list[i].get_course_code().equalsIgnoreCase(cc)) {
					course_list[i].remove_student(id);
					break;
				}
			}

			if ((i == num_of_courses) && (!course_list[i-1].get_course_code().equalsIgnoreCase(cc)))
				throw new CourseNotFoundException();
		}

		catch (CourseNotFoundException ex) {
			System.out.println("CourseNotFoundException : Roster_manager.delete_student : could not find course code : " + cc);
		}
	}


	// prints out the Roster Manager in the correct format for UI
	public void print_roster() {
		System.out.println("********************");
		for (int i = 0; i < num_of_courses; ++i) {
			System.out.println(course_list[i].get_course_code() + ": " + course_list[i].get_course_name() + "\nEnrolled: " + course_list[i].get_enrolled());

			Student[] temp_list = course_list[i].get_student_list();
			for (int j = 0; j < course_list[i].get_enrolled(); ++j) {
				System.out.println("\t" + temp_list[j].get_student_id() + " | " + temp_list[j].get_last_name() + ", " + temp_list[j].get_first_name());
			}
		}
		System.out.println("********************");

	}


	public int get_num_of_courses() {
		return num_of_courses;
	}

	public Course[] get_course_list() {
		return course_list;
	}

	public void set_num_of_courses(int noc) {
		num_of_courses = noc;
	}

	public void set_course_list(Course[] cl) {
		course_list = cl;
	}

	// public static void main (String[] args) throws DuplicateCourseException, DuplicateStudentException, EmptyStudentListException, EmptyCourseListException, CourseNotFoundException, CourseLimitException, StudentNotFoundException, StudentLimitException{
	// 	Roster_Manager rm = new Roster_Manager();

	// 	Course c1 = new Course("ICS45J", "Programming in Java");
	// 	Course c2 = new Course("CS122A", "Databases");
	// 	Course c3 = new Course("ICS90", "Seminar");

	// 	Student s1 = new Student(10, "A", "A");
	// 	Student s2 = new Student(20, "B", "B");
	// 	Student s3 = new Student(20, "C", "C");

	// 	rm.add_course(c1);
	// 	rm.add_course(c2);
	// 	rm.add_course(c3);

	// 	// System.out.println(rm.get_num_of_courses());

	// 	rm.add_student("ICS45J", s1);
	// 	rm.add_student("ICS45J", s2);
	// 	rm.add_student("rugijkj", s1);
	// 	rm.add_student("CS122A", s3);
	// 	// rm.add_student("ICS45J", s3);

	// 	rm.delete_student(349, "ICS45J");

	// 	// rm.delete_course("CS122A");

	// 	// System.out.println(rm.get_num_of_courses());

	// 	rm.print_roster();

	// 	// rm.run();

	// }




}