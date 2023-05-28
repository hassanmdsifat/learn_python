class User:

    def __init__(self, user_name, total_purchase):
        self.name = user_name
        self.total_purchase = total_purchase


    def get_shipping_cost(self):
        if self.total_purchase > 1000:
            return 40
        return 60


class PremiumUser(User):

    def get_discount(self):
        if self.total_purchase > 2000:
            return 100
        return 20

    def get_shipping_cost(self):
        return 0


premium_user = PremiumUser("sifat_hassan", 2000)
normal_user = User("test_user", 100)

print(premium_user.get_shipping_cost())
print(normal_user.get_shipping_cost())
