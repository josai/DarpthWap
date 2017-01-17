import random
import string
import os


def weasel_program():
    inputs = prompt_user()
    data = evolution(inputs)


def prompt_user():
    while True:
        info_1 = ('The weasel program, Dawkins weasel, or the Dawkins weasel'+
                ' is a thought experiment and a variety of computer '+
                'simulations illustrating it. Their aim is to demonstrate '+
                'that the process that drives evolutionary systems random '+ 
                'variation combined with nonrandom cumulative selection is '+
                'different from pure chance. - wikipedia'
                 )
        info_2 = ('This program accepts a seed and target word as input. '+
                'The seed word is simply the word you want to start with and'+
                ' the target is the word you want to end with. The words can'+
                ' be completely random!'
                 )
        info_3 = ('The program also calculates how long it would take to get'+
                ' to your target word by randomly generating strings '+
                'of random characters on your machine. Randomly generating '+
                'strings is basically the same as putting a monkey at a '+
                'typewriter, eventually you will get shakespeare, or the'+
                ' script for The Phantom Menace if you are too impatient,'+
                ' surrounded by yes monkeys and rush production.'
                 )
        print_lines(lines=(['']*2))
        print_lines(normalize_string(info_1, 4, 79))
        print_lines(lines=(['']*1))
        print_lines(normalize_string(info_2, 4, 79))
        print_lines(lines=(['']*1))
        print_lines(normalize_string(info_3, 4, 79))
        print_lines(lines=(['']*2))
        seed = raw_input('    Enter Seed: ')
        target = raw_input('    Enter Target: ')
        clear_screen()
        if validate_input(seed) and validate_input(target):
            inputs = equalize_strings(seed, target)
            return inputs


def normalize_string(string, start_space, max_line_ength):
    """
    Normalizes length of lines and returns each line as a list.
    Also adds some space to the begging of each line.
    """
    string = str(string)
    string = string.split()
    lines = []
    line = (' ' * start_space)
    for word in string:
        if (len(line+word)+1) > max_line_ength:
            lines.append(line)
            line = (' ' * start_space)
        line += (word + " ")
    if len(line) > 0:
        lines == lines.append(line)
    return (lines)


def print_lines(lines):
    """
    Input 'lines=([''] * x)' for blank lines.
    """
    for line in lines:
        print (line)


def validate_input(user_input):
    for character in user_input:
        if character not in string.printable:
            return False
    return True


def clear_screen():
    """
    Clears console window of all text.
    """
    os.system('cls')


def equalize_strings(string_1, string_2):
    if len(string_1) > len(string_2):
        length = len(string_1)
        string_2 = (string_2 + (" "*length))[:length]
    else:
        length = len(string_2)
        string_1 = (string_1 + (" "*length))[:length]
    strings = [string_1, string_2]
    return strings


def evolution(inputs):
    seed = inputs[0]
    target = inputs[1]
    while True:
        generation = birth_generation([seed,target], 100)
        print_generation(generation)
        generation.reverse()
        seed = generation[0][1]
        fitness = generation[0][0]
        raw_input('stawp')
        

def birth_generation(inputs, num_babies):
    new_borns = []
    while len(new_borns) < num_babies:
        baby = mutate(inputs)
        new_borns.append(baby)
    new_borns.sort()
    return new_borns
    

def mutate(inputs):
    mutation_rate = 0.1
    DNA = inputs[0]
    new_DNA = ''
    for gene in DNA:
        chance = random.uniform(0.0, 1.0)
        if chance > (1.0 - mutation_rate):
            gene = random.choice(string.printable)
        new_DNA += gene
    fitness = fitness_function(new_DNA,inputs[1])
    return [fitness,new_DNA]


def fitness_function(new_DNA, DNA):
    index = 0
    fitness = 0.0
    for character in new_DNA:
        if character == DNA[index]:
            fitness += 1.0
        index += 1
    fitness = int((fitness / float(len(DNA))) * 100)
    return fitness


def print_generation(generation):
    for baby in generation:
        print "    " + str(baby[1]) + ' Fitness: ' + str(baby[0]) + '%'
        



weasel_program()
raw_input('stawp')

