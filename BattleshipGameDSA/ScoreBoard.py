from MaxHeapSB import *

class ScoreBoard:

    def __init__(self, capacity):
        self.score_board = MaxHeapSB(capacity)

    def add_score(self, player_node):
        self.score_board.insert(player_node)

    #grab the top three scores but put them back in the heap to not get rid of them
    def display_scores(self):
        top_three = []
        for i in range(0, 3):
            if self.score_board.peek() is not None:
                top_three.append(self.score_board.delete())
            else:
                top_three.append(None)

        for s in top_three:
            if s is not None:
                self.score_board.insert(s)

        print("TOP 3 SCORES:\n")
        for score in top_three:
            if score is None:
                print("No current scores...")
            else:
                print(score.name + " : " + str(score.score))

