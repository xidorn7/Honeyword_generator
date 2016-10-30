import itertools
import sys
import random
import numpy


def rockyou():
  text_file = open("rockyou.txt", "r")
  fullSet = []
  for line in text_file.readlines():
    line = line.split(' ')
    line = line[-1].strip('\n')
    fullSet.append(line)
  return fullSet
  #print fullSet

def makeHw(cnt, inputfile, outputfile):
  with open(inputfile) as infile:
    for line in infile:
        isLetter = any(single.isalpha() for single in line)
        line = line.replace("\n", "")
        
        if(isLetter == True):
          uplowData = map(''.join, itertools.product(*((single.upper(), single.lower()) for single in line)))
          rockData = rockyou()
          pick = random.sample(rockData, 3)
          isLetter1 = any(single.isalpha() for single in pick[0])
          isLetter2 = any(single.isalpha() for single in pick[1])
          isLetter3 = any(single.isalpha() for single in pick[2])
          if isLetter1 == True:
           pick1 = numpy.repeat((map(''.join, itertools.product(*((single.upper(), single.lower()) for single in pick[0])))), 999)
           pick1 = random.sample(pick1, cnt)
          if isLetter2 == True:
           pick2 = numpy.repeat((map(''.join, itertools.product(*((single.upper(), single.lower()) for single in pick[1])))), 999)
           pick2 = random.sample(pick2, cnt)
          if isLetter3 == True:
           pick3 = numpy.repeat((map(''.join, itertools.product(*((single.upper(), single.lower()) for single in pick[2])))), 999)
           pick3 = random.sample(pick3, cnt)
          repeatData = numpy.repeat(uplowData, 999)
          honeyData = random.sample(repeatData, cnt)
          honeyPass = []
          for i in range(0, cnt):
            honeyPass.append(str(random.randint(0, 99)) + honeyData[i] + str(random.randint(0, 99)))
            honeyPass.append(pick1[i] + str(random.randint(0, 99)))
            honeyPass.append(str(random.randint(0, 99)) + pick2[i] + str(random.randint(0, 99)))
            honeyPass.append(pick3[i] + str(random.randint(0, 99)))
  
          result = random.sample(honeyPass, cnt)
          print result
          outfile = open(outputfile, "a")
          for line in result:
            outfile.write(line + "|")
          outfile.write("\n")
        
        else:
          pick = random.sample(rockData, 3)
          isLetter1 = any(single.isalpha() for single in pick[0])
          isLetter2 = any(single.isalpha() for single in pick[1])
          isLetter3 = any(single.isalpha() for single in pick[2])
          if isLetter1 == True:
           pick1 = numpy.repeat((map(''.join, itertools.product(*((single.upper(), single.lower()) for single in pick[0])))), 999)
           pick1 = random.sample(pick1, cnt)
          if isLetter2 == True:
           pick2 = numpy.repeat((map(''.join, itertools.product(*((single.upper(), single.lower()) for single in pick[1])))), 999)
           pick2 = random.sample(pick2, cnt)
          if isLetter3 == True:
           pick3 = numpy.repeat((map(''.join, itertools.product(*((single.upper(), single.lower()) for single in pick[2])))), 999)
           pick3 = random.sample(pick3, cnt)
          repeatData = numpy.repeat(uplowData, 999)
          honeyData = random.sample(repeatData, cnt)
          honeyPass = []
          for i in range(0, cnt):
            honeyPass.append(str(random.randint(0, 99)) + honeyData[i] + str(random.randint(0, 99)))
            honeyPass.append(pick1[i] + str(random.randint(0, 99)))
            honeyPass.append(str(random.randint(0, 99)) + pick2[i] + str(random.randint(0, 99)))
            honeyPass.append(pick3[i] + str(random.randint(0, 99)))
  
          result = random.sample(honeyPass, cnt)
          print result
          outfile = open(outputfile, "a")
          for line in result:
            outfile.write(line + "|")
          outfile.write("\n")

        outfile.close()
        honeyPass[:] = []

if __name__ == '__main__':
  N = int(sys.argv[1])
  inputfile = sys.argv[2]
  outputfile = sys.argv[3]
  makeHw(N, inputfile, outputfile)
