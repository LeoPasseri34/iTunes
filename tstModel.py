from model.model import Model

mymodel = Model()
mymodel.buildGraph(60)
nodi, archi = mymodel.getGraphDetails()
print(f"Numero di nodi: {nodi}; Numero archi: {archi}")
