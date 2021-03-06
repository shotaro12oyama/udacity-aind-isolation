"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)

    """
    def test_custom_score(self):
    
    test method for custome_score
    
        from isolation import Board
        from sample_players import RandomPlayer
        from sample_players import GreedyPlayer

        # create an isolation board (by default 7x7)
        player1 = RandomPlayer()
        player2 = RandomPlayer()
        game = Board(player1, player2)
        game.apply_move((0, 0))
        game.apply_move((0, 1))

        expected = -2
        actual = game_agent.custom_score(game, player1)
        self.assertEqual(expected, actual)
    """

    def test_minimax(self):
        """test method for minimax"""
        from isolation import Board
        from sample_players import RandomPlayer
        from sample_players import GreedyPlayer
        from game_agent import IsolationPlayer
        from game_agent import MinimaxPlayer


        # create an isolation board (by default 7x7)
        player1 = MinimaxPlayer()
        player2 = MinimaxPlayer()
        game = Board(player1, player2)
        game.apply_move((1, 1))
        game.apply_move((0, 1))
        game.apply_move((3, 0))
        game.apply_move((2, 0))
        game.apply_move((4, 2))
        game.apply_move((3, 2))
        game.apply_move((2, 3))
        game.apply_move((2, 4))
        game.apply_move((4, 4))
        game.apply_move((0, 3))
        game.apply_move((5, 6))
        game.apply_move((2, 2))
        game.apply_move((6, 4))
        game.apply_move((1, 4))
        game.apply_move((4, 5))
        game.apply_move((3, 3))
        game.apply_move((2, 6))
        game.apply_move((4, 1))
        game.apply_move((3, 4))
        game.apply_move((6, 2))
        game.apply_move((5, 3))
        game.apply_move((5, 4))
        game.apply_move((6, 1))
        game.apply_move((4, 6))
        game.apply_move((4, 0))
        game.apply_move((2, 5))
        game.apply_move((2, 1))
#        game.apply_move((1, 3))
#        game.apply_move((0, 0))
#        game.apply_move((0, 5))
#        game.apply_move((1, 2))

        expected = (-1,-1)
        depth = 3
        actual = player2.minimax(game, depth)
        print(game.to_string())
        print(actual)
        print(expected)
        self.assertEqual(expected, actual)


def test_alphabeta(self):
        """test method for minimax"""
        from isolation import Board
        from sample_players import RandomPlayer
        from sample_players import GreedyPlayer
        from game_agent import IsolationPlayer
        from game_agent import MinimaxPlayer
        from game_agent import AlphaBetaPlayer


        # create an isolation board (by default 7x7)
        player1 = AlphaBetaPlayer()
        player2 = AlphaBetaPlayer()
        game = Board(player1, player2)
        game.apply_move((1, 1))
        game.apply_move((0, 1))
        game.apply_move((3, 0))
        game.apply_move((2, 0))
        game.apply_move((4, 2))
        game.apply_move((3, 2))
        game.apply_move((2, 3))
        game.apply_move((2, 4))
        game.apply_move((4, 4))
        game.apply_move((0, 3))
        game.apply_move((5, 6))
        game.apply_move((2, 2))
        game.apply_move((6, 4))
        game.apply_move((1, 4))
        game.apply_move((4, 5))
        game.apply_move((3, 3))
        game.apply_move((2, 6))
        game.apply_move((4, 1))
        game.apply_move((3, 4))
        game.apply_move((6, 2))
        game.apply_move((5, 3))
        game.apply_move((5, 4))
        game.apply_move((6, 1))
        game.apply_move((4, 6))
        game.apply_move((4, 0))
        game.apply_move((2, 5))
        game.apply_move((2, 1))
#        game.apply_move((1, 3))
#        game.apply_move((0, 0))
#        game.apply_move((0, 5))
#        game.apply_move((1, 2))

        expected = (-1,-1)
        depth = 3
        actual = player1.alphabeta(game, depth)
        print(game.to_string())
        print(actual)
        print(expected)
        self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()
