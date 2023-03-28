def generate_hashtag(s):
    if s == '' or len(s) > 140:
        return False
    s = s.title()
    s = ''.join(s.split())
    return '#' + s

if __name__ == '__main__':
    print(generate_hashtag('          codewars       '))