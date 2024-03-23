if __name__ == "__main__":
    try:
        f = open('dramsim3.txt', 'r')
    except FileNotFoundError:
        print('ERROR! Cannot find the result file dramsim3.txt')
        exit(1)
    
    num_cycles = 1
    total_energy = 0
    for line in f:
        info = line.split()
        if info[0] == 'num_cycles':
            num_cycles = int(info[2])
        elif info[0] == 'total_energy':
            total_energy = float(info[2])
    
    energy_per_cycle = total_energy / num_cycles
    print(f'Energy per cycle: {energy_per_cycle} pJ')
