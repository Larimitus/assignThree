print("ISQA 3900 Letter Grade Calculator\n")

print("Enter total number of points earned:\t")
gradeValue = input()
gradeValue = float(gradeValue)

letterGrade = ""
if gradeValue > 919.9:
    letterGrade = "A"
elif gradeValue > 879.9:
    letterGrade = "B+"
elif gradeValue > 819.9:
    letterGrade = "B"
elif gradeValue > 779.9:
    letterGrade = "C+"
elif gradeValue > 699.9:
    letterGrade = "C"
elif gradeValue > 600:
    letterGrade = "D"
else:
    letterGrade = "F"

print("Letter grade: ", letterGrade)
