import random



class settings(object):
    """Default settings assignment"""
    def __init__(self):
        """Default or seed settings"""
        self.fitness = 999999999999999 # the fitness level of the genes. 0 is 100% fit.
        self.p1x = 8
        self.p1y = 3
        self.p1z = 2
        self.p2x = 32
        self.p2y = 3
        self.p2z = 2
        self.dis_norm = 112
        self.window_size = 3
        self.min_disp = 16
        self.num_disp = self.dis_norm-self.min_disp
        self.minDisparity = self.min_disp
        self.numDisparities = self.num_disp
        self.blockSize = 16
        self.P1 = self.p1x*self.p1y*self.window_size**self.p1z
        self.P2 = self.p2x*self.p2y*self.window_size**self.p2z
        self.disp12MaxDiff = 1
        self.uniquenessRatio = 3
        self.speckleWindowSize = 10
        self.speckleRange = 32
        self.mutation_rate = 0.025
        self.minimum = 0 # min value allowed for variables
        self.maximum = 500 # max value allowed for variables
        self.name = 0 # the name or number of the phenotype
        self.path = ''
        self.path2 = ''
    
    def build_list(self):
        the_list = [self.fitness,
        self.p1x,
        self.p1y,
        self.p1z,
        self.p2x,
        self.p2y,
        self.p2z,
        self.dis_norm,
        self.window_size,
        self.min_disp,
        self.num_disp,
        self.minDisparity,
        self.numDisparities,
        self.blockSize,
        self.P1,
        self.P2,
        self.disp12MaxDiff,
        self.uniquenessRatio,
        self.speckleWindowSize,
        self.speckleRange,
        self.mutation_rate,
        self.minimum,
        self.maximum,
        self.name
        ]
        return the_list

class gene(settings):
    """Default settings assignment"""
    def print_windows(self):
        """Prints current settings"""
        keys = []
        values = []
        index = 0
        for i in self.__dict__.keys():
            item = str(i) + " " + str(self.__dict__.values()[index])
            index = index + 1
            print item
    
    def get_values(self):
        """saves items to a list"""
        values = []
        index = 0
        for i in self.__dict__.keys():
            item = self.__dict__.values()[index]
            index = index + 1
            values.append(item)
        self.values = values
    

    def mutate(self):
        """Roles the dice for a mutation and returns the new values if 
        it mutates"""
        rate = self.mutation_rate # Short-hand
        self.p1x = mutation(rate, self.p1x, self)
        self.p1y = mutation(rate, self.p1y, self)
        self.p1z = mutation(rate, self.p1z, self)
        self.p2x = mutation(rate, self.p2x, self)
        self.p2y = mutation(rate, self.p2y, self)
        self.p2z = mutation(rate, self.p2z, self)
        self.dis_norm = mutation(rate, self.dis_norm, self)
        self.window_size = mutation(rate, self.window_size, self)
        self.min_disp = mutation(rate, self.min_disp, self)
        self.num_disp = self.dis_norm-self.min_disp
        self.minDisparity = self.min_disp # Don't mutate again!
        self.numDisparities = self.num_disp # Don't mutate again!
        self.blockSize = mutation(rate, self.blockSize, self)
        self.P1 = self.p1x*self.p1y*self.window_size**self.p1z
        self.P2 = self.p2x*self.p2y*self.window_size**self.p2z
        self.disp12MaxDiff = mutation(rate, self.disp12MaxDiff, self)
        self.uniquenessRatio = mutation(rate,self.uniquenessRatio,self)
        self.speckleWindowSize = mutation(rate,self.uniquenessRatio, self)
        self.speckleRange = mutation(rate, self.speckleRange, self)
    

    def randomize(self):
        """Randomizes settings within given range."""
        minimum = self.minimum
        maximum = self.maximum
        self.p1x = random.randrange(minimum,maximum)
        self.p1y = random.randrange(minimum,maximum)
        self.p1z = random.randrange(minimum,maximum)
        self.p2x = random.randrange(minimum,maximum)
        self.p2y = random.randrange(minimum,maximum)
        self.p2z = random.randrange(minimum,maximum)
        self.dis_norm = random.randrange(minimum,maximum)
        self.window_size = random.randrange(minimum,maximum)
        self.min_disp = random.randrange(minimum,maximum)
        self.num_disp = self.dis_norm-self.min_disp
        self.minDisparity = self.min_disp
        self.numDisparities = self.num_disp
        self.blockSize = random.randrange(minimum,maximum)
        self.P1 = self.p1x*self.p1y*self.window_size**self.p1z
        self.P2 = self.p2x*self.p2y*self.window_size**self.p2z
        self.disp12MaxDiff = random.randrange(minimum,maximum)
        self.uniquenessRatio = random.randrange(minimum,maximum)
        self.speckleWindowSize = random.randrange(minimum,maximum)
        self.speckleRange = random.randrange(minimum,maximum) #Maybe change back to normal?
    
    def import_gene(self, a_list):
        """Assigns new defualt values based on items in  the list"""
        self.fitness = int(a_list[1])
        self.p1x = int(a_list[2])
        self.p1y = int(a_list[3])
        self.p1z = int(a_list[4])
        self.p2x = int(a_list[5])
        self.p2y = int(a_list[6])
        self.p2z = int(a_list[7])
        self.dis_norm = int(a_list[8])
        self.window_size = int(a_list[9])
        self.min_disp = int(a_list[10])
        self.num_disp = int(a_list[11])
        self.minDisparity = int(a_list[12])
        self.numDisparities = int(a_list[13])
        self.blockSize = int(a_list[14])
        self.P1 = int(a_list[15])
        self.P2 = int(a_list[16])
        self.disp12MaxDiff = int(a_list[17])
        self.uniquenessRatio = int(a_list[18])
        self.speckleWindowSize = int(a_list[19])
        self.speckleRange = int(a_list[20])
        self.mutation_rate = float(a_list[21])
        self.minimum = int(a_list[22])
        self.maximum = int(a_list[23])
        self.name = int(a_list[24])
    
    def copy_gene(self, papa):
        """Randomly blends DNA togeth from mother and papa"""
        f = papa
        self.p1x = int(papa.p1x)
        self.p1y = int(papa.p1y)
        self.p1z = int(papa.p1z)
        self.p2x = int(papa.p2x)
        self.p2y = int(papa.p2y)
        self.p2z = int(papa.p2z)
        self.dis_norm = int(papa.dis_norm)
        self.window_size = int(papa.window_size)
        self.min_disp = int(papa.min_disp)
        self.num_disp = int(papa.num_disp)
        self.minDisparity = int(papa.minDisparity)
        self.numDisparities = int(papa.numDisparities)
        self.blockSize = int(papa.blockSize)
        self.P1 = int(papa.P1)
        self.P2 = int(papa.P2)
        self.disp12MaxDiff = int(papa.disp12MaxDiff)
        self.uniquenessRatio = int(papa.uniquenessRatio)
        self.speckleWindowSize = int(papa.speckleWindowSize)
        self.speckleRange = int(papa.speckleRange)


    def mate(self, papa, mamma):
        """Randomly blends DNA togeth from mother and papa"""
        m = papa
        f = papa
        self.p1x = int(random.choice([m.p1x, f.p1x]))
        self.p1y = int(random.choice([m.p1y, f.p1y]))
        self.p1z = int(random.choice([m.p1z, f.p1z]))
        self.p2x = int(random.choice([m.p2x, f.p2x]))
        self.p2y = int(random.choice([m.p2y, f.p2y]))
        self.p2z = int(random.choice([m.p2z, f.p2z]))
        self.dis_norm = int(random.choice([m.dis_norm, f.dis_norm]))
        self.window_size = int(random.choice([m.window_size, f.window_size]))
        self.min_disp = int(random.choice([m.min_disp, f.min_disp]))
        self.num_disp = int(random.choice([m.num_disp, f.num_disp]))
        self.minDisparity = int(random.choice([m.minDisparity, f.minDisparity]))
        self.numDisparities = int(random.choice([m.numDisparities, f.numDisparities]))
        self.blockSize = int(random.choice([m.blockSize, f.blockSize]))
        self.P1 = int(random.choice([m.P1, f.P1]))
        self.P2 = int(random.choice([m.P2, f.P2]))
        self.disp12MaxDiff = int(random.choice([m.disp12MaxDiff, f.disp12MaxDiff]))
        self.uniquenessRatio = int(random.choice([m.uniquenessRatio, f.uniquenessRatio]))
        self.speckleWindowSize = int(random.choice([m.speckleWindowSize, f.speckleWindowSize]))
        self.speckleRange = int(random.choice([m.speckleRange, f.speckleRange]))


    def restate(self):
        """Recalculates variables... This may not actually be needed."""
        self.num_disp = self.dis_norm-self.min_disp
        self.minDisparity = self.min_disp
        self.numDisparities = self.num_disp
        self.P1 = self.p1x*self.p1y*self.window_size**self.p1z
        self.P2 = self.p2x*self.p2y*self.window_size**self.p2z


def mutation(mutation_rate, current_gene, genes):
    """Returns a random number if True"""
    True_False = dice(mutation_rate)
    if True_False == True:
        #print " Mutation occured!"
        return random.randint(genes.minimum, genes.maximum)
    else:
        return current_gene


def dice(chances):
    """Returns true if probablitly is randomly select"""
    num = random.uniform(0.0, 1.0)
    if num < chances:
        return True
    else:
        return False
    
