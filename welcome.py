from datetime import datetime

def greet_user():
    name = input("Please enter your name: ")
    current_hour = datetime.now().hour

    if 5 <= current_hour < 12:
        greeting = "Good morning"
    elif 12 <= current_hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    print(f"{greeting}, {name}!")

if __name__ == "__main__":
    greet_user()