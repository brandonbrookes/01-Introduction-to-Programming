print("\nWelcome to the Weather Converter")

while True:
    def endScreen():
        if tempScale == 1:
            celsiusTemp = initTemp
            farenheitTemp = conTemp
        elif tempScale ==2:
            celsiusTemp = conTemp
            farenheitTemp = initTemp
        #ensures that the end screen is printed with the correct information in the right spaces
        
        print("\n///////////////////////")
        print("Your temperature in Celsius: ",(celsiusTemp),"°C ","\n")
        print("Your temperature in Farenheit: ",(farenheitTemp),"°F","\n")
        print("Thank you for using our temperature converter!")
        print("///////////////////////\n")
    
    print("Please enter your temperature to be converted: ")

    while True:
    #gets the users initial temeprature to be converted
        try:
            initTemp = float(input())
            break
        except ValueError:
            print("\nPlease enter a valid number")
        
    while True:
     #asks the user what the initial tememperatures scale is, basically if its in farenheit or celsius
        try:
            tempScale = int(input("Please enter your initial temperature scale (1 for Celsius, 2 for Farenheit): \n"))
            break
        except ValueError:
            print("\nPlease enter a valid number")

    if tempScale == 1:
        #converting from celcius to farenheit
        conTemp = (initTemp * 9/5) + 32 
        endScreen()
    elif tempScale == 2:
        #converting from farenheit to celcius
        conTemp = (initTemp - 32) * 5/9
        endScreen()
    else:
        print("Invalid input, please select 1 for celsius, or 2 for farenheit")
    end = input("End Program? y/n \n")
    if end == "y":
        exit()
    else:
        continue
    




