grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
	for a in grades_input:
		print (a)
    


print("The grades are :")
print_grades(grades)

def grades_sum(scores):
  total=0
  for a in scores:
    total+=a
  return total

print ("The sum of the gardes are :",grades_sum(grades))

def grades_average(grades_input):
	return (grades_sum(grades_input)/float(len(grades_input)))

print("the gardes average is",grades_average(grades))

def grades_variance(scores):
	average=grades_average(scores)
	variance=0
	for a in scores:
		variance+=(average - a) ** 2
	return variance/float(len(scores))


print ("The grades varaince is",grades_variance(grades))

def grades_std_deviation(variance):
	return variance**0.5

variance=grades_variance(grades)
print("The std Deviation is",grades_std_deviation(variance))



