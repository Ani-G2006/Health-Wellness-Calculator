
from store import get_path
a=1
while a>0:
    choice=int(input("1 for calculate(BMI, BMR, Ideal Weight, Ideal Waterintake, Required Calorie)\n2 for View History\n3 for delete data\n4 for exit\nEnter any one: "))
    match choice:
        case 1:
            while a>0:
                choice1 = int(input("1 for BMI\n2 for daily minimum water intake\n3 for calculate bmr\n4 required calorie\n5 for ideal weight\n6 for exit\nEnter any one: "))
                match choice1:
                    case 1:
                        from calculator import calculate_bmi, BMI
                        from store import save_new_entries
                        before = len(BMI)
                        calculate_bmi()
                        save_new_entries(BMI, before, "BMI_data.txt")   
                    case 2:
                        from calculator import daily_water_intake, Waterintake
                        from store import save_new_entries
                        before = len(Waterintake)
                        daily_water_intake()
                        save_new_entries(Waterintake, before, "Waterintake_data.txt")
                    case 3:
                        from calculator import calculate_bmr, BMR
                        from store import save_new_entries
                        before = len(BMR)
                        calculate_bmr()
                        save_new_entries(BMR, before, "BMR_data.txt")
                    case 4:
                        from calculator import required_calorie, Calorie
                        from store import save_new_entries
                        before = len(Calorie)
                        required_calorie()
                        save_new_entries(Calorie, before, "calorie_data.txt")
                    case 5:
                        from calculator import ideal_weight, Weight
                        from store import save_new_entries
                        before = len(Weight)
                        ideal_weight()
                        save_new_entries(Weight, before, "Weight_data.txt")
                    case 6:
                        break
                    case _:
                        print("Invalid choice")
                    
            choice2 = int(input("1 View History \n2 to Exit\nEnter any one: ")) 
            match choice2:
                case 1:                                         
                    while a>0:
                        choice3 = int(input("1 for BMI\n2 for daily minimum water intake\n3 for calculate bmr\n4 required calorie\n5 for ideal weight\n6 for stop\nEnter any one: "))
                        from store import view_file
                        match choice3:
                            case 1:
                                view_file("BMI_data.txt")
                            case 2:
                                view_file("Waterintake_data.txt")
                            case 3:
                                view_file("BMR_data.txt")
                            case 4:
                                view_file("Calorie_data.txt")
                            case 5:
                                view_file("Weight_data.txt")
                            case 6:
                                print("BYE")
                                break
                            case _:
                                print("Invalid choice")
                case 2:
                    print('BYE') 
                case _:
                    print("Invalid choice")
        case 2:
            while a>0:
                choice3 = int(input("1 for BMI\n2 for daily minimum water intake\n3 for calculate bmr\n4 required calorie\n5 for ideal weight\n6 for stop\nEnter any one: "))
                from store import view_file
                match choice3:
                    case 1:
                        view_file("BMI_data.txt")
                    case 2:
                        view_file("Waterintake_data.txt")
                    case 3:
                        view_file("BMR_data.txt")
                    case 4:
                        view_file("Calorie_data.txt")
                    case 5:
                        view_file("Weight_data.txt")
                    case 6:
                        print("BYE")
                        break
                    case _:
                        print("Invalid choice")
        case 3:
            while a>0:
                from store import file_delete
                choice3 = int(input("1 for BMI\n2 for daily minimum water intake\n3 for calculate bmr\n4 required calorie\n5 for ideal weight\n6 for stop\nEnter any one: "))
                match choice3:
                    case 1:
                        file_delete("BMI_data.txt")
                    case 2:
                        file_delete("Waterintake_data.txt")
                    case 3:
                        file_delete("BMR_data.txt")
                    case 4:
                        file_delete("Calorie_data.txt")
                    case 5:
                        file_delete("Weight_data.txt")
                    case 6:
                        print("Thank You")
                        break
                    case _:
                        print("Invalid choice")
        case 4:
            print("Thank You")
            break
    
            