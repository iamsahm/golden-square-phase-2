from lib.game import Game
import pytest

"""
Initialises with a length and width of 10
"""
def test_initialises_with_a_length_and_width_of_10():
    game = Game()
    assert game.rows == 10
    assert game.cols == 10

"""
Initialises with five ships of length 2, 3, 3, 4, 5
"""
def test_initialises_with_five_ships_of_right_length():
    game = Game()
    unplaced_ships = game.remaining_ships
    assert len(unplaced_ships) == 5
    assert unplaced_ships[0].length == 2
    assert unplaced_ships[1].length == 3
    assert unplaced_ships[2].length == 3
    assert unplaced_ships[3].length == 4
    assert unplaced_ships[4].length == 5

"""
Initialises with a totally empty board
"""
def test_initialises_with_a_totally_empty_board():
    game = Game()
    for row in range(1, 11):
        for col in range(1, 11):
            assert not game.ship_at(row, col)

"""
When we place a ship
Then its place on the board is marked out
"""
def test_when_we_place_a_ship_then_its_place_on_the_board_is_marked_out():
    game = Game()
    game.place_ship(length=2, orientation="vertical", row=3, col=2)
    assert game.ship_at(3, 2)
    assert game.ship_at(4, 2)
    assert not game.ship_at(3, 3)
    assert not game.ship_at(4, 3)
    assert not game.ship_at(3, 1)
    assert not game.ship_at(4, 1)

def test_ship_placed_over_another():
    game = Game()
    game.place_ship(length=2, orientation='vertical', row=9, col=2)
    
    result = game.place_ship(length=3, orientation='horizontal', row=9, col=1)
    assert result == 'There\'s already a ship there! Try again.'


'''
When we place a ship outside the board it throws an error
'''
def test_ship_placement_outside_board_exception():
    game = Game()
    
    result = game.place_ship(length=2, orientation='vertical', row=11, col=11)
    assert result == 'Your ship won\'t fit there! Try again.'

def test_ship_placement_outside_board_exception():
    game = Game()
    
    result = game.place_ship(length=2, orientation='vertical', row=-1, col=11)
    assert result == 'Your ship won\'t fit there! Try again.'

'''
When we place a ship that would extend outside the board it throws an error
'''
def test_ship_extends_outside_board_exception():
    game = Game()
    
    result = game.place_ship(length=3, orientation='vertical', row=9, col=9)
    assert result == 'Your ship won\'t fit there! Try again.'

'''
When we try to place an already placed ship
throw exception
'''

def test_ship_placed_twice_exception():
    game = Game()

    game.place_ship(length=2, orientation='vertical', row=9, col=9)
    result = game.place_ship(length=2, orientation='vertical', row=9, col=9)
    assert result == 'You\'ve got no ships with that length left!'
