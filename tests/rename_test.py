from functions.rename import validation

def test_validation():
    assert validation("validname.txt")
    assert not validation("invalid<name>.txt")