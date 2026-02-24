from src import rename

def test_validation():
    assert rename.validation("validname.txt")
    assert not rename.validation("invalid<name>.txt")