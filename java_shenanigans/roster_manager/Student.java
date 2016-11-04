public class Student {
	//private variables
	private int studentID;
	private String firstName;
	private String lastName;

	// constructor for Student
	public Student (int sID, String fName, String lName) {
		studentID = sID;
		firstName = fName;
		lastName = lName;
	}

	// copy constructor for Student
	public Student (Student s) {
		this.studentID = s.studentID;
		this.firstName = s.firstName;
		this.lastName = s.lastName;
	}

	// getters for Student
	public int getStudentID () {
		return studentID;
	}

	public String getFirstName () {
		return firstName;
	} 

	public String getLastName () {
		return lastName;
	}

	// setters for Student
	public void setStudentID (int sid) {
		studentID = sid;
	}

	public void setFirstName (String fn) {
		firstName = fn;
	}

	public void setLastName (String ln) {
		lastName = ln;
	}
}

