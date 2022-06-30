import register
import login

print("Welcome to the Crowd-Funding console app.\n")
print("Options: r:Register | l:Login | e:Exit\n")
while True:
    option = input("Please choose l for login, r for registered or e for exit : ")
    print("\n")
    if option == "l":
        login.login()
    elif option == "r":
        register.register()
    elif option == "e":
        break
    else:
        print(option + " is not an option")

print("Shutting down...")
