import algorithms
from game import create_board
import math
import matplotlib.pyplot as plt
def benchmark(board, algorithm, **kwargs):
    #name, selected move, evaluation score, number of explored nodes, and execution time
    dico=dict()
    dico["name"]=algorithm.__name__
    if len(kwargs)==1:
        depth=kwargs.get("depth")
        res=algorithm(board,depth)
    elif len(kwargs)==3:
        num_simulation=kwargs.get("num_simulations")
        exploration=kwargs.get("exploration")
        seed=kwargs.get("seed")
        res=algorithm(board,num_simulation,exploration,seed)
    else:
        res=algorithm(board)
    dico["move"]=res.get("move")
    dico["score"]=res.get("score")
    dico["explored nodes"]=res.get("nodes_explored")
    dico["time"]=res.get("time")


    return dico
minmax={}
alphabeta={}
mcts={}
table=[["Algorithm","Configuration","Move","Nodes","Time (s)"]]
for i in range (1,7):
    minmax[i]=(benchmark(create_board(),algorithms.minimax,depth=i))
    alphabeta[i]=(benchmark(create_board(),algorithms.alphabeta,depth=i))
    assert(minmax[i]["explored nodes"]>=alphabeta[i]["explored nodes"])
for i in [100,500,1000,2000]:
    mcts[i]=benchmark(create_board(),algorithms.mcts,num_simulations=i, exploration=math.sqrt(2), seed=18)
    

for i in minmax:
    conf="Depth "+str(i)
    table+=[[minmax[i]["name"],conf,minmax[i]["move"],minmax[i]["explored nodes"],minmax[i]["time"]]]
for i in alphabeta:
    conf="Depth "+str(i)
    table+=[[alphabeta[i]["name"],conf,alphabeta[i]["move"],alphabeta[i]["explored nodes"],alphabeta[i]["time"]]]
for i in mcts:
    conf=str(i)+" simulations"
    table+=[[mcts[i]["name"],conf,mcts[i]["move"],mcts[i]["explored nodes"],mcts[i]["time"]]]

print(table)


plt.plot([i for i in minmax], [minmax[i]["explored nodes"] for i in minmax], color="blue", label="minmax")
plt.plot([i for i in minmax], [alphabeta[i]["explored nodes"] for i in alphabeta], color="red", label="alphabeta")
plt.xlabel("depth")
plt.ylabel("explored nodes")
plt.title("Nodes exploration for minmax and alphabeta depending on their depth")
plt.legend()
plt.grid(True)

plt.show()

plt.clf()
plt.plot([i for i in mcts], [mcts[i]["time"] for i in mcts], color="blue", label="time")
plt.xlabel("number of simulations")
plt.ylabel("time(s)")
plt.title("Comparison of time taken depending on the number of simulations")
plt.legend()
plt.grid(True)

plt.show()