"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other

Given an integer n, return all distintict solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distintic board coniguration of the n-queens' placement, quere 'Q' and '.' both indicate a queen and an empty space, respectively

Example:
- Input: n 0 4
Output:
[[".Q..","...Q","Q...","..Q."],
["..Q.","Q...","...Q",".Q.."]]


"""

class Solution:
    """
    example on the top: [1,3,0,2]
    example on the bottom: [2,0,3,1]
    """
    def solveNQueens(self, n: int) -> list[list[str]]:
        solutions = []
        state = []
        self.search(state, solutions,n)
        return solutions

    def is_valid_state(self,state,n):
        #check if it is a valid solution
        return len(state) == n
    
    def get_candidates(self,state, n):
        if not state:
            return range(n)
        
        #find the next position in the state to populate
        position = len(state)
        candidates = set(range(n))
        #prune down candidates that place the queen into attacks
        for row, col in enumerate(state):
            #discard the coluumn index if it's occupied y a queen
            candidates.discard(col)
            dist = position - row
            #discard diagonals
            candidates.discard(col + dist)
            candidates.discard(col - dist)

        return candidates

    def search(self,state, solutions, n):
        if self.is_valid_state(state,n):
            state_string = self.state_to_string(state,n)
            solutions.append(state_string)
            return
    
        for candidate in self.get_candidates(state,n):
            #recurse
            state.append(candidate)
            self.search(state, solutions,n)
            state.pop()
    def state_to_string(self, state, n):
        # ex. [1,3,0,1]
        #output:[".Q..","...Q","Q...","..Q."]
        ret = []
        for i in state:
            string = '.' * i + 'Q' + '.' * (n - i - 1)
            ret.append(string)
        return ret



solution = Solution()   
print(solution.solveNQueens(4))