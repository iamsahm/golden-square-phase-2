from lib.listening_list import *
import pytest

# test add a track
def test_listening_list_add_adds_track():
    listeninglist = ListeningList()
    listeninglist.add_track('come fly with me')
    result = listeninglist.listened_list
    assert result == ['come fly with me']

# test add a non string
def test_listening_list_add_adding_non_string_errors():
    listeninglist = ListeningList()
    
    with pytest.raises(Exception) as e:
        listeninglist.add_track(2323151)
    assert str(e.value) == 'dont put a number in me!'

# test return list
def test_return_listened_track_list_returns_tracks():
    listeninglist = ListeningList()
    listeninglist.add_track('come fly with me')
    assert listeninglist.view_list() == 'Here is a list of tracks you have heard: come fly with me'

def test_return_listened_track_list_returns_tracks():
    listeninglist = ListeningList()
    listeninglist.add_track('come fly with me')
    listeninglist.add_track('fly me to the moon')
    listeninglist.add_track('great balls of fire')
    assert listeninglist.view_list() == 'Here is a list of tracks you have heard: come fly with me, fly me to the moon, great balls of fire'


# test return empty list
def test_return_empty_listened_track_returns_exception():
    listeninglist = ListeningList()
    with pytest.raises(Exception) as e:
        listeninglist.view_list()
    assert str(e.value) == 'You have not listened to anything!'
    pass
