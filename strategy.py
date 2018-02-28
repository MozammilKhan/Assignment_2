"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
from typing import Any, Union
from game_state import GameState
from game import Game


# TODO: Adjust the type annotation as needed.
def interactive_strategy(game: Any) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)

def rough_outcome_strategy(game: Any) -> Any:
    """
    Return a move for game by picking a move which results in a state with
    the lowest rough_outcome() for the opponent.
    
    NOTE: game.rough_outcome() should do the following:
        - For a state that's over, it returns the score for the current
          player of that state.
        - For a state that's not over:
            - If there is a move that results in the current player winning,
              return 1.
            - If all moves result in states where the other player can
              immediately win, return -1.
            - Otherwise; return a number between -1 and 1 corresponding to how
              'likely' the current player will win from the current state.

        In essence: rough_outcome() will only look 1 or 2 states ahead to
        'guess' the outcome of the game, but no further. It's better than
        random, but worse than minimax.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2 # Temporarily -- just so we can replace this easily later
    
    # Get the move that results in the lowest rough_outcome for the opponent
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)
        
        # We multiply the below by -1 since a state that's bad for the opponent
        # is good for us.
        guessed_score = new_state.rough_outcome() * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move
    
    # Return the move that resulted in the best rough_outcome
    return best_move

# TODO: Implement a recursive version of the minimax strategy.
def recursive_minimax_helper(game: Any, state: Any) -> Any:
    """
    Return a move for game through recursively using minimax strategy
    """
    game.current_state = state
    if game.is_over(state):
        if game.is_winner(state.get_current_player_name()):
            return GameState.WIN
        elif not game.is_winner(state.get_current_player_name()):
            return GameState.LOSE
        return GameState.DRAW
    scores = []
    possible_moves = state.get_possible_moves()

        # Get scores for all current possible moves
    for i in possible_moves:
        new_state = state.make_move(i)
        scores.append(recursive_minimax_helper(game, new_state) * -1)

    # Return the highest resulting score
    return max(scores)

def recursive_minimax(game: Any) -> Any:
    """
    do this later
    :param game:
    :return:
    """
    lst = []
    current_state = game.current_state
    possible_moves = current_state.get_possible_moves()
    for i in possible_moves:
        new_state = current_state.make_move(i)
        lst.append(recursive_minimax_helper(game, new_state) * -1)
    game.current_state = current_state

    return possible_moves[lst.index(max(lst))]


#  TODO: Implement an iterative version of the minimax strategy.

if __name__ == "__main__":
    from python_ta import check_all

    check_all(config="a2_pyta.txt")
