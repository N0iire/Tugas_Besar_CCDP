from member import Member

class PointRewardDecorator(Member):
    def __init__(self, member, points):
        super().__init__(member.name)
        self.member = member
        self.points = points

    def get_membership_info(self):
        return f"{self.member.get_membership_info()} They have {self.points} reward points."
