class AllFiveFunctions:
    def subFields():
        lists = ['Machine Learning', 'Neural Networks', 'Vision', 'Robotics', 'Speech Processing', 'Natural Language Processing']
        print("Sub-fields in AI are : ")
        for subfieldsInAI in lists:
            print(subfieldsInAI)

    def oddEven():
        num = int(input("Enter the Number : "))
        if num % 2 == 0:
            print("The given number is an Even Number")
            msg = "Even Number"
        else:
            print("The given number is an Odd Number")
            msg = "Odd Number"
        return msg

    def Eligible():
        gender = input("Enter Your Gender : ")
        age = int(input("Enter the Age : "))
        if gender == 'Male' and age >= 21:
            print("Male Eligible For Marriage")
        elif gender == 'Female' and age >= 18:
            print("Female Eligible For Marriage")
        else:
            print("Not Eligible For Marriage")

    def percentage():
        sub1 = 98
        sub2 = 87
        sub3 = 95
        sub4 = 95
        sub5 = 93
        marks = sub1 + sub2 + sub3 + sub4 + sub5
        Total = marks
        Percentage = Total / 5
        print("Subject1 = ", sub1)
        print("Subject2 = ", sub2)
        print("Subject3 = ", sub3)
        print("Subject4 = ", sub4)
        print("Subject5 = ", sub5)
        print("Total : ", Total)
        print("Percentage : ", Percentage)

    def triangle():
        Height = int(input("Enter Height : "))
        Breadth = int(input("Enter Breadth :"))
        Area = Height * Breadth / 2
        print("The Area of Triangle is : ", Area)
        print("**************************************")
        Height1 = int(input("Enter Height1 : "))
        Height2 = int(input("Enter Height2 : "))
        Breadth1 = int(input("Enter Breadth1 :"))
        Perimeter = Height1 + Height2 + Breadth1
        print("The Perimeter of Triangle is7 : ", Perimeter)