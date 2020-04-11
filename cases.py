
def main():
    result = ""
    tc = int(input())

    for case in range(tc):
        k= 0
        r = 0
        c = 0
        N = int(input())
        matrix = []
        for i in range(N):
            row = list(map(int,input().split()))
            k+= row[i]
            if len(unique(row)) != N :# fila con elementos repetidos
                r+=1
            matrix.append(row)

        for column in range(N):
            if len(unique_column(matrix,column)) != N :# columna con elementos repetidos
                c+=1
        result+= "Case #{0}: {1} {2} {3}\n".format(case+1,k,r,c)
    print(result)






def unique_column(matrix,column):
    unique_list = []
    for  row in matrix:
        x = row[column]
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

def unique(l):
    unique_list = []
    for x in l:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

if __name__ == '__main__':
    main()
