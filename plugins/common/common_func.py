def get_sftp():
    print('sftp 작업을 시작합니다')
    

def regist(name, sex, *args):
    print(f'이름: {name}')
    print(f'성별: {sex}')
    print(f'기타옵션들: {args}')


def regist2(name, sex, *args, **kwargs):
    print(f'이름: {name}')
    print(f'성별: {sex}')
    print(f'기타옵션들: {args}')
    email = kwargs['email'] or 'empty'
    phone = kwargs['phone'] or 'empty'
    if email:
        print(email)
    if phone:
        print(phone)

    data_interval_start = kwargs.get('data_interval_start')
    data_interval_end = kwargs.get('data_interval_end')
    print(data_interval_start)
    print(data_interval_end)