class Team:
    def __init__(self):
        self.members = ["Alice", "Bob", "Charlie"]
    def __contains__(self,name):
        # returns True if the specified name is in the members list, otherwise it returns False

        return name in self.members
#only need to call the class and use the in operator to check if the name is in the members list or not
mem=Team()
print("Alice" in mem)
        
    