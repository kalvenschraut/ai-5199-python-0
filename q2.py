currentCourses = {}
def add_course(name, credits):
    currentCourses[name] = credits
    return currentCourses

assert len(currentCourses) == 0
updatedDict = add_course('AI', 3)
assert len(currentCourses) == 1
assert currentCourses['AI'] == 3
assert currentCourses['AI'] == updatedDict['AI']
updatedDict = add_course('CLOUD', 3)
assert len(currentCourses) == 2
assert currentCourses['CLOUD'] == 3
assert updatedDict['CLOUD'] == currentCourses['CLOUD']
updatedDict = add_course('UI/UX', 2)
assert len(currentCourses) == 3
assert updatedDict['UI/UX'] == 2
assert updatedDict['UI/UX'] == currentCourses['UI/UX']
print('All tests passed');
