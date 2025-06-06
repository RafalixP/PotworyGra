with open('port_in.txt', 'r') as source:
    with open('port_out.txt', 'w') as target:    
        for line in source:
            target.write(line)

