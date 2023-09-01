# I don't think I need to explain. You're not a stupid dude.
print("-------------------------------------------------------")
print("this app is made by @MEGH2008")
print("-------------------------------------------------------")

def subnetting():
    def ip_to_bin(ip):
        segments = ip.split(".")
        bin_ip = ""
        for segment in segments:
            bin_ip += format(int(segment), "08b")
        return bin_ip

    def bin_to_ip(bin):
        segments = [bin[i:i+8] for i in range(0, len(bin), 8)]
        ip = ""
        for segment in segments:
            ip += str(int(segment, 2)) + "."
        return ip[:-1]

    def bits_for_subnets(n):
        bits = 0
        while 2**bits < n:
            bits += 1
        return bits

    def subnet_mask(prefix, subnet_bits):
        mask = "1" * prefix + "1" * subnet_bits + "0" * (32 - prefix - subnet_bits)
        return bin_to_ip(mask)

    def network_id(ip, mask):
        bin_ip = ip_to_bin(ip)
        bin_mask = ip_to_bin(mask)
        bin_net_id = ""
        for i in range(32):
            bin_net_id += str(int(bin_ip[i]) and int(bin_mask[i]))
        return bin_to_ip(bin_net_id)

    def broadcast_id(net_id, mask):
        bin_net_id = ip_to_bin(net_id)
        bin_mask = ip_to_bin(mask)
        bin_bcast_id = ""
        for i in range(32):
            bin_bcast_id += str(int(bin_net_id[i]) or (1 - int(bin_mask[i])))
        return bin_to_ip(bin_bcast_id)

    def first_ip(net_id):
        bin_net_id = ip_to_bin(net_id)
        return bin_to_ip(format(int(bin_net_id, 2) + 1, "032b"))

    def last_ip(bcast_id):
        bin_bcast_id = ip_to_bin(bcast_id)
        return bin_to_ip(format(int(bin_bcast_id, 2) - 1, "032b"))

    ip = input("Enter an IP address: ")
    prefix = int(input("Enter a prefix: "))
    subnets = int(input("Enter the desired number of subnets: "))
    print("-------------------------------------------------------")

    subnet_bits = bits_for_subnets(subnets)

    if prefix + subnet_bits > 32:
        print("Invalid input. The prefix and the subnet bits exceed 32 bits.")
    else:
        mask = subnet_mask(prefix, subnet_bits)

        print("The subnet mask is:", mask)

        for i in range(subnets):
            net_id = bin_to_ip(format(int(ip_to_bin(ip), 2) + i * 2**(32 - prefix - subnet_bits), "032b"))

            bcast_id = broadcast_id(net_id, mask)

            first = first_ip(net_id)
            last = last_ip(bcast_id)

            print("Subnet", i + 1, ":")
            print("Network ID:", net_id)
            print("Broadcast ID:", bcast_id)
            print("First usable IP:", first)
            print("Last usable IP:", last)

            print("-------------------------------------------------------")
        
subnetting()

again_todo = str(input("Do you want to do that again ? (yes/no) : "))
        
if again_todo == "yes" :
    print("-------------------------------------------------------")
    subnetting()
    

  
#easy
