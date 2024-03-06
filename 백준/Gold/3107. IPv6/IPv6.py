def IPv6(ipv6_address):
    ipv6_address = ipv6_address.split(":")
    
    continue_check = False
    
    full_address = []
    
    for address in ipv6_address:
        if address == "" and not continue_check:
            full_address += ['0000' for _ in range(8 - len(ipv6_address) + 1)]
            continue_check = True
        else:
            full_address.append(address.zfill(4))
            
    return ":".join(full_address)

if __name__ == "__main__":
    ipv6_address = input()
    print(IPv6(ipv6_address=ipv6_address))