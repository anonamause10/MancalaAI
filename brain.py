import numpy as np
import os

class Brain:
    
    def __init__(self,hiddenlayersizes,numinputs, numoutputs):
        self.weights = []
        self.biases = []
        self.inputshape = numinputs
        self.outputshape = numoutputs
        self.currepoch = 0
        r = numinputs
        for i in range(len(hiddenlayersizes)+1):
            if(i<len(hiddenlayersizes)):
                c = hiddenlayersizes[i]
            else:
                c = numoutputs
            weightmatrix = np.ones((c,r))
            biasvector = np.zeros((c))
            self.weights.append(weightmatrix)
            self.biases.append(biasvector)
            r = c

    def evaluate(self,input):
        output = np.copy(input)

        if(input.shape[0]!=self.inputshape):
            return np.zeros(input.shape)
        
        for i in range(len(self.weights)):
            output = np.matmul(self.weights[i],output)
            output = np.add(output,self.biases[i])
        
        return output

    def actionindex(self,outputvec):
        return np.argmax(outputvec)

    def mutate(self,weightfactor = 1,biasfactor = 1):
        
        for i in range(len(self.weights)):
            w =  self.weights[i]
            self.weights[i] = np.add(w,(np.random.rand(w.shape[0],w.shape[1])-0.5)*2*weightfactor)
            b = self.biases[i]
            self.biases[i] = np.add(b,(np.random.rand(b.shape[0])-0.5)*2*biasfactor) 
        self.currepoch += 1

    def setlayers(self, newbrain):
        self.weights = np.copy(newbrain.weights)
        self.biases = np.copy(newbrain.biases)
        self.inputshape = newbrain.inputshape
        self.outputshape = newbrain.outputshape
        self.currepoch = newbrain.currepoch

    def printweights(self):
        print("Weights:")
        for i in range(len(self.weights)):
            print("Layer " + str(i) + " weights:")
            print(self.weights[i])

    def printbiases(self):
        print("Biases:")
        for i in range(len(self.biases)):
            print("Layer " + str(i) + " biases:")
            print(self.biases[i])

    def save(self):
        for i in range(len(self.weights)):
            np.save("weights/weights" + str(i),self.weights[i])
            np.save("biases/biases" + str(i),self.biases[i])

    def load(self):
        self.weights = []
        self.biases = []
        for f in os.listdir("weights"):
            self.weights.append(np.load(f))


            
        
brain = Brain([10,10,10],14,6)
brain.mutate()
brain.printweights()
print(brain.actionindex(brain.evaluate(np.array([4,4,4,4,4,4,0,4,4,4,4,4,4,0]))))
brain.save()
