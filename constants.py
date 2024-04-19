ROW, COL = 10, 10
START_SQUARE = 0
END_SQUARE = 101
NUMBER_OF_SQUARES = ROW * COL
PLAYER_X, PLAYER_Y, PLAYER_AI, PLAYER_DUMMY = "X", "Y", "A", "D"
NUMBER_OF_PAWNS = 2
GAME_OVER = "GAME_OVER"
GAME_MODE_STRING = "Game modes available:  \n 1 (Default): Single Player \n 2: Two Players \n 3: Two Players with Power Cards \n 4: Single AI \n 5: Player and AI"
POSITIVE_INFINITY = 2147483647
NEGATIVE_INFINITY = -2147483647
HEURISTIC = [5.01, 5.0, 4.99, 4.98, 3.97, 3.96, 3.95, 4.94, 3.93, 4.92, 3.91, 3.9, 3.89, 3.88, 3.87, 3.86, 2.85, 3.84, 3.83, 2.82, 2.81, 3.8, 3.79, 3.78, 2.77, 
2.76, 3.75, 3.74, 3.73, 3.72, 3.71, 3.7, 2.69, 2.68, 3.67, 3.66, 3.65, 3.64, 3.63, 3.62, 3.61, 4.6, 3.59, 3.58, 3.57, 3.56, 3.55, 3.54, 2.53, 2.52, 
2.51, 3.5, 3.49, 3.48, 3.47, 3.46, 3.45, 3.44, 4.43, 4.42, 3.41, 4.4, 4.39, 4.38, 3.37, 4.36, 3.35, 4.34, 4.33, 4.32, 4.31, 4.3, 3.29, 4.28, 4.27, 3.26, 3.25, 4.24, 4.23, 4.22, 3.21, 4.2, 4.19, 3.18, 3.17, 3.16, 3.15, 3.14, 3.13, 2.12, 2.11, 2.1, 2.09, 2.08, 2.07, 1.06, 1.05, 1.04, 1.03, 1.02, 1.01, 0.0]