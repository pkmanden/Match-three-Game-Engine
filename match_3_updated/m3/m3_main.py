import csv
from m3_globals import *
from m3_game import *
from m3_agent import *
from m3_exp import *
import sys

if __name__ == "__main__":

    agents = []
    game_settings = []
    exp_stats = {}

    # All agents listed
    a1 = Agent("top_agent")
    a2 = Agent("bottom_agent")
    a3 = Agent("random_agent")
    a4 = Agent("human")
    # a5 = Agent("dqn")

    # Adding only the required agents to the list
    agents.append(a1)
    agents.append(a2)

    # Create a statistics instance for each agent and one for cases where agent is not relevant
    for agent in agents:
        exp_stats[agent.get_type()] = ExpStatus(agent.get_type())
    exp_stats["NotApplicable"] = ExpStatus("NotApplicable")

    # Read game settings
    with open('exp_game_setting.csv', newline='') as settings_file:
        settings_reader = csv.reader(settings_file)
        next(settings_reader)
        for setting in settings_reader:
            gs = setting[0].split(', ')
            game_settings.append([(int(gs[0]), int(gs[1])), int(setting[1])])

    for each_settings in game_settings:

        exp_to_end = EXP_DIFF_BOARD_REPEAT
        while exp_to_end > 0:

            game = Game(each_settings[0], each_settings[1])

            # Consolidate result if game cannot be started with the setting
            if game.init_board().stat_gameplay_status == "NoStart":
                exp_stats["NotApplicable"].consolidate_result(game.get_stats())
                print("Experiment cancelled.")
                break

            # Fix board if the game can be started
            fix_init_board = game.get_board()
            fix_possible_moves = game.move_helper()

            games_to_end = EXP_SAME_BOARD_REPEAT
            while games_to_end > 0:

                for agent in agents:

                    game.reinit_board(fix_init_board.copy(), fix_possible_moves)
                    gamestats = None

                    moves_to_end = NUM_OF_MOVES_PER_GAME
                    while moves_to_end > 0:
                        board = game.get_board()

                        possible_moves = game.move_helper()
                        agent.give_help(possible_moves)

                        agent.find_row_moves(possible_moves)
                        move = agent.select_move(board)

                        game.input_tiles(move)
                        gamestats = game.get_stats()
                        if gamestats.stat_gameplay_status == "Invalid":
                            pass
                        elif gamestats.stat_gameplay_status == "Error":
                            moves_to_end = 0
                        elif gamestats.stat_gameplay_status == "Valid":
                            moves_to_end -= 1
                    # gamestats.write_csv(agent.get_type())
                    exp_stats[agent.get_type()].consolidate_result(gamestats)
                games_to_end -= 1
            exp_to_end -= 1

            for experiment_agent in exp_stats:
                exp_stats[experiment_agent].write_csv()
                exp_stats[experiment_agent].reinit_exp()




