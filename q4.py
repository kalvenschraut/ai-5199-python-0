class Course:
    __students = set()
    __max = 0
    def __init__(self, max=0, defaultStudents=[]):
        self.__max = max
        if len(defaultStudents) > max:
            raise ValueError('Default students length is higher than max')
        for student in defaultStudents:
            self.__students.add(student)

    def addStudent(self, name):
        if (len(self.__students) == self.__max):
            raise ValueError('Course is full')
        self.__students.add(name)
    def studentInClass(self, studentName):
        return studentName in self.__students

courses = {
  'AI': Course(max=6, defaultStudents=['bob', 'fred', 'josh', 'gabrielle', 'jeff', 'kalven']),
  'CLOUD': Course(max=2)
}
def enroll_student(studentName, courseName):
    if not courseName in courses:
        raise ValueError('Course does not exist')
    courses[courseName].addStudent(studentName)
try:
    enroll_student(courseName='UI/UX', studentName='Bob')
    raise Exception('Did not raise course does not exist exception')
except ValueError as e:
    assert str(e) == 'Course does not exist'
try:
    enroll_student(courseName='AI', studentName='Kyle')
    raise Exception('Did not raise course is full')
except ValueError as e:
    assert str(e) == 'Course is full'

assert courses['AI'].studentInClass(studentName='Kalven') == False
enroll_student(courseName='CLOUD', studentName='Kalven')
assert courses['AI'].studentInClass(studentName='Kalven') == True
