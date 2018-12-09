"""Assignment 3: Tweet Analysis"""

from typing import List, Dict, TextIO, Tuple

HASH_SYMBOL = '#'
MENTION_SYMBOL = '@'
URL_START = 'http'

# Order of data in the file
FILE_DATE_INDEX = 0
FILE_LOCATION_INDEX = 1
FILE_SOURCE_INDEX = 2
FILE_FAVOURITE_INDEX = 3
FILE_RETWEET_INDEX = 4

# Order of data in a tweet tuple
TWEET_TEXT_INDEX = 0
TWEET_DATE_INDEX = 1
TWEET_SOURCE_INDEX = 2
TWEET_FAVOURITE_INDEX = 3
TWEET_RETWEET_INDEX = 4

# Helper functions.

def alnum_prefix(text: str) -> str:
    """Return the alphanumeric prefix of text, converted to
    lowercase. That is, return all characters in text from the
    beginning until the first non-alphanumeric character or until the
    end of text, if text does not contain any non-alphanumeric
    characters.

    >>> alnum_prefix('')
    ''
    >>> alnum_prefix('IamIamIam')
    'iamiamiam'
    >>> alnum_prefix('IamIamIam!!')
    'iamiamiam'
    >>> alnum_prefix('IamIamIam!!andMore')
    'iamiamiam'
    >>> alnum_prefix('$$$money')
    ''

    """

    index = 0
    while index < len(text) and text[index].isalnum():
        index += 1
    return text[:index].lower()

def clean_word(word: str) -> str:
    """Return all alphanumeric characters from word, in the same order as
    they appear in word, converted to lowercase.

    >>> clean_word('')
    ''
    >>> clean_word('AlreadyClean?')
    'alreadyclean'
    >>> clean_word('very123mes$_sy?')
    'very123messy'

    """

    cleaned_word = ''
    for char in word.lower():
        if char.isalnum():
            cleaned_word = cleaned_word + char
    return cleaned_word

def hashtag_finder(tweets: Dict[str, List[tuple]]) -> Dict[str, List[str]]:
    '''Return a dictionary with the hashtags each username had tweeted, given
    a dictionary similar to the on in read_tweets, tweets.
    
    >>> hashtag_finder({'hi': [('#hi #hey #ho #bo', 1, 'lol ok', 0, 5)]})
    {'hi': ['hi', 'hey', 'ho', 'bo']}
    >>> hashtag_finder({'hi': [('#lol', 1, 'ok', 0, 5), ('#ok', 2, 'lol',1, 6)]\
    , 'hey': [('#lmao', 3, 'ikr', 2, 7)]})
    {'hi': ['lol', 'ok'], 'hey': ['lmao']}
    '''
    
    new_dict = {}
    for k in tweets:
        hash_lst = []
        for v in tweets[k]:
            hash_lst.append(extract_hashtags(v[TWEET_TEXT_INDEX]))
        new_dict[k] = []
        for val in hash_lst:
            for val1 in val:
                new_dict[k].append(val1)
    return new_dict

# Required functions

def extract_mentions(text: str) -> List[str]:
    """Return a list of all mentions in text, converted to lowercase, with
    duplicates included.

    >>> extract_mentions('Hi @UofT do you like @cats @CATS #meowmeow')
    ['uoft', 'cats', 'cats']
    >>> extract_mentions('@cats are #cute @cats @cat meow @meow')
    ['cats', 'cats', 'cat', 'meow']
    >>> extract_mentions('@many @cats$extra @meow?!')
    ['many', 'cats', 'meow']
    >>> extract_mentions('No valid mentions @! here?')
    []
    """
    
    string_list = []
    text = text.split()
    for i in text:
        if MENTION_SYMBOL == i[0]:
            string_list.append(alnum_prefix(i[1:]))
    while '' in string_list:
        string_list.remove('')
    return string_list    

def extract_hashtags(text: str) -> List[str]:
    '''Return a list containing all of the unique hashtags in the text, in the
    order they appear in the text, converted to lowercase and duplicates not
    included.

    >>> extract_hashtags('Hi @UofT do you like @cats @CATS #meowmeow')
    ['meowmeow']
    >>> extract_hashtags('#cats are @cute #cats #cat #MEOW #meow')
    ['cats', 'cat', 'meow']
    >>> extract_hashtags('#many #cats$extra #meow?!')
    ['many', 'cats', 'meow']
    >>> extract_hashtags('No valid mentions #! here?')
    []
    '''

    string_list = []
    text = text.split()
    for i in text:
        if HASH_SYMBOL == i[0]:
            if alnum_prefix(i[1:]) not in string_list:
                string_list.append(alnum_prefix(i[1:]))
    while '' in string_list:
        string_list.remove('')
    return string_list

def count_words(text: str, words: Dict[str, int]) -> None:
    '''Update a dictionary, words, given a text such that it has words in the 
    text lowercased and cleaned representing keys, and the frequency of the 
    strings represting the values.

    >>> h = '#UofT Nick Frosst: he is so, so cool @goodkid'
    >>> b = {'nick': 7}
    >>> count_words(h, b)
    >>> b
    {'nick': 8, 'frosst': 1, 'he': 1, 'is': 1, 'so': 2, 'cool': 1}
    '''
    
    symbols = [MENTION_SYMBOL, HASH_SYMBOL]
    text = text.split()
    same_text = []
    for w in text:
        for ch in symbols:
            if ch in w[0]:
                same_text.append(w)
        if URL_START in w[:len(URL_START)]:
            same_text.append(w)
    for wrd in same_text:
        text.remove(wrd)
    for word in text:
        if clean_word(word) not in words:
            words[clean_word(word)] = 1
        else:
            words[clean_word(word)] += 1
    while '' in words:
        del words['']

def common_words(words: Dict[str, int], n: int) -> None:
    '''Update words, the result of a dictionary similar to the one described
    in count_words such that it has, at most, n most common words.
    
    >>> b = {'nick': 3, 'fro': 2, 'he': 2, 'is': 2, 'so': 2, 'cool': 1}
    >>> common_words(b, 5)
    >>> b
    {'nick': 3, 'fro': 2, 'he': 2, 'is': 2, 'so': 2}
    >>> b = {'nick': 3, 'fro': 2, 'he': 2, 'is': 2, 'so': 2, 'cool': 1}
    >>> common_words(b, 4)
    >>> b
    {'nick': 3}
    '''
    
    og_lst, remain = [], []
    if len(words) == 0:
        return None
    for w in words:
        remain.append(words[w])
    while len(og_lst) < n:
        if len(remain) == 0:
            break
        else:
            og_lst.append(max(remain))
            remain.remove(max(remain))
    remain = list(set(remain))
    for rem in remain:
        if rem in og_lst:
            while rem in og_lst:
                og_lst.remove(rem)
    for k, v in list(words.items()):
        for num in remain:
            if v == num and num not in og_lst:
                del words[k]    
    
def read_tweets(file: TextIO) -> Dict[str, List[tuple]]:
    '''Return a dictionary with the keys being lowercase Twitter usernames and
    the items in the list being tuples representing tweets of each username 
    after reading an opened file, file.
    '''
    new_dict = {}
    usernames, user_num = [], []
    line = file.readlines()
    for w in range(len(line)):
        if w == 0 or (line[w - 1] == '<<<EOT\n' or w - 1 in user_num) and \
           line[w].strip().endswith(':'):
            new_dict[line[w].strip().strip(':').lower()] = []
            usernames.append(line[w].strip().strip(':').lower())
            user_num.append(line.index(line[w]))
    for n in range(len(user_num)):
        x = user_num[n] + 1
        while x < len(line) and (x not in user_num or not \
                                 line[x].strip().endswith(':')):
            tweet_text = ''
            y = x + 1
            while y < len(line) and line[y] != '<<<EOT\n':
                tweet_text += line[y]
                y += 1
            tweet_rt = int(line[x].strip().split(',')[FILE_RETWEET_INDEX])
            tweet_fav = int(line[x].strip().split(',')[FILE_FAVOURITE_INDEX])
            tweet_source = line[x].strip().split(',')[FILE_SOURCE_INDEX]
            tweet_date = int(line[x].strip().split(',')[FILE_DATE_INDEX])
            new_dict[usernames[n]].append((tweet_text.strip(), tweet_date, 
                                           tweet_source, tweet_fav, tweet_rt))
            x = y + 1
    return new_dict

def most_popular(tweets: Dict[str, List[tuple]], date1: int, date2: int) -> str:
    '''Return the username of the Twitter user who was the most popular on
    Twitter between two dates, date1 and date2, given a dictionary, tweets. In 
    case of a tie in popularity or no tweet was tweeted in the date range,
    return 'tie'.
    
    >>> t_twt = {'Ar': [('Yo', 0, 'lol', 1, 11)], 'Me': [('ha', 9, 'he', 1, 1)]}
    >>> most_popular(t_twt, 0, 10)
    'ar'
    >>> t_twt = {'Lol': [('ni', 2, 'br', 6, 6)], 'Mo': [('ad', 3, 'sc', 6, 6)]}
    >>> most_popular(t_twt, 0, 5)
    'tie'
    '''
    
    temp_dict = {}
    max_vals, new_vals = [], []
    for k in tweets:
        max_val = 0
        for v in tweets[k]:
            if date1 <= v[TWEET_DATE_INDEX] <= date2:
                max_val += v[TWEET_FAVOURITE_INDEX] + v[TWEET_RETWEET_INDEX]
        max_vals.append(max_val)
        for val in max_vals:
            temp_dict[k.lower()] = val
    if len(temp_dict) == 0:
        return 'tie'
    else:
        max_num = max(temp_dict.values())
        for k1 in temp_dict:
            if temp_dict[k1] == max_num:
                new_vals.append(k1)
        if len(new_vals) > 1:
            return 'tie'
        return new_vals[0]

def detect_author(tweets: Dict[str, List[tuple]], text: str) -> str:
    '''Return the username (in lowercase), given in tweets,
    if all the hashtags in the tweet, text, are uniquely used by a single user. 
    Otherwise, return the 'unknown'.
    
    >>> detect_author({'boom': [('#hi', 3, 'add', 0, 5), ('#hey', 2, 'dsa', 6, \
    1)], 'bam': [('#hi', 5, 'DSi', 0, 5), ('#hey', 3, 'b', 5, 0)]}, '#hey')
    'unknown'
    >>> detect_author({'bow': [('#hi', 3, 'add', 0, 5), ('#hey', 2, 'dsa', 6, \
    1)], 'pew': [('#don', 5, 'DSi', 0, 5), ('#dog', 3, 'b', 5, 0)]}, '#hey')
    'bow'
    '''
    
    user_hash = hashtag_finder(tweets)
    users, temp_len = [], []
    for u in user_hash:
        dup_hash = extract_hashtags(text)
        for hasht in user_hash[u]:
            for extract_hash in dup_hash:
                if extract_hash == hasht:
                    users.append(u)
                    dup_hash.remove(extract_hash)
        temp_len.append(len(dup_hash))
    if len(users) > 1 or len(users) == 0 or temp_len[0] > 1:
        return 'unknown'
    return users[0].lower()

if __name__ == '__main__':
    pass

    import doctest
    doctest.testmod()
