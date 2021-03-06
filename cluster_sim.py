import cluster
import cluster_physics as phys
import pylab

MAX_NUMBER_MOLECULES = 100
T = 1300
number_clusters_start = 1
dt = 1e-8/phys.jump_rate(T)
dt = dt * 1e6
time_steps = int(1e5)
 
class ClusterSimulation:
    def __init__(self,temperature, time_steps):
        self.cluster_dict = {}
        self.temperature = temperature
        self.time_steps = time_steps
        for nof_molecules in range(MAX_NUMBER_MOLECULES):
            if(nof_molecules == 1) : start = number_clusters_start
            else : start = 0
            new_cluster = cluster.Cluster(T, nof_molecules, start) 
            self.cluster_dict[nof_molecules] = new_cluster

    def change_in_clusters_at_number(self, number_molecules):
        current_cluster = self.cluster_dict[number_molecules]
        if(number_molecules > 0):
            prev_cluster = self.cluster_dict[number_molecules - 1]
        else:
            prev_cluster = current_cluster
        if(number_molecules < MAX_NUMBER_MOLECULES - 1):
            next_cluster = self.cluster_dict[number_molecules + 1]
        else:
            next_cluster = current_cluster
        return -current_cluster.forward_rate()-current_cluster.backward_rate()+prev_cluster.forward_rate()+next_cluster.backward_rate()

    def update_cluster_at_number(self, number_molecules):
        new_number_clusters = self.cluster_dict[number_molecules].get_number_of_clusters() + dt * self.change_in_clusters_at_number(number_molecules)
        self.cluster_dict[number_molecules].set_number_of_clusters(new_number_clusters)

    def update_all_clusters(self):
        for number_of_molecules in self.cluster_dict.keys():
            self.update_cluster_at_number(number_of_molecules)                
    
    def simulate(self):
        accumulated_time = 0.0
        for time in range(self.time_steps):
            self.update_all_clusters()
            accumulated_time += dt
        print 'accumulated_time', accumulated_time

    def pp(self):
        for key in self.cluster_dict.keys():
            print key, self.cluster_dict[key].get_number_of_clusters()

    def number_molecules_as_array(self):
        return self.cluster_dict.keys()

    def number_clusters_as_array(self):
        return [ self.cluster_dict[key].get_number_of_clusters() for key in self.cluster_dict.keys() ]

#time_step_array = [int(1e5), int(2e5), int(3e5), int(4e5), int(5e5)]
time_step_array = [int(1e2), int(1e3), int(1e4), int(1e5)]

x_array = []
y_array = []
for ts in time_step_array:
    sim = ClusterSimulation(T, ts)
    sim.simulate()
    x = sim.number_molecules_as_array()
    y = sim.number_clusters_as_array()
    x_array.append(x)
    y_array.append(y)
    
for x, y in zip(x_array, y_array):    
    pylab.semilogy(x,y)
pylab.show()



