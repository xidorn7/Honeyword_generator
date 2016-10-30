import itertools
import sys
import random
import numpy


def makeHw(cnt, inputfile, outputfile):

  honeyPass = []

  with open(inputfile) as infile:
    for line in infile:
        isLetter = any(single.isalpha() for single in line)
        line = line.replace("\n", "")
        
        if(isLetter == True):
          uplowData = map(''.join, itertools.product( * ((single.upper(), single.lower()) for single in line)))
          repeatData = numpy.repeat(uplowData, 999)
          honeyData = random.sample(repeatData, cnt)
          for i in range(0, cnt):
            honeyPass.append(str(random.randint(0, 99)) + honeyData[i] + str(random.randint(0, 99)))
           
          result = random.sample(honeyPass, cnt) 
          outfile = open(outputfile, "a")
          for line in result:
            outfile.write(line + "|")
          outfile.write("\n")
        
        else:
          for i in range(0, cnt):
            honeyPass.append(str(random.randint(0, 99)) + str(line) + str(random.randint(0, 99)))
        
          result = random.sample(honeywords, cnt)
          outfile = open(outputfile, "a")
          for line in honey:
            outfile.write(line + "|")
          outfile.write("\n")
          
        outfile.close()
        honeyPass[:] = []

if __name__ == '__main__':
  N = int(sys.argv[1])
  inputfile = sys.argv[2]
  outputfile = sys.argv[3]
  makeHw(N, inputfile, outputfile)
