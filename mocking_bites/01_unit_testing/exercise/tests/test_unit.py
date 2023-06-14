from unittest.mock import Mock
from lib.music_library import MusicLibrary
from lib.track import Track

def test_music_library_adds_mock_track():
    music_library = MusicLibrary()

    fake_track = Mock()

    music_library.add(fake_track)

    assert fake_track in music_library.tracks

def test_music_library_search():
    music_library = MusicLibrary()

    fake_track_1 = Mock()
    fake_track_1.matches.return_value = True

    fake_track_2 = Mock()
    fake_track_2.matches.return_value = False

    music_library.add(fake_track_1)
    music_library.add(fake_track_2)

    assert fake_track_1 in music_library.search("MyKeyword")

def test_track_matches():
    track = Track("My Bands First Song!", "Band #1")

    assert track.matches("Band") == True