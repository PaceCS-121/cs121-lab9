import re
import guess_the_number2

def test_check_num_output(capsys, monkeypatch):
    inputs = '50'
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    guess_the_number2.main()
    captured = capsys.readouterr()
    assert re.search(r"high", captured.out, re.IGNORECASE)
    assert re.search(r"low", captured.out, re.IGNORECASE)

def test_err(monkeypatch):
    inputs = '50'
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    try:
        guess_the_number2.main()
    except Exception as e:
        assert re.search(r'[Assertion|Error]', str(e), re.IGNORECASE)