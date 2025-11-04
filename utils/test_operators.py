import operators as op

def test_true():
    assert op.multiply(5,5)==25
def test_false():
    assert op.multiply(5,"5")==25
    assert op.multiply("a","b")== TypeError
