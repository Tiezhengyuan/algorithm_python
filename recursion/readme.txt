
# incrusive
## Advantages
1. Recursive functions make the code look clean and elegant.
2. A complex task can be broken down into simpler sub-problems using recursion.
3. Sequence generation is easier with recursion than using some nested iteration.
## weakness
1. Sometimes the logic behind recursion is hard to follow through.
2. Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
3. Complex recursive functions are hard to debug.
### features
1: recursion Direction:  start from most complicated input to simplest input
2. easy to get result with the simplest input 
3. easy to go into the next input given a current input. 
4. Not difficult to get relationships between the results of a current input and its next input.

Flow control: suppose there are n inputs. always get the next input and output based on current input and output
func(n)->func(n-1)->...->func(1)


recursive pattern

def func(...):
    #base case: result with simplest input
    #Check to see whether the current value(s) being processed match the base case.
    if ...:
        return ...
    #recursion
    #Redefine the answer in terms of a smaller or simpler sub-problem or sub-problems.
    else:
        #Run the algorithm on the sub-problem.
        retrun func(...)