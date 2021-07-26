"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy


X = "X"
O = "O"
EMPTY = None
c=0


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]



def player(board):
    """
    Returns player who has the next turn on a board.
    """#
    x=0
    o=0
    for i in range(3):
        for j in range(3):
            #print(board[i][j])
            if board[i][j] is X:
                x+=1
            elif board[i][j] is O:
                o+=1
   # print(x,o)
    if x==0 and o==0: return X
    #print(X)


    if x<=o:
        return X 
    else:
        return O


    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    actions_list=set()
    if terminal(board)==1:
        return 0
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                actions_list.add((i,j))

    return actions_list
            
        
   # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
     """
    if action is not EMPTY:
        copy_board=deepcopy(board)
        if copy_board[action[0]][action[1]] is EMPTY:
            copy_board[action[0]][action[1]]=player(board)
            return copy_board
        else:
            raise Exception("Invalid Action")

    else:
        raise Exception("None error Line 72")

    #raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    if board[0][0]==board[1][1]==board[2][2] and board[2][2] is not EMPTY:
        return board[2][2] 
    elif board[0][2]==board[1][1]==board[2][0] and board[2][0] is not EMPTY:
        return board[2][0]; #Diagonal check

    else:
        
        for i in range(3):
            if board[0][i]==board[1][i] and board[2][i]==board[1][i]  and board[2][i] is not EMPTY:
             return board[2][i]
            if board[i][0]==board[i][1]and  board[i][1]==board[i][2] and board[i][2] is not EMPTY:
             return board[i][2]

    return None


             

        


   # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is None:
        for i in range(3):
            for j in range(3):
                if board[i][j] is EMPTY:
                 return 0
    else:
        return 1
   
    
    return 1
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    elif winner(board)==None:
         return 0
    else:
        raise Exception("Terminal state not reached")
    #raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    actions_list2=set()
    if terminal(board):
        return None
 
    min_val=-math.inf
    max_val=math.inf


    actions_list2=actions(board)
    
    best_act=None
    #for action in actions_list2:
    if player(board)==X:
        for action in actions_list2:
                score=min_act(result(board,action))
                if score>min_val:
                    min_val=score
                    best_act=action
        return best_act



    elif player(board)==O:
        for action in actions_list2:
                score=max_act(result(board,action))
                if score<max_val:
                    max_val=score
                    best_act=action

        return best_act

def max_act(board):


    neg=-math.inf
    # max_val=math.inf

    if terminal(board)==1:
        return utility(board)

    actions_list2=actions(board)
    for action in actions_list2:
        neg=max(neg,  min_act(result(board,action)))

    return neg



def min_act(board):


    # min_val=-math.inf
    pos=math.inf

    if terminal(board)==1:
        return utility(board)

    actions_list2=actions(board)
    for action in actions_list2:
        pos=min(pos,max_act(result(board,action)))

    return pos






    
       
   # i=iter(actions_list2)
    # if player(board)==X:
    #    # if terminal(board) != 1:
    #         minimax(result(board,action))
    #     else:
    #         if utility(board) > max_val:
    #             max_val=utility(board)
    #             best_act=action
    # else:
    #     for action in actions_list2:
    #         if terminal(board) !=1:
    #              minimax(result(board,action))
    #         else:
    #             if utility(board) < min_val:
    #                 min_val=utility(board)
    #                 best_act=action
 
    # return best_act

            


           

        
        


 #raise NotImplementedError
