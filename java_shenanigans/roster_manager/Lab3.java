public class Lab3 {
	public static void main (String [] args) throws DuplicateCourseException, DuplicateStudentException, EmptyStudentListException, EmptyCourseListException, CourseNotFoundException, CourseLimitException, StudentNotFoundException, StudentLimitException{
		Roster_Manager rm = new Roster_Manager();
		rm.run();
	}
}