import pytest
import View_Model as model
from datetime import datetime

"""
Tests that items completed today go into recent_done_items list and the rest
into the older_done_items list
"""


def test_recent_done_items_today():
    today = datetime.today().strftime('%Y-%m-%d')
    obj1 = model.ViewModel()
    obj1._doneItems = [{'id': '123456', 'name': 'Sweep Yard', 'status': 'Done', 'date': today},
                       {'id': '789456', 'name': 'Prune Trees',
                           'status': 'Done', 'date': today},
                       {'id': '987654', 'name': 'Wash Floor',
                           'status': 'Done', 'date': today},
                       {'id': '987625', 'name': 'Clean Windows',
                           'status': 'Done', 'date': '2021-01-21'},
                       {'id': '963625', 'name': 'Wash Car', 'status': 'Done', 'date': '2021-01-19'}]
    obj1.seperate_done_items()
    assert (len(obj1.recent_done_items) == 3) & (
        len(obj1.older_done_items) == 2)


"""
Tests that items go into recent_done_items as less than 5
"""


def test_done_items_less_than_5_old():
    obj1 = model.ViewModel()
    obj1._doneItems = [{'id': '123456', 'name': 'Sweep Yard', 'status': 'Done', 'date': '2021-01-21'},
                       {'id': '789456', 'name': 'Prune Trees',
                           'status': 'Done', 'date': '2021-01-21'},
                       {'id': '987625', 'name': 'Clean Windows',
                           'status': 'Done', 'date': '2021-01-21'},
                       {'id': '963625', 'name': 'Wash Car', 'status': 'Done', 'date': '2021-01-19'}]
    obj1.seperate_done_items()
    assert (len(obj1.recent_done_items) == 4) & (
        len(obj1.older_done_items) == 0)


"""
Tests that items go into recent_done_items as more than 5
"""


def test_done_items_less_more_5_old():
    obj1 = model.ViewModel()
    obj1._doneItems = [{'id': '123456', 'name': 'Sweep Yard', 'status': 'Done', 'date': '2021-01-21'},
                       {'id': '789456', 'name': 'Prune Trees',
                           'status': 'Done', 'date': '2021-01-21'},
                       {'id': '987625', 'name': 'Clean Windows',
                           'status': 'Done', 'date': '2021-01-21'},
                       {'id': '963625', 'name': 'Wash Car',
                           'status': 'Done', 'date': '2021-01-19'},
                       {'id': '741963', 'name': 'Wash Dishes', 'status': 'Done', 'date': '2021-01-01'}]
    obj1.seperate_done_items()
    assert (len(obj1.recent_done_items) == 0) & (
        len(obj1.older_done_items) == 5)


"""
Tests that items go into recent_done_items 10 items 
"""


def test_recent_done_items_10():
    today = datetime.today().strftime('%Y-%m-%d')
    obj1 = model.ViewModel()
    obj1._doneItems = [{'id': '123456', 'name': 'Sweep Yard', 'status': 'Done', 'date': today},
                       {'id': '789456', 'name': 'Prune Trees',
                           'status': 'Done', 'date': today},
                       {'id': '987654', 'name': 'Wash Floor',
                           'status': 'Done', 'date': today},
                       {'id': '987625', 'name': 'Clean Windows',
                           'status': 'Done', 'date': today},
                       {'id': '963626', 'name': 'Wash Car',
                           'status': 'Done', 'date': today},
                       {'id': '963627', 'name': 'Clean Carpet',
                           'status': 'Done', 'date': today},
                       {'id': '963628', 'name': 'Wash Curtains',
                           'status': 'Done', 'date': today},
                       {'id': '963629', 'name': 'Clean Windows',
                           'status': 'Done', 'date': today},
                       {'id': '963630', 'name': 'Vacuum',
                           'status': 'Done', 'date': today},
                       {'id': '963631', 'name': 'Polish Furniture', 'status': 'Done', 'date': today}]
    obj1.seperate_done_items()
    assert (len(obj1.recent_done_items) == 10)


"""
Tests that items go into older_done_items 10 items 
"""


def test_older_done_items_10():
    obj1 = model.ViewModel()
    obj1._doneItems = [{'id': '123456', 'name': 'Sweep Yard', 'status': 'Done', 'date': '2021-01-01'},
                       {'id': '789456', 'name': 'Prune Trees',
                           'status': 'Done', 'date': '2021-01-02'},
                       {'id': '987654', 'name': 'Wash Floor',
                           'status': 'Done', 'date': '2021-01-03'},
                       {'id': '987625', 'name': 'Clean Windows',
                           'status': 'Done', 'date': '2021-01-04'},
                       {'id': '963626', 'name': 'Wash Car',
                           'status': 'Done', 'date': '2021-01-05'},
                       {'id': '963627', 'name': 'Clean Carpet',
                           'status': 'Done', 'date': '2021-01-06'},
                       {'id': '963628', 'name': 'Wash Curtains',
                           'status': 'Done', 'date': '2021-01-07'},
                       {'id': '963629', 'name': 'Clean Windows',
                           'status': 'Done', 'date': '2021-01-08'},
                       {'id': '963630', 'name': 'Vacuum',
                           'status': 'Done', 'date': '2021-01-09'},
                       {'id': '963631', 'name': 'Polish Furniture', 'status': 'Done', 'date': '2021-01-10'}]
    obj1.seperate_done_items()
    assert (len(obj1.older_done_items) == 10)


"""
Tests contents of item
"""


def test_list_contents():
    today = datetime.today().strftime('%Y-%m-%d')
    obj1 = model.ViewModel()
    obj1._doneItems = [
        {'id': '123456', 'name': 'Sweep Yard', 'status': 'Done', 'date': today}]
    obj1.seperate_done_items()
    assert (obj1.recent_done_items[0]['id'] == '123456') & (obj1.recent_done_items[0]['name'] == 'Sweep Yard') & (
        obj1.recent_done_items[0]['status'] == 'Done') & (obj1.recent_done_items[0]['date'] == today)
