import ApiAccess as api
from datetime import datetime


class ViewModel:

    def __init__(self):
        self._todoItems = []
        self._doingItems = []
        self._recent_done_items = []
        self._older_done_items = []
        self._doneItems = []
        self.apiInterface = api.AccessTrelloApi()

    @property
    def get_todo_items(self):
        return self._todoItems

    @property
    def get_doing_items(self):
        return self._doingItems

    @property
    def recent_done_items(self):
        return self._recent_done_items

    @property
    def older_done_items(self):
        return self._older_done_items

    @property
    def show_all_done_items(self):
        return self._doneItems

    def seperate_done_items(self):
        self._recent_done_items.clear()
        self._older_done_items.clear()
        noOfItems = len(self._doneItems)
        if noOfItems < 5:
            self._recent_done_items = self._doneItems.copy()
        else:
            today = datetime.today().strftime('%Y-%m-%d')
            for item in self._doneItems:
                if item['date'] == today:
                    self._recent_done_items.append(item)
                else:
                    self._older_done_items.append(item)

    def add_items(self):
        self._todoItems = self.apiInterface.getCardsFromTrelloList(
            api.TODOLISTURL, 'To Do')

        self._doingItems = self.apiInterface.getCardsFromTrelloList(
            api.DOINGLISTURL, 'Doing')

        self._doneItems = self.apiInterface.getCardsFromTrelloList(
            api.DONELISTURL, 'Done')

    def create_new_item(self, itemName):
        self.apiInterface.AddItemTodoList(itemName)

    def complete_item(self, itemName):
        self.apiInterface.MarkItemAsDone(itemName)

    def start_item(self, itemName):
        self.apiInterface.MarkItemAsDoing(itemName)
