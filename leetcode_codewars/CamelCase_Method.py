def camel_case(s):
    h = []
    for i in s.split():
        h.append(i.capitalize())
    return ''.join(h)


'''
def camel_case(string):
    return string.title().replace(" ", "")
'''


if __name__ == '__main__':
    print(camel_case('Camel case method'))
