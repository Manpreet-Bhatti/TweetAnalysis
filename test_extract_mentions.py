import unittest
import tweets

class TestExtractMentions(unittest.TestCase):
    '''Tester for the function extract_mentions in tweets.
    '''

    def test_empty(self):
        '''Empty tweet.'''

        arg = ''
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_nonempty_no_mention(self):
        '''Non-empty tweet with no mentions.'''

        arg = 'tweet test case'
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_mention(self):
        '''A tweet with one mention.'''

        arg = '@Hey my name is Bob'
        actual = tweets.extract_mentions(arg)
        expected = ['hey']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)   
        
    def test_mention_multiple(self):
        '''A tweet with multiple mentions.'''

        arg = '@Hey @my @name is @Bob'
        actual = tweets.extract_mentions(arg)
        expected = ['hey', 'my', 'name', 'bob']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
    
    def test_same_mention(self):
        '''A tweet with the duplicate mentions.'''

        arg = '@Hey @Hey @Hey Bob @hey'
        actual = tweets.extract_mentions(arg)
        expected = ['hey', 'hey', 'hey', 'hey']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
    
    def test_mixed_mention(self):
        '''A tweet with mentions and other characters mixed.'''

        arg = '@hey! !@wow @!ok @@k'
        actual = tweets.extract_mentions(arg)
        expected = ['hey']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_consec_mention(self):
        '''A tweet with consecutive mentions.'''

        arg = '@hi@my@name@is@manpreet'
        actual = tweets.extract_mentions(arg)
        expected = ['hi']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)    

if __name__ == '__main__':
    unittest.main(exit=False)
