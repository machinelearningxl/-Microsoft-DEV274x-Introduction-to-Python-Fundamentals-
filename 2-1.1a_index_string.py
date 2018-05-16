student_name="Alton"

print(student_name[0], "<--first character at index 0")
print(student_name[1])
print(student_name[2])
print(student_name[3])
print(student_name[4])

student_name_2="Jin"

if student_name[0].lower()=="a":
  print("Winner! Name starts with A:", student_name_2)
elif student_name_2[0].lower()=="j":
  print("Winner! Name starts with J", student_name_2)
else:
  print("Not a match, try again tomorrow", student_name_2)

  student_name_3="Tobias"

  print(student_name_3[6])


#TASK 1

#[ ] assign a string 5 or more letters long to the variable: street_name
# [ ] print the 1st, 3rd and 5th characters

# [ ] Create an input variable: team_name - ask that second letter = "i", "o", or "u"
# [ ] Test if team_name 2nd character = "i", "o", or "u" and print a message
# note: use if, elif and else

street_name="Goulston Street"

print(street_name[0])
print(street_name[2])
print(street_name[4])

teame_name="Coub Win"
if(teame_name[1].lower()=="i"):
  print("Yes, second letter is ", teame_name[1])
elif(teame_name[1].lower()=="o"):
  print("Yes, second letter is ", teame_name[1])
elif(teame_name[1].lower()=="u"):
  print("Yes, second letter is ", teame_name[1])
else:
  print("Try again!")

