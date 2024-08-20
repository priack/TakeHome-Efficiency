# TakeHome-Efficiency

Some players are standing in a field playing a game. If two players can see each other then they can
throw a ball between them.

Write a program to calculate the maximum number of players that can touch a single ball. The ball can
be given to any single player at the start, and each player can touch the ball an unlimited number of
times.

You are given an input file containing details of the players, as follows:

    player1,visible_player_1,visible_player_2,...
    player2,visible_player_1,visible_player_2,...
    ...

Each line of the file contains a comma-separated set of fields. The first field on each line is the name of
a player (as a string), and the remaining fields are the names of the players that that player can see.
Player names have a maximum length of 20 characters.

Your program should read the input file and print the answer to standard output.

For example, given the following input:

    George,Beth, Sue
    Rick,Anne
    Anne,Beth
    Beth, Anne ,George
     Sue,Beth

The program should print 3 . This is because George can see Beth and Beth can see George.
Additionally, Beth can see Anne, and Anne can see Beth. However, despite Rick being able to see
Anne, Anne cannot see Rick, and despite George being able to see Sue, Sue cannot see George.

Your program should have the following properties:
- Given a file with n players, where each player can see at most m other players, the expected
time complexity of your solution should be O(n*m) . Please explain the time complexity of
your implementation in documentation.
- If the data is not in the expected format, your solution should output a user-friendly error
message explaining what the problem is.
- You should write your solution as if you were writing production code .
- Please include automated tests and whatever documentation you feel are necessary.
- The solution can be written in the language of your choice, but it must be easy to compile and
run . Please include documentation for how to compile and run your solution.

Please document any assumptions that you make.

Feel free to use the Internet to help you with your solution, but please don't copy any code from the
Internet (everything needs to be your own code). Use of readily available 3rd party libraries is
acceptable, but you should make sure that you demonstrate your coding skills in the solution.

We expect this exercise to take around 3-4 hours to complete, but you are welcome to use as much
time as you like. Do let us know how much time you ended up using.
