# python3
#Jēkabs Kindzulis 221RDC047

def read_input():

    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    input_type = input()

    if 'I' in input_type:

        return (input().rstrip(), input().rstrip())

    elif 'F' in input_type:

        with open("tests/06") as file:

            return (file.readline().rstrip(), file.readline().rstrip())
        

    
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
    txt_len = len(text)
    pt_len = len(pattern)
    pt_hs = hash(pattern)
    txt_hs = [hash(text[:pt_len])]
    txt_hs_len = len(txt_hs)

    if txt_len < pt_len:
        return output
    
    for i in range (txt_hs_len):
         
         if pt_hs == txt_hs[i] and text[i:i+pt_len] == pattern:

            output.append(i)

    return output

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

