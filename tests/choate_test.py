import re
import choate
import statistics, json, requests, pandas as pd

def get_values():
    choate_json = json.loads(requests.get('https://vulcan.seidenberg.pace.edu/~lkeeley/CS121/choateData.php').text)
    return choate_json

def test_vars_lists():
    varnames = choate.main.__code__.co_varnames
    assert 'choate_json' in varnames
    varnames_str = ','.join(varnames)
    assert re.search(r'ph', varnames_str, re.IGNORECASE)
    assert re.search(r'cond', varnames_str, re.IGNORECASE)
    assert re.search(r'do', varnames_str, re.IGNORECASE)
    assert re.search(r'temp', varnames_str, re.IGNORECASE)
    assert re.search(r'turb', varnames_str, re.IGNORECASE)
    assert re.search(r'sal', varnames_str, re.IGNORECASE)

def test_mean_stdd(capsys):
    outputs = get_values()
    choate.main()
    captured = capsys.readouterr()
    for sensor in outputs:
        for value in outputs[sensor]:
            assert re.search(str(outputs[sensor][value]), captured.out, re.IGNORECASE)