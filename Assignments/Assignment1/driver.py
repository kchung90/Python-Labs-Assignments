"""
@author Kevin Chung

This module drives the Family Appointed Moderator (F.A.M.) program
which monitors the user's expenses in each category of budget.

This module provides the UI to enter user inputs to select menu to
perform tasks.
"""
from Assignments.Assignment1.user import User


class Driver:
    """
    Driver class interacts with the user by providing the menu and
    asking for user inputs.

    A user can register himself first, then use menu options to perform
    any desired tasks until he decides to exit the program.

    More features on the menu are to be added in the future.
    """
    def __init__(self):
        """
        Initializes the driver object
        """
        self.user = None

    def register_user(self):
        """
        Register a user to the program. Calls a method to add a bank
        account for the user.
        """
        input_name = input("\nEnter the user's name: ")
        input_age = int(input("Enter the user's age: "))

        self.user = User(input_name, input_age)
        self.user.add_bank_account()

    def menu(self):
        """
        Show menu prompts to the user. A user can perform actions by
        following the prompts until he decides to exit the program.

        :precondition: a user must input correct type for each prompt
        """
        print("-" * 50)
        print("{0:^50}".format("Family Appointed Moderator"))
        print("-" * 50)

        input_option = None
        input_menu = None

        while input_option != 1 and input_option != 2:
            print("\nPlease select an option:")
            input_option = int(input("1) Register a new user\n"
                                     "2) Load test users\n"))
            if input_option == 1:
                self.register_user()
            elif input_option == 2:
                self.user = User.load_test_user()

        while input_menu != 2:
            input_menu = int(input("\nSelect the following menu:\n"
                                   "1) Record Transaction\n"
                                   "2) Quit\n"))
            if input_menu == 1:
                self.record_transaction()

    def record_transaction(self):
        """
        Initiate to create a transaction. Successful transactions are
        recorded in the list of transactions in the bank account object
        and printed out.
        """
        self.user.bank_account.process_transaction()


def main():
    """
    Drives the program by creating a Driver object and calling the
    menu method
    """
    driver = Driver()
    driver.menu()


if __name__ == '__main__':
    main()
