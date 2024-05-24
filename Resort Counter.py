#Let's make a resort counter
print("Welcome to Jeet's Resorts.")
name = input("What's your name? ")
print("Hello " + name + ", what would you like? ")
choice = input("A normal room or a penthouse? ")

if choice == "penthouse" :
  price = str(1200)
  choice = "Penthouse"

else:
  price = str(800)
  choice = "Normal room"
  
print("A " + choice + " will cost $" + price + ".")
room = str(input(choice + " 101, 102, 103, 104 and 105 are available. Which one would you like? "))
print("Here's your key to your " + choice + " no. " + room + ".")
print("If you want any sevices you can go to our services counter.")
print("Thank you for your visit!")



