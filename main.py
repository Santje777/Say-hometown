
hometown = "Groningen"
country_of_birth = "The Netherlands"
celsius = 27
fahrenheit = (celsius * 9 / 5) + 32
    
print(country_of_birth[0:4].upper() + hometown[0:7] + country_of_birth[8:10])
print(celsius)
print(fahrenheit)
print(round(fahrenheit))
print(hometown.strip("n"))
print(hometown.replace("n", "x"))
print(f"In {hometown} it is {celsius} celius and {fahrenheit} fahrenheit")
    
sentence = f"I am from {hometown}, in {country_of_birth}. The first three letters of my country are {country_of_birth[0:3].upper()}"
    
print(sentence)