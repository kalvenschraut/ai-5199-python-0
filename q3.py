filePath = input('Path to students file (./files/students.txt) ').strip() or './files/students.txt';
file = open(filePath, 'r');
GPA = {
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'D-': 0.7,
    'F': 0.0
}
inverse_GPA = {number: letter for letter, number in GPA.items()}

sum = 0;
count = 0;
for line in file:
    sum += int(GPA[line.split(',')[1].strip()])
    count += 1
average = sum/count;
def printGrade(grade):
    print("Average grade is", grade)
try:
    printGrade(inverse_GPA[round(average, 1)]);
except:
    lowestDifference = ['A', 4.0]
    for gpa,letter in inverse_GPA.items():
        diff = round(abs(gpa - average), 2)
        # less than .3 then for sure found our target
        if diff < .3:
            lowestDifference = [letter, diff];
            break;
        elif diff < lowestDifference[1]:
            lowestDifference = [letter, diff];
    printGrade(lowestDifference[0]);
