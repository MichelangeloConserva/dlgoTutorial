import enum
import random

from dlgo.agent.base import Agent

__all__ = [
    'MinimaxAgent'
]


class GameResult(enum.Enum):
    loss = 1
    draw = 2
    win  = 3
    

def best_result(game_state):
    """
    Find the best result that next_player can get from this game state.
    
    Returns:
    GameResult.win if next_player can guarantee a win
    GameResult.draw if next_player can guarantee a draw
    GameResult.loss if, no matter what next_player chooses, the
    opponent can still force a win
    """
    if game_state.is_over():
        if game_state.winner() == game_state.next_player:
            return GameResult.win
        if game_state.winner() is None:
            return GameResult.draw
        return GameResult.loss
    
    # if not over we recursively look into the future
    best_result_so_far = GameResult.loss
    for candidate_move in game_state.legal_moves():
        next_state = game_state.apply_move(candidate_move)
        opponent_best_result = best_result(next_state)
        our_result= reverse_game_result(opponent_best_result)
        if our_result.value > best_result_so_far.value:
            best_result_so_far = our_result
    return best_result_so_far
    


def reverse_game_result(game_result):
    if game_result == GameResult.loss:
        return GameResult.win
    if game_result == GameResult.win:
        return GameResult.loss
    return GameResult.draw

class MinimaxAgent(Agent):
    def select_move(self, game_state):
        winning_moves = []
        draw_moves    = []
        losing_moves  = []
        for possible_move in game_state.legal_moves():
            next_state = game_state.apply_move(possible_move)
            # searching for opponent best outcome
            opponent_best_outcome = best_result(next_state)
            # checking if the oppenent situation
            our_best_outcome = reverse_game_result(opponent_best_outcome)
            if our_best_outcome == GameResult.win:
                winning_moves.append(possible_move)
            elif our_best_outcome == GameResult.draw:
                draw_moves.append(possible_move)
            else:
                losing_moves.append(possible_move)
        if winning_moves:
            return random.choice(winning_moves)
        if draw_moves:
            return random.choice(draw_moves)
        return random.choice(losing_moves)










































