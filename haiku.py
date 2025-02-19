import random
import json

class HaikuApp:
    def __init__(self):
        self.haiku_file = "haikus.txt"
        self.haiku_db = "haikus.json"
        self.load_haiku_data()

    def load_haiku_data(self):
        try:
            with open(self.haiku_db, "r") as file:
                self.haikus = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.haikus = {"love": [], "happy": [], "sadness": []}

    def save_haiku_data(self):
        with open(self.haiku_db, "w") as file:
            json.dump(self.haikus, file, indent=4)

    def generate_random_haiku(self):
        theme = input("Choose a theme (love/happy/sadness): ").lower()
        if theme in self.haikus and self.haikus[theme]:
            haiku = random.choice(self.haikus[theme])
            print("\nRandom Haiku:\n")
            print(haiku)
        else:
            print("No haikus found for this theme!")

    def add_haiku_to_theme(self):
        theme = input("Choose a theme to add to (love/happy/sadness): ").lower()
        if theme not in self.haikus:
            print("Invalid theme.")
            return
        line1 = input("Enter Line 1: ")
        line2 = input("Enter Line 2: ")
        line3 = input("Enter Line 3: ")
        haiku = f"{line1}\n{line2}\n{line3}"
        self.haikus[theme].append(haiku)
        self.save_haiku_data()
        print("Haiku added to theme successfully!")

    def save_haiku(self, haiku): 
        with open(self.haiku_file, "a") as file:
            file.write(haiku + "\n\n")
        print("Haiku saved successfully!")

    def view_saved_haikus(self):
        try:
            with open(self.haiku_file, "r") as file:
                print("\nPast Haikus:")
                print(file.read())
        except FileNotFoundError:
            print("No saved haikus found.")

    def generate_custom_haiku(self):  
        line1 = input("Enter Line 1: ")
        line2 = input("Enter Line 2: ")
        line3 = input("Enter Line 3: ")
        haiku = f"{line1}\n{line2}\n{line3}"
        print("\nYour Custom Haiku:\n")
        print(haiku)
        self.save_haiku(haiku)  

    def main_menu(self):
        while True:
            print("\nHaiku App Menu:")
            print("1. Generate a Custom Haiku")
            print("2. View Saved Haikus")
            print("3. Generate a Random Haiku from Theme")
            print("4. Add a Haiku to a Theme")
            print("5. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                self.generate_custom_haiku()  
            elif choice == "2":
                self.view_saved_haikus()
            elif choice == "3":
                self.generate_random_haiku()
            elif choice == "4":
                self.add_haiku_to_theme()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, try again.")

if __name__ == "__main__":
    app = HaikuApp()
    app.main_menu()