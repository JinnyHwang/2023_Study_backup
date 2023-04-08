text = '100%'

try :
    number = int(text)
except ValueError :
    print('{} 숫자 아님'.format(text))


def safe_pop_print(list, index):
    try :
        print(list.pop(index))
    except IndexError :
        print('{} 값을 가져올 수 없다.'.format(index))

def safe_pop_print2(list, index):
    if index<len(list):
        print(list.pop(index))
    else :
        print('{} 값을 가져올 수 없다.'.format(index))


safe_pop_print([1, 2, 3], 5)
safe_pop_print2([1, 2, 3], 5)


try :
    import my_module
except ImportError :
    print('없는 모듈')

