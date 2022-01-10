%%   YOUR NAME
%

%
%%factorial definition
factorial(0,1).
factorial(N,Result) :- N > 0,P is N-1,factorial(P,Q),Result is N*Q.

%%bigger definition
bigger(X,Y,X) :- X > Y.
bigger(X, Y, Y) :- Y >= X.

%% odd size def. starts with base case of list size 1, then checks if head is two long and has a tail, recursively calls on tail
oddSize([_]).
oddSize([_,_|Tail]) :- oddSize(Tail).

%%even size def. similar of oddSize,
evenSize([]).
evenSize([_,_|Tail]) :- evenSize(Tail).

%%isPrefix first checks null case
isPrefix([],_).
%%list of 1 element equal to head of list2, and recursion
isPrefix([X|Tax],[X|Yax]) :- isPrefix(Tax,Yax).

%%isMember first see if only object in list matches X
isMember(X, [X]).
isMember(X , [X|Tail]).
%%if first element matches
isMember(X, [Y|Tail]) :- isMember(X, [Tail]).
%%goes through tail and checkes

%% x removed from y makes Z, first case is nothing removed,
remove([],Y,Y).
remove(X,[X|Tail],Tail).
%%head of Y matches X, then Tail => Z tail
remove(X, [Y|Tail], [Z|Zail]) :- (Y = Z),  remove(X, Tail, Zail).
%%recursion where heads match (past searches match)

%%isUnion nil case, then one list nil makes final equal to other list.
%%Then if x head matches Z head it calls isUnion recursively, seperate check if Y head matches.
isUnion([],[],[]).
isUnion(X, [], X).
isUnion([], Y, Y).
isUnion([X|Tail],Y,[X|Zail]) :- isUnion(Tail, Y, Zail).
isUnion(X,[Y|Tail],[Y|Zail]) :- isUnion(X,Tail,Zail).

%%both lists empty base case,
%%Checks if head elements are equal, then checks rest of list
%% final line sees if X is member of Yail, and if Y is member of Tail
isEqual([],[]).
isEqual(X|Tail, X|Yail) :- isEqual(Tail,Yail).
isEqual(X|Tail, Y|Yail) :- isMember(X, Yail), isMember(Y, Tail), isEqual(Tail,Yail).

%%list of ALL elements between N1 and N2
%%null case
isBetween(_,_,[]).
%%1 element 
isBetween(N1,N2,[Z]) :- (Z=N1+1),(Z=N2-1).
%%head must be 1 more than n1 and less then n2, recursion for next head to be +1 more higher then n1
isBetween(N1,N2,[Z|Zail]) :- (R is N1+1),(Z = R),(Z < N2), isBetween(R,N2,Zail).
%
%!  ADD YOUR CODE ABOVE
%!  ADD YOUR CODE ABOVE
%!
%!  MAKE NO CHANGES BELOW
%%  MAKE NO CHANGES BELOW
%%  MAKE NO CHANGES BELOW
%%  MAKE NO CHANGES BELOW
%% Unit tests for Prolog Assignment 1
%!  %%%%%%%%
%
%

cls :- write('\33\[2J').


%% factorial
:- begin_tests(factorial).
test(factorial_test1,[true]) :- factorial(0, 1).
test(factorial_test2) :- factorial(6,720).
:- end_tests(factorial).

%%  max
:- begin_tests(bigger).
test(max_test1) :- bigger(4,2,4).
test(max_test2) :- bigger(2,12,12).
:- end_tests(bigger).

/* oddSize */
:- begin_tests(oddSize).
test(oddSize_test1) :- oddSize([13,21,2,101,205,9,3]).
test(oddSize_test2) :- oddSize([101]).
test(oddSize_test3) :- oddSize(['apple','ball','cat']).
test(oddSize_test4, [fail]) :- oddSize([13,21,2,11]).
:- end_tests(oddSize).

/* evenSize */
:- begin_tests(evenSize).
test(evenSize_test1) :- evenSize([13,21,2,101,205,9]).
test(evenSize_test2) :- evenSize([]).
test(evenSize_test3) :- evenSize(['apple','ball','cat','dog']).
test(evenSize_test4, [fail]) :- evenSize([13,21,2,11,82]).
:- end_tests(evenSize).

/* prefix */
:- begin_tests(isPrefix).
test(prefix_test1) :- isPrefix([1,2], [1,2,3,4,5]).
test(prefix_test2) :- isPrefix([1,2,3,4], [1,2,3,4,5]).
test(prefix_test3) :- isPrefix([], [1,2,3,4,5]).
test(prefix_test4,all(X==[[],[1],[1,2],[1,2,3]])) :- isPrefix(X, [1,2,3]).
test(prefix_test5, [fail]) :- isPrefix([1,2], [1,3,2,4,5]).
:- end_tests(isPrefix).

/* isBetween */
:- begin_tests(isBetween).
test(isBetween_test1) :- isBetween(3, 8, [4,5,6,7]).
test(isBetween_test2) :- isBetween(2, 9, [3,4,5,6,7,8]).
test(isBetween_test3) :- isBetween(1, 2, []).
test(isBetween_test4,[fail]) :- isBetween(2, 7, [4,5,6,7]).
:- end_tests(isBetween).

/* isMember */
:- begin_tests(isMember).
test(isMember1) :- isMember(1, [1,2,3,4,5]).
test(isMember2) :- isMember(4, [1,2,13,4,5,16,7]).
test(isMember3) :- isMember(5, [11,21,13,41,5]).
test(isMember4, all(X==[1,2,3,20])) :- isMember(X, [1,2,3,20]).
test(isMember5, [fail]) :- isMember(100, [1,2,3,6]).
:- end_tests(isMember).

/* isUnion */
:- begin_tests(isUnion).
test(isUnion_test1) :- isUnion([3,1,2],[4,1,5,14],X), sort(X, [1,2,3,4,5,14]).
test(isUnion_test2) :- isUnion([2,1,3,4],[4,1,2,3],X), sort(X, [1,2,3,4]).
test(isUnion_test3) :- isUnion([4,2,6],[13,7,11],X), sort(X, [2,4,6,7,11,13]).
:- end_tests(isUnion).

/* isEqual */
:- begin_tests(isEqual).
test(isEqual_test1) :- isEqual([3,1,2],[1,2,3]).
test(isEqual_test2,[fail]) :- isEqual([3,1,2],[3,1,4]).
test(isEqual_test3) :- isEqual([1,2,3,4,5],[5,4,3,2,1]).
test(isEqual_test4) :- isEqual(['a','b','c'],['b','c','a']).
:- end_tests(isEqual).

/* remove */
:- begin_tests(remove).
test(remove_test1) :- remove(1, [1,2,3,4], [2,3,4]).
test(remove_test2) :- remove(2, [1,1,2,3,2,4], [1,1,3,2,4]).
test(remove_test3) :- remove(11, [1,1,2,3,2,4,11], [1,1,2,3,2,4]).
test(remove_test4) :- remove(13, [1,1,2,3,2,4,11], [1,1,2,3,2,4,11]).
:- end_tests(remove).

%% The following directives (at the shell prompt ?-) run the tests.
%% run_tests(testName). - runs the corresponding test
%% run_tests. - runs all the tests in the file

