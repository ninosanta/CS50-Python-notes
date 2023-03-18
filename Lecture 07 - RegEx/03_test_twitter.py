from twitter import username

def test_valid_url():
    assert username("https://twitter.com/elonmusk") == "elonmusk"
    assert username("twitter.com/elonmusk/") == "elonmusk"
    assert username("http://twitter.com/elonmusk") == "elonmusk"
    assert username("https://www.twitter.com/elonmusk") == "elonmusk"
    assert username("https://www.twitter.com/elon_tusk") == "elon_tusk"


def test_invalid_url():
    assert username("https://twitterAcom/elonmusk") == ""
    assert username("https://twitterBcom/elonmusk") == ""
    assert username("https://google.com/elonmusk") == ""
    