import random 
import string

counter = 0

string2 = []


def generate_password():
  all_signs = list(string.printable)
  sign = str(random.choice(all_signs))
  return sign

while True:
  number_of_signs = int(input("Enter lenght of password (max 100 char):  "))
  if number_of_signs <= 100:
    for counter in range(number_of_signs):
        string2 += generate_password()
        counter += 1
        string3 =''.join(string2)
    print(string3)
    break
  else:
    print("Too many characters!!!")
