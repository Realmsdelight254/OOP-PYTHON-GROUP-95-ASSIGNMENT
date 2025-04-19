class Pet:
    def __init__(self, name):
        """Initialize a new pet with given name and default attributes"""
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
    
    def eat(self):
        """Reduce hunger and increase happiness"""
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        return f"{self.name} ate some food. Yum!"
    
    def sleep(self):
        """Restore energy"""
        self.energy = min(10, self.energy + 5)
        return f"{self.name} took a nap. Zzzzz..."
    
    def play(self):
        """Play with pet, affecting energy, happiness, and hunger"""
        if self.energy >= 2:
            self.energy = max(0, self.energy - 2)
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            return f"{self.name} had fun playing!"
        return f"{self.name} is too tired to play."
    
    def get_status(self):
        """Return a string with current pet status"""
        status = f"\n{self.name}'s Status:\n"
        status += f"Hunger: {self.hunger}/10\n"
        status += f"Energy: {self.energy}/10\n"
        status += f"Happiness: {self.happiness}/10\n"
        
        # Status messages
        if self.hunger >= 8:
            status += f"{self.name} is starving!\n"
        elif self.hunger >= 5:
            status += f"{self.name} could eat.\n"
        
        if self.energy <= 2:
            status += f"{self.name} needs sleep!\n"
        elif self.energy <= 5:
            status += f"{self.name} is getting tired.\n"
        
        if self.happiness <= 2:
            status += f"{self.name} is depressed.\n"
        elif self.happiness <= 5:
            status += f"{self.name} could use some playtime.\n"
        
        return status
    
    # Bonus methods
    def train(self, trick):
        """Teach pet a new trick if they have enough energy"""
        if self.energy >= 3:
            self.energy -= 3
            self.happiness += 1
            self.tricks.append(trick)
            return f"{self.name} learned '{trick}'!"
        return f"{self.name} is too tired to train."
    
    def show_tricks(self):
        """Return a string listing all learned tricks"""
        if not self.tricks:
            return f"{self.name} hasn't learned any tricks yet."
        tricks_list = "\n".join(f"{i+1}. {trick}" for i, trick in enumerate(self.tricks))
        return f"{self.name} knows these tricks:\n{tricks_list}"