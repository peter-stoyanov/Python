import unittest
# import io
# import sys
import caesar_login as sut

class TestCaesarLogins(unittest.TestCase):

    def test_extract_credentials(self):
        tokens = sut.extract_credentials('/tickticktocktockticktock/')
        self.assertSequenceEqual(('tick', 'tock'), tokens)

    def test_extract_credentials2(self):
        tokens = sut.extract_credentials('/wrong-wrong->cc&passpasswrong+pass/')
        self.assertIsNone(tokens)

    # def test_extract_credentials3(self):
    #     tokens = sut.extract_credentials(r'\^\muynu_muynu^789%;789muynu789\\')
    #     self.assertSequenceEqual(('muynu', '789'), tokens)

    def test_extract_credentials4(self):
        tokens = sut.extract_credentials(r'\rgujq)rgujqrgpmcrgpmc+rgujqrgpmc\\')
        self.assertSequenceEqual(('rgujq', 'rgpmc'), tokens)

    def test_extract_credentials5(self):
        tokens = sut.extract_credentials('/gg_gg_xxxxggxx\\')
        self.assertIsNone(tokens)
        

    def test_trash(self):
        trash_chars = sut.get_trash_chars('\\/FkcoqpfFkcoqpfjwpvgt4jwpvgt4Fkcoqpfjwpvgt4\\\\')
        self.assertSequenceEqual(['/', '\\'], trash_chars)

    def test_decrypt(self):
        decrypted = sut.decrypt('bcd', 1)
        self.assertEqual('abc', decrypted)
    
    def test_decrypt2(self):
        decrypted = sut.decrypt('muynu', 6)
        self.assertEqual('gosho', decrypted)

    


suite = unittest.TestLoader().loadTestsFromTestCase(TestCaesarLogins)
unittest.TextTestRunner(verbosity=2).run(suite)