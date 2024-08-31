def finance_analysis():
    print("Lets ask you some basic questions to get started.")
    income = float(input("What is your monthly income? "))
    food_expenses = float(input("What are your weekly expenses for food? ")) * (30/7)
    rent = float(input("What is your monthly rent? "))
    utilities = float(input("What are your monthly utilities? "))
    other_expenses = float(input("What are your other monthly expenses, (e.g. college loan payment, transport etc.)? "))
    savings = float(input("How much do you save each month? "))

    total_expenses = food_expenses + rent + utilities + other_expenses
    spending = income - (total_expenses + savings)

    #Average expenses/income in US
    NORMAL_RENT = 1563
    NORMAL_UTILITIES = 430
    NORMAL_FOOD = 470
    NORMAL_MSC = 1237
    NORMAL_SALARY = 6200
    NORMAL_SAVINGS = 1500
    NORMAL_SPENDING = 1000


    salary_scale = income/NORMAL_SALARY
    ideal_rent = NORMAL_RENT*salary_scale
    ideal_utilities = NORMAL_UTILITIES*salary_scale
    ideal_food = NORMAL_FOOD*salary_scale
    ideal_msc = NORMAL_MSC*salary_scale
    ideal_savings = NORMAL_SAVINGS*salary_scale
    ideal_spending = NORMAL_SPENDING*salary_scale

    print("Your total monthly expenses are: ", total_expenses)

    if total_expenses > income:
        print("You are spending more than you are making.")
        print("You need to cut back on your expenses.")

    if rent > ideal_rent:
        increased_rent = (rent - ideal_rent)/(ideal_rent)
        print(f"You are spending {round((increased_rent-1)*100)}% more on rent than you should be.")
        print("Consider moving to a cheaper place.")
        print(f"Your ideal rent should be {ideal_rent} per month.")

    if utilities > ideal_utilities:
        increased_utilities = (utilities - ideal_utilities)/(ideal_utilities)
        print(f"You are spending {round((increased_utilities-1)*100)}% more on utilities than you should be.")
        print("Consider using less electricity and water.")
        print(f"Your ideal utilities should be {ideal_utilities} per month.")

    if food_expenses > ideal_food:
        increased_food = (food_expenses - ideal_food)/(ideal_food)
        print(f"You are spending {round((increased_food-1)*100)}% more on food than you should be.")
        print("Consider eating out less and cooking at home more.")
        print(f"Your ideal food expenses should be {ideal_food} per month.")

    if other_expenses > ideal_msc:
        increased_msc = (other_expenses - ideal_msc)/(ideal_msc)
        print(f"You are spending {round((increased_msc-1)*100)}% more on other expenses than you should be.")
        print("Consider cutting back on your misellaneous expenses.")
        print(f"Your ideal other expenses should be {ideal_msc} per month.")

    if savings < ideal_savings:
        decreased_savings = (ideal_savings - savings)/(ideal_savings)
        print(f"You are saving {round((decreased_savings-1)*100)}% less than you should be.")
        print("Consider saving up more.")
        print(f"Your ideal savings should be {ideal_savings} per month.")

    if spending > ideal_spending:
        increased_spending = (spending - ideal_spending)/(ideal_spending)
        print(f"You are spending {round((increased_spending-1)*100)}% more than you should be.")
        print("Consider saving more.")
        print(f"Your ideal 'fun' spending should be {ideal_spending} per month.")

def split_bill():
    print("Lets ask you some basic questions to get started.")
    total = float(input("What was the bill? "))
    num_people = int(input("How many people are splitting the bill? "))
    tax = input("What is the tax on the bill (can be in percentage or amount)? ").strip()
    tip = input("What is the tip on the bill (can be in percentage or amount)").strip()
    if tax[-1] == "%":
        tax = float(tax[:-1])/100 * total
    else:
        tax = float(tax)
    if tip[-1] == "%":
        tip = float(tip[:-1])/100 * total
    else:
        tip = float(tip)
    total = total + tax + tip
    print("The total bill is: ", total)
    print("Each person should pay: ", total/num_people)

    print("Would you like to split the bill in unequal manner (y/n)?")
    choice = input().strip().lower()
    if choice in {'n','no','nada','nope'}:
        return

    names = []
    for i in range(0, num_people):
        names.append(input(f"Enter the name of person {i+1}: "))
    
    amounts = [0 for i in range(0, num_people)]

    current_bill = 0

    while current_bill < total:
        print(f"The current remaining bill to split is {total - current_bill}.")
        print("How would you like to modify the split?")
        print("1. Add a fixed amount to a person's bill (e.g. person 1 pays $5 of the bill or 5% of the bill before split)")
        print("2. Split the remaining bill in an equal ratio.")
        print("3. Split the remaining bill in a custom ratio.")
        print("4. Split a certain amount of the bill in a custom ratio.")
        choice = None
        while choice not in [i for i in range(1, 5)]:
            try:
                choice = int(input("Enter your choice number: "))
            except:
                print("Invalid input. Please enter a number.")
        
        if choice == 1:
            person = input("Enter the name of the person: ").lower()
            index = None
            for i in range(0, num_people):
                if names[i].lower() == person:
                    index = i
                    break
            if index == None:
                print("Person not found.")
                continue
            amount = input("Enter the amount to add to the bill: ")
            if amount[-1] == "%":
                amount = float(amount[:-1])/100 * total
            else:
                amount = float(amount)
            amounts[index] += amount
            current_bill += amount
        elif choice == 2:
            for i in range(0, num_people):
                amounts[i] += (total - current_bill)/num_people
            current_bill = total
        elif choice == 3:
            ratios = []
            for i in range(0,num_people):
                while True:
                    try:
                        ans = input(f"Enter the ratio for {names[i]}: ")
                        if ans[-1] == "%":
                            ans = ans[:-1]
                        ratios.append(float(ans))
                        break
                    except:
                        print("Invalid input. Please enter a number.")

            total_ratio = sum(ratios)
            for i in range(0, num_people):
                amounts[i] += (total - current_bill) * (ratios[i]/total_ratio)
        elif choice == 4:
            amount = input("Enter the amount to split: ")
            if amount[-1] == "%":
                amount = (float(amount[:-1])/100) * total
            else:
                amount = float(amount)
            ratios = []
            for i in range(0,num_people):
                while True:
                    try:
                        ans = input(f"Enter the ratio for {names[i]}: ")
                        if ans[-1] == "%":
                            ans = ans[:-1]
                        ratios.append(float(ans))
                        break
                    except:
                        print("Invalid input. Please enter a number.")

            total_ratio = sum(ratios)
            for i in range(0, num_people):
                amounts[i] += amount * (ratios[i]/total_ratio)
            current_bill += amount
    
    print(f"\nHere is the final bill: ")
    for i in range(0, num_people):
        print(f"{names[i]} should pay {amounts[i]}.")

print("Welcome to the finance manager!")
print("\nWhat would you like to do?")
print("1. Analyze your finances (income, expenses, savings etc.)")
print("2. Split a bill between multiple people (includes custom splits!)")
choice = None
print("")
while choice not in [i for i in range(1, 3)]:
    try:
        choice = int(input("Enter your choice number: "))
    except:
        print("Invalid input. Please enter a number.")

if choice == 1:
    finance_analysis()
elif choice == 2:
    split_bill()
