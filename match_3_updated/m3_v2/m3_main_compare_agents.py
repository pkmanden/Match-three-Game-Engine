import numpy as np
from gameplay_heatmap import GameplayHeatmap
from m3_agent import *
from m3_exp import *
from m3_globals import *

if __name__ == "__main__":

    agents = []
    game_settings = []
    exp_stats = {}

    # All agents listed
    a1 = Agent("top_agent")
    a2 = Agent("bottom_agent")
    a3 = Agent("random_agent")
    a4 = Agent("human")
    # a5 = Agent("rl_agent")

    # Adding only the required agents to the list
    agents.append(a1)
    agents.append(a2)
    agents.append(a3)

    edges_gh = GameplayHeatmap()

    # Create a statistics instance for each agent and one for cases where agent is not relevant
    for agent in agents:
        exp_stats[agent.get_type()] = ExpStatus(agent.get_type())
    arrays_list = list()
    exp_to_end = EXP_DIFF_BOARD_REPEAT
    while exp_to_end > 0:
        game = Game(BOARD_SIZE, COLOR_END)
        # Consolidate result if game cannot be started with the setting
        if game.init_board().stat_gameplay_status == "NoStart":
            exp_stats["NotApplicable"].consolidate_result(game.get_stats())
            print("Experiment cancelled.")
            break
        # Fix board if the game can be started
        fix_init_board = game.get_board()
        arrays_list.append(fix_init_board)
        np.savez('starting_boards.npz', *arrays_list[:EXP_DIFF_BOARD_REPEAT])
        fix_possible_moves = game.move_helper()
        games_to_end = EXP_SAME_BOARD_REPEAT
        while games_to_end > 0:
            for agent in agents:
                game.reinit_board(fix_init_board.copy(), fix_possible_moves)
                gamestats = None
                moves_to_end = NUM_OF_MOVES_PER_GAME
                while moves_to_end > 0:
                    possible_moves = game.move_helper()
                    agent.give_help(possible_moves)
                    agent.find_row_moves(possible_moves)
                    move = agent.select_move(game.game_grid)
                    game.input_tiles(move)
                    edges_gh.add_move_to_graph(move, agent.get_type())
                    gamestats = game.get_stats()
                    if gamestats.stat_gameplay_status == "Invalid":
                        pass
                    elif gamestats.stat_gameplay_status == "Error":
                        moves_to_end = 0
                    elif gamestats.stat_gameplay_status == "Valid":
                        moves_to_end -= 1
                exp_stats[agent.get_type()].consolidate_result(gamestats)
            games_to_end -= 1
            for experiment_agent in exp_stats:
                exp_stats[experiment_agent].write_csv_compare_agents()
                exp_stats[experiment_agent].reinit_exp()
        exp_to_end -= 1
    for ag in agents:
        edges_gh.draw_map(ag.get_type())
