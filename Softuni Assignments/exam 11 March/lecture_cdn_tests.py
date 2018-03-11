import unittest
# import io
# import sys
import lecture_cdn as sut

class TestLectureCDN(unittest.TestCase):

    def test_get_tokens(self):
        tokens = sut.extract_tokens('trainer:housey;course:csharp-oop-basics;lecture:polymorphism;duration:3h05m')
        self.assertSequenceEqual(
            sorted(['polymorphism', 'housey', 'csharp-oop-basics', '3h05m']), 
            sorted(list(tokens))
            )


    def test_get_tokens2(self):
        tokens = sut.extract_tokens('lecture:matrices-extra;trainer:bojo;course:csharp-oop-basics;duration:4h35m')
        self.assertSequenceEqual(
            sorted(['matrices-extra', 'bojo', 'csharp-oop-basics', '4h35m']), 
            sorted(list(tokens))
            )


suite = unittest.TestLoader().loadTestsFromTestCase(TestLectureCDN)
unittest.TextTestRunner(verbosity=2).run(suite)