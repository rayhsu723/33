import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.After;
import org.junit.Test;
import org.junit.BeforeClass;
import org.junit.AfterClass;


public class JUnit_Tester {

	
	private RosterManager manager;
	private Course[] course_list;
	private Student[] student_list;
	
	@Before // Executed before each test in this class 
		
	public void executeBeforeEachTest() {
		System.out.println("@Before: ******Single test starts*******"); 
		manager = new RosterManager();
		course_list = new Course[10];
		student_list = new Student[50];
	}

	@Test

	public void testAdd_DeleteCourse() throws DuplicateCourseException, CourseLimitException, EmptyCourseListException, CourseNotFoundException {
		
		//test add course
		Course c1 = new Course("ICS45J","Programming in Java");
		this.course_list[0] = c1;
		manager.addCourse(c1);
		
		assertArrayEquals(course_list, manager.getCourseList());
		
		Course c2 = new Course("ICS45C","Programming in C++");
		this.course_list[1] = c2;
		manager.addCourse(c2);
		
		Course c3 = new Course("ICS31","Programming in Python 1");
		this.course_list[2] = c3;
		manager.addCourse(c3);
		
		assertArrayEquals(course_list, manager.getCourseList());
		
		Course c4 = new Course("ICS32","Programming in Python 2");
		this.course_list[3] = c4;
		manager.addCourse(c4);
		
		Course c5 = new Course("ICS33","Programming in Python 3");
		this.course_list[4] = c5;
		manager.addCourse(c5);
		
		assertArrayEquals(course_list, manager.getCourseList());
		
		//delete the last course
		manager.deleteCourse("ICS33");
		this.course_list[4] = null;
		assertArrayEquals(course_list, manager.getCourseList());
		
		//delete the middle course
		manager.deleteCourse("ICS45C");
		this.course_list[1] = this.course_list[2];
		this.course_list[2] = this.course_list[3];
		this.course_list[3] = this.course_list[4];
		assertArrayEquals(course_list, manager.getCourseList());
		
		//delete the first course
		manager.deleteCourse("ICS45J");
		this.course_list[0] = this.course_list[1];
		this.course_list[1] = this.course_list[2];
		this.course_list[2] = this.course_list[3];
		assertArrayEquals(course_list, manager.getCourseList());
		
		
	}

	
	
	

	@Test
	
	public void testAdd_DeleteStudent() throws DuplicateCourseException, CourseLimitException, CourseNotFoundException, StudentLimitException, DuplicateStudentException, EmptyStudentListException, StudentNotFoundException {
		
		//add course
		Course c1 = new Course("ICS45J","Programming in Java");
		this.course_list[0] = c1;
		manager.addCourse(c1);
		
		
		//test add student
		Student s1 = new Student(12345678, "Melody", "Wang");
		manager.addStudent("ICS45J", s1);
		this.student_list[0] = s1;
		assertArrayEquals(this.student_list, manager.getCourseList()[0].getStudentList());

		Student s2 = new Student(87654321, "Ray", "Hsu");
		manager.addStudent("ICS45J", s2);
		this.student_list[0] = s2;
		this.student_list[1] = s1;
		assertArrayEquals(this.student_list, manager.getCourseList()[0].getStudentList());

		
		//test delete student
		//delete the last student in the list
		manager.deleteStudent(12345678, "ICS45j");
		this.student_list[1] = null;
		assertArrayEquals(this.student_list, manager.getCourseList()[0].getStudentList());
	
		//delete one student except the last one in the list
		manager.addStudent("ICS45J", s1);
		manager.deleteStudent(87654321, "ICS45j");
		this.student_list[0] = s1;
		this.student_list[1] = null;
		assertArrayEquals(this.student_list, manager.getCourseList()[0].getStudentList());
		
		
		
	}
	
	
	
	// Testing an Expected Exception was thrown 
	
	@Test(expected=DuplicateCourseException.class) 
	
	public void testExceptionThrown1() throws DuplicateCourseException, CourseLimitException {
		try{
			Course c1 = new Course("ICS45J","Programming in Java");
			Course c2 = new Course("ICS45J","Programming in java");
			manager.addCourse(c1);
			manager.addCourse(c2);
		}catch(DuplicateCourseException e){
			System.out.println("hey");
			throw new DuplicateCourseException();
		}
	}
	
	
	@Test(expected=CourseLimitException.class) 
	
	public void testExceptionThrown2() throws DuplicateCourseException, CourseLimitException {
		int i;
		for (i = 0; i < 10; i++){
			Course c = new Course(Integer.toString(i),"abc");
			manager.addCourse(c);
		}
		Course c = new Course(Integer.toString(123),"abc");
		manager.addCourse(c);
		
	
	}
	

	@Test(expected=CourseNotFoundException.class) 

	public void testExceptionThrown3() throws DuplicateCourseException, CourseLimitException, EmptyStudentListException, StudentNotFoundException, CourseNotFoundException {
		Course c1 = new Course("ICS45J","Programming in Java");
		manager.addCourse(c1);
		manager.deleteStudent(12345678, "ICS45c");

		
	}



	@Test(expected=EmptyCourseListException.class) 

	public void testExceptionThrown4() throws EmptyCourseListException, CourseNotFoundException {
	
	manager.deleteCourse("aaa");
	
	
	}

	@Test(expected=EmptyStudentListException.class) 

	public void testExceptionThrown5() throws DuplicateCourseException, CourseLimitException, EmptyStudentListException, StudentNotFoundException, CourseNotFoundException {
		Course c1 = new Course("ICS45J","Programming in Java");
		manager.addCourse(c1);
		manager.getCourseList()[0].removeStudent(1234567);
	
	
	}
	
	@Test(expected=StudentLimitException.class) 

	public void testExceptionThrown6() throws CourseNotFoundException, StudentLimitException, DuplicateStudentException, DuplicateCourseException, CourseLimitException {
	
		Course c = new Course("ICS45J","Programming in Java");
		manager.addCourse(c);
		int i;
		for (i = 0; i < 50; i++){
			Student s = new Student(i,"abc","bcd");
			manager.addStudent("ics45j", s);;
		}
		Student s = new Student(98765,"abc","sdff");
		manager.addStudent("ics45j",s);
	
	
	}
	
	@Test(expected=StudentNotFoundException.class) 

	public void testExceptionThrown7() throws DuplicateCourseException, CourseLimitException, CourseNotFoundException, StudentLimitException, DuplicateStudentException, EmptyStudentListException, StudentNotFoundException {
	
		Course c1 = new Course("ICS45J","Programming in Java");
		manager.addCourse(c1);
		Student s1 = new Student(12345678, "Melody", "Wang");
		manager.addStudent("ICS45J", s1);
		manager.getCourseList()[0].removeStudent(23456);
	
	
	
	}
	
	@Test(expected=DuplicateStudentException.class) 

	public void testExceptionThrown8() throws DuplicateCourseException, CourseLimitException, CourseNotFoundException, StudentLimitException, DuplicateStudentException {
		Course c1 = new Course("ICS45J","Programming in Java");
		manager.addCourse(c1);
		Student s1 = new Student(12345678, "Melody", "Wang");
		manager.addStudent("ICS45J", s1);
		Student s2 = new Student(12345678, "Melody", "Wang");
		manager.getCourseList()[0].addStudent(s2);
	
	
	}

	@After

	public void executeAfterTest() {
		System.out.println("@After: ******Single test ends*******"); }

	@AfterClass

	public static void executeAfterAllTests() {

		System.out.println("@AfterClass: End all tests");
	}

	@BeforeClass

	public static void executeBeforeAllTests() {

		System.out.println("@BeforeClass: Begin all tests"); 
		}
	
	
	
	
}