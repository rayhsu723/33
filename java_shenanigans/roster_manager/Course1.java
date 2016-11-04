public class Course1 {
	// private variables 
	private String course_code;
	private String course_name;
	private int enrolled = 0;
	private Student[] student_list = new Student[50];

	// constructor for Course1. Takes in a course code and a course name
	public Course1 (String cc, String cn) {
		course_code = cc;
		course_name = cn;
	}

	// copy constructor for Course1
	public Course1 (Course1 c) {
		this.course_code = c.course_code;
		this.course_name = c.course_name;
		this.enrolled = c.enrolled;
		this.student_list = c.student_list;
	}

	// the add_student method takes in a Student and stores that student in the course's student list
	// student_list is sorted by the student's last name. If last names are equal, we go by ID next
	// these are the cases that I check for
	// --------------------------------------------------------------------------------------------------------------------------------------------------
	// CASE 1: if the student list is empty, just put the student in the first index
	// CASE 2: if the student list is full (50), throw a StudentLimitException
	// the cases after case 2 are when we are going through the student list
	// CASE 3: if the student ID is found in the student list already, throw a DuplicateStudentException
	// CASE 4: if the student's last name is greater than the current student's last name, we continue
	// CASE 5: if the student's last name is less than the current student's last name, we want to put the new student before the current student
	// CASE 6: if the student's last name is equal to the current student's last name and the new student's ID is less than the current student's ID,
	// 		   we put the new student before the current student
	// CASE 7: If the student's last name is equal to the current student's last name and the new student's ID is greater than the current student's ID,
	//		   we simply continue
	// CASE 8: when we get out of this for-loop and we find that there is no change in the number of enrolled and no exception was thrown,
	//	   	   we simply add the student to the rear of the list
	// --------------------------------------------------------------------------------------------------------------------------------------------------

	public void add_student (Student s) throws StudentLimitException{
		// // CASE 1
		// if (student_list[0] == null) {
		// 	student_list[0] = s;
		// 	++enrolled;
		// 	return s;
		// }

		// more complicated stuff
		try {
			// the reason I have a previous enrolled integer is because I want to check after all these checks whether or not the
			// enrollment number changed or not. If it did not, that means we simply add the student to the next available index at
			// the end of the list
			int prev_enrolled = enrolled;
			int i = 0;

			// CASE 2
			if (enrolled == 50)
				throw new StudentLimitException(); 

			// now we go through every single student in the student list and add the student in the right place
			for (; i < enrolled; ++i) {
				// CASE 1
				if (student_list[0] == null) {
					student_list[0] = s;
					++enrolled;
					break;
				}
				// CASE 3
				if (student_list[i].get_student_id() == s.get_student_id())
					throw new DuplicateStudentException();

				// CASE 4
				else if ( s.get_last_name().compareTo(student_list[i].get_last_name()) > 0 )
					continue;

				// CASE 5
				else if (s.get_last_name().compareTo(student_list[i].get_last_name()) < 0) {
					int temp_count = i;
					Student current = student_list[temp_count]; // possible for this to be null
					student_list[i] = s; 

					for (; temp_count < enrolled; ++temp_count) {
						Student next = student_list[temp_count+1];

						student_list[temp_count+1] = current;
						current = next;
					}
					++enrolled;
					break;
				}

				// CASE 6
				else if (s.get_last_name().equals(student_list[i].get_last_name()) && s.get_student_id() < student_list[i].get_student_id()) {
					int temp_count = i;
					Student current = student_list[temp_count];
					student_list[i] = s;

					for (; temp_count < enrolled; ++ temp_count) {
						Student next = student_list[temp_count+1];

						student_list[temp_count+1] = current;
						current = next;
					}
					++enrolled;
					break;
				}
				// CASE 7
				else if (s.get_last_name().equals(student_list[i].get_last_name()) && s.get_student_id() > student_list[i].get_student_id())
					continue;

				}
				// CASE 8
				if (enrolled == prev_enrolled) {
				student_list[enrolled] = s;
				++enrolled;
				}

		}


		// Exception handling
		catch (StudentLimitException ex) {
			System.out.println("StudentLimitException : Course1.add_student : cannot add student into full class");
		}
		catch (DuplicateStudentException ex) {
			System.out.println("DuplicateStudentException : Course1.add_student : cannot add student " + s.get_first_name() + " " + s.get_last_name() + " to class; has duplicate student ID");
		}
	}

	// the remove_student method will take in a student ID and go through the student_list and try to delete the student from the course
	// here are the cases that I check for
	// --------------------------------------------------------------------------------------------------------------------------------------------------
	// CASE 1: if the student list is empty, we throw an EmptyStudentListException
	// cases 2-4 assume that the student ID is found in the student list
	// CASE 2: if the student we are removing happens to be the last student in a full class (index 49 && enrollment 50), we simply set the last index to null
	// CASE 3: if the index after the student we are removing is null, we simply set the index of the student we are removing to null
	// CASE 4: if there are students after the student we are removing, we need to set the current to null and bump everything past it back one index
	// CASE 5: after we go through the entire student list, if nothing changed, then we throw a StudentNotFoundException
	// --------------------------------------------------------------------------------------------------------------------------------------------------

	public Student remove_student (int student_id) {
		try {
			// CASE 1
			if (enrolled == 0) 
				throw new EmptyStudentListException();
			int i = 0;
			int prev_enrolled = enrolled;

			for (; i < enrolled; ++i) {
				// CASE 2
				if (student_list[i].get_student_id() == student_id) {
					if (i == 49) {
						Student to_return = student_list[49];
						student_list[49] = null;
						--enrolled;
						return to_return;
					}
					// CASE 3
					else if (student_list[i+1] == null) {
						Student to_return = student_list[i];
						student_list[i] = null;
						--enrolled;
						return to_return;
					}
					// CASE 4
					else if (student_list[i+1] != null) {
						Student to_return = student_list[i];
						int temp = i;
						int after = i+1;
						while (student_list[after] != null) {
							student_list[temp] = student_list[after];
							++temp; ++after;
						}
						student_list[temp] = null;
						--enrolled;
						return to_return;
					}

				}

			}
			// CASE 5
			if (prev_enrolled == enrolled)
				throw new StudentNotFoundException();
		}

		catch (EmptyStudentListException ex) {
			System.out.println ("Course1.remove_student : cannot remove student from empty course");
			return null;
		}
		catch (StudentNotFoundException ex) {
			System.out.println ("Course1.remove_student : cannot find student ID : " + student_id + " in course");
			return null;
		}
		return null;
	}



	// getters for Course1.java
	public String get_course_code () {
		return course_code;
	}

	public String get_course_name () {
		return course_name;
	}

	public int get_enrolled () {
		return enrolled;
	}

	public Student[] get_student_list () {
		return student_list;
	}

	// setters for Course1.java
	public void set_course_code (String cc) {
		course_code = cc;
	}

	public void set_course_name (String cn) {
		course_name = cn;
	}

	public void set_enrolled (int e) {
		enrolled = e;
	}

	public void set_student_list (Student[] sl) {
		student_list = sl;
	}




	// running some tests
	public static void main(String[] args) {
		Course1 c = new Course1("course_code", "course_name");
		c.remove_student(1);

		Student s1 = new Student(5, "A", "G");
		Student s2 = new Student(4, "A", "B");
		Student s3 = new Student(3, "A", "G");
		Student s4 = new Student(7, "A", "G");
		Student sF = new Student(5, "sad", "sadjk");


		// Student s5 = new Student(4, "A", "C");

		Student s6 = new Student(6, "A", "G");
		// c.remove_student(1);
		c.add_student(s1);
		c.add_student(s2);
		c.add_student(s3);
		c.add_student(s4);
		c.add_student(s6);
		c.remove_student(4);
		c.remove_student(4);
		c.add_student(sF);
		System.out.println(c.get_enrolled());

		for (int i = 0; c.student_list[i] != null; ++i) {
			System.out.println(c.student_list[i].get_last_name() + " " + c.student_list[i].get_student_id());
		}
	}

	
}

