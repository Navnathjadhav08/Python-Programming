import sklearn

def main():
    print("Ball Classification Case Study ")
    
    # manual Encoding -- 
    # Rought replace with 1 & Smooth with 0
    features=[[35,1],
              [47,1],
              [90,0],
              [48,0],
              [90,0],
              [35,1],
              [92,0],
              [35,1],
              [35,1],
              [35,1]]
    
     # Tennis replace with 1 & Cricket with 0
    Labels = ["1","1","2","1","2","1","2","1","1","1"]
    
if __name__ == "__main__":
    main()
    
# Dataset size : 15
# Training size : 10
# testing size :5