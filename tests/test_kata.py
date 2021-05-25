import unittest
from src.kata import in_array
from random import randint, shuffle

U = ["I", "should", "have", "known", "that", "you", "would", "have", "a", "perfect", "answer", "for", "me",
    "(since", "most", "Ruby", "questions", "I", "browse", "here", "have", "your", "input", "somewhere).",
    "I", "am", "glad", "you", "pointed", "out", "the", "versioning;", "I", "am", "using", "1.9.2.", "apidock",
    "mladens", "comment", "does", "not", "have", "sample;", "neither", "does", "ruby-doc.", "In", "your",
    "opinion,", "what", "is", "the", "best", "reference", "for", "Ruby,", "updated", "to", "1.9?"]
V = ["ou", "ve", "ect", "omm", "gla", "oint", "pini", "wh", "oes", "by", "ion", "or", "he", "ple", "ing",
    "ouv", "vec", "ect", "ommo", "glac", "ointer", "pinilo", "wh", "oesi", "byc", "tion", "tor", "he", "ple", "ing"]

def do_ex():
    n = randint(8, 20)
    shuffle(V)
    shuffle(U)
    return (V[0:n], U[0:n+15])


class TestInArray(unittest.TestCase):
    def test_basics(self):
        a1 = ["live", "arp", "strong"] 
        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
        expectedResult = ['arp', 'live', 'strong']
        self.assertEqual(in_array(a1,a2), expectedResult)
        a1 = ["arp", "mice", "bull"] 
        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
        expectedResult = ['arp']
        self.assertEqual(in_array(a1,a2), expectedResult)
        a1 = ["cod", "code", "wars", "ewar"] 
        a2 = ["lively", "alive", "harp", "sharp", "armstrong", "codewars"]
        expectedResult = ["cod", "code", "ewar", "wars"]
        self.assertEqual(in_array(a1, a2), expectedResult)          
        a1 = ["cod", "code", "wars", "ewar", "ar"] 
        a2 = ["lively", "alive", "harp", "sharp", "armstrong", "codewars"]
        expectedResult = ["ar", "cod", "code", "ewar", "wars"]
        self.assertEqual(in_array(a1, a2), expectedResult)       
        a1 = ["cod", "code", "wars", "ewar", "ar"] 
        a2 = []
        expectedResult = []
        self.assertEqual(in_array(a1, a2), expectedResult)          
        a1 = ["1295", "code", "1346", "1028", "ar"] 
        a2 = ["12951295", "ode", "46", "10281066", "par"]
        expectedResult = ["1028", "1295", "ar"]
        self.assertEqual(in_array(a1, a2), expectedResult)          
        a1 = ["&()", "code", "1346", "1028", "ar"] 
        a2 = ["12&()95", "coderange", "46", "1066", "par"]
        expectedResult = ["&()", "ar", "code"]
        self.assertEqual(in_array(a1, a2), expectedResult)         
        a1 = ["ohio", "code", "1346", "1028", "art"] 
        a2 = ["Carolina", "Ohio", "4600", "NY", "California"]
        expectedResult = []
        self.assertEqual(in_array(a1, a2), expectedResult)     
        a1 = ["duplicates", "duplicates"] 
        a2 = ["duplicates", "duplicates"] 
        expectedResult = ["duplicates"]
        self.assertEqual(in_array(a1, a2), expectedResult)
    
    def test_random_tests(self):
        i = 0
        while (i < 250):
            a, b = do_ex()
            expectedResult = in_array(a, b)
            self.assertEqual(in_array(a, b), expectedResult)
            i += 1

if __name__ == '__main__':
    unittest.main()
