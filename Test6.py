if __name__ == '__main__':
    lst=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append([name,score])
        lst.sort()
        print(lst)
    #for i in range (len(lst)):
