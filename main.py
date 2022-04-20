# Package: package_calculator
# Author: Logan Talley
# Western Governors University
import csv

from .hash import HashBrowns, TaterTot
start_time = datetime.strptime("08:00 AM", "%I:%M %p")
eod = datetime.strptime("05:00 PM", "%I:%M %p")

def populate_hash_table():
    hash_table = HashBrowns()
    with open('supplemental/package.csv', newline='') as csvfile:
        pkg_reader = csv.reader(csvfile, delimiter=',')
        for index, row in enumerate(pkg_reader):
            if row[1] != 'address':
                pkg_id = int(row[0])
                address = row[1]
                city = row[2]
                zip_code = int(row[3])
                deadline = row[4]
                mass = float(row[5])
                special_notes = row[6]
                status = 'Not Delivered'
                hash_table[f"p_{index}"] = TaterTot(pkg_id, address, deadline, city, zip_code, mass, special_notes, status)
    return hash_table

def get_nearest_neighbors():
    with open('supplemental/distance.csv', newline='') as csvfile:
        distance_reader = csv.reader(csvfile, delimiter=',')
        for row in distance_reader:
            csv_addr = row[0] 
    
def priority_queue(hash_table):
    pkg_deltas = {}
    for pkg in h.dictionary:
        if pkg[1].deadline == 'EOD':
            delta = eod - start_time
        else:
            delta = pkg[1].deadline - start_time

        pkg_deltas[pkg[0]] = delta.seconds
    return {k: v for k, v in sorted(pkg_deltas.items(), key=lambda pkg: pkg[1])}

def route_mapper(hash_table, priority_queue):
    truck_0_route = []
    truck_1_route = []
    truck_2_route = []
    
    first_stop = next(iter(priority_queue.keys()))
    truck_0_route.append(first_stop)
    sub_queue = {k:v for k,v in priority_queue.items() if v == 9000}
    for k,v in priority_queue.items:
        if v == 9000:
            sub_queue[k] = v
    first_nn = nearest_neighbors(first_stop)
    possible_next_destinations = set(sub_queue.keys()).intersect(first_nn)
        
            

def main():
    hash_table = populate_hash_table()
    
if __name__ == '__main__':
    main()