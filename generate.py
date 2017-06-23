super_country = "us"

peer_country = "us"

user_name = ""

zone_name = ""

zone_password = ""

num_proxies = int(input("Enter the number of proxies to generate: "))

with open('proxies.txt', 'w') as file:

    for i in range(num_proxies):
        
        file.write('servercountry-%s.zproxy.luminati.io:22225:lum-customer-%s-zone-%s-country-%s-session-rand%d:%s\n' % (super_country, user_name, zone_name, peer_country, i+1, zone_password))

print("Proxies have been generated and stored in the proxies.txt file")
