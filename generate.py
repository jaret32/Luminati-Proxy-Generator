user_name = ""

zone_name = ""

zone_password = ""

num_proxies = int(input("Enter the number of proxies to generate: "))

with open('proxies.txt', 'w') as file:

    for i in range(num_proxies):
        
        file.write('servercountry-us.zproxy.luminati.io:22225:lum-customer-%s-zone-%s-country-us-session-rand%d:%s\n' % (user_name, zone_name, i+1, zone_password))

print("Proxies have been generated and stored in the proxies.txt file")
