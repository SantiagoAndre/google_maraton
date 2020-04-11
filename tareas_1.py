
def main():

    result = ""
    tc = int(input())

    for case in range(tc):

        n_tasks = int(input())
        tasks = [tuple(map(int,input().split()))]
        sol = [[0]]
        for i in range(n_tasks-1):
            i+=1
            task = tuple(map(int,input().split()))
            tasks.append(task)
            #crossing_i = []
            defined = 0
            for j in range(i):
                if crossing(task,tasks[j]):
                    defined = 1 # valor tentativo
                #    crossing_i.append(1)
                    add_to_sols(sol,i+1,j)# no hay solucion posible
                #else:
                #    crossing_i.append(0)
            if not defined: # no hay restriccion, se puede asignar a cualquiera de los dos a esa tarea
            # se duplican las soluciones
                add_to_sols(sol)
        if not sol:
            sol = 'IMPOSSIBLE'
        else:
            sol = "".join([ 'J' if e==0 else 'C' for e in sol[0] ])
        result+= 'Case #{0}: {1}\n'.format(case+1,sol)
    print(result)
        #    matrix_cx.append(crossing_i)

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
def add_to_sols(sols,number_tasks=-1,task_crossing=-1)  :
    '''
        administra las soluciones
        number_tasks: numero de tareas asignadas
        task_crossing: tarea que se cruza con la nueva tarea a asignar
    '''
    if not sols:
        return
#    print(sols)
    if number_tasks == len(sols[0]) and task_crossing != -1: # ya se h asignado la tarea actual
        #print("corssing verify")
        i = 0
        while i < len(sols):
            sol = sols[i]
            if sol[task_crossing] == sol[-1]:
                del sols[i]
            else:
                i+=1
    elif task_crossing != -1:
        #print("corssing append")
        for sol in sols:
            sol.append(not sol[task_crossing])
    else:
        #print("duplicate solutions")
        size = len(sols)
        for i in range(size):
            sol = sols[i]
            new_sol = list(sol)
            sol.append(0)
            new_sol.append(1)
            sols.append(new_sol)

if __name__ == '__main__':
    main()
