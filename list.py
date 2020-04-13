import builtins

def tupleone():
    input_list = map(int, integer_list)
    input_list = [int(x) for x in input_list]
    m = tuple(input_list)
    t = hash(m)
    return t


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tupleone()
