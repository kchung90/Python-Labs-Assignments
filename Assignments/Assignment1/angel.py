from Assignments.Assignment1.user import User


class Angel(User):

    def __init__(self, name, age, user_type):
        super().__init__(name, age)
        self.user_type = user_type

    def record_transaction(self, amount, category, shop_name):
        self.bank_account.process_transaction(amount, category, shop_name)
        self.overage_notification(category)
        self.warning_notification(category)

    def overage_notification(self, category):
        if self.bank_account.verify_budget_limit(category):
            print("\nYou have exceeded your total budget for this category.")

    def warning_notification(self, category):
        if self.bank_account.verify_warning_level(category, 0.9):
            print("\nYou have exceeded 90% of your budget for this category.")
