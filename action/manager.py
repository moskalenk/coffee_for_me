from action.common_type import Common


class Manager(Common):
    def __init__(self, name, position="manager"):
        super().__init__(name, position)

    def get_summary(self):
        pass
