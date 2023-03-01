import random
import string


def gen_random_string(pre_fix='test_',str_len=10):
    return pre_fix+''.join(
        random.choice(string.digits+string.ascii_letters)#0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
        for _ in range(str_len-len(pre_fix))
    )

def gen_random_num(pre_fix='181',str_len=11):
    return pre_fix+''.join(
        random.choice(string.digits)
        for _ in range(str_len-len(pre_fix))
    )

def unicode(n):
    s=''
    for i in range(n):
        val = random.randint(0x4E00, 0x9FBF)
        val=chr(val)
        s=s+val

    return s



def create_digits(n):
    seed='!@#$%^&*()+=-'
    sa=[]
    for i in range(n):
        sa.append(random.choice(seed))
    salt=''.join(sa)
    return salt

def create_letters(n):
    name=''
    for i in range(n):
        s=random.choice(string.ascii_letters)
        name=name+s
    return name


if __name__ == '__main__':
    a=unicode(10)
    print(a)
