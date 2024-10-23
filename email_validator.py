# source https://snov.io/knowledgebase/what-is-a-valid-email-address-format/
#        https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains

#        Original Top Level Domains Lang huhuhu
#        com,org,net,int,edu,gov,mil

# The reason akong gi separate ang checker from start until domain. and domain ending kay
# ma broken siya sa tungod sa isalnum and isalpha na checker sa first part

# i couldve done something about it pero it was 2 am and I was sleepy maybe add a condition or something HAHAHAHAHAHAHAHAH

# FSM A everthing before domain ending
#   State  period   dash    underscore  isalpha isalnum @  
#   0      -1       -1      -1          1       1       -1 
#   1      2        2       2           1       1       4 
#   2      -1       -1      -1          3       3       -1 
#   3       2       2       2           3       3       4  
#   4      -1       -1      -1          5       5       -1
#   5      7        6       -1          5       5       -1
#   6      -1       -1      -1          8       8       -1 
#   7      -1       -1      -1          -1      -1      -1  FS
#   8      7        6       -1          8       8       -1 
# FSM B domain ending top level only 
# com,org,net,int,edu,gov,mil
#   STATE  C   O   M   R   G   N   E   T   I   U   V   L   D
#   0      1   3   13 -1   11  5   9  -1   7  -1  -1  -1   -1
#   com
#   1      -1   2  -1  -1  -1  -1  -1  -1  -1  -1  -1  -1  -1
#   2      -1  -1  15  -1  -1  -1  -1  -1  -1  -1  -1  -1  -1
#   org
#   3      -1  -1  -1   5  -1  -1  -1  -1  -1  -1  -1  -1  -1
#   4      -1  -1  -1  -1  15  -1  -1  -1  -1  -1  -1  -1  -1
#   net
#   5      -1  -1  -1  -1  -1  -1   6  -1  -1  -1  -1  -1  -1
#   6      -1  -1  -1  -1  -1  -1  -1  15  -1  -1  -1  -1  -1
#   int
#   7      -1  -1  -1  -1  -1   8  -1  -1  -1  -1  -1  -1  -1
#   8      -1  -1  -1  -1  -1  -1  -1  15  -1  -1  -1  -1  -1
#   edu
#   9      -1  -1  -1  -1  -1  -1  -1  -1  -1  -1  -1  -1  10
#   10     -1  -1  -1  -1  -1  -1  -1  -1  -1  15  -1  -1  -1
#   gov
#   11     -1  12  -1  -1  -1  -1  -1  -1  -1  -1  -1  -1  -1
#   12     -1  -1  -1  -1  -1  -1  -1  -1  -1  -1  15  -1  -1
#   mil
#   13     -1  -1  -1  -1  -1  -1  -1  -1  14  -1  -1  -1  -1
#   14     -1  -1  -1  -1  -1  -1  -1  -1  -1  -1  -1  -1  15
#   check ending
#   15     -1  -1  -1  -1  -1  -1  -1  -1  -1  -1  -1  -1  -1

transition_table = [
    #    State, period, dash, underscore, isalpha, isalnum, @
    [0,   -1,    -1,   -1,       1,       1,      -1],  # State 0
    [1,    2,     2,    2,       1,       1,       4],  # State 1
    [2,   -1,    -1,   -1,       3,       3,      -1],  # State 2
    [3,    2,     2,    2,       3,       3,       4],  # State 3
    [4,   -1,    -1,   -1,       5,       5,      -1],  # State 4
    [5,    7,     6,    -1,       5,       5,      -1],  # State 5
    [6,   -1,    -1,   -1,       8,       8,      -1],  # State 6
    [7,   -1,    -1,   -1,      -1,      -1,      -1],  # State 7 (Final State)
    [8,    7,     6,    -1,       8,       8,      -1],  # State 8
]

domain_end_check = [
    #    C    O   M   R   G   N   E   T   I   U   V   L   D
    [0,  1,   3,  13, -1,  11,  5,   9,  -1,  7,  -1, -1, -1, -1],  # State 0
    [1, -1,   2,  -1, -1, -1, -1,  -1, -1, -1, -1, -1, -1, -1],  # State 1 com
    [2, -1,  -1,  15, -1, -1, -1,  -1, -1, -1, -1, -1, -1, -1],  # State 2

    [3, -1,  -1,  -1,  4, -1, -1,  -1, -1, -1, -1, -1, -1, -1],  # State 3 org
    [4, -1,  -1,  -1, -1, 15, -1,  -1, -1, -1, -1, -1, -1, -1],  # State 4 

    [5, -1,  -1,  -1, -1, -1, -1,   6, -1, -1, -1, -1, -1, -1],  # State 5  net
    [6, -1,  -1,  -1, -1, -1, -1,  -1, 15, -1, -1, -1, -1, -1],  # State 6

    [7, -1,  -1,  -1, -1, -1,  8,  -1, -1, -1, -1, -1, -1, -1],  # State 7  int
    [8, -1,  -1,  -1, -1, -1, -1,  -1, 15, -1, -1, -1, -1, -1],  # State 8

    [9, -1,  -1,  -1, -1, -1, -1,  -1, -1, -1, -1, -1, -1, 10],  # State 9  edu
    [10,-1,  -1,  -1, -1, -1, -1,  -1, -1, -1, 15, -1, -1, -1],  # State 10

    [11, -1,  12,  -1, -1, -1, -1,  -1, -1, -1, -1, -1, -1, -1],  # State 11 gov
    [12, -1,  -1,  -1, -1, -1, -1,  -1, -1, -1, -1, 15, -1, -1],  # State 12

    [13, -1,  -1,  -1, -1, -1, -1,  -1, -1, 14, -1, -1, -1, -1],  # State 13 mil
    [14, -1,  -1,  -1, -1, -1, -1,  -1, -1, -1, -1, -1, -1, 15],  # State 14 (check ending)

    [15,-1,  -1,  -1, -1, -1, -1,  -1, -1, -1, -1, -1, -1, -1]   # State 15
]

def is_valid_char(char):
    if char.isalpha():
        return 4
    elif char.isalnum():
        return 5 
    elif char == '.':
        return 1 
    elif char == '-':
        return 2 
    elif char == '_':
        return 3  
    elif char == '@':
        return 6  
    else:
        return -1

def domain_char_check(arg):
    char = arg.upper()
    # C   O   M   R   G   N   E   T   I   U   V   L   D
    if char == 'C': return 1
    elif char == 'O': return 2
    elif char == 'M': return 3
    elif char == 'R': return 4
    elif char == 'G': return 5
    elif char == 'N': return 6
    elif char == 'E': return 7
    elif char == 'T': return 8
    elif char == 'I': return 9
    elif char == 'U': return 10
    elif char == 'V': return 11
    elif char == 'L': return 12
    elif char == 'D': return 13
    else: return -1

def check_left(email):
    # print(email)
    state = 0
    for i in email:
        char_type = is_valid_char(i)
        if char_type == -1: 
            return False
        
        next_state = transition_table[state][char_type]
        if next_state == -1: 
            return False
        
        state = next_state

    return state == 7 

def check_right(email):
    # print(email)
    state = 0
    for i in email:
        char_type = domain_char_check(i)

        if char_type == -1:
            return False
        
        next_state = domain_end_check[state][char_type]
        if next_state == -1:
            return False
        
        state = next_state

    return state == 15
        
# email = input("Enter email: ")
# if check_left(email[:-3]) and check_right(email[-3:]):
#     print("Valid Email")
# else:
#     print("Not valid ://")

def checkmany(emails):
    for email in emails:
        print(email)
        if check_left(email[:-3]) and check_right(email[-3:]):
            print("Valid Email")
        else:
            print("Not valid ://")

emails = [
    # "j-doe1234@domain.com",
    # "sara.smith85@domain.com",
    # "jessy_luther@domain.com",
    # "my.email123@domain.com",
    # "sales@domain.com",
    # "username@domain.org",
    # "username@mail-provider.edu",
    # "plainaddress",
    # "@missingusername.com",
    # "username@.com",
    # "username@domain..com",
    # "user@domain.c",
    # "user@domain.123",
    # "user@domain-.com",
    # "user@domain.com.",
    # "user@.domain.com",
    # "user@domain.c@om"
    "nino-rey.cabiltes@gmail.com"
]

checkmany(emails)