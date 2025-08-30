def log(filename = ''):
    """логирование начала и конца выполнения функции, а также ее результаты или возникшие ошибки"""
    def wrapper(func):
        def inner(*args, **kwargs):
            list_log = []
            func_name = func.__name__
            list_log.append( f'Starting {func_name}\n')
            try:
                result = func(*args, **kwargs)
                list_log.append(f'{func_name} ok\n')
                list_log.append(f'Finished {func_name}\n')
                if filename != '':
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.writelines(list_log)
                else:
                    print(''.join(list_log))
                return result
            except Exception as e:
                list_log.append(f'{func_name} error: {e}. Inputs: {args}\n')
                list_log.append(f'Finished {func_name}\n')
                if filename != '':
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.writelines(list_log)
                else:
                    print(''.join(list_log))

        return inner

    return wrapper




# @log(filename="mylog.txt")