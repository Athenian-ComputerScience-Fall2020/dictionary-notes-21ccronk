# Use this to take notes on the Edpuzzle video. Try each example rather than just watching it - you will get much more out of it!
#  

student = {'name': 'john','age': 25, 4:['jellyfish','sea otter']}
print(student['name'])
print(student[4])

student.update({'name':'sara'})

print(student['name'])

#del student['age']
#print(student)

#age = student.pop('age')
#print(25)

for key, value in student.items():
    print(key, value)