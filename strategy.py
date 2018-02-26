"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
from typing import Any
from game_state import GameState


def interactive_strategy(game: Any) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def recursive_minimax_helper(game: Any) -> Any:
    # TODO: Implement a recursive version of the minimax strategy.
    """
    Return a move for game through recursively using minimax strategy
    """
    if game.is_over(game):
        if game.is_winner(game.current_state.get_current_player_name()):
            return GameState.WIN
        elif not game.is_winner(game.current_state.get_current_player_name()):
            return GameState.LOSE
        return GameState.DRAW
    else:
        return max([-recursive_minimax(game.current_state.make_move(i))
                    for i in game.current_state.get_possible_moves()])


def recursive_minimax(game: Any) -> Any:
    """
    do this later
    :param game:
    :return:
    """
    pass


def iterative_minimax(game: Any) -> Any:
    # TODO: Implement a iterative version of the minimax strategy.
    """
    Return a move for game through iterative using minimax strategy
    """
    pass


if __name__ == "__main__":
    from python_ta import check_all

    check_all(config="a2_pyta.txt")
