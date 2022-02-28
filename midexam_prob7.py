# Write a function called score that meets the specifications below.

def score(word, f):
    """
       word, a string of length > 1 of alphabetical 
             characters (upper and lowercase)
       f, a function that takes in two int arguments and returns an int

       Returns the score of word as defined by the method:

    1) Score for each letter is its location in the alphabet (a=1 ... z=26) 
       times its distance from start of word.  
       Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.
    2) The score for a word is the result of applying f to the
       scores of the word's two highest scoring letters. 
       The first parameter to f is the highest letter score, 
       and the second parameter is the second highest letter score.
       Ex. If f returns the sum of its arguments, then the 
           score for 'adD' is 12 
    """
    # YOUR CODE HERE
    scores = []
    scores_high = []

    for i in range(len(word)):
        letter = word[i].lower()
        scor_loc = ord(letter) - 96
        letr_scor = i * scor_loc
        scores.append(letr_scor)

    scores.sort(reverse=True)
    scores_high = scores[0:2]
    return f(scores_high)

# notice!!! This works out in my local IDE but not on the grader. The grader instead accepts:
    # scores.sort(reverse=True)
    # return f(scores[0], scores[1])
# which would lead to TypeError: 'int' object is not iterable in IDE. Weird.


x = score('adD', sum)
print(x)
