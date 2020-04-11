def main():
    result = ""
    T = int(input())
    B = int(input())
    MaxQueries = 150
    for case in range(T):
        queries = 0
        equial_pairs = [-1]*(B//2) # parejas equidistantes que son iguales
        other_pairs = [-1]*(B//2) #  parejas equidistantes diferentes
        firstEq,firstNeq = -1,-1 # indice de la primera pareja igual, y difente
        i=1
        while i <= (B//2):

            if queries >= MaxQueries:
                break
            # cada 5 pares de consultas cambia la matriz
            if i!= 1 and (queries%10) == 0: #cambia la matriz

                if firstNeq != -1:# solo parejas diferentes
                    queries += 1
                    print(firstNeq+1)
                    element = int(input())

                    if element != other_pairs[firstNeq]:
                        deny(other_pairs)
                    #else: no se hace nada

                if firstEq != -1:#  hay parejas iguales
                    queries += 1
                    print(firstEq+1)
                    element = int(input())

                    if element != equial_pairs[firstEq]:

                        deny(equial_pairs)
                    #else: no se hace nada
                if queries %2  !=0 :
                    #consulta  que no hce nada
                    print('1')
                    element = int(input())
                    queries+=1

            queries+=2
            pos1,pos2 = i,B-i+1 #posiciones equidistantes`
            print(pos1)
            element1  = int(input())
            print(pos2)
            element2 = int(input())
            if element1 == element2:#
                if firstEq == -1: firstEq = pos1-1
                equial_pairs[pos1-1] = element1
            else:
                if firstNeq == -1: firstNeq = pos1-1
                other_pairs[pos1-1] = element1


            # pedir dos valores
            # si se conoce toda la matriz
            # se imprime y se lee la respuesta del juez
            # se rompe el ciclo
            i+=1
        print("".join(join_vectors(equial_pairs,other_pairs,B)))
        result = input()# Y o N
        if result == "N":
            exit(0)







def join_vectors(equial_pairs,other_pairs,B):

    result = [-1]*B
    i = 0
    for elementEq,elementNeq in zip(equial_pairs,other_pairs):
        if elementEq != -1:
            first_element = str(elementEq)
            second_element = str(elementEq)
        else:
            first_element = str(elementNeq)
            second_element = '1' if elementNeq == 0 else '0'
        result[i] =  first_element
        result[B-1-i] =  second_element
        i+=1
    return result

def deny(vector):
    for i,element in enumerate(vector):
        if element == -1:
            continue
        vector[i] = 1 if element == 0 else 0
if __name__ == '__main__':
    main()
