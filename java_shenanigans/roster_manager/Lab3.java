public class Lab3 {
	public static void main (String [] args) throws DuplicateCourseException, DuplicateStudentException, EmptyStudentListException, EmptyCourseListException, CourseNotFoundException, CourseLimitException, StudentNotFoundException, StudentLimitException{
		RosterManager rm = new RosterManager();
		rm.run();
	}
}