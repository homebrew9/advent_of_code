import sys
from collections import Counter

def determineType(hand):
    cntr = Counter(hand)
    type_no = ''.join([str(x) for x in sorted(cntr.values())])
    if type_no == '5':
        hand_type = ['five_kind', 7]
    elif type_no == '14':
        hand_type = ['four_kind', 6]
    elif type_no == '23':
        hand_type = ['full_house', 5]
    elif type_no == '113':
        hand_type = ['three_kind', 4]
    elif type_no == '122':
        hand_type = ['two_pair', 3]
    elif type_no == '1112':
        hand_type = ['one_pair', 2]
    elif type_no == '11111':
        hand_type = ['high_card', 1]
    return hand_type

def determineTypeWithNewRule(hand):
    #print(f'\thand = {hand}')
    cntr = Counter(hand)
    if 'J' in hand:
        if cntr['J'] == 5:
            # '5' => 'JJJJJ', keep it as it is
            hand_type = ['five_kind', 7]
        elif cntr['J'] == 4:
            # '14' => 'AJJJJ', set it to 'AAAAA'
            hand_type = ['five_kind', 7]
        elif cntr['J'] == 3:
            # '23'  => '55JJJ', set it to '55555'
            # '113' => 'K6JJJ', set it to 'K6KKK'
            max_val = max(Counter(hand.replace('J','')).values())
            if max_val == 2:
                hand_type = ['five_kind', 7]
            elif max_val == 1:
                hand_type = ['four_kind', 6]
        elif cntr['J'] == 2:
            # '23'   => 'JJAAA', set it to 'AAAAA'
            # '122'  => 'AKKJJ', set it to 'AKKKK'
            # '1112' => 'T98JJ', set it to 'T98TT'
            max_val = max(Counter(hand.replace('J','')).values())
            if max_val == 3:
                hand_type = ['five_kind', 7]
            elif max_val == 2:
                hand_type = ['four_kind', 6]
            elif max_val == 1:
                hand_type = ['three_kind', 4]
        elif cntr['J'] == 1:
            # '11111' => 'AKQTJ' , set it to 'AKQTA' (one_pair)
            # '1112'  => 'JAK77' , set it to '7AK77' (three_kind)
            # '122'   => 'JAAQQ' , set it to 'AAAQQ' (full_house)
            # '113'   => 'J9555' , set it to '59555' (four_kind)
            # '14'    => 'JQQQQ' , set it to 'QQQQQ' (five_kind)
            cntr1 = Counter(hand.replace('J',''))
            type_no1 = ''.join([str(x) for x in sorted(cntr1.values())])
            if type_no1 == '1111':
                hand_type = ['one_pair', 2]
            elif type_no1 == '112':
                hand_type = ['three_kind', 4]
            elif type_no1 == '22':
                hand_type = ['full_house', 5]
            elif type_no1 == '13':
                hand_type = ['four_kind', 6]
            elif type_no1 == '4':
                hand_type = ['five_kind', 7]
    else:
        type_no = ''.join([str(x) for x in sorted(cntr.values())])
        if type_no == '5':
            hand_type = ['five_kind', 7]
        elif type_no == '14':
            hand_type = ['four_kind', 6]
        elif type_no == '23':
            hand_type = ['full_house', 5]
        elif type_no == '113':
            hand_type = ['three_kind', 4]
        elif type_no == '122':
            hand_type = ['two_pair', 3]
        elif type_no == '1112':
            hand_type = ['one_pair', 2]
        elif type_no == '11111':
            hand_type = ['high_card', 1]
    return hand_type

# =========================
# Main section
# =========================

file = sys.argv[1]
hsh = dict()
for line in open(file):
    line = line.rstrip('\n')
    hand, bid = line.split()
    hand_type, strength = determineType(hand)
    hsh[hand] = [int(bid), hand_type, strength]

#for k, v in hsh.items():
#    print(k, v)

hsh_val = [(k, v) for k, v in hsh.items()]
#print(hsh_val)

# In Camel Cards, you get a list of hands, and your goal is to order them based on the strength of each hand.
# A hand consists of five cards labeled one of A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2.
# The relative strength of each card follows this order, where A is the highest and 2 is the lowest.
# => We apply translation as follows: 'AKQJT98765432' => 'ZYXWV98765432'

arr = sorted(hsh_val, key=lambda x: (x[1][2], x[0].replace('A','Z').replace('K','Y').replace('Q','X').replace('J','W').replace('T','V')))
#print(arr)
#for item in arr:
#    print(item)

res = sum([(i+1) * v[1][0] for i, v in enumerate(arr)])
print(res)

# =================
# Part 2
# =================
hsh1 = dict()
for line in open(file):
    line = line.rstrip('\n')
    hand, bid = line.split()
    hand_type, strength = determineTypeWithNewRule(hand)
    hsh1[hand] = [int(bid), hand_type, strength]

hsh_val1 = [(k, v) for k, v in hsh1.items()]
#print(hsh_val1)

arr1 = sorted(hsh_val1, key=lambda x: (x[1][2], x[0].replace('A','Z').replace('K','Y').replace('Q','X').replace('T','W').replace('J','1')))
#for item in arr1:
#    print(item)

# 252017385 : That's not the right answer; your answer is too high.
# 251824095 : That's the right answer!
res1 = sum([(i+1) * v[1][0] for i, v in enumerate(arr1)])
print(res1)


#  --- Part Two ---
#  
#  To make things a little more interesting, the Elf introduces one additional rule.
#  Now, J cards are jokers - wildcards that can act like whatever card would make the hand the strongest type possible.
#  
#  To balance this, J cards are now the weakest individual cards, weaker even than 2.
#  The other cards stay in the same order: A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J.
#  
#  J cards can pretend to be whatever card is best for the purpose of determining hand type; for example, QJJQ2 is now considered four of a kind.
#  However, for the purpose of breaking ties between two hands of the same type, J is always treated as J,
#  not the card it's pretending to be: JKKK2 is weaker than QQQQ2 because J is weaker than Q.
#  
#  Now, the above example goes very differently:
#  
#  32T3K 765
#  T55J5 684
#  KK677 28
#  KTJJT 220
#  QQQJA 483
#  
#      32T3K is still the only one pair; it doesn't contain any jokers, so its strength doesn't increase.
#      KK677 is now the only two pair, making it the second-weakest hand.
#      T55J5, KTJJT, and QQQJA are now all four of a kind! T55J5 gets rank 3, QQQJA gets rank 4, and KTJJT gets rank 5.
#  
#  With the new joker rule, the total winnings in this example are 5905.
#  
#  Using the new joker rule, find the rank of every hand in your set. What are the new total winnings?
#  


