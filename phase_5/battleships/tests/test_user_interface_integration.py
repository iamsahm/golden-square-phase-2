import unittest
from lib.user_interface import UserInterface
from lib.game import Game
from tests.terminal_interface_helper_mock import TerminalInterfaceHelperMock
from unittest.mock import Mock



class TestUserInterface(unittest.TestCase):
    # def test_ship_setup_scenario(self):
    #     io = TerminalInterfaceHelperMock()
    #     interface = UserInterface(io, Game())
    #     io.expect_print("Welcome to the game!")
    #     io.expect_print("Set up your ships first.")
    #     io.expect_print("You have these ships remaining: 2, 3, 3, 4, 5")
    #     io.expect_print("Which do you wish to place?")
    #     io.provide("2")
    #     io.expect_print("Vertical or horizontal? [vh]")
    #     io.provide("v")
    #     io.expect_print("Which row?")
    #     io.provide("3")
    #     io.expect_print("Which column?")
    #     io.provide("2")
    #     io.expect_print("OK.")
    #     io.expect_print("This is your board now:")
    #     io.expect_print("\n".join([
    #         "..........",
    #         "..........",
    #         ".S........",
    #         ".S........",
    #         "..........",
    #         "..........",
    #         "..........",
    #         "..........",
    #         "..........",
    #         ".........."
    #     ]))
    #     interface.run()
    

    
    def test_ship_setup_scenario_full(self):
        io = TerminalInterfaceHelperMock()
        user1 = Mock()
        interface = UserInterface(io, Game(), user1)
        io.expect_print("Welcome to the game player!")
        io.expect_print("Set up your ships first.")
        io.expect_print("You have these ships remaining: 2, 3, 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("2")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("3")
        io.expect_print("Which column?")
        io.provide("2")
        io.expect_print("OK.")
        io.expect_print("Ship placed!")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
        ]))
        io.expect_print("You have these ships remaining: 3, 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("3")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("4")
        io.expect_print("Which column?")
        io.provide("4")
        io.expect_print("OK.")
        io.expect_print("Ship placed!")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S.S......",
            "...S......",
            "...S......",
            "..........",
            "..........",
            "..........",
            ".........."
        ]))
        io.expect_print("You have these ships remaining: 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("4")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("5")
        io.expect_print("Which column?")
        io.provide("5")
        io.expect_print("OK.")
        io.expect_print("Ship placed!")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S.S......",
            "...SS.....",
            "...SS.....",
            "....S.....",
            "....S.....",
            "..........",
            ".........."
        ]))
        io.expect_print("You have these ships remaining: 3, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("3")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Which row?")
        io.provide("1")
        io.expect_print("Which column?")
        io.provide("2")
        io.expect_print("OK.")
        io.expect_print("Ship placed!")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            ".SSS......",
            "..........",
            ".S........",
            ".S.S......",
            "...SS.....",
            "...SS.....",
            "....S.....",
            "....S.....",
            "..........",
            ".........."
        ]))
        io.expect_print("You have these ships remaining: 5")
        io.expect_print("Which do you wish to place?")
        io.provide("5")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("2")
        io.expect_print("Which column?")
        io.provide("10")
        io.expect_print("OK.")
        io.expect_print("Ship placed!")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            ".SSS......",
            ".........S",
            ".S.......S",
            ".S.S.....S",
            "...SS....S",
            "...SS....S",
            "....S.....",
            "....S.....",
            "..........",
            ".........."
        ]))
        interface.run('player')

    # def test_ship_placement_error(self):
        io = TerminalInterfaceHelperMock()
        user1 = Mock()
        interface = UserInterface(io, Game(), user1)
        io.expect_print("Welcome to the game player!")
        io.expect_print("Set up your ships first.")
        io.expect_print("You have these ships remaining: 2, 3, 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("2")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("3")
        io.expect_print("Which column?")
        io.provide("2")
        io.expect_print("OK.")
        io.expect_print("Ship placed!")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
        ]))
        io.expect_print("You have these ships remaining: 3, 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("3")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("4")
        io.expect_print("Which column?")
        io.provide("4")
        io.expect_print("OK.")
        io.expect_print("Ship placed!")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S.S......",
            "...S......",
            "...S......",
            "..........",
            "..........",
            "..........",
            ".........."
        ]))
        
        io.expect_print("You have these ships remaining: 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("2")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("5")
        io.expect_print("Which column?")
        io.provide("5")
        io.expect_print("OK.")
        io.expect_print("You\'ve got no ships with that length left!")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S.S......",
            "...S......",
            "...S......",
            "..........",
            "..........",
            "..........",
            ".........."
        ]))


        io.expect_print("You have these ships remaining: 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("4")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("5")
        io.expect_print("Which column?")
        io.provide("5")
        io.expect_print("OK.")
        io.expect_print("Ship placed!")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S.S......",
            "...SS.....",
            "...SS.....",
            "....S.....",
            "....S.....",
            "..........",
            ".........."
        ]))



        io.expect_print("You have these ships remaining: 3, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("3")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Which row?")
        io.provide("1")
        io.expect_print("Which column?")
        io.provide("2")
        io.expect_print("OK.")
        io.expect_print("Ship placed!")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            ".SSS......",
            "..........",
            ".S........",
            ".S.S......",
            "...SS.....",
            "...SS.....",
            "....S.....",
            "....S.....",
            "..........",
            ".........."
        ]))
        io.expect_print("You have these ships remaining: 5")
        io.expect_print("Which do you wish to place?")
        io.provide("5")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("2")
        io.expect_print("Which column?")
        io.provide("10")
        io.expect_print("OK.")
        io.expect_print("Ship placed!")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            ".SSS......",
            ".........S",
            ".S.......S",
            ".S.S.....S",
            "...SS....S",
            "...SS....S",
            "....S.....",
            "....S.....",
            "..........",
            ".........."
        ]))
        interface.run('player')


'''
When we place our penultimate ship
The program prompts us to place our final ship and returns a completing message
'''

'''
When we finish placing player 1s ships
Player 2s ship prompts start
'''

'''
When we finish placing P2s ships
P1s first move starts
'''

'''
When P1s move starts
They are reminded of their current score and their previous guesses
'''

'''
When one player has hit all of the ships of the other
They are declared the winner and the game ends
'''

'''
When a winner is declared
The game ends and the user has the option to restart
'''

'''
When the user restarts the game
The board is empty and the P1 prompts begin
'''

