
def main():

    tc = int(input())

    for case in range(tc):

        n_tasks = int(input())
        tasks = get_tasks(n_tasks)
        sol = [-1]*(n_tasks)
        sol[0] = 0
        branches = []
        i = 1
        while i < n_tasks:
            defined = False
            for j in range(i):
                if crossing(tasks[i],tasks[j]):
                    if not defined:
                        sol[i] = not sol[j]
                        defined = True
                    elif sol[i] == sol[j]:
                        # no se cumple la restriccion, descartaamos esta solucion
                        if branches:# se aplica la ultima rama

                            #print("branches: ",branches)
                            i = branches[-1]
                            sol[i:]= [-1]*(n_tasks-i)# se elimina el ultimo aignacion
                            sol[i] = 0
                            del branches[-1]

                        else:
                            i = n_tasks
                            sol[0] =  -1
                            break

            if not defined: # no hay restriccion, se puede asignar a cualquiera de los dos a esa tarea
            # se crea una nueva rama
                branches.append(i)
                sol[i] = 1
            i+=1
        if sol[0] == -1:
            sol = 'IMPOSSIBLE'
        else:
            #print(sol)
            sol = "".join([ 'J' if e else 'C' for e in sol ])
        print('Case #{0}: {1}'.format(case+1,sol))
        #    matrix_cx.append(crossing_i)
def get_tasks(N):
    tasks = []
    for _ in range(N):
        task = tuple(map(int,input().split()))
        tasks.append(task)
    return tasks
def crossing(task1,task2):
    '''
    define si una tarea se cruza con otra
    task = (minuto-inicio,minuto-fin)
    '''
    #print("compare crossing",task1," <> ",task2,end="")
    if task1[0] > task2[0]:#las ordeno
        task2,task1=task1,task2
    if task1[1]<= task2[0]: # el final de la primera es antes que el inicio de la segunda
        #print(" = false")
        return False
     # el final de la primera es despues que el inicio de la segunda
     #se cruzan
    #print(" = true")
    return True

if __name__ == '__main__':
    main()


'''
    A B C D E
  A
  B 0
  C 0 1
  D 0 0 0
  E 0 1 0 1


 SOL:
    1 0 1 0 1
    1 0 1 0 0
    1 1 0 0 1
    1 1 0 0 0
'''
