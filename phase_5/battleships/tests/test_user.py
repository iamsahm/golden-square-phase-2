from lib.user import *
from unittest.mock import Mock
from unittest.mock import patch


def test_user_can_shoot_opponents_board():
    with patch('builtins.input', side_effect = [2,2]) as mock_input:
        mock_own_game = Mock()
        mock_own_game.rows= 10
        mock_own_game.cols= 10
        mock_opponent_game = Mock()
        mock_opponent_game.rows= 10
        mock_opponent_game.cols= 10
        mock_opponent_game.ship_at.return_value = False
        player = User(mock_own_game, mock_opponent_game, 'name')
        assert player.shoot() == 'Shot missed!'
        assert player.opponent_board == [
            '..........',
            '.O........',
            '..........',
            '..........',
            '..........',
            '..........',
            '..........',
            '..........',
            '..........',
            '..........',
        ]

def test_shooting_outside_board_returns_error():
    with patch('builtins.input', side_effect = [-1,2]) as mock_input:
        mock_own_game = Mock()
        mock_own_game.rows= 10
        mock_own_game.cols= 10
        mock_opponent_game = Mock()
        mock_opponent_game.rows= 10
        mock_opponent_game.cols= 10
        mock_opponent_game.ship_at.return_value = False
        player = User(mock_own_game, mock_opponent_game, 'name')
        assert player.shoot() == 'That\'s not on the board!'
        assert player.opponent_board == [
            '..........',
            '..........',
            '..........',
            '..........',
            '..........',
            '..........',
            '..........',
            '..........',
            '..........',
            '..........',
        ]

def test_shooting_at_ship_returns_success_message():
    with patch('builtins.input', side_effect = [1,2]) as mock_input:
        mock_own_game = Mock()
        mock_own_game.rows= 10
        mock_own_game.cols= 10
        mock_opponent_game = Mock()
        mock_opponent_game.rows= 10
        mock_opponent_game.cols= 10
        mock_opponent_game.ship_at.return_value = True
        mock_opponent_game.ships_placed = [Mock(status = 2, coords= [(1,2), (2,2)])]
        player = User(mock_own_game, mock_opponent_game, 'name')
        assert player.shoot() == 'Hit!'
        assert player.opponent_board == [
            '.X........',
            '..........',
            '..........',
            '..........',
            '..........',
            '..........',
            '..........',
            '..........',
            '..........',
            '..........',
        ]

def test_destroying_ship_returns_shipdestroyed_message():
    with patch('builtins.input', side_effect = [2,1,1,1]) as mock_input:
        mock_own_game = Mock()
        mock_own_game.rows= 10
        mock_own_game.cols= 10
        mock_opponent_game = Mock()
        mock_opponent_game.rows= 10
        mock_opponent_game.cols= 10
        mock_opponent_game.ships_placed = [Mock(status=2, coords = [(1,1), (2,1)])]
        player = User(mock_own_game, mock_opponent_game, 'name')
        player.shoot()
        player.shoot()
        assert player.opponent.ships_placed[0].status == 0
        assert player.opponent_board == [
            'X.........',
            'X.........',
            '..........',
            '..........',
            '..........',
            '..........',
            '..........',
            '..........',
            '..........',
            '..........',]

def test_is_game_over_returns_true_after_all_ships_exploded():
    with patch('builtins.input', side_effect = [2,1,1,1]) as mock_input:
        mock_own_game = Mock()
        mock_own_game.rows= 10
        mock_own_game.cols= 10
        mock_opponent_game = Mock()
        mock_opponent_game.rows= 10
        mock_opponent_game.cols= 10
        mock_opponent_game.ships_placed = [Mock(status=2, coords = [(1,1), (2,1)])]
        player = User(mock_own_game, mock_opponent_game, 'name')
        player.shoot()
        player.shoot()
        assert player.is_game_over() == True

def test_is_game_over_returns_false_after_some_ships_exploded():
    with patch('builtins.input', side_effect = [3,2]) as mock_input:
        mock_own_game = Mock()
        mock_own_game.rows= 10
        mock_own_game.cols= 10
        mock_opponent_game = Mock()
        mock_opponent_game.rows= 10
        mock_opponent_game.cols= 10
        mock_opponent_game.ships_placed = [Mock(status=2, coords = [(1,1), (2,1)])]
        player = User(mock_own_game, mock_opponent_game, 'name')
        player.shoot()
        assert player.is_game_over() == False
