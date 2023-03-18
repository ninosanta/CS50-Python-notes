from numb3rs import validate


def test_valid_ips():
    assert validate("192.168.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("127.0.0.1") == True


def test_invalid_ips():
    assert validate("192_168.0.1") == False
    assert validate("256.255.255.255") == False
    assert validate("0.$.0.0") == False
    assert validate("128.127.0.0.1") == False
    assert validate("127.0.0.1000") == False
    assert validate("127.0.0") == False
    assert validate("cat") == False
