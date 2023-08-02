from membership import Member

class MembershipManager:
    def __init__(self):
        self.members = []

    def add_member(self, name, age, address):
        member = Member(name, age, address)
        self.members.append(member)

    def get_member_by_index(self, index):
        return self.members[index]

    def get_all_members(self):
        return self.members

    def clone_member(self, index):
        if index < len(self.members):
            return self.members[index].clone()
        return None
