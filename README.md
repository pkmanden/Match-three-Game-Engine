# Match-three Game Engine

A simple match-three game engine implementation along with the implementations of multiple agents.
This is a part of my Master thesis on 'Analysing a general match-three game for developing agents'.
This repository includes the game engine, empirical analysis of the match-three game, etc.

The game engine and the agents are inside the folder m3_engine, and the empirical analysis code is inside Experiment_results_analysis folder. 

To run the game, go to m3_engine folder, and the game parametrs (grid size and number of colours) should be specified in the csv file exp_game_setting.csv.
The game API is configured to play with random agent now. It can be changed to make the rule-based agents play the game.

The number of moves per game is specified inside m3_globals.py. Also, the constants used for experiments are specified here. These should be set to 1 if not using for experiments.

Once these are set, the game engine can be run using the python script m3_main.py with the following command

python3 m3_main.py

