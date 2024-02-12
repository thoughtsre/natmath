import math
import random
import argparse
import datetime
from pathlib import Path

symbols = ["+", "-"]

minInt = 1
maxInt = 20
maxSubtractInt = 10 # can be None
N = 20


def generate_question(minInt, maxInt, maxSubtractInt):
    
    firstNum = random.randint(minInt, maxInt)
    
    op = random.choice(symbols)
    
    if op == "+":
        
        secondNum = random.randint(minInt, maxInt)
        
    elif op == "-":
        
        if firstNum == 0:
            
            secondNum = 0
        
        else:
            
            secondNum = random.randint(0, maxSubtractInt) if maxSubtractInt else random.randint(0, firstNum)
            
    return " ".join([str(firstNum), op, str(secondNum), "="])


parser = argparse.ArgumentParser("Nat's Math")
parser.add_argument("--n", type = int, default = N)
parser.add_argument("--min", type = int, default = minInt)
parser.add_argument("--max", type = int, default = maxInt)
parser.add_argument("--maxS", type = int, default = maxSubtractInt)

if __name__ == "__main__":
    
    args = parser.parse_args()
    
    path = Path("outputs") / (str(datetime.date.today()) + ".txt")
    
    with open(path, "a+") as f:
        
        for i in range(args.n):
        
            f.write(generate_question(args.min, args.max, args.maxS))
            f.write("\n")