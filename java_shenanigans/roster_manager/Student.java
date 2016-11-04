public class Student {
	//private variables
	private int student_id;
	private String first_name;
	private String last_name;

	// constructor for Student
	public Student (int s_id, String f_name, String l_name) {
		student_id = s_id;
		first_name = f_name;
		last_name = l_name;
	}

	// copy constructor for Student
	public Student (Student s) {
		this.student_id = s.student_id;
		this.first_name = s.first_name;
		this.last_name = s.last_name;
	}

	// getters for Student
	public int get_student_id () {
		return student_id;
	}

	public String get_first_name () {
		return first_name;
	} 

	public String get_last_name () {
		return last_name;
	}

	// setters for Student
	public void set_student_id (int sid) {
		student_id = sid;
	}

	public void set_first_name (String fn) {
		first_name = fn;
	}

	public void set_last_name (String ln) {
		last_name = ln;
	}
}

