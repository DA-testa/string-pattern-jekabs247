# python3
#Jēkabs Kindzulis 221RDC047

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    input_k = input()

    while 'I' not in input_k or 'F' not in input_k:

        if 'I' in input_k:

            return (input().rstrip(), input().rstrip())

        elif 'F' in input_k:

            with open("./tests/06", "r") as file:

                return (file.readline().rstrip(), file.readline().rstrip())
        
        input_k = input()
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):

    # this function should find the occurances using Rabin Karp alghoritm 

    output = []
    text_len = len(text)
    pattern_len = len(pattern)

    output = []

    for i in range(text_len - pattern_len + 1):

        if (pattern == text[i:i+p]):

            output.append(i)

    # and return an iterable variable
    return output




# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

