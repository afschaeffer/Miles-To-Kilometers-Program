# Amy Schaeffer
# Calculates the number of kilometers a user drove when they enter the miles, utilizing try and except blocks

print("Welcome to the miles to kilometers calculator")
def m_to_km(miles_inputted):
            """Converts entered miles to kilometers"""
            kilometers = miles_inputted * 1.609
            print(f"{miles_inputted} miles is equal to {kilometers} kilometers.")
while True:
    while True:
        miles = input('How many miles did you drive? : ')
        try:
            value = float(miles)
            print("Thank you for your milage input of ", value)
            m_to_km(value)
            break
        except ValueError:
            print("Input invalid, please enter a number.")
    stay = input('Type "q" to quit, or type anything to return to prompt : ' )
    if stay == "q":
        break
    
    
