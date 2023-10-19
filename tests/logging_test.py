import re
import simple_logging

def test_division():
    assert simple_logging.division(2, 1) == 2

def test_dictionary_lookup():
    assert simple_logging.dictionary_lookup({'a': 1, 'b': 2}, 'a') == 1

def test_parsefile():
    assert len(simple_logging.parsefile('diet.py')) > 0

def test_log_error():
    simple_logging.log_error('errors.txt', 'In a hole in the ground there lived a hobbit.')
    f = open('errors.txt', 'r')
    lines = f.readlines()
    f.close()
    assert len(lines) > 0
    assert re.search(r'In a hole in the ground there lived a hobbit', lines[-1])

def test_main():
    simple_logging.main()
    f = open('errors.txt', 'r')
    lines = f.readlines()
    f.close()
    assert len(lines) >= 3
    assert re.search(r'[0|zero]', lines[0], re.IGNORECASE)
    assert re.search(r'[key|word|dict]', lines[1], re.IGNORECASE)
    assert re.search(r'[found|file]', lines[2], re.IGNORECASE)