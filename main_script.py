

import numpy as np
import os.path
from GeneMaker import *
from cv2 import *
import cv2
import PIL
from PIL import Image
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import gc
import os
from DataFetcher import *



def run_program():
    #spread_seeds(100)
    da = gene()
    while True:
        clear_screen()
        clear__data()
        da = breed(100,2,da)
        gc.collect()


def clear_screen():
    """Clears console window of all text."""
    clear = lambda: os.system('cls')
    clear()


def spread_seeds(num):
    """Creates random seeds of settings. Returns a list
    a list of random seeds."""
    population = get_pop_size()
    count = population
    num = num + population
    while count < (num+1):
        birth_baby(count, 0)
        print " baby number: " + str(count)
        count = count + 1


def breed(breeding_pool, survial_rate, dada):
    """Breeds the breeding pool, which is the number of recent genes,
    so a breeding pool of 10 = the last 10 genes produced. It then 
    sorts the breeding pool by the ones with the best fitness score.
    After the sorted list it breeds only the ones in the top survival
    pool. So a survival rate of 5 would mean only the top 5 survive.
    """
    breed_pool = get_pool(breeding_pool)
    breed_pool = breed_pool[:survial_rate]
    breed_pool.reverse()
    for i in breed_pool:
        print i.fitness
    breed_pool.reverse()
    print " Top creatures so far ^"
    breed_count = 0
    population = get_pop_size()
    while breed_count < len(breed_pool):
        father = breed_pool[breed_count]
        mother = breed_pool[(breed_count+1)]
        if dada.fitness < father.fitness:
            print ' we didnt get a better dad'
            father = dada # Makes sure the top guy always wins
        num_offspring = 100 #random.randrange(0, 5)
        babies = 0
        while babies < (num_offspring + 1):
            baby = birth_baby(population, father, mother)
            population = population + 1
            babies = babies + 1            
        breed_count = breed_count + 2
    return father


def get_pool(max_index):
    """Imports a list of object within the max index
    Returns them in sorted order"""
    index = 0
    all_genes = []
    while index < (max_index + 1):
        gene_data = get_gene_data(index)
        a_gene = gene()
        a_gene.import_gene(gene_data)
        all_genes.append(a_gene)
        index = index + 1
    all_genes = sorted(all_genes, 
            key=lambda g: 
            g.fitness, 
            reverse=False
    )
    return all_genes


def birth_baby(population_size, papa, mamma):
    """handles exceptions and trys to birth a disparity map until
    it is successful."""
    try_again = True
    still_born = 0
    while try_again == True:
        try:
            #ot_gene.mate(mom, papa)
            pot_gene = gene()
            pot_gene.copy_gene(papa)
            pot_gene.mutate()
            pot_gene.restate()
            pot_gene.name = population_size
            create_disparity_map(pot_gene)
            log_ping()
            try_again = False
        except:
            still_born = still_born + 1
            print " Still born, trying again..."

    output_im = Image.open(pot_gene.path).convert('LA')
    truth = Image.open("truth_L.png").convert('LA')
    max_diff_ground_truth = float(len(list(truth.getdata())) * 255)
    pot_gene.name = population_size
    pot_gene.fitness = calculate_similarity(truth, output_im)
    fitness_percent = 1.0 - (float((pot_gene.fitness)/max_diff_ground_truth))
    print str(pot_gene.name) +' '+ str(fitness_percent)
    fitness_percent = str(fitness_percent*100).replace(".","_")
    
    #raw_input(fitness_percent)
    file_name = str(fitness_percent) + ".png"
    pot_gene.path2 = os.path.join(pot_gene.path2, file_name)
    output_im.save(pot_gene.path2)
    log_data(pot_gene)
    return pot_gene


def get_gene_data(an_index):
    """Gets the gene data from an index. Returns a list"""
    file_name = "population data.txt"
    text_file = open(file_name, "r")
    data = text_file.readlines()
    text_file.close()
    data.reverse()
    data = str(data[an_index])
    data = data.split()
    return data


def clear__data(): 
    """cleans the text file up"""
    file_name = "population data.txt"
    text_file = open(file_name, "r")
    data = text_file.readlines()
    text_file.close()
    data.reverse()
    if len(data) > 500:
        data = data[:200]
        data.reverse()
        text_file = open(file_name, "w")
        for i in data:
             data = text_file.write(i)
        text_file.close()
        print " Data cleaned"


def create_disparity_map(settings):
    """Calculates and saves a disparity in the render bin."""
    imgL = cv2.imread('L.png',0)
    imgR = cv2.imread('R.png',0)
    stereo = cv2.StereoSGBM_create(settings.minDisparity,
        settings.numDisparities,
        settings.blockSize,
        settings.P1,
        settings.P2,
        settings.disp12MaxDiff,
        settings.uniquenessRatio,
        settings.speckleWindowSize,
        settings.speckleRange
    )
    #print " trying to give birth..."
    disparity = stereo.compute(imgL,imgR)
    
    phenotype = disparity
    path = ('C:\Users\The Atomizer\Desktop\Disparity'
            + ' Map Maker\Render bin')
    path2 = ('C:\Users\The Atomizer\Desktop\Disparity'
            + ' Map Maker\Rated images')
    file_name = str(settings.name) + ".png"
    full_name = os.path.join(path, file_name)
    #cv2.imwrite(file_name, phenotype) this is junk!!! Use matplt!
    mpimg.imsave(full_name, disparity)
    settings.path = full_name
    settings.path2 = path2


def calculate_similarity(ground_truth, an_image):
    """Returns the sum of absolute differences between the colors of
    the same pixels of truth image to an_image. If the number was 0
    then the image is identical"""
    an_image = list(an_image.getdata())
    ground_truth = list(ground_truth.getdata())
    index = 0
    total = 0
    for pixel in ground_truth:
        output_pixel = an_image[index]
        n = abs(pixel[0] - output_pixel[0]) # Doesn't take into account
        total = total + n                   # alpha channels.
        index = index + 1
    return total
        

def log_data(a_gene):
    """Logs all the data in a text file for each individual"""
    file_name = "population data.txt"
    data = a_gene.__dict__.values()
    data = a_gene.build_list()
    text_file = open(file_name, "a")
    text_file.write((str(a_gene.name) + " "))
    for item in data:
        item = str(item) + " "
        text_file.write(item)
    logs_list = text_file.write("\n")
    text_file.close()


def get_pop_size():
    file_name = "population data.txt"
    text_file = open(file_name, "r")
    data = text_file.readlines()
    text_file.close()
    data.reverse()
    data = str(data[0])
    data = data.split()
    #print " Population Size : " + data[0]
    return int(data[0])


def log_ping():
    """Logs all the data in a text file for each individual"""
    file_name = "ping1.txt"
    ping = basic_data()
    pid = os.getpid()
    #print pid
    text_file = open(file_name, "w")
    text_file.write(str(ping.start_time))
    text_file.write('\n')
    text_file.write(str(pid))
    text_file.close()
    #print ping.start_time


run_program()




