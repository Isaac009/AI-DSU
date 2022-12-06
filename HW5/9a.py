from pgmpy.readwrite import BIFReader
import networkx as nx
import pylab as plt


reader = BIFReader('ab.bif')
print(reader.get_values())

nx_graph = nx.DiGraph(reader.get_edges())
nx.draw(nx_graph, with_labels=True)
plt.show()