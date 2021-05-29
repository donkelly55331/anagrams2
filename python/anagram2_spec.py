# Test anagrams_for

import unittest
from anagram2 import anagrams_for 

tests = [{'word': 'saltier', 'list_in': ['cognac', 'saltier', 'realist', 'retails'], 'expect': ['saltier', 'realist', 'retails']}, {'word': 'threads', 'list_in': ["threads", "trashed", "hardest", "hatreds"], 'expect': ["threads", "trashed", "hardest", "hatreds"]}, {'word': 'apple', 'list_in': [], 'expect': []}]

print("test running")

i = int(input("Which case:  "))

class MyTestCases(unittest.TestCase):
    def test_af(self):
        result = anagrams_for(tests[i]['word'], tests[i]['list_in'])
        self.assertEqual(result, tests[i]['expect'], "They're different")
        print(result)
        print(tests[i]['word'])
        print(tests[i]['list_in'])       
        print(tests[i]['expect'])
    
if __name__ == '__main__':
    unittest.main()



