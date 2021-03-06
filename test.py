# Unit Testing Code
# No new ideas for any other test cases -- Will add if something comes up

import sys
from tictactoe import tictactoe

import random


class TestCases(tictactoe):

    def __init__(self):
        print '\n\n'
        print 'Initialised Unit Testing for TicTacToe.\n\n'
        print '-' * 50

    def testPassAllValues(self):

        print '1: Testing Register Move for all values.'
        print '-' * 50
        for i in range(0, 3):
            for j in range(0, 3):
                print 'Testing registerMove(' + str(i) + ', ' + str(j) + ')'
                game = tictactoe()
                try:
                    assert game.registerMove(i, j) == True
                except AssertionError as e:
                    print '-' * 50
                    print 'Test Cases Failed'
                    print '\n\n'
                    return e

        print '-' * 50
        print '9 Values checked ...'
        print 'Test Case passed.'
        print '\n\n'
        return True

    def testRowsWinCases(self):
        print '2: Testing Winning returns for all Row win types.'
        print '-' * 50

        # Making all possible row wins
        for k in range(1, 3):
            for i in range(0, 3):
                game = tictactoe()
                agent = game.agent
                x = []
                for j in range(0, 3):
                    x.append(k)
                agent[i] = x
                game.agent = agent
                try:
                    assert game.gameWin() == False
                except AssertionError as e:
                    print '-' * 50
                    print 'Test Cases Failed'
                    print '\n\n'
                    return e

        print '-' * 50
        print '6 Rows checked ...'
        print 'Test Case passed.'
        print '\n\n'
        return True

    def testColumnsWinCases(self):
        print '3: Testing Winning returns for all Column win types.'
        print '-' * 50

        # Making all possible column wins
        for k in range(1, 3):
            for i in range(0, 3):
                game = tictactoe()
                agent = game.agent
                x = []
                for j in range(0, 3):
                    agent[j][i] = k
                game.agent = agent
                try:
                    assert game.gameWin() == False
                except AssertionError as e:
                    print '-' * 50
                    print 'Test Cases Failed'
                    print '\n\n'
                    return e

        print '-' * 50
        print '6 Columns checked ...'
        print 'Test Case passed.'
        print '\n\n'
        return True

    def testDiagonalWinCases(self):
        print '4: Testing Winning returns for all Diagonal win types.'
        print '-' * 50

        # Making all possible Diagonal wins
        for k in range(1, 3):
            game = tictactoe()
            agent = game.agent
            x = []
            for j in range(0, 3):
                agent[j][j] = k
            game.agent = agent
            try:
                assert game.gameWin() == False
            except AssertionError as e:
                print '-' * 50
                print 'Test Cases Failed'
                print '\n\n'
                return e

        for k in range(1, 3):
            game = tictactoe()
            agent = game.agent
            x = []
            for j in range(0, 3):
                agent[j][2 - j] = k
            game.agent = agent
            try:
                assert game.gameWin() == False
            except AssertionError as e:
                print '-' * 50
                print 'Test Cases Failed'
                print '\n\n'
                return e

        print '-' * 50
        print '4 Diagonals checked ...'
        print 'Test Case passed.'
        print '\n\n'
        return True

    def testNotWinCases(self):
        print '5. Checking possible cases that are not a Win'
        print '-' * 50

        for i in range(0, 3):
            for j in range(0, 3):
                game = tictactoe()
                game.agent[i][j] = 1
                game.agent[j][i] = 2
                game.displayBoard()
                try:
                    assert game.gameWin() == True
                except AssertionError as e:
                    print '-' * 50
                    print 'Test Cases Failed'
                    print '\n\n'
                    return e

        print '-' * 50
        print '9 No Win cases checked ...'
        print 'Test Case passed.'
        print '\n\n'
        return True

    def testInvalidMoves(self):
        print '6. Testing Invalid Moves'
        print '-' * 50

        for i in range(-1, 5):
            for j in range(-1, 5):
                if i < 0 or i > 2 or j < 0 or j > 2:
                    game = tictactoe()
                    print i, j
                    try:
                        assert game.registerMove(i, j) == 'Invalid Move'
                    except AssertionError, e:
                        # game.displayBoard()
                        print '-' * 50
                        print 'Test Cases Failed'
                        print '\n\n'
                        return
                        # raise e

        for i in range(0, 3):
            for j in range(0, 3):
                game = tictactoe()
                game.agent[i][j] = random.randint(1, 2)
                try:
                    game.displayBoard()
                    assert game.registerMove(i, j) == 'Invalid Move'
                except AssertionError, e:
                    print '-' * 50
                    print 'Test Cases Failed'
                    print '\n\n'
                    return

        print '-' * 50
        print 'Invalid Moves checked ...'
        print 'Test Case passed.'
        print '\n\n'
        return True

if __name__ == '__main__':
    # game = tictactoe()
    test = TestCases()
    test.testPassAllValues()
    test.testRowsWinCases()
    test.testColumnsWinCases()
    test.testDiagonalWinCases()
    test.testNotWinCases()
    test.testInvalidMoves()
