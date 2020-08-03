from brain import Brain
from board import Board
from gamedata import DataManager

import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import random

matplotlib.use("Qt5agg")
colordict = ['turquoise','slateblue','navy','black']

class Generation:
    
    def __init__(self,size = 20,initmutate = False,display = True, load = False):
        self.size = size
        self.brains = [Brain()]*self.size
        self.boards = [Board()]*self.size
        self.data = DataManager()
        self.display = display
        if(initmutate):
            for brain in self.brains:
                brain.mutate()
        if(self.display):
            self.initDisplay()

    def load(self, mutate = False):
        for brain in self.brains:
            brain.load()
            if(mutate):
                brain.mutate()

    def trainingiteration(self):
        #board.player should be for NN, else is minimax
        #positive score for NN winning, negative for minimax
        endscores = [0] * self.size
        for i in range(self.size):
            #print("Brain" + str(i + 1))
            board = self.boards[i]
            brain = self.brains[i]
            tries = []
            board = Board()
            if(random.randint(0,1)==0):
                board = board.opposingBoard()
            while(not board.isGameOver()):
                num = 0
                if(board.player):
                    num = brain.actionindex(brain.evaluate(np.array(board.board)))
                    if(len(tries)>6):
                        num = board.makeDecision(3)
                else:
                    num = board.makeDecision(0,True,False)
                valid = board.movePiece(num)
                if(valid == 1):
                    board = board.opposingBoard()   
                if(valid == 0 and board.player):
                    tries.append(num)
            
            endscores[i] = board.scoreDelta() * (1 if board.player else -1)

        return endscores

    def traningloop(self,epochs = 10, save = False):
        for i in range(epochs):
            print("Epoch" + str(i + 1) + ":")
            endscores = self.trainingiteration()
            winrate = sum(score > 0 for score in endscores)/(self.size+0.0)
            self.data.winrateaddpoint(winrate)
            average = sum([(endscores[index]+(self.boards[0].total/2)) for index in range(len(endscores))])/(len(endscores)+0.0)
            self.data.avgscoreaddpoint(average)
            topscoreindices = sorted(range(len(endscores)), key=lambda score: endscores[score])[-4:] #ascending
            self.data.top4scoreaddpoints([(endscores[index]) for index in topscoreindices])
            fitnesses = [self.fitness(score) for score in endscores]
            self.data.fitnessaddpoint(sum(fitnesses)/(len(endscores)+0.0))
            if(self.display):
                self.displayData()
            if(save):
                self.brains[topscoreindices[-1]].save()
                self.data.save()
            self.updateBrains(fitnesses)


    def updateBrains(self,fitnesses):
        for i in range(len(fitnesses)):
            self.brains[i].mutate(fitnesses[i],fitnesses[i])


    def fitness(self, score):
        return (self.boards[0].total-score)/(self.boards[0].total+0.0)

    def initDisplay(self):
        self.fig, self.axs = plt.subplots(2, 2)
        self.axs[0,0].set_title("Overall winrate")
        self.axs[0,1].set_title("Average score")
        self.axs[1,0].set_title("Top 4 score")
        self.axs[1,1].set_title("Fitness")
        self.axs[0,1].axhline(y=self.boards[0].total/2,color = 'yellow')
        self.axs[1,0].axhline(y=self.boards[0].total/2,color = 'yellow')
        #plt.show()


    def displayData(self):
        if(not self.display):
            return

        self.axs[0,0].plot(self.data.winrate, color = 'red')
        self.axs[0,1].plot(self.data.avgscore, color = 'blue')
        self.axs[1,1].plot(self.data.fitness, color = 'green')
        
        for i in range(4):
            self.axs[1,0].plot(self.data.top4score[i],color = colordict[i])
        plt.pause(0.02)

if __name__ == "__main__":
    generation = Generation()
    generation.traningloop(epochs = 100)



