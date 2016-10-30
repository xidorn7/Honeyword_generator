#The algorithm goes as follow:

##Part of training model:
1. Choose the size of training sample.
2. Compute the distribution of passwords' length in training sample(F_length).
3. Compute the distribution of all characters(F_char).
4. For every character 'chr', compute the distribution for characters following 'chr'(F_length).

##Part of generate honeyword:
1. Length.
 1.1 With probability of 30%, the honeyword share the same length as real password.
 1.2 Else, pick a length from length distribution(according to F_length).
2. Pick the init character of the honeyword:
 2.1 With probability of 50%, the init character is ramdonly pick from real password.
 2.2 Else, pick a random character from distribution of character(F_char).
3. Pick the following character:
  3.1 With the probability of 10%, the following is ramdonly pick from real password.
  3.2 Else, pick a random character from the distribution of characters following initial character's(F_char[init]).
  let init = the last character picked and do (3) again until honeyword's length is equal to length decided by (1)
