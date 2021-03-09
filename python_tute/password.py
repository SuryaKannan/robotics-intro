#Make a random password generator
import random
lower_characters="abcdefghijklmnopqrstuvwxyz"#use string as a list start counting from 0 lower_characters[0]="a"
upper_characters=lower_characters.upper() #convert the list above to capitals
num_special_characters="0123456789!@#$%^&*()<>?-_+="
#make a list of the 3 lists above
lst=[lower_characters,upper_characters,num_special_characters]
#Get user to enter length of password they want
len=int(input("How long would you like your password?"))
password="" #intialise this variable
for i in range(len):
    a=#Write your code# choose one of the three lists randomly
    b=#Write your code #  choose one of the elements from the list above
    password+=b
print("Here is your password: "+ password)

#Turn this into a function!!
