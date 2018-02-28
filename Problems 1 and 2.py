# HW 5, Problems 1 and 2

# load NumPy, requires Anaconda to be installed locally and chosen as the interpreter
import numpy as numpy

# load FigureSupport from SupportLib, requires newest version of SupportLib to be loaded in content root
import scr.FigureSupport as FigureSupport

# Modified HW 4 code to complete HW 5
# create Game class
class Game(object):
    def __init__(self, flip_probability):
        self.flip_probability = flip_probability #probability of heads

    # create Simulate function
    def Simulate(self, number_of_flips, number_of_realizations):
        self.number_of_flips = number_of_flips
        self.number_of_realizations = number_of_realizations

        gamecost = -250 # cost of playing the game
        totalwinnings = 0 # initialize total winnings
        winningslist = [] # empty list to place each game's winnging into and then graph
        losecount = 0 # keep track of any time you lose money

        for j in range(0, self.number_of_realizations):
            fliplist = "" # create an empty string

            for i in range(0, self.number_of_flips): # iterate through 20 flips, treating 1's as heads and 0's as tails
                fliplist = fliplist + str((numpy.random.binomial(1, self.flip_probability))) #per https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.binomial.html, add each flip to fliplist

            winnings = gamecost+(100*(fliplist.count("001"))) # find the number of Tails, Tails, Heads, multiply by fifty, add to cost of game to find winnings
            winningslist.append(winnings) # append winningslist with each games winnings
            if winnings < 0:
                losecount = losecount +1 # if winnings are less than 0, add to losecount
            totalwinnings = totalwinnings + winnings # add all the realizations of winnings together

        averagewinnings = '${:,.2f}'.format((totalwinnings/self.number_of_realizations)) # find the average winnings

        # print("Expected reward: ", averagewinnings) # print the average winnings

        # Problem 1
        FigureSupport.graph_histogram(
            observations=winningslist,
            title='Histogram of Game Winnings (1000 Games)',
            x_label='Game Winnings (Dollars)',
            y_label='Count')


        print("Problem 1: It appears that the minimum award is approximately $ -250 while the maximum award is approximately $ 250")

        # Problem 2
        loseprob = losecount/self.number_of_realizations
        print("Problem 2: Probability of Losing Money: ",loseprob)



# Running above code

# Initialize an even 50-50 game
fiftyfiftyflip = Game(0.5)
# Run the simulation
fiftyfiftyflip.Simulate(20, 1000)
