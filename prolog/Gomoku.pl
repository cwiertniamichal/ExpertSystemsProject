%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%   Some facts:
%       - Players:
%           - we have two players - x and o
%       - Board:
%           - if board field is empty, then e is in that field
%           - possible directions:
%               - horizontal_inc and horizontal_dec
%               - vertical_inv and vertical_dev
%               - diag_right_inc and diag_right_dec (\)
%               - diag_left_inc and diag_left_dev (/)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
:- style_check(-singleton).


opponent(x, Opponent) :-
    Opponent = o.
opponent(o, Opponent) :-
    Opponent = x.


oppositeDirection(horizontal_inc, OppositeDirection) :-
    OppositeDirection = horizontal_dec.
oppositeDirection(horizontal_dec, OppositeDirection) :-
    OppositeDirection = horizontal_inc.
oppositeDirection(vertical_inc, OppositeDirection) :-
    OppositeDirection = vertical_dec.
oppositeDirection(vertical_dec, OppositeDirection) :-
    OppositeDirection = vertical_inc.
oppositeDirection(diag_right_inc, OppositeDirection) :-
    OppositeDirection = diag_right_dec.
oppositeDirection(diag_right_dec, OppositeDirection) :-
    OppositeDirection = diag_right_inc.
oppositeDirection(diag_left_inc, OppositeDirection) :-
    OppositeDirection = diag_left_dec.
oppositeDirection(diag_left_dec, OppositeDirection) :-
    OppositeDirection = diag_left_inc.


moves(M) :-
    M = [default, free2, free3, double2Threat, double3Threat, free4, win].


getMovePriority(Move, Priority, N) :-
    moves(M),
    nth0(N, M, MoveName),
    MoveName \= Move,
    NewN is N + 1,
    getMovePriority(Move, Priority, NewN).
getMovePriority(Move, Priority, N) :-
    moves(M),
    nth0(N, M, MoveName),
    MoveName = Move,
    Priority is N.


getNextFieldInGivenDirection(X, Y, horizontal_inc, NextX, NextY) :-
    NextX is X,
    NextY is Y + 1.
getNextFieldInGivenDirection(X, Y,  horizontal_dec, NextX, NextY) :-
    NextX is X,
    NextY is Y - 1.
getNextFieldInGivenDirection(X, Y, vertical_inc, NextX, NextY) :-
    NextX is X + 1,
    NextY is Y.
getNextFieldInGivenDirection(X, Y,  vertical_dec, NextX, NextY) :-
    NextX is X - 1,
    NextY is Y.
getNextFieldInGivenDirection(X, Y, diag_right_inc, NextX, NextY) :-
    NextX is X + 1,
    NextY is Y + 1.
getNextFieldInGivenDirection(X, Y, diag_right_dec, NextX, NextY) :-
    NextX is X - 1,
    NextY is Y - 1.
getNextFieldInGivenDirection(X, Y, diag_left_inc, NextX, NextY) :-
    NextX is X + 1,
    NextY is Y - 1.
getNextFieldInGivenDirection(X, Y, diag_left_dec, NextX, NextY) :-
    NextX is X - 1,
    NextY is Y + 1.

getNthFieldInGivenDirection(X, Y, 1, Direction, NthX, NthY) :-
    getNextFieldInGivenDirection(X, Y, Direction, NthX, NthY),
    !.
getNthFieldInGivenDirection(X, Y, N, Direction, NthX, NthY) :-
    getNextFieldInGivenDirection(X, Y, Direction, NextX, NextY),
    NewN is N - 1,
    getNthFieldInGivenDirection(NextX, NextY, NewN, Direction, NthX, NthY).

getPrevFieldInGivenDirection(X, Y, Direction, PrevX, PrevY) :-
    oppositeDirection(Direction, OppositeDirection),
    getNextFieldInGivenDirection(X, Y, OppositeDirection, PrevX, PrevY).



fieldOccupiedByPlayer(X, Y, Player, Board) :-
    nth0(X, Board, Row),
    nth0(Y, Row, BoardElem),
    BoardElem = Player.

isFieldEmpty(X, Y, Board) :-
    fieldOccupiedByPlayer(X, Y, e, Board).



continuousChainExists(X, Y, N, Direction, Player, Board) :-
    fieldOccupiedByPlayer(X, Y, Player, Board),
    NewN is N - 1,
    getNextFieldInGivenDirection(X, Y, Direction, NextX, NextY),
    continuousChainExists(NextX, NextY, NewN, Direction, Player, Board).
continuousChainExists(X, Y, 1, Direction, Player, Board) :-
    fieldOccupiedByPlayer(X, Y, Player, Board).



brokenChainExists(X, Y, N, Direction, Player, Board, EmptyX, EmptyY) :-
    fieldOccupiedByPlayer(X, Y, Player, Board),
    NewN is N - 1,
    getNextFieldInGivenDirection(X, Y, Direction, NextX, NextY),
    brokenChainExists(NextX, NextY, NewN, Direction, Player, Board, EmptyX, EmptyY).
brokenChainExists(X, Y, N, Direction, Player, Board, EmptyX, EmptyY) :-
    isFieldEmpty(X, Y, Board),
    NewN is N - 1,
    EmptyX = X,
    EmptyY = Y,
    getNextFieldInGivenDirection(X, Y, Direction, NextX, NextY),
    continuousChainExists(NextX, NextY, NewN, Direction, Player, Board).



canBuildContinuousChainInOneMove(N, Direction, Player, Board, TargetX, TargetY) :-
    NewN is N - 1,
    continuousChainExists(X, Y, NewN, Direction, Player, Board),
    getNthFieldInGivenDirection(X, Y, NewN, Direction, TargetX, TargetY),
    isFieldEmpty(TargetX, TargetY, Board).
canBuildContinuousChainInOneMove(N, Direction, Player, Board, TargetX, TargetY) :-
    brokenChainExists(_, _, N, Direction, Player, Board, TargetX, TargetY).


canBuildContinuousChainInOneMoveAttackingGivenFiled(FieldX, FieldY, N, Player, Board) :-
    isFieldEmpty(FieldX, FieldY, Board),
    getNextFieldInGivenDirection(FieldX, FieldY, Direction, NextX, NextY),
    NewN is N - 1,
    continuousChainExists(NextX, NextY, NewN, Direction, Player, Board).
canBuildContinuousChainInOneMoveAttackingGivenFiled(FieldX, FieldY, N, Player, Board) :-
	brokenChainExists( _, _, N, Direction, Player, Board, FieldX, FieldY).



% TODO sometimes fields do not have to be empty - our mark is ok
emptyNFieldsInGivenDirectionExists(X, Y, N, Direction, Board) :-
    continuousChainExists(X, Y, N, Direction, e, Board),
    !.


canBuildFreeNAttackingGivenField(Player, Board, N, FieldX, FieldY, ChainX, ChainY, ChainDirection) :-
	isFieldEmpty(FieldX, FieldY, Board),
	getNextFieldInGivenDirection(FieldX, FieldY, ChainDirection, ChainX, ChainY),
    NewN is N - 1,
    continuousChainExists(ChainX, ChainY, NewN, ChainDirection, Player, Board),
    oppositeDirection(ChainDirection, OppositeDirection),
    N1 is 5 - NewN,
    N2 is N1 - 1,
    emptyNFieldsInGivenDirectionExists(FieldX, FieldY, N1, OppositeDirection, Board),
    getNthFieldInGivenDirection(ChainX, ChainY, NewN, ChainDirection, AfterChainX, AfterChainY),
    emptyNFieldsInGivenDirectionExists(AfterChainX, AfterChainY, N2, ChainDirection, Board).
canBuildFreeNAttackingGivenField(Player, Board, N, FieldX, FieldY, ChainX, ChainY, ChainDirection) :-
	isFieldEmpty(FieldX, FieldY, Board),
    N1 is 5 - N,
    oppositeDirection(ChainDirection, OppositeDirection),
    brokenChainExists(ChainX, ChainY, N, ChainDirection, Player, Board, FieldX, FieldY),
    getPrevFieldInGivenDirection(ChainX, ChainY, ChainDirection, BeforeChainX, BeforeChainY),
    emptyNFieldsInGivenDirectionExists(BeforeChainX, BeforeChainY, N1, OppositeDirection, Board),
    getNthFieldInGivenDirection(ChainX, ChainY, N, ChainDirection, AfterChainX, AfterChainY),
    emptyNFieldsInGivenDirectionExists(AfterChainX, AfterChainY, N1, ChainDirection, Board).


canBuildFreeN(Player, Board, N, TargetX, TargetY, ChainX, ChainY, ChainDirection) :-
    ExistingChainLen is N - 1,
    oppositeDirection(ChainDirection, OppositeDirection),
    N1 is 5 - ExistingChainLen,
    N2 is N1 - 1,
    continuousChainExists(ChainX, ChainY, ExistingChainLen, ChainDirection, Player, Board),
    getPrevFieldInGivenDirection(ChainX, ChainY, ChainDirection, BeforeChainX, BeforeChainY),
    emptyNFieldsInGivenDirectionExists(BeforeChainX, BeforeChainY, N1, OppositeDirection, Board),
    getNthFieldInGivenDirection(ChainX, ChainY, ExistingChainLen, ChainDirection, AfterChainX, AfterChainY),
    emptyNFieldsInGivenDirectionExists(AfterChainX, AfterChainY, N2, ChainDirection, Board),
    TargetX = BeforeChainX,
    TargetY = BeforeChainY,
    isFieldEmpty(TargetX, TargetY, Board).
canBuildFreeN(Player, Board, N, TargetX, TargetY, ChainX, ChainY, ChainDirection) :-
    ExistingChainLen is N - 1,
    oppositeDirection(ChainDirection, OppositeDirection),
    N1 is 5 - ExistingChainLen,
    N2 is N1 - 1,
    continuousChainExists(ChainX, ChainY, ExistingChainLen, ChainDirection, Player, Board),
    getPrevFieldInGivenDirection(ChainX, ChainY, ChainDirection, BeforeChainX, BeforeChainY),
    emptyNFieldsInGivenDirectionExists(BeforeChainX, BeforeChainY, N2, OppositeDirection, Board),
    getNthFieldInGivenDirection(ChainX, ChainY, ExistingChainLen, ChainDirection, AfterChainX, AfterChainY),
    emptyNFieldsInGivenDirectionExists(AfterChainX, AfterChainY, N1, ChainDirection, Board),
    TargetX = AfterChainX,
    TargetY = AfterChainY,
    isFieldEmpty(TargetX, TargetY, Board).
canBuildFreeN(Player, Board, N, TargetX, TargetY, ChainX, ChainY, ChainDirection) :-
    ExistingChainLen is N,
    N1 is 5 - ExistingChainLen,
    oppositeDirection(ChainDirection, OppositeDirection),
    brokenChainExists(ChainX, ChainY, ExistingChainLen, ChainDirection, Player, Board, TargetX, TargetY),
    getPrevFieldInGivenDirection(ChainX, ChainY, ChainDirection, BeforeChainX, BeforeChainY),
    emptyNFieldsInGivenDirectionExists(BeforeChainX, BeforeChainY, N1, OppositeDirection, Board),
    getNthFieldInGivenDirection(ChainX, ChainY, ExistingChainLen, ChainDirection, AfterChainX, AfterChainY),
    emptyNFieldsInGivenDirectionExists(AfterChainX, AfterChainY, N1, ChainDirection, Board).
canBuildFreeN(Player, Board, 1, TargetX, TargetY, ChainX, ChainY, ChainDirection) :-
    oppositeDirection(ChainDirection, OppositeDirection),
    opponent(Player, Opponent),
    N1 is 5,
    N2 is 4,
    continuousChainExists(ChainX, ChainY, 1, ChainDirection, Opponent, Board),
    getPrevFieldInGivenDirection(ChainX, ChainY, ChainDirection, BeforeChainX, BeforeChainY),
    emptyNFieldsInGivenDirectionExists(BeforeChainX, BeforeChainY, N1, OppositeDirection, Board),
    getNthFieldInGivenDirection(ChainX, ChainY, ExistingChainLen, ChainDirection, AfterChainX, AfterChainY),
    emptyNFieldsInGivenDirectionExists(AfterChainX, AfterChainY, N2, ChainDirection, Board),
    TargetX = BeforeChainX,
    TargetY = BeforeChainY,
    isFieldEmpty(TargetX, TargetY, Board).
canBuildFreeN(Player, Board, 1, TargetX, TargetY, ChainX, ChainY, ChainDirection) :-
    oppositeDirection(ChainDirection, OppositeDirection),
    opponent(Player, Opponent),
    N1 is 5,
    N2 is 4,
    continuousChainExists(ChainX, ChainY, 1, ChainDirection, Opponent, Board),
    getPrevFieldInGivenDirection(ChainX, ChainY, ChainDirection, BeforeChainX, BeforeChainY),
    emptyNFieldsInGivenDirectionExists(BeforeChainX, BeforeChainY, N2, OppositeDirection, Board),
    getNthFieldInGivenDirection(ChainX, ChainY, ExistingChainLen, ChainDirection, AfterChainX, AfterChainY),
    emptyNFieldsInGivenDirectionExists(AfterChainX, AfterChainY, N1, ChainDirection, Board),
    TargetX = AfterChainX,
    TargetY = AfterChainY,
    isFieldEmpty(TargetX, TargetY, Board).


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% TODO: handle broken chain
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
canBuildDoubleNThreat(Player, N, Board, Target1X, Target1Y) :-
    canBuildFreeN(Player, Board, N, Target1X, Target1Y, Chain1X, Chain1Y, Chain1Direction),
    canBuildFreeN(Player, Board, N, Target2X, Target2Y, Chain2X, Chain2Y, Chain2Direction),
    Target1X = Target2X,
    Target1Y = Target2Y,
    Chain1X \= Chain2X,
    oppositeDirection(Chain1Direction, Chain1OppositeDirection),
    Chain1Direction \= Chain2Direction,
    Chain1OppositeDirection \= Chain2Direction.
canBuildDoubleNThreat(Player, N, Board, Target1X, Target1Y) :-
    canBuildFreeN(Player, Board, N, Target1X, Target1Y, Chain1X, Chain1Y, Chain1Direction),
    canBuildFreeN(Player, Board, N, Target2X, Target2Y, Chain2X, Chain2Y, Chain2Direction),
    Target1X = Target2X,
    Target1Y = Target2Y,
    Chain1Y \= Chain2Y,
    oppositeDirection(Chain1Direction, Chain1OppositeDirection),
    Chain1Direction \= Chain2Direction,
    Chain1OppositeDirection \= Chain2Direction.

canBuildDoubleNThreatAttackingGivenFiled(Player, N, Board, FieldX, FieldY) :-
    canBuildFreeNAttackingGivenField(Player, Board, N, FieldX, FieldY, Chain1X, Chain1Y, Chain1Direction),
    canBuildFreeNAttackingGivenField(Player, Board, N, FieldX, FieldY, Chain2X, Chain2Y, Chain2Direction),
    Chain1X \= Chain2X,
    Chain1Direction \= Chain2Direction,
    oppositeDirection(Chain1Direction, Chain1OppositeDirection),
    Chain1OppositeDirection \= Chain2Direction.
canBuildDoubleNThreatAttackingGivenFiled(Player, N, Board, FieldX, FieldY) :-
    canBuildFreeNAttackingGivenField(Player, Board, N, FieldX, FieldY, Chain1X, Chain1Y, Chain1Direction),
    canBuildFreeNAttackingGivenField(Player, Board, N, FieldX, FieldY, Chain2X, Chain2Y, Chain2Direction),
    Chain1Y \= Chain2Y,
    Chain1Direction \= Chain2Direction,
    oppositeDirection(Chain1Direction, Chain1OppositeDirection),
    Chain1OppositeDirection \= Chain2Direction.


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% High level rules to advice player.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

canWinInOneMove(Player, Board, X, Y) :-
    canBuildContinuousChainInOneMove(5, Direction, Player, Board, X, Y).

canBuildFree4(Player, Board, TargetX, TargetY) :-
    canBuildFreeN(Player, Board, 4, TargetX, TargetY, _, _, _).

canBuildDouble3Threat(Player, Board, X, Y) :-
    canBuildDoubleNThreat(Player, 3, Board, X, Y).

canBuildDouble2Threat(Player, Board, X, Y) :-
    canBuildDoubleNThreat(Player, 2, Board, X, Y).

opponentCanWinInOneMove(Player, Board, X, Y) :-
    opponent(Player, Opponent),
    canWinInOneMove(Opponent, Board, X ,Y).

opponentCanBuildFree4(X, Y, CurrBestMovePriority, NewBestMovePriority, Player, Board) :-
    opponent(Player, Opponent),
    canBuildFree4(Opponent, Board, X, Y),
    setBestMove(X, Y, CurrBestMovePriority, NewBestMovePriority, Player, Board),
    opponentCanBuildFree4(_, _, NewBestMovePriority, _, Player, Board).

opponentCanBuildDouble3Threat(Player, Board, X, Y) :-
    opponent(Player, Opponent),
    canBuildDouble3Threat(Opponent, Board, X, Y).

opponentCanBuildDouble2Threat(Player, Board, X, Y) :-
    opponent(Player, Opponent),
    canBuildDouble2Threat(Opponent, Board, X, Y).


setBestMove(X, Y, CurrBestMovePriority, NewBestMovePriority, Player, Board) :-
    attackMoves(X, Y, CurrBestMovePriority, NewBestMovePriority, Player, Board),
    NewBestMovePriority > CurrBestMovePriority,
    retractall(best(_, _)),
    asserta(best(X, Y)),
    !.

attackMoves(X, Y, CurrBestPriority, NewBestPriority, Player, Board) :-
	canBuildContinuousChainInOneMoveAttackingGivenFiled(X, Y, 5, Player, Board),
	getMovePriority(win, NewBestPriority, 0),
    CurrBestPriority < NewBestPriority.
attackMoves(X, Y, CurrBestPriority, NewBestPriority, Player, Board) :-
    canBuildFreeNAttackingGivenField(Player, Board, 4, X, Y, _, _, _),
    getMovePriority(free4, NewBestPriority, 0),
    CurrBestPriority < NewBestPriority.
attackMoves(X, Y, CurrBestPriority, NewBestPriority, Player, Board) :-
    canBuildDoubleNThreatAttackingGivenFiled(Player, 3, Board, X, Y),
    getMovePriority(double3Threat, NewBestPriority, 0),
    CurrBestPriority < NewBestPriority.
attackMoves(X, Y, CurrBestPriority, NewBestPriority, Player, Board) :-
    canBuildDoubleNThreatAttackingGivenFiled(Player, 2, Board, X, Y),
    getMovePriority(double2Threat, NewBestPriority, 0),
    CurrBestPriority < NewBestPriority.
attackMoves(X, Y, CurrBestPriority, NewBestPriority, Player, Board) :-
    canBuildFreeNAttackingGivenField(Player, 3, Board, X, Y, _, _, _),
    getMovePriority(free3, NewBestPriority, 0),
    CurrBestPriority < NewBestPriority.
attackMoves(X, Y, CurrBestPriority, NewBestPriority, Player, Board) :-
    canBuildFreeNAttackingGivenField(Player, 2, Board, X, Y, _, _, _),
    getMovePriority(free2, NewBestPriority, 0),
    CurrBestPriority < NewBestPriority.
attackMoves(X, Y, CurrBestPriority, NewBestPriority, Player, Board) :-
    getMovePriority(default, NewBestPriority, 0),
    CurrBestPriority < NewBestPriority.


blockOpponentFree4(Player, Board, X ,Y) :-
    \+ opponentCanBuildFree4(_, _, -1, _, Player, Board),
    current_predicate(best/2),
    best(X, Y).


givePlayerAdvice(Player, Board, X, Y, PredName) :-
    canWinInOneMove(Player, Board, X, Y),
    PredName = canWinInOneMove, !;
    opponentCanWinInOneMove(Player, Board, X, Y),
    PredName = opponentCanWinInOneMove, !;

    canBuildFree4(Player, Board, X, Y),
    PredName = canBuildFree4, !;
    blockOpponentFree4(Player, Board, X, Y),
    retractall(best(_, _)),
    PredName = blockOpponentFree4, !;

    canBuildDouble3Threat(Player, Board, X, Y),
    PredName = canBuildDouble3Threat, !;
    opponentCanBuildDouble3Threat(Player, Board, X, Y),
    PredName = opponentCanBuildDouble3Threat, !;

    canBuildFreeN(Player, Board, 3, X, Y, _, _, _),
    PredName = canBuildFree3, !;

    canBuildDouble2Threat(Player, Board, X, Y),
    PredName = canBuildDouble2Threat, !;

    canBuildFreeN(Player, Board, 2, X, Y, _, _, _),
    PredName = canBuildFree2, !;

    opponentCanBuildDouble2Threat(Player, Board, X, Y),
    PredName = opponentCanBuildDouble2Threat, !;

    canBuildFreeN(Player, Board, 1, X, Y, _, _, _),
    PredName = canBuildFree1, !;

    X is 5,
    Y is 5,
    isFieldEmpty(X, Y, Board).
