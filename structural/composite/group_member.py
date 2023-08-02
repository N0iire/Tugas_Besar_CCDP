from member import Member

class GroupMember(Member):
    def __init__(self, name):
        super().__init__(name)
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member):
        self.members.remove(member)

    def display(self):
        print(f"Group Member: {self.name}")
        for member in self.members:
            member.display()
