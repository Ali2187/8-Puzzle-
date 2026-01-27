

class EightPuzzle:
    def __init__(self, start_initial_state, goal=None):
        self.start_initial_state = start_initial_state
        if goal is None:
            self.goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        else:
            self.goal = goal

        self.moves={"up":-3,
                    "down":+3,
                    "left":+1,
                    "right":-1}

    def neighbors(self,state):
            zero=state.index(0)       #to find the zero
            result=[]
            for move,x in self.moves.items():
                new=zero+x
                if 0 <=new < 9 :
                    if (move == "right" and zero % 3 == 0) or (move == "left" and zero % 3 == 2):  #
                        continue

                    new_state=state.copy()
                    new_state[zero],new_state[new]=new_state[new],new_state[zero]
                    result.append((new_state,move))


            return result


    def display(self,state):
        for i in range(0,9,3):
            print(state[i:i+3])

