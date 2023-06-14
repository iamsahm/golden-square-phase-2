from lib.music_library import MusicLibrary
from lib.track import Track

def test_add_track():
    music_library = MusicLibrary()
    track = Track("MyTitle", "MyArtist")

    music_library.add(track)

    assert track in music_library.tracks

def test_search():
    music_library = MusicLibrary()
    track_1 = Track("Title", "Singer")
    track_2 = Track("Title 2", "Singer 2")
    track_3 = Track("Title 3", "Band")
    track_4 = Track("Title 4", "Band 2")

    music_library.add(track_1)
    music_library.add(track_2)
    music_library.add(track_3)
    music_library.add(track_4)

    search_keyword = "Band"

    matches = music_library.search(search_keyword)

    assert track_3 in matches and track_4 in matches



