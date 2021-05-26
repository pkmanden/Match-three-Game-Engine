from m3_agent import *
from m3_exp import *

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
    # agents.append(a1)
    agents.append(a2)
    agents.append(a3)

    # Create a statistics instance for each agent and one for cases where agent is not relevant
    for agent in agents:
        exp_stats[agent.get_type()] = ExpStatus(agent.get_type())

    game = Game((10, 10), 10)
    game.game_grid = SAME_BOARD_10X10_10
    possible_moves = game.find_moves()

    # Fix board
    fix_init_board = game.get_board()
    fix_possible_moves = possible_moves

    for agent in agents:
        for _ in range(EXP_SAME_BOARD_REPEAT):
            print(f'Starting board : \n{fix_init_board}')
            game.reinit_board(fix_init_board.copy(), fix_possible_moves)
            gamestats = None
            moves_to_end = NUM_OF_MOVES_PER_GAME
            while moves_to_end > 0:
                possible_moves = game.move_helper()
                agent.give_help(possible_moves)
                agent.find_row_moves(possible_moves)
                move = agent.select_move(game.game_grid)
                game.input_tiles(move)
                gamestats = game.get_stats()
                if gamestats.stat_gameplay_status == "Invalid":
                    pass
                elif gamestats.stat_gameplay_status == "Error":
                    moves_to_end = 0
                elif gamestats.stat_gameplay_status == "Valid":
                    moves_to_end -= 1
            exp_stats[agent.get_type()].consolidate_result(gamestats)

            for experiment_agent in exp_stats:
                exp_stats[experiment_agent].write_csv_compare_agents()
                exp_stats[experiment_agent].reinit_exp()






