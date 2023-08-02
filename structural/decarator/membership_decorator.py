from member import Member

class MembershipDecorator(Member):
    def __init__(self, member, membership_type):
        super().__init__(member.name)
        self.member = member
        self.membership_type = membership_type

    def get_membership_info(self):
        return f"{self.member.get_membership_info()} They have a {self.membership_type} membership."
