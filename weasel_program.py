import random
import string
import os
import time


def weasel_program():
    while True:
        clear_screen()
        inputs = prompt_user()
        start_time = time.time()
        data = evolution(inputs)
        years_elapsed = (time.time() - start_time) / 3.154e+7
        num_of_generations = data[0]
        len_of_word = data[1]
        avg_time = average_time_per_character(3000, len_of_word)
        final_statement(avg_time, years_elapsed, num_of_generations)


def prompt_user():
    while True:
        info_1 = ('The weasel program, Dawkins weasel, or the Dawkins weasel' +
                  ' is a thought experiment and a variety of computer ' +
                  'simulations illustrating it. Their aim is to demonstrate ' +
                  'that the process that drives evolutionary systems random ' +
                  'variation combined with nonrandom cumulative selection is' +
                  ' different from pure chance. - wikipedia'
                  )
        info_2 = ('This program accepts a seed and target word as input. ' +
                  'The seed word is simply the word you want to start with ' +
                  'and the target is the word you want to end with. The ' +
                  'words can be completely random!'
                  )
        info_3 = ('The program also calculates how long it would take to ' +
                  'get to your target word by randomly generating strings ' +
                  'of random characters on your machine. Randomly generating' +
                  ' strings is basically the same as putting a monkey at a ' +
                  'typewriter, eventually you will get Shakespeare, or the' +
                  ' script for The Phantom Menace if you are too impatient,' +
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


def average_time_per_character(samples, num):
    """
    Calculates the average time to randomly and correctly generate a word.
    Returns the years it would take.
    """
    data = []
    target = "A"
    count = 0
    start_time = time.time()
    while count < samples:
        selection = random.choice(string.printable)
        if selection == target:
            time_elapsed = time.time() - start_time
            count += 1
            data.append(time_elapsed)
            start_time = time.time()
    average_time = sum(data) / len(data)
    second = 1.0
    microseconds = 1000000.0 * second
    avg_microseconds = average_time * microseconds
    time_in_seconds = (avg_microseconds ** num) / microseconds
    seconds_in_year = 3.154e+7
    years = time_in_seconds / seconds_in_year
    return years


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
    gen_num = 1
    print ''
    print '    GEN   DNA'
    while True:
        generation = birth_generation([seed, target], 100)
        generation.reverse()
        seed = generation[0][1]
        fitness = generation[0][0]
        print_generation([[fitness, seed]], gen_num)
        gen_num += 1
        if fitness >= 100:
            print ''
            print ''
            return [gen_num, len(target)]


def birth_generation(inputs, num_babies):
    new_borns = []
    while len(new_borns) < num_babies:
        baby = mutate(inputs)
        new_borns.append(baby)
    new_borns.sort()
    return new_borns


def mutate(inputs):
    mutation_rate = 0.05
    DNA = inputs[0]
    new_DNA = ''
    for gene in DNA:
        chance = random.uniform(0.0, 1.0)
        if chance > (1.0 - mutation_rate):
            gene = random.choice(string.printable)
        new_DNA += gene
    fitness = fitness_function(new_DNA, inputs[1])
    return [fitness, new_DNA]


def fitness_function(new_DNA, DNA):
    index = 0
    fitness = 0.0
    for character in new_DNA:
        if character == DNA[index]:
            fitness += 1.0
        index += 1
    fitness = int((fitness / float(len(DNA))) * 100)
    return fitness


def print_generation(generation, gen_num):
    gen_num = (str(gen_num) + '.          ')[:6]
    for baby in generation:
        print_statement = ((" "*4) +
                           gen_num +
                           str(baby[1]) +
                           '    Fitness: ' +
                           str(baby[0]) +
                           '%'
                           )
        print print_statement


def final_statement(time, actual_time, gen_num):
    """
    Prints the final statement. Which changes depending on the time it would
    take to randomly generate the word.
    """
    from time import sleep
    gen_num += -1
    age_of_the_universe = 1382000000.0
    if time < 1.0:
        length = 5
        if 'e-' in str(time):
            length = 1000
        years = str(time)[:length]
    else:
        years = add_comma(str(int(time)))
    percent = str(((time / actual_time)))
    universes = add_comma(str(int(time / age_of_the_universe)))
    end_1 = ('It would take %s years to correctly, randomly generate this ' +
             'string on this computer. ') % (years,)
    end_2 = ('It would take %s years to correctly, randomly generate this' +
             ' string from pure chance on this computer. That is longer ' +
             'than the universe has existed. which is 13.82 billion years.' +
             ' Thats %s universes!!! ') % (years, universes, )
    end_stat = ('The actual time it took was %s seconds, which is %s times' +
                ' faster because of evolution via selection. %s creatures ' +
                'or %s generations had to be born in order to get to this ' +
                'answer.'
                ' ') % (str(actual_time*3.154e+7),
                        percent, str(gen_num*100),
                        str(gen_num)
                        )
    if time < age_of_the_universe:
        end = end_1 + end_stat
    else:
        end = end_2 + end_stat
    statement = normalize_string(end, 4, 79)
    joke = 'Now spending the next %s years calculating that string!' % (years,)
    print_lines(statement)
    sleep(16)
    print ''
    print_lines(normalize_string(joke, 4, 79))
    print ''
    sleep(8)
    print'    Just kidding!!!'
    sleep(4)
    print ''
    print ''
    raw_input('    Press any key to restart game.')


def add_comma(a_string):
    a_string = a_string[::-1]
    new_string = ''
    count = 1
    if len(a_string) > 3:
        for c in a_string:
            if count == 3:
                c = c + ','
                count = 0
            new_string += c
            count = count + 1
        return new_string[::-1]
    return a_string[::-1]


weasel_program()
