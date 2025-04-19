from pet import Pet

def main():
    print("🐶 Welcome to Digital Pet Simulator! 🐱")
    
    # Create pet
    pet_name = input("What would you like to name your pet? ")
    pet = Pet(pet_name)
    print(f"\nMeet your new pet, {pet_name}!")
    
    # Main game loop
    while True:
        print("\nWhat would you like to do?")
        print("1. Feed your pet")
        print("2. Put your pet to sleep")
        print("3. Play with your pet")
        print("4. Check pet status")
        print("5. Teach a new trick")
        print("6. Show learned tricks")
        print("7. Quit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            print(pet.eat())
        elif choice == "2":
            print(pet.sleep())
        elif choice == "3":
            print(pet.play())
        elif choice == "4":
            print(pet.get_status())
        elif choice == "5":
            trick = input("What trick would you like to teach? ")
            print(pet.train(trick))
        elif choice == "6":
            print(pet.show_tricks())
        elif choice == "7":
            print(f"Goodbye! {pet.name} will miss you!")
            break
        else:
            print("Invalid choice. Please enter a number 1-7.")

if __name__ == "__main__":
    main()