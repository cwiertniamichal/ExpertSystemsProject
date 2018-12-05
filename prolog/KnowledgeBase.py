PATH = 'prolog/Gomoku.pl'

BOARD_SIZE_FACT = 'boardSize({}, {})'

GIVE_PLAYER_ADVICE_PREDICATE = 'givePlayerAdvice({}, {}, X, Y, PredName).'

CAN_BUILD_DOUBLE_3_THREAD_PREDICATE = 'canBuildDouble3Threat({}, {}, X, Y).'
OPPONENT_CAN_BUILD_DOUBLE_3_THREAD_PREDICATE = 'opponentCanBuildDouble3Threat({}, {}, X, Y).'

CAN_BUILD_FREE_4_PREDICATE = 'canBuildFree4({}, {}, X, Y).'
OPPONENT_CAN_BUILD_FREE_4_PREDICATE = 'blockOpponentFree4({}, {}, X, Y).'

CAN_WIN_IN_ONE_MOVE_PREDICATE = 'canWinInOneMove({}, {}, X, Y).'
OPPONENT_CAN_WIN_IN_ONE_MOVE_PREDICATE = \
    'opponentCanWinInOneMove({}, {}, X, Y).'
