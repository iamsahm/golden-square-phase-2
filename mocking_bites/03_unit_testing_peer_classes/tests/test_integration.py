

"""raises error for locked diary"""
from lib.diary import *
from lib.secret_diary import *
import pytest

def test_secret_diary_includes_diary():
    diary = Diary('my diary')
    secret_diary = SecretDiary(diary)
    assert secret_diary.diary == diary

def test_read_while_locked():
    diary = Diary('my diary')
    secret_diary = SecretDiary(diary)
    with pytest.raises(Exception) as e:
        secret_diary.read()
    assert str(e.value) == 'Go away!'

    
def test_diary_lock_functions():
    diary = Diary('my diary')
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == 'my diary'
    secret_diary.lock()
    with pytest.raises(Exception) as e:
        secret_diary.read()
    assert str(e.value) == 'Go away!'