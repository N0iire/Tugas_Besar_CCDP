from member import Member
from membership_decorator import MembershipDecorator
from point_reward_decorator import PointRewardDecorator

def main():
    # Membuat objek member dasar
    member = Member("John")

    # Menerapkan decorator untuk menambahkan fitur keanggotaan dan poin reward
    premium_member = MembershipDecorator(member, "premium")
    premium_member_with_points = PointRewardDecorator(premium_member, 100)

    # Memanggil metode get_membership_info setelah diterapkan decorator
    print(premium_member_with_points.get_membership_info())

if __name__ == "__main__":
    main()
