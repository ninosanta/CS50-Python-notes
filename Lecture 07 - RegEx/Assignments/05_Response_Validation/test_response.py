from response import validate


def test_valid_emails():
    assert validate("malan@harvard.edu") == True
    assert validate("s123456@studenti.polito.it") == True
    assert validate("name.surname@polito.it") == True
    assert validate("name_surname@polito.it") == True
    

def test_invalid_emails():
    assert validate("malan@@@harvard.edu") == False
    assert validate("malan@harvard..edu") == False