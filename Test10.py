if __name__ == '__main__':
    #This is added by jeevan0023
    records=[]
    lst=[]
    names=[]
    names = ["hello"]
    names = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        #print(records)
    for i in range(len(records)):
        lst.append(records[i][1])
    lst.sort()
    for i in range(len(lst)):
        if lst[i]==lst[i+1]:
            continue
        else:
            second=lst[i+1]
            break
    for i in range(len(records)):
        if second == records[i][1] :
            names.append(records[i][0])
    names.sort()

    print(*names, sep="\n")
    print("hello mu ashu")
    print("Changes by neha")
    print("Chnage by pravakar")
