import re
import diet

def test_phyllo_dough(capsys, monkeypatch):
    inputs = iter(['Phyllo dough', 'calories'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    diet.main()
    captured = capsys.readouterr()
    assert re.search(r'299', captured.out, re.IGNORECASE)