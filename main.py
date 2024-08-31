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
