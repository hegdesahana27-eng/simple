from simpleInterest import  simpInt

def test_simpleInt_pos():
    assert simpInt(20000,8,12)==19200

def test_simpleInt_zer():
    assert simpInt(10000,7,0)==0

