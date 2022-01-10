
%% You can fill the 4 gallon jug from the faucet, taking you from a
%% problem state [X,Y] to a problem state [4,Y],
%% provided X < 4.
move([X,Y],'Fill 4-gallon jug from faucet',[4,Y]) :- X<4.
%%
%
%2. Rule corresponding to the move 'Fill 3-gallon jug from faucet'
move([X,Y],'Fill 3 gallon jug from faucet', [X,3] ) :- Y<3.
%
%3. Rule corresponding to the move 'Empty 4-gallon jug onto the ground'
move([X,Y],'Empty 4-gallon jug onto the ground', [0,Y]) :- X>0.
%
%4. Rule corresponding to the move 'Empty 3-gallon jug onto the ground'
move([X,Y], 'Empty 3-gallon jug onto the ground', [X,0]) :- Y>0.
%
%5. Rule corresponding to the move 'Fill 4-gallon jug from 3-gallon jug'
move([X,Y], 'Fill 4-gallon jug from 3-gallon jug', [4,(Ynew)]) :- Ynew is (Y-(4-X)), X < 4, Y > 0.
%
%6. Rule corresponding to the move 'Fill 3-gallon jug from 4-gallon jug'
move([X,Y], 'Fill 3 gallon jug from 4 gallon jug', [Xnew, 3]) :- Xnew is (X-(3-Y)), Y < 3, X > 0.
%
%7. Rule corresponding to the move 'Empty 3-gallon jug into 4-gallon jug'
move([X,Y], 'Empty 3-gallon jug into 4-gallon jug', [Xnew,0]) :- Xnew is X+Y , Y > 0, X+Y =< 4.
%
%8. Rule corresponding to the move 'Empty 4-gallon jug into 3-gallon jug'
move([X,Y], 'Empty 4-gallon jug into 3-gallon jug', [0,Ynew]) :- Ynew is Y+X,  X > 0, X+Y =< 3.
%
%
%%solution predicates
% To solve the problem try this: length(X, Y), Y < 10, solution([0,0], X).
%
% [2,0] is the goal state. No move required if you are in this state
solution([2,0],[]).
%
%The list of moves [Move|Rest] constitutes a solution from PresentState
%if Move takes you from PresentState to NextState
%and Rest represents a sequence of moves that will take
%you from NextState to the goal state.
solution(PresentState,[Move|Rest]) :- move(PresentState,Move,NextState),
    solution(NextState,Rest).


