'''
Скрипт обновления конфигурации кластера.
Конфигурация кластера представлена в виде словаря 'example_data'
Ввод осуществляется в интерактивном режиме.
Результат отображается в консоли
'''

def main():
    my_dict = {'server8': {'print': 8, 'service2': 24, 'web': 18, 'service8': 8},
              'server3': {'print': 8, 'service2': 24, 'web': 18, 'service3': 3},
              'server4': {'service4': 4, 'print': 8, 'service2': 24, 'web': 18},
              'server5': {'print': 8, 'service5': 5, 'web': 18, 'service2': 24},
              'server6': {'print': 8, 'service2': 24, 'web': 18, 'service6': 6},
              'server7': {'print': 8, 'service2': 24, 'web': 18, 'service7': 7},
              'server1': {'print': 7, 'service2': 24, 'web': 18, 'service1': 1},
              'server0': {'service0': 0, 'print': 8, 'service2': 34, 'web': 18},
              'server10': {'service10': 10, 'print': 8, 'service2': 24, 'web': 18},
              'server9': {'print': 8, 'service2': 24, 'web': 18, 'service9': 9},
              'server2': {'print': 8, 'service2': 26, 'web': 18}}

    example_data = {
        'ginger': {
            'django': 2,
            'flask': 3,
        },
        'cucumber': {
            'flask': 1,
        },
    }

    new_service = input('Enter service name:\n')

    if not new_service:
        print('Service name is missing! Try again.')
        raise SystemExit

    service_quantity_input = input('Enter number of instances:\n')

    try:
        service_quantity = int(service_quantity_input)
    except ValueError:
        print('An integer is expected! Try again.')
        raise SystemExit

    if service_quantity == 0:
        print('Be careful, {} = 0'.format(new_service))

    service_distribution(example_data, new_service, service_quantity)
    print(example_data)


def less_load_server(config_dict):
    '''Определение менее нагруженного сервера'''
    service_sum = {}
    for i in config_dict:
        service_sum[i] = sum(config_dict[i].values())

    less_server = min(service_sum, key=service_sum.get)
    return less_server


def service_distribution(config_dict, new_service, service_quantity):
    '''Распределение сервисов по серверам'''
    for i in range(int(service_quantity)):
        server = less_load_server(config_dict)

        if new_service in config_dict[server]:
            config_dict[server][new_service] += 1
        else:
            config_dict[server][new_service] = 1


if __name__ == '__main__':
    main()