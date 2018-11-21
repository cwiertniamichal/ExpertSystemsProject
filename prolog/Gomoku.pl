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



continuousChainExists(Player, N, X, Y, Direction, Board) :-
    fieldOccupiedByPlayer(X, Y, Player, Board),
    NewN is N - 1,
    getNextFieldInGivenDirection(X, Y, Direction, NextX, NextY),
    continuousChainExists(Player, NewN, NextX, NextY, Direction, Board).
continuousChainExists(Player, 1, X, Y, Direction, Board) :-
    fieldOccupiedByPlayer(X, Y, Player, Board).



brokenChainExists(Player, N, X, Y, Direction, Board, EmptyX, EmptyY) :-
    fieldOccupiedByPlayer(X, Y, Player, Board),
    NewN is N - 1,
    getNextFieldInGivenDirection(X, Y, Direction, NextX, NextY),
    brokenChainExists(Player, NewN, NextX, NextY, Direction, Board, EmptyX, EmptyY).
brokenChainExists(Player, N, X, Y, Direction, Board, EmptyX, EmptyY) :-
    isFieldEmpty(X, Y, Board),
    NewN is N - 1,
    EmptyX = X,
    EmptyY = Y,
    getNextFieldInGivenDirection(X, Y, Direction, NextX, NextY),
    continuousChainExists(Player, NewN, NextX, NextY, Direction, Board).



canBuildContinuousChainInOneMove(Player, N, Direction, Board, TargetX, TargetY) :-
    NewN is N - 1,
    continuousChainExists(Player, NewN, X, Y, Direction, Board),
    getNthFieldInGivenDirection(X, Y, NewN, Direction, TargetX, TargetY),
    isFieldEmpty(TargetX, TargetY, Board).
canBuildContinuousChainInOneMove(Player, N, Direction, Board, TargetX, TargetY) :-
    brokenChainExists(Player, N, NewX, NewY, Direction, Board, TargetX, TargetY).



% TODO sometimes fields do not have to be empty - our mark is ok
emptyNFieldsInGivenDirectionExists(N, X, Y, Direction, Board) :-
    continuousChainExists(e, N, X, Y, Direction, Board),
    !.




canBuildFreeN(Player, Board, N, TargetX, TargetY, ChainX, ChainY, ChainDirection) :-
    ExistingChainLen is N - 1,
    oppositeDirection(ChainDirection, OppositeDirection),
    N1 is 5 - ExistingChainLen,
    N2 is N1 - 1,
    continuousChainExists(Player, ExistingChainLen, ChainX, ChainY, ChainDirection, Board),
    getPrevFieldInGivenDirection(ChainX, ChainY, ChainDirection, BeforeChainX, BeforeChainY),
    emptyNFieldsInGivenDirectionExists(N1, BeforeChainX, BeforeChainY, OppositeDirection, Board),
    getNthFieldInGivenDirection(ChainX, ChainY, ExistingChainLen, ChainDirection, AfterChainX, AfterChainY),
    emptyNFieldsInGivenDirectionExists(N2, AfterChainX, AfterChainY, ChainDirection, Board),
    TargetX = BeforeChainX,
    TargetY = BeforeChainY.
canBuildFreeN(Player, Board, N, TargetX, TargetY, ChainX, ChainY, ChainDirection) :-
    ExistingChainLen is N - 1,
    oppositeDirection(ChainDirection, OppositeDirection),
    N1 is 5 - ExistingChainLen,
    N2 is N1 - 1,
    continuousChainExists(Player, ExistingChainLen, ChainX, ChainY, ChainDirection, Board),
    getPrevFieldInGivenDirection(ChainX, ChainY, ChainDirection, BeforeChainX, BeforeChainY),
    emptyNFieldsInGivenDirectionExists(N2, BeforeChainX, BeforeChainY, OppositeDirection, Board),
    getNthFieldInGivenDirection(ChainX, ChainY, ExistingChainLen, ChainDirection, AfterChainX, AfterChainY),
    emptyNFieldsInGivenDirectionExists(N1, AfterChainX, AfterChainY, ChainDirection, Board),
    TargetX = AfterChainX,
    TargetY = AfterChainY.
canBuildFreeN(Player, Board, N, TargetX, TargetY, ChainX, ChainY, ChainDirection) :-
    ExistingChainLen is N,
    N1 is 5 - ExistingChainLen,
    brokenChainExists(Player, ExistingChainLen, ChainX, ChainY, ChainDirection, Board, TargetX, TargetY),
    getPrevFieldInGivenDirection(ChainX, ChainY, ChainDirection, BeforeChainX, BeforeChainY),
    emptyNFieldsInGivenDirectionExists(N1, BeforeChainX, BeforeChainY, OppositeDirection, Board),
    getNthFieldInGivenDirection(ChainX, ChainY, ExistingChainLen, ChainDirection, AfterChainX, AfterChainY),
    emptyNFieldsInGivenDirectionExists(N1, AfterChainX, AfterChainY, ChainDirection, Board).


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% TODO: handle broken chain
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
canBuildDoubleNThreat(Player, N, Board, Target1X, Target1Y) :-
    canBuildFreeN(Player, Board, N, Target1X, Target1Y, Chain1X, ChainY, Chain1Direction),
    canBuildFreeN(Player, Board, N, Target2X, Target2Y, Chain2X, Chain2Y, Chain2Direction),
    TargetX1 = TargetX2,
    TargetY1 = TargetY2,
    Chain1X \= Chain2X,
    Chain1Direction \= Chain2Direction,
    oppositeDirection(Chain1Direction, Chain1OppositeDirection),
    Chain1OppositeDirection \= Chain2Direction.
canBuildDoubleNThreat(Player, N, Board, Target1X, Target1Y) :-
    canBuildFreeN(Player, Board, N, Target1X, Target1Y, Chain1X, ChainY, Chain1Direction),
    canBuildFreeN(Player, Board, N, Target2X, Target2Y, Chain2X, Chain2Y, Chain2Direction),
    TargetX1 = TargetX2,
    TargetY1 = TargetY2,
    Chain1Y \= Chain2Y,
    Chain1Direction \= Chain2Direction,
    oppositeDirection(Chain1Direction, Chain1OppositeDirection),
    Chain1OppositeDirection \= Chain2Direction.


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% High level rules to advice player.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

canWinInOneMove(Player, Board, X, Y) :-
    canBuildContinuousChainInOneMove(Player, 5, Direction, Board, X, Y).

canBuildFree4(Player, Board, TargetX, TargetY) :-
    canBuildFreeN(Player, Board, 4, TargetX, TargetY, _, _, _).
% canBuildFree4(Player, Board, TargetX, TargetY) :-
%    brokenChainExists(Player, 4, ChainX, ChainY, Direction, Board, TargetX, TargetY),
%    getPrevFieldInGivenDirection(ChainX, ChainY, Direction, BeforeChainX, BeforeChainY),
%    isFieldEmpty(BeforeChainX, BeforeChainY, Board),
%    getNthFieldInGivenDirection(ChainX, ChainY, 4, Direction, AfterChainX, AfterChainY),
%    isFieldEmpty(AfterChainX, AfterChainY, Board).


canBuildDouble3Threat(Player, Board, X, Y) :-
    canBuildDoubleNThreat(Player, 3, Board, X, Y).

canBuildDouble2Threat(Player, Board, X, Y) :-
    canBuildDoubleNThreat(Player, 2, Board, X, Y).

opponentCanWinInOneMove(Player, Board, X, Y) :-
    opponent(Player, Opponent),
    canWinInOneMove(Opponent, Board, X ,Y).

opponentCanBuildFree4(Player, Board, X, Y) :-
    opponent(Player, Opponent),
    canBuildFree4(Opponent, Board, X, Y).

opponentCanBuildDouble3Threat(Player, Board, X, Y) :-
    opponent(Player, Opponent),
    canBuildDouble3Threat(Opponent, Board, X, Y).

opponentCanBuildDouble2Threat(Player, Board, X, Y) :-
    opponent(Player, Opponent),
    canBuildDouble2Threat(Opponent, Board, X, Y).



givePlayerAdvice(Player, Board, X, Y) :-
    canWinInOneMove(Player, Board, X, Y), !;
    opponentCanWinInOneMove(Player, Board, X, Y), !;
    canBuildFree4(Player, Board, X, Y), !;
    opponentCanBuildFree4(Player, Board, X, Y), !;
    canBuildDouble3Threat(Player, Board, X, Y), !;
    opponentCanBuildDouble3Threat(Player, Board, X, Y), !;
    canBuildDouble2Threat(Player, Board, X, Y), !;
    opponentCanBuildDouble2Threat(Player, Board, X, Y), !;
    canBuildFreeN(Player, Board, 3, X, Y, _, _, _), !;
    canBuildFreeN(Player, Board, 2, X, Y, _, _, _), !;
    canBuildFreeN(Player, Board, 1, X, Y, _, _, _), !.


