import unittest
import io
import sys
import array_manipulator as sut

class TestArrayManipulator(unittest.TestCase):

    def test_exchange(self):
        source_arr = [1,2,3,4,5]
        modified_arr = sut.exchange(source_arr, 'exchange 2')
        self.assertSequenceEqual(modified_arr, [4,5,1,2,3])

    def test_exchange_invalid_index(self):
        source_arr = [1,2,3,4,5]
        modified_arr = sut.exchange(source_arr, 'exchange 20')
        self.assertSequenceEqual(modified_arr, source_arr)

    # def test_exchange_0(self):
    #     source_arr = [1,2,3,4,5]
    #     modified_arr = sut.exchange(source_arr, 'exchange 1')
    #     self.assertSequenceEqual(modified_arr, source_arr)

    def test_max_odd(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        source_arr = [1,2,3,4,5]
        modified_arr = sut.get_max(source_arr, 'max odd')
        
        self.assertEqual(source_arr, modified_arr)
        self.assertEqual('4\n', capturedOutput.getvalue())

    def test_max_even(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        source_arr = [1,2,3,4,5]
        modified_arr = sut.get_max(source_arr, 'max even')
        
        self.assertEqual(source_arr, modified_arr)
        self.assertEqual('3\n', capturedOutput.getvalue())

    def test_max_no_matches(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        source_arr = [0, 2, 4]
        modified_arr = sut.get_max(source_arr, 'max odd')
        
        self.assertEqual(source_arr, modified_arr)
        self.assertEqual('No matches\n', capturedOutput.getvalue())

    def test_min_odd(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        source_arr = [1,2,3,4,5]
        modified_arr = sut.get_min(source_arr, 'min odd')
        
        self.assertEqual(source_arr, modified_arr)
        self.assertEqual('0\n', capturedOutput.getvalue())

    def test_min_even(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        source_arr = [1,2,3,4,5]
        modified_arr = sut.get_min(source_arr, 'min even')
        
        self.assertEqual(source_arr, modified_arr)
        self.assertEqual('1\n', capturedOutput.getvalue())

    def test_min_no_matches(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        source_arr = [1, 3, 5]
        modified_arr = sut.get_min(source_arr, 'min even')
        
        self.assertEqual(source_arr, modified_arr)
        self.assertEqual('No matches\n', capturedOutput.getvalue())

    def test_first_odd(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        source_arr = [1, 3, 5]
        modified_arr = sut.get_first(source_arr, 'first 3 odd')
        
        self.assertEqual(source_arr, modified_arr)
        self.assertEqual('[1, 3, 5]\n', capturedOutput.getvalue())
    
    def test_first_even(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        source_arr = [0, 2, 4]
        modified_arr = sut.get_first(source_arr, 'first 3 even')
        
        self.assertEqual(source_arr, modified_arr)
        self.assertEqual('[0, 2, 4]\n', capturedOutput.getvalue())
    
    def test_first_invalid_count(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        source_arr = [1, 3, 5]
        modified_arr = sut.get_first(source_arr, 'first 5 odd')
        
        self.assertEqual(source_arr, modified_arr)
        self.assertEqual('Invalid count\n', capturedOutput.getvalue())

    def test_last_odd(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        source_arr = [1, 3, 5]
        modified_arr = sut.get_last(source_arr, 'last 3 odd')
        
        self.assertEqual(source_arr, modified_arr)
        self.assertEqual('[1, 3, 5]\n', capturedOutput.getvalue())
    
    def test_last_even(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        source_arr = [0, 2, 4]
        modified_arr = sut.get_last(source_arr, 'last 3 even')
        
        self.assertEqual(source_arr, modified_arr)
        self.assertEqual('[0, 2, 4]\n', capturedOutput.getvalue())

    def test_last_even_from_longlist(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        source_arr = [0, 2, 4, 6, 8, 10]
        modified_arr = sut.get_last(source_arr, 'last 3 even')
        
        self.assertEqual(source_arr, modified_arr)
        self.assertEqual('[6, 8, 10]\n', capturedOutput.getvalue())
    
    def test_last_invalid_count(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        source_arr = [1, 3, 5]
        modified_arr = sut.get_last(source_arr, 'last 5 odd')
        
        self.assertEqual(source_arr, modified_arr)
        self.assertEqual('Invalid count\n', capturedOutput.getvalue())

# if __name__ == '__main__':
#     unittest.main()

suite = unittest.TestLoader().loadTestsFromTestCase(TestArrayManipulator)
unittest.TextTestRunner(verbosity=2).run(suite)