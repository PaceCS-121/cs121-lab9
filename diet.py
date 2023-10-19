import pandas as pd

def parsefile(filename):
    df = pd.read_csv(filename)
    return df

def main():
    # import nutrition data
    filename = 'nutrition.csv'
    df = parsefile(filename)
    # write your code here

    
    return

if __name__ == '__main__':
    main()