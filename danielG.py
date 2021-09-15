# Orginal code written by Markus Sköld

# Welcome message.
print("Welcome, i can help you to calculate your rate and total money")

# Get user to tell us the amount of savings each year. Create variable and input.
yearlysavings = int(input("Tell me how much you will save each year by printing it in the terminal? "))

# Get user to tell us the rate on his bank. Create variable and input.
bankrate = int(input("Please tell me how much your rate is: "))

# Get user to tell us how many years he will save money. Create variable and input.
yearstosave = int(input("please tell for how many years you will save? "))

# calculate the rate. Create variable and calculate the variables.
sumofrate = yearlysavings*pow((1 + bankrate/100), yearstosave)-yearlysavings

# calculate how much money the user have in x years. Create variable and calculate the variables.
totalcash = yearlysavings*pow((1 + bankrate/100), yearstosave)

# tell the user how much rate it will be and the total sum by using format and the variables.
print(f"in {yearstosave} years your rate is {sumofrate} and the total money on your account is {totalcash}")
