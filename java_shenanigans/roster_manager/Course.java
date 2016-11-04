public class Course {
	// private variables 
	private String courseCode;
	private String courseName;
	private int enrolled = 0;
	private Student[] studentList = new Student[50];

	// constructor for Course. Takes in a course code and a course name
	public Course (String cc, String cn) {
		courseCode = cc;
		courseName = cn;
	}

	// copy constructor for Course
	public Course (Course c) {
		this.courseCode = c.courseCode;
		this.courseName = c.courseName;
		this.enrolled = c.enrolled;
		this.studentList = c.studentList;
	}

	// the addStudent method takes in a Student and stores that student in the course's student list
	// studentList is sorted by the student's last name. If last names are equal, we go by ID next
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

	public void addStudent (Student s) throws StudentLimitException, DuplicateStudentException{

		try {
			// the reason I have a previous enrolled integer is because I want to check after all these checks whether or not the
			// enrollment number changed or not. If it did not, that means we simply add the student to the next available index at
			// the end of the list
			int prevEnrolled = enrolled;
			int i = 0;

			// CASE 2
			if (enrolled == 50)
				throw new StudentLimitException();

			// now we go through every single student in the student list and add the student in the right place
			for (; i < enrolled; ++i) {
				// // CASE 2
				// if (enrolled == 50)
				// 	throw new StudentLimitException();

				// CASE 3
				if (studentList[i].getStudentID() == s.getStudentID()) {
					// System.out.println(studentList[i].getStudentID() + " " + s.getStudentID());
					// System.out.print("here");
					throw new DuplicateStudentException();
				}

				//CASE 1
				if (studentList[0] == null) {
					studentList[0] = s;
					++enrolled;
					break;
				}


				// CASE 4
				else if ( s.getLastName().compareTo(studentList[i].getLastName()) > 0 )
					continue;

				// CASE 5
				else if (s.getLastName().compareTo(studentList[i].getLastName()) < 0) {
					int temp_count = i;
					Student current = studentList[temp_count]; // possible for this to be null
					studentList[i] = s; 

					for (; temp_count < enrolled; ++temp_count) {
						Student next = studentList[temp_count+1];

						studentList[temp_count+1] = current;
						current = next;
					}
					++enrolled;
					break;
				}

				// CASE 6
				else if (s.getLastName().equals(studentList[i].getLastName()) && s.getStudentID() < studentList[i].getStudentID()) {
					int temp_count = i;
					Student current = studentList[temp_count];
					studentList[i] = s;

					for (; temp_count < enrolled; ++ temp_count) {
						Student next = studentList[temp_count+1];

						studentList[temp_count+1] = current;
						current = next;
					}
					++enrolled;
					break;
				}
				// CASE 7
				else if (s.getLastName().equals(studentList[i].getLastName()) && s.getStudentID() > studentList[i].getStudentID())
					continue;

			}
				// CASE 8
				if (enrolled == prevEnrolled) {
				studentList[enrolled] = s;
				++enrolled;
				}

		}


		// Exception handling
		catch (StudentLimitException ex) {
			System.out.println("StudentLimitException : Course.addStudent : cannot add student into full class");

		}
		catch (DuplicateStudentException ex) {
			System.out.println("DuplicateStudentException : Course.addStudent : cannot add student " + s.getFirstName() + " " + s.getLastName() + " to class; has duplicate student ID");
		}
	}

	// the remove_student method will take in a student ID and go through the studentList and try to delete the student from the course
	// here are the cases that I check for
	// --------------------------------------------------------------------------------------------------------------------------------------------------
	// CASE 1: if the student list is empty, we throw an EmptyStudentListException
	// cases 2-4 assume that the student ID is found in the student list
	// CASE 2: if the student we are removing happens to be the last student in a full class (index 49 && enrollment 50), we simply set the last index to null
	// CASE 3: if the index after the student we are removing is null, we simply set the index of the student we are removing to null
	// CASE 4: if there are students after the student we are removing, we need to set the current to null and bump everything past it back one index
	// CASE 5: after we go through the entire student list, if nothing changed, then we throw a StudentNotFoundException
	// --------------------------------------------------------------------------------------------------------------------------------------------------

	public void removeStudent (int studentID) throws EmptyStudentListException, StudentNotFoundException{
		try {
			// CASE 1
			if (enrolled == 0) 
				throw new EmptyStudentListException();

			int i = 0;
			int prevEnrolled = enrolled;

			for (; i < enrolled; ++i) {
				// CASE 2
				if (studentList[i].getStudentID() == studentID) {
					if (i == 49) {
						// Student to_return = studentList[49];
						studentList[49] = null;
						--enrolled;
						break;
					}
					// CASE 3
					else if (studentList[i+1] == null) {
						// Student to_return = studentList[i];
						studentList[i] = null;
						--enrolled;
						break;
					}
					// CASE 4
					else if (studentList[i+1] != null) {
						// Student to_return = studentList[i];
						int temp = i;
						int after = i+1;
						while (studentList[after] != null) {
							studentList[temp] = studentList[after];
							++temp; ++after;
						}
						studentList[temp] = null;
						--enrolled;
						break;
					}

				}

			}
			// CASE 5
			if (prevEnrolled == enrolled)
				throw new StudentNotFoundException();
		}

		catch (EmptyStudentListException ex) {
			System.out.println ("Course.remove_student : cannot remove student from empty course");
		}
		catch (StudentNotFoundException ex) {
			System.out.println ("Course.remove_student : cannot find student ID : " + studentID + " in course");
		}
	}



	// getters for Course.java
	public String getCourseCode () {
		return courseCode;
	}

	public String getCourseName () {
		return courseName;
	}

	public int getEnrolled () {
		return enrolled;
	}

	public Student[] getStudentList () {
		return studentList;
	}

	// setters for Course.java
	public void setCourseCode (String cc) {
		courseCode = cc;
	}

	public void setCourseName (String cn) {
		courseName = cn;
	}

	public void setEnrolled (int e) {
		enrolled = e;
	}

	public void setStudentList (Student[] sl) {
		studentList = sl;
	}

	// // running some tests
	// public static void main(String[] args) throws StudentLimitException, DuplicateStudentException, StudentNotFoundException, EmptyStudentListException{
	// 	Course c = new Course("courseCode", "courseName");
	// 	c.remove_student(1);

	// 	Student s1 = new Student(5, "A", "G");
	// 	Student s2 = new Student(4, "A", "B");
	// 	Student s3 = new Student(3, "A", "G");
	// 	Student s4 = new Student(7, "A", "G");
	// 	Student sF = new Student(5, "sad", "sadjk");


	// 	// Student s5 = new Student(4, "A", "C");

	// 	Student s6 = new Student(6, "A", "G");
	// 	// c.remove_student(1);
	// 	c.addStudent(s1);
	// 	c.addStudent(s2);
	// 	c.addStudent(s3);
	// 	c.addStudent(s4);
	// 	c.addStudent(s6);
	// 	c.remove_student(4);
	// 	c.remove_student(4);
	// 	c.addStudent(sF);
	// 	System.out.println(c.get_enrolled());

	// 	for (int i = 0; c.studentList[i] != null; ++i) {
	// 		System.out.println(c.studentList[i].getLastName() + " " + c.studentList[i].getStudentID());
	// 	}
	// }

	
}

