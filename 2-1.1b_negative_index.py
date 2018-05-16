#-*- coding: utf-8 -*-
# @Author: Antero Maripuu <machinelearningxl>
# @Date:   2018-05-13-21-08
# @Email:  antero.maripuu@gmail.com
# @Project: -Microsoft-DEV274x-Introduction-to-Python-Fundamentals-
# @Filename: 2-1.1b_negative_index
# @Last modified by:   Antero Maripuu
# @Last modified time: 21:08

student_name="Joana"

print(student_name[-1])

end_letter=student_name[-1]
second_last_letter=student_name[-2]

print(student_name,"ends with ", "'"+end_letter+"'")
print(student_name, "has 2nd to last letter of ", "'" + second_last_letter + "'")

#TASK 2

# [ ] assign a string 5 or more letters long to the variable: street_name
# [ ] print the last 3 characters of street_name

# [ ] create and assign string variable: first_name
# [ ] print the first and last letters of name

street_name = "Goulston"
print(street_name[-1])
print(street_name[-2])
print(street_name[-3])

first_name="Antero"
print("First letter of ",first_name,"",first_name[0])
print("Last letter of ",first_name,"",first_name[-1])

#TASK 3

# Fix the Errors

# [ ] Review, Run, Fix the error using string index shoe = "tennis"
# print the last letter print(shoe(-1))

shoe="tennis"
print("Last letter of the word tennis is: ",shoe[-1])
