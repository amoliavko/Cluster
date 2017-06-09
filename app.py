#my_map = {'server8': {'print': 8, 'service2': 24, 'web': 18, 'service8': 8}, 'server3': {'print': 8, 'service2': 24, 'web': 18, 'service3': 3}, 'server4': {'service4': 4, 'print': 8, 'service2': 24, 'web': 18}, 'server5': {'print': 8, 'service5': 5, 'web': 18, 'service2': 24}, 'server6': {'print': 8, 'service2': 24, 'web': 18, 'service6': 6}, 'server7': {'print': 8, 'service2': 24, 'web': 18, 'service7': 7}, 'server1': {'print': 7, 'service2': 24, 'web': 18, 'service1': 1}, 'server0': {'service0': 0, 'print': 8, 'service2': 24, 'web': 18}, 'server10': {'service10': 10, 'print': 8, 'service2': 24, 'web': 18}, 'server9': {'print': 8, 'service2': 24, 'web': 18, 'service9': 9}, 'server2': {'print': 8, 'service2': 26, 'web': 18}}

file = open('config', 'r')
my_map = eval(file.read())
file.close()

new_service = input('Enter service name:\n')
service_quantity = input('Enter number of instances:\n')

# new_service = 'print'
# service_quantity = 201


def less_load_server(config_dict):
    service_sum = {}
    for i in config_dict:
        service_sum[i] = sum(config_dict[i].values())

    less_server = min(service_sum, key=service_sum.get)
    return less_server


def service_distribution(config_dict, new_service, service_quantity):
    for i in range(int(service_quantity)):
        server = less_load_server(config_dict)

        if new_service in config_dict[server]:
            config_dict[server][new_service] += 1
        else:
            config_dict[server][new_service] = 1


service_distribution(my_map, new_service, service_quantity)

file = open('config', 'w')
file.write(str(my_map))
file.close()

print(my_map)

