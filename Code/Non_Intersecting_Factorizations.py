import math

def generate_primes(n):
    prime_list = []
    prime_list.append(2)
    for num in range(3, n, 2):
        if all(num%i != 0 for i in range(3,int(math.sqrt(num))+1, 2)):
            prime_list.append(num)
    return prime_list

def factorization(num, prime_list):
    exponents = [0]*len(prime_list)
    for i in range(0, len(prime_list)):
        prime = prime_list[i]
        while num % prime == 0:
            num /= prime
            exponents[i] += 1
    return exponents

def get_next_iterate(decision_array):
    #try all combinations with no zeros
    #before trying combinations with one zero
    #before trying combinations with two zeros
    #...
    #this iteration technique was HARD to figure out but key to minimizing the zeros
    try:
        #decrement the first occurance of a +1 to a -1
        one_idx = decision_array.index(1)
        decision_array[one_idx] = -1
        return [x if x != -1 else 1 for x in decision_array[:one_idx]] + decision_array[one_idx:]

    except ValueError: #There are no 1's, only 0's and -1's
        try:
            #move the first possible zero to the left, change all -1's to +1's
            num_leading_zeros = 0
            while decision_array[num_leading_zeros] == 0:
                num_leading_zeros += 1
                if num_leading_zeros == len(decision_array):
                    return [1]*len(decision_array) #wrap around to 1111...11

            shifting_zero_idx = decision_array.index(0, num_leading_zeros) #goto exception if all zeros are leading zeros
            new_leading_zero_idx = shifting_zero_idx - num_leading_zeros - 1
            decision_array[:new_leading_zero_idx] = [1]*new_leading_zero_idx
            decision_array[new_leading_zero_idx:shifting_zero_idx] = [0]*(shifting_zero_idx-new_leading_zero_idx)
            decision_array[shifting_zero_idx] = 1
            return [ 1 if x != 0 else 0 for x in decision_array ]

        except ValueError: #introduce another zero and put them all on the right, everything else +1
            num_zeros = num_leading_zeros + 1
            decision_array[:-num_zeros] = [1]*(len(decision_array)-num_zeros)
            decision_array[-num_zeros:] = [0]*num_zeros
            return decision_array


def find_max_decision(candidates, column_idx, decision_map):
    #this recursive algorithm assigns +1, -1, or 0 to row of the candidates
    #it operates only one prime at a time larger to smaller based on column_idx
    #the decisions it makes at each recursion are stored in the decision map
    rows_to_decide = []
    decided_sum = 0
    num_candidates = len(candidates)
    for row in range(0, num_candidates):
        if candidates[row][column_idx] == 0: #dont care, anything works
            continue
        if row in decision_map: #decision has already been made
            decided_sum += decision_map[row] * candidates[row][column_idx]
            continue
        rows_to_decide.append(row)

    num_decisions = len(rows_to_decide)
    ones = [1]*num_decisions
    trial_decision = list(ones)
    while True: #do-while loop
        #print(trial_decision)
        trial_sum = 0
        for idx in range(0, num_decisions):
            row = rows_to_decide[idx]
            qualifier = trial_decision[idx]
            decision_map[row] = qualifier
            trial_sum += qualifier * candidates[row][column_idx]

        if decided_sum + trial_sum == 0:
            if column_idx == 0: #end of the line, we found a solution!
                return decision_map
            else:
                #make a copy of the decision map and solve a subproblem
                sub_problem = find_max_decision(candidates, column_idx-1, dict(decision_map))
                if sub_problem is not None: #subproblem found a solution
                    #print(sub_problem)
                    return sub_problem

        trial_decision = get_next_iterate(trial_decision)
        if trial_decision == ones:
            break #got back to beginning, break the do-while

    return None


MAX = 150 #the total number of problems we are going to solve
master_prime_list = generate_primes(MAX)

for problem_num in range(2, MAX+1): #the maximum number for a particular problem
    N = problem_num
    prime_list = [ x for x in master_prime_list if x <= N ] #avoid generating primes everytime
    #print(str(N) + " prime_list = " + str(prime_list))

    candidates = []
    for num in range(2, N+1): #just arrays of the prime factorizations for numbers 2 to N
        candidate = factorization(num, prime_list)
        candidates.append(candidate)
        #print(candidate)

    #we are after two equal products that do not intersect in any number containing numbers <= N
    #the counts of the primes in the prime factorizations must be equal, or equivalently if one set of the prime factorizations counts is negative, the sum must be 0 for each prime
    #candidates are assigned +1, -1, or 0 depending on if they are in the left(top) set, right(bottom) set, or not used
    #the goal is to assign as few zeros as possible
    #a solution exists if the sum of qualified candidates sums to the zero vector
    #this must also be true for each individual prime
    #there are fewer decisions for large primes as there are for small ones
    #these decisions affect an entire row and can be propogated to the smaller primes, thus reducing their number of decisions

    solution = find_max_decision(candidates, len(prime_list)-1, {}) #a recursive algorithm
    if solution is not None:
        #print(solution)
        left_set = []
        right_set = []
        for i in range(0, N-1):
            num = i+2 #numbers 2 to N are indexed 0 to N-2
            if solution[i] == -1:
                left_set.append(num)
            elif solution[i] == 1:
                right_set.append(num)
            else:
                #these are the numbers not included in the final fraction, including the 'poisonous primes'
                pass
        print(str(problem_num) + ": " + str(left_set) + ", " + str(right_set))
    else:
        print(str(problem_num) + ": No Solution") #this doesnt actually happen becuase zeros yield the solutions to smaller N