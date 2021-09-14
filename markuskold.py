
print("Welcome, i can help you to calculate your rate and total money bla")
#Welcome message.

yearlysavings=int(input("Tell me how much you will save each year by printing it in the terminal?"))
#Get user to tell us the amount of savings each year. Create variabel and input.

bankrate= int(input("Please tell me how much your rate is"))
#Get user to tell us the rate on his bank. Create variabel and input.

yearstosave=int(input("please tell us how many years you will save?"))
#Get user to tell us how many years he will save money. Create variabel and input.

sumofrate= yearlysavings*pow((1+ bankrate/100), yearstosave)-yearlysavings
#calculate the rate. Create variabel and calculate the variabels. 

totalcash=yearlysavings*pow((1+ bankrate/100), yearstosave)
#calculate how much money the user have in x years. Create variabel and calculate the variabels. 

print(int(f"in {yearstosave} years your rate is {sumofrate} and the total money on your account is {totalcash}"))
# tell the user how much rate it will be and the total sum by using format and the  variabels. 
