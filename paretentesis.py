result = ""
tc = int(input())

for case in range(tc):
    numbers = list(map(int,input()))
    first = numbers[0]
    second = first
    output = '('*first
    for second in numbers[1:]:
        output+= str(first)
        if first == second:
            first = second
            continue
        if second<first:
            output+=')'*(first-second)
        else:
            output+='('*(second-first)
        first = second
    output+= str(second)+')'*second
    result+= 'Case #{0}: {1}\n'.format(case+1,output)
print(result)
