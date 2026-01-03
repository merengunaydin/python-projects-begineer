def print_development_period(gender_f, age_f):
    if(gender_f == "M" or gender_f == "m"):
        if(age_f < 3):
            print("Baby Boy")
        elif(age_f < 11):
            print("Child Boy")
        elif(age_f < 18):
            print("Adolescent Boy")
        elif(age_f < 30):
            print("Young Man")
        elif(age_f < 60):
            print("Adult Man")
        else:
            print("Old Man")
    else:
        if(age_f < 3):
            print("Baby Girl")
        elif(age_f < 11):
            print("Child Girl")
        elif(age_f < 18):
            print("Adolescent Girl")
        elif(age_f < 30):
            print("Young Woman")
        elif(age_f < 60):
            print("Adult Woman")
        else:
            print("Old Woman")


gender = input("Enter Gender (M/F) (m/f): ")
age = int(input("Enter Age: "))

print_development_period(gender, age)