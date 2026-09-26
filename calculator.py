# Calculate BMI

BMI=[]

def calculate_bmi():
    date=input("Enter date(DD/MM/YYYY): ")

    a=1
    while a>0:
        name=input('Enter your name: ')
        entry = {"Date": date, "Name": name}

        height=float(input("enter your hight(inch): "))
        weight=float(input("enter your weight(Kg) : "))
        height=(height/39.3701)
        bmi=weight/(height**2)
        entry["BMI"]=bmi
        print("your BMI is:",bmi)

        if bmi<18.5:
            print("Underweight")
            entry["Nature"]='Underweight'
        elif bmi>=18.5 and bmi<25:
            entry["Nature"]='Healthy'
            print("Healthy")
        elif bmi>=25 and bmi<30:
            entry["Nature"]="Overweight"
            print("Overweight")
        elif bmi>=30 and bmi<35:
            entry["Nature"]="Obesity(class 1)"
            print("Obesity(class 1)")
        elif bmi>=35 and bmi<40:
            entry["Nature"]="Obesity(class 2)"
            print("Obesity(class 2)")
        elif bmi>=40:
            entry["Nature"]="Obesity(class 3)"
            print("Obesity(class 3)")  
        BMI.append(entry)  


        choice = int(input("1 to calculate again\n2 to stop \nenter any one: "))
        match choice:
            case 1:
                print("count no: ",a)
            case 2:
                break
            case _:
                print("Invalid choice")


# calculate bmr

BMR=[]

def calculate_bmr():
    date=input("Enter date(DD/MM/YYYY): ")

    a=1
    while a>0:
        name=input("Enter your name: ")
        entry = {"Date": date, "Name": name}
        
        weight=float(input("Enter your weight(Kg): "))
        height=float(input("Enter your height(inch): "))
        age=int(input("Enter your age(years): "))
   
        choice = int(input("1 for male\n2 for women\nenter any one: "))
        match choice:
            case 1:
                bmr= (10 * weight) + (6.25 * (height*2.54)) - (5 * age) + 5
                entry["BMR"]=bmr
                BMR.append(entry)
                print(bmr)
            case 2:
                bmr = (10 * weight) + (6.25 * (height*2.54)) - (5 * age) - 161
                print(bmr)
                BMR.append(entry)
                entry["BMR"]=bmr
            case _:
                print("Invalid choice")

        choice2 = int(input("1 to calculate again\n2 to stop \nenter any one: "))
        match choice2:
            case 1:
                print("count no: ",a)
            case 2:
                break
            case _:
                print("Invalid choice") 


# ideal weight calculation

Weight=[]

def ideal_weight():
    date=input("Enter date(DD/MM/YYYY): ")

    a=1
    while a>0:
        name=input("Enter your name: ")
        entry={"Date":date,"Name":name}
        
        height=float(input("enter your height(inch): "))

        choice = int(input("1 for male\n2 for women\n enter any one: "))
        match choice:
            case 1:
                weight=50+(2.3*(height-60))
                entry["Expected Weight"]=weight
                Weight.append(entry)
                print("Expected Weight",weight)
            case 2:
                weight=45.5+(2.3*(height-60))
                entry["Expected Weight"]=weight
                Weight.append(entry)
                print("Expected Weight",weight)
            case _:
                print("Invalid choice")
        choice = int(input("1 to calculate again\n2 to stop \nenter any one: "))
        match choice:
            case 1:
                print("count no: ",a)
            case 2:
                break
            case _:
                print("Invalid choice")


# calori requirment/day

Calorie=[]

def required_calorie():
    date=input("Enter date(DD/MM/YYYY): ")

    a=1
    while a>0:
        name=input("Enter your name: ")
        entry = {"Date": date, "Name": name}
        
        bmr=float(input("enter your bmr: "))

        choice=int(input("1 for Sedentary(no exercise)\n2 for Lightly active(light exercise)\n3 for Moderately active(moderate exercise)\n4 for Very active(hard exercise)\n5 for Extra active(very hard exercise)\nEnter any one: " ))
        match choice:
            case 1:
                calorie=bmr*1.2
                entry["Minium Calorie"]=calorie
                Calorie.append(entry)
                print("minimum calorie required: ",calorie)
            case 2:
                calorie=bmr*1.375
                entry["Minium Calorie"]=calorie
                Calorie.append(entry)
                print("minimum calorie required: ",calorie)
            case 3:
                calorie=bmr*1.55
                entry["Minium Calorie"]=calorie
                Calorie.append(entry)
                print("minimum calorie required: ",calorie)
            case 4:
                calorie=bmr*1.725
                entry["Minium Calorie"]=calorie
                Calorie.append(entry)
                print("minimum calorie required: ",calorie)
            case 5:
                calorie=bmr*1.9
                entry["Minium Calorie"]=calorie
                Calorie.append(entry)
                print("minimum calorie required: ",calorie)
            case _:
                    print("Invalid choice")
                    return()
        
        choice = int(input("1 to calculate again\n2 to stop \nenter any one: "))
        match choice:
            case 1:
                print("count no: ",a)
            case 2:
                break
            case _:
                print("Invalid choice")


# calculate daily water intake lavel

Waterintake=[]

def daily_water_intake():
    date=input("Enter date(DD/MM/YYYY): ")
    
    a=1
    while a>0:
        name=input('Enter your name: ')
        entry = {"Date": date, "Name": name}
        
        weight = float(input('Enter your weight(Kg): '))
        activity_level = int(input('1 for sedentary \n2 for moderate \n3 for active\nEnter any one: '))

        if activity_level == 1:
            water_intake = (weight * 30) / 1000
            entry["minimum water intake"]=water_intake,"L"
            Waterintake.append(entry)
            print("minimum water intake",water_intake, "L")
        elif activity_level == 2:
            water_intake = (weight * 35) / 1000
            Waterintake.append(entry)
            entry["minimum water intake"]=water_intake,"L"
            print("minimum water intake",water_intake, "L")
        elif activity_level == 3:
            water_intake = (weight * 40) / 1000
            Waterintake.append(entry)
            entry["minimum water intake"]=water_intake,'L'
            print("minimum water intake",water_intake, "L")
        else:
            print("Invalid activity level")

        choice = int(input("1 to calculate again\n2 to stop \nenter any one: "))
        match choice:
            case 1:
                print("count no: ",a)
            case 2:
                break
            case _:
                print("Invalid choice")
 