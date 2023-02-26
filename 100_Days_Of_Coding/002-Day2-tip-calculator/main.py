print("Welcome to the tip calculator!")

bill = input("Enter the amount of the bill: \n$")
tip = input("What is the percentage would you like to give as tip? (E.g. 12%)\n%")
no_ppl = input("How many people to split the bill?\n")

# Results
results = round((float(bill)/int(no_ppl) * (1 + int(tip)/100)), 2)
print(f"The tip you will have to pay is {results:.2f}.")
