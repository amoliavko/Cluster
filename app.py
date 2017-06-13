'''
Скрипт обновления конфигурации кластера.
Конфигурация кластера представлена в виде словаря 'example_data'
Ввод осуществляется в интерактивном режиме.
Результат отображается в консоли
'''


def main():

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

    if service_quantity <= 0:
        print('Be careful, {} equals or less then 0'.format(new_service))

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