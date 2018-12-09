'''A3. Tester for the function common_words in tweets.
'''

import unittest
import tweets

class TestCommonWords(unittest.TestCase):
    '''Tester for the function common_words in tweets.
    '''

    def test_empty(self):
        '''Empty dictionary.'''

        arg1 = {}
        arg2 = 1
        exp_arg1 = {}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be\n {}, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)


    def test_one_word_limit_one(self):
        '''Dictionary with one word.'''

        arg1 = {'hello': 2}
        arg2 = 1
        exp_arg1 = {'hello': 2}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)
        
    def test_same(self):
        '''Length of dictionary is the same as the integer.'''

        arg1 = {'hello': 5, 'hi': 4, 'wassup': 3, 'heynmman': 2, 'ok': 1}
        arg2 = 5
        exp_arg1 = {'hello': 5, 'hi': 4, 'wassup': 3, 'heynmman': 2, 'ok': 1}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be\n {}, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)
        
    def test_exceed(self):
        '''Word count exceeds the length of the dictionary needed.'''

        arg1 = {'Hey': 4, 'Hi': 3, 'Wow': 2, 'Wdym': 2, 'Why': 1}
        arg2 = 3
        exp_arg1 = {'Hey': 4, 'Hi': 3}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be\n {}, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)
        
    def test_same_count(self):
        '''The dictionary is full of the same word count.'''

        arg1 = {'Hi': 2, 'Hey': 2, 'What': 2, 'Is': 2, 'Up': 2}
        arg2 = 3
        exp_arg1 = {}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be\n {}, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)
        
    def test_int_more_than_dict(self):
        '''The integer is larger than the length of the dictionary.'''

        arg1 = {'Yo': 3, 'Yoo': 3, 'Yooo': 2, 'Masheil': 2, 'Sucks': 1}
        arg2 = 7
        exp_arg1 = {'Yo': 3, 'Yoo': 3, 'Yooo': 2, 'Masheil': 2, 'Sucks': 1}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be\n {}, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)    
        
if __name__ == '__main__':
    unittest.main(exit=False)
