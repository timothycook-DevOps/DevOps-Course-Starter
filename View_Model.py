import ApiAccess as api


class ViewModel:

    def __init__(self):
        # self.items = []
        self.todoItems = []
        self.doingItems = []
        self.doneItems = []
    """
    def get_items(self):
        return self.items
    """

    def get_todo_items(self):
        return self.todoItems

    def get_doing_items(self):
        return self.doingItems

    def get_done_items(self):
        return self.doneItems

    """
    def add_items(self):
        obj1 = api.AccessTrelloApi()

        Items1 = obj1.getCardsFromTrelloList(
            api.TODOLISTURL, 'To Do')

        Items3 = obj1.getCardsFromTrelloList(
            api.DOINGLISTURL, 'Doing')

        Items2 = obj1.getCardsFromTrelloList(
            api.DONELISTURL, 'Done')

        self.items = Items1 + Items3 + Items2
    """

    def add_todo_items(self):
        obj1 = api.AccessTrelloApi()
        self.todoItems = obj1.getCardsFromTrelloList(
            api.TODOLISTURL, 'To Do')

    def add_doing_items(self):
        obj1 = api.AccessTrelloApi()
        self.doingItems = obj1.getCardsFromTrelloList(
            api.DOINGLISTURL, 'Doing')

    def add_done_items(self):
        obj1 = api.AccessTrelloApi()
        self.doneItems = obj1.getCardsFromTrelloList(
            api.DONELISTURL, 'Done')


"""
obj2 = ViewModel()

obj2.add_items()

print(obj2.get_items())
"""
