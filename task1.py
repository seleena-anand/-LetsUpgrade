def Calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else :
        return "Fail"
        
while True :
    try:
        marks = float(input("Enter marks obtained :"))
        if marks < 0 or marks > 100 :
            raise ValueError("Invaild marks. Please enter marks between 0 to 100")
        grade = Calculate_grade(marks)
        print("Grade : ", grade)
    except ValueError as e:
        print(e)
    choice = input("Do you want to continue ? (y/n) : ").lower()
    if choice == "n":
        break
    
