from lib.diary import *
from lib.secret_diary import *
import pytest
from unittest.mock import Mock

def test_init_locked():
    diary = Mock()
    secret_diary = SecretDiary(diary)
    assert secret_diary.locked == True

def test_read_locked_raises_exception():
    diary = Mock()
    secret_diary = SecretDiary(diary)

    with pytest.raises(Exception) as e:
        secret_diary.read()
    assert str(e.value) == 'Go away!'

def test_read_unlocked_returns_contents():
    diary = Mock()
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    diary.read.return_value = 'my diary'
    assert secret_diary.read() == 'my diary'
