from um import count


def test_valid_inputs():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("um, um") == 2
    assert count("Um, thanks, um...") == 2
    assert count("foo, bar, um, don, um, joe, um") == 3
    assert count("um um um um... that's what she said") == 4
    assert count("Podium, unum-canum um um") == 2
    assert count("gallium um um um um portium") == 4