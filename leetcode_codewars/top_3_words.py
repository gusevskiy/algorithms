#  https://www.codewars.com/kata/51e056fe544cf36c410000fb/solutions/python

import re
import unittest


#  Мое не решенное

# def dict_words(text):
#     signs = {
#         ord(","): None, ord("."): None, ord(":"): None, ord("/"): None
#         }

#     new_text = text.lower().translate(signs).split()

#     res = {}

#     while new_text:
#         i = new_text[0]
#         max_word = new_text.count(i)
#         res[i] = max_word
#         while new_text.count(i) > 0:
#             new_text.remove(i)
#         if len(new_text) != 0:
#             i = new_text[0]

#     return res


# def top_3_words(res):
#     result = dict_words(res)
#     tree_res = []
#     if len(result) < 3:
#         return list(sorted(result.keys()))
#     while len(tree_res) < 3:
#         max_key = max(result, key=result.get)
#         tree_res.append(max_key)
#         result.pop(max_key)
#     return tree_res


def top_3_words(text):
    text.strip()
    if not text or not re.findall(r'([a-zA-Z]+)',text):
        return []
    else:
        l_words = re.split(r'[\s\,\.\?\:\;\/\-\_\!]+', text)
        l_words = list(filter(lambda x: x != '', l_words))
        l_ele = list(set(l_words))
        count = []
        for each in l_ele:
            count.append([each, l_words.count(each)])
        count.sort(key=lambda x:x[0])
        count.sort(key=lambda x:x[1], reverse=True)
        if len(count) < 4:
            return [i[0].lower() for i in count]
        else:
            return [i[0].lower() for i in count[:3]]


class TestWord(unittest.TestCase):
    """run: python3 -m unittest top_3_words"""
    def test_words(self):
        self.assertEqual(top_3_words("a a a  b  c c  d d d d  e e e e e"), ["e", "d", "a"])
        self.assertEqual(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"])
        self.assertEqual(top_3_words("  //wont won't won't "), ["won't", "wont"])
        self.assertEqual(top_3_words("  , e   .. "), ["e"])
    
    def test_without_words(self):
        self.assertEqual(top_3_words("  ...  "), [])
        self.assertEqual(top_3_words("  '  "), [])
        self.assertEqual(top_3_words("  '''  "), [])
        
    def test_big_text(self):
        self.assertEqual(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
            mind, there lived not long since one of those gentlemen that keep a lance
            in the lance-rack, an old buckler, a lean hack, and a greyhound for
            coursing. An olla of rather more beef than mutton, a salad on most)
            nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra)
            on Sundays, made away with three-quarters of his income."""), ["a", "of", "on"])


# if __name__ == '__main__':

