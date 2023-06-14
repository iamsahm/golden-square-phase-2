from lib.tasker import *
import pytest

# test username entry
def test_username():
    reminder = Reminder('Sam')
    result = reminder.name
    assert result == 'Sam'
# test task saves to user object
def test_task_to_user():
    reminder = Reminder('Sam')
    reminder.remind_me_to('breathe')
    result = reminder.tasklist
    assert result == ['breathe']

# test returns exception if the task isnt a string
def test_task_exception_not_string():
    reminder = Reminder('Sam')
    with pytest.raises(Exception) as e:
        reminder.remind_me_to(434243)
    error_message = str(e.value)
    assert error_message == 'Only strings in the task list pls'
# test remind returns list of tasks
def test_remind_returns_lists():
    reminder = Reminder('Sam')
    reminder.remind_me_to('breathe')
    reminder.remind_me_to('stretch')
    result = reminder.remind()
    assert result == 'Here is your tasklist: breathe, stretch'

# test returns exception if there are no tasks
def test_reminder_exception_empty_tasklist():
    reminder = Reminder('Sam')
    with pytest.raises(Exception) as e:
        reminder.remind()
    error_message = str(e.value)
    assert error_message == 'You are all caught up! Well done!'

def test_reminder_complete_task_removes_list_entry():
    reminder = Reminder('Sam')
    reminder.remind_me_to('breathe')
    reminder.remind_me_to('stretch')
    reminder.complete_task('breathe')
    assert reminder.remind() == 'Here is your tasklist: stretch'
# test complete task removes task from list
def test_reminder_completing_non_task_throws_exception():
    reminder = Reminder('Sam')
    reminder.remind_me_to('breathe')
    reminder.remind_me_to('stretch')
    reminder.complete_task('breathe')
    with pytest.raises(Exception) as e:
        reminder.complete_task('breathe')
    error_message = str(e.value)
    assert error_message == 'That task is not on the task list!'

# test returns exception if the task doesnt exist