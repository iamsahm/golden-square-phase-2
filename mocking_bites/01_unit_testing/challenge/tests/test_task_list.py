from lib.task_list import TaskList
from unittest.mock import Mock


def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []


def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False

def test_task_list_add():
    task_list = TaskList()

    fake_task = Mock()

    task_list.add(fake_task)

    assert fake_task in task_list.tasks

def test_all_method():
    task_list = TaskList()

    fake_task_1 = Mock()
    fake_task_2 = Mock()

    task_list.add(fake_task_1)
    task_list.add(fake_task_2)

    all_tasks = task_list.all()
    assert all(item in all_tasks for item in [fake_task_1, fake_task_2])

def test_task_all_complete():

    task_list = TaskList()

    fake_task_1 = Mock()
    fake_task_2 = Mock()

    task_list.add(fake_task_1)
    task_list.add(fake_task_2)

    fake_task_1.is_complete.return_value = True
    fake_task_2.is_complete.return_value = True

    assert task_list.all_complete() == True


    
    


# Unit test `#tasks` and `#all_complete` behaviour
