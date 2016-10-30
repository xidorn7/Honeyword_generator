#The algrothm goes as follow:
##Part of training model:
1. Choose the size of training sample.
2. Compute the distribution of passwords' length in training sample.
3. Compute the frequency of every character.
4. For every character 'chr', compute the distribution for characters following 'chr'

##Part of generate honeyword:
Given a password:
1. Length:
  1.1 With probability of 30%, the honeyword share the same length as real password.
  1.2 Else, pick a length from 
