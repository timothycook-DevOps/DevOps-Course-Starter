import requests
import os

TODOLISTURL = 'https://api.trello.com/1/lists/5f6f787bf9461c809f224d0d/cards/'
DOINGLISTURL = 'https://api.trello.com/1/lists/5fa80ea247eeb75b38c7259e/cards/'
DONELISTURL = 'https://api.trello.com/1/lists/5f6f7883333c1880d598e148/cards/'

CARDSURL = 'https://api.trello.com/1/cards/'
LISTURL = 'https://api.trello.com/1/lists/'
TODOLISTID = '5f6f787bf9461c809f224d0d'
DOINGLISTID = '5fa80ea247eeb75b38c7259e'
DONELISTID = '5f6f7883333c1880d598e148'

TRELLO_API_KEY = os.environ.get('TRELLO_API_KEY')
TRELLO_SERVER_TOKEN = os.environ.get('TRELLO_SERVER_TOKEN')

class AccessTrelloApi:


    """
    Method used to handle Trello get requests.
    """

    def get_json_data(self, InputValue, payload):
        api_jsondata = requests.get(InputValue, params=payload).json()
        return api_jsondata
    """
        Returns cards from Trello based on the list name.

    """

    def getCardsFromTrelloList(self, ListURL, ListName):
        ApiValue = ListURL
        payload = {'key': TRELLO_API_KEY,
                   'token': TRELLO_SERVER_TOKEN}
        jsondata = requests.get(ApiValue, params=payload).json()
        ReturnList = []
        ListDataDict = {}
        for item in jsondata:
            ListDataDict['id'] = item['id']
            ListDataDict['name'] = item['name']
            ListDataDict['status'] = ListName
            ListDataDict['date'] = item['dateLastActivity'][0:10]
            CopyOfListDataDict = ListDataDict.copy()
            ReturnList.append(CopyOfListDataDict)
        return ReturnList

    """
        Adds and Item to the todo list
    """

    def AddItemTodoList(self, name_of_item):
        ApiValue = CARDSURL
        payload = {'key': TRELLO_API_KEY,
                   'token': TRELLO_SERVER_TOKEN, 'idList': TODOLISTID, 'name': name_of_item}
        requests.post(ApiValue, params=payload)

    """
        Takes item id and adds to the done list
    """

    def MarkItemAsDone(self, ItemID):
        ApiValue = CARDSURL + ItemID
        payload = {'key': TRELLO_API_KEY,
                   'token': TRELLO_SERVER_TOKEN, 'idList': DONELISTID}
        requests.put(ApiValue, params=payload)

    """
        Takes item id and adds to the doing list
    """

    def MarkItemAsDoing(self, ItemID):
        ApiValue = CARDSURL + ItemID
        payload = {'key': TRELLO_API_KEY,
                   'token': TRELLO_SERVER_TOKEN, 'idList': DOINGLISTID}
        requests.put(ApiValue, params=payload)
