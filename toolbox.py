def generate_device_name(device, description): 
    """ This function generates a name 
    of a VNF running in RTP data center  
    """  
    datacenter = 'RTP' 
    devices = {'firewall': 'Cisco_ASAv', 'router': 'Cisco_CSR-1000v'} 

    device_type = devices[device] 
    name = f"{device_type}--{description}__{datacenter}"  
     
    return name 


def is_ipv4_address(ip): 
    """ Return True if ipv4 address, 
    False if not 
    """  
    octet_range = range(256) 
    octets = ip.split('.') 

    if len(octets) != 4: 
        return False 
    elif any(not octet.isdigit() for octet in octets): 
        return False 
    elif any(int(octet) not in octet_range for octet in octets): 
        return False 

    return True

if __name__ == '__main__':
    print(is_ipv4_address('10.10.10.1'))
