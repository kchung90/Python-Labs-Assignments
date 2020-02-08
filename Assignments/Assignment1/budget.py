"""
@author Kevin Chung

This module holds information about the 4 budget categories used in the
F.A.M. system.

Each budget category has their own budget limits and hold amount spent
for each budget. Budgets can be locked depending on the amount spent
and the type of the user.
"""
import enum


class Budget:
    """
    Represent a budget of one category for the user.
    """
    def __init__(self, budget_type, total_budget):
        """
        Initialize the budget object
        :param budget_type: category of the budget as a String
        :param total_budget: total limit for the budget as a float
        """
        self.budget_type = budget_type
        self._total_budget = total_budget
        self._budget_spent = 0
        self._budget_remaining = total_budget
        self._is_locked = False

    @property
    def total_budget(self):
        """
        Return the amount of the total budget
        :return: total budget as a float
        """
        return self._total_budget

    @property
    def budget_spent(self):
        """
        Return the budget amount spent
        :return: amount spent as a float
        """
        return self._budget_spent

    @property
    def budget_remaining(self):
        """
        Return the budget amount remaining
        :return: budget amount remaining as a float
        """
        return self._budget_remaining

    @property
    def is_locked(self):
        """
        Return the status of the budget
        :return: True if the budget is locked
        """
        return self._is_locked

    def __str__(self):
        """
        Return the description of the budget object
        :return: the description as a String
        """
        return "%-20s%-20s%-20s%-20s%s" % (f"{self.budget_type}",
                                           f"${self.total_budget:.2f}",
                                           f"${self.budget_spent:.2f}",
                                           f"${self.budget_remaining:.2f}",
                                           f"{self.get_lock_status()}")

    def get_lock_status(self):
        """
        Return the status of the budget. Used to find out whether the
        budget is locked or not.
        :return: status of the budget as a String
        """
        if self.is_locked:
            return "Locked"
        return "Unlocked"


class BudgetTypes(enum.Enum):
    """
    Store information about each of 4 budget categories as enumerates.
    """
    GAMES = 1
    CLOTHING = 2
    FOOD = 3
    MISC = 4
