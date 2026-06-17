from logic_utils import check_guess, update_score, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"


def test_update_score_too_high_even_attempt_deducts_5():
    # Verify that "Too High" deducts 5 points on even attempts (bug fix)
    current_score = 100
    new_score = update_score(current_score, "Too High", attempt_number=2)
    assert new_score == 95

def test_consecutive_guesses_with_integer_secret():
    # Test that consecutive guesses (odd and even attempts) work with integer secret
    # This ensures the secret is not converted to a string on even attempts
    secret = 50

    # First guess (odd attempt)
    result1 = check_guess(40, secret)
    assert result1[0] == "Too Low"

    # Second guess (even attempt) - should work correctly with integer secret
    result2 = check_guess(60, secret)
    assert result2[0] == "Too High"


# Edge case tests for parse_guess
def test_parse_guess_sentence_input():
    # Test that a sentence/string input is rejected
    ok, guess_int, err = parse_guess("hello world")
    assert ok is False
    assert guess_int is None
    assert err == "That is not a number."


def test_parse_guess_negative_number():
    # Test that negative numbers are parsed correctly
    ok, guess_int, err = parse_guess("-42")
    assert ok is True
    assert guess_int == -42
    assert err is None


def test_parse_guess_very_large_number():
    # Test that very large numbers are parsed correctly
    ok, guess_int, err = parse_guess("999999999999")
    assert ok is True
    assert guess_int == 999999999999
    assert err is None


def test_parse_guess_floating_point_number():
    # Test that floating point numbers are converted to integers
    ok, guess_int, err = parse_guess("42.7")
    assert ok is True
    assert guess_int == 42
    assert err is None


def test_parse_guess_empty_string():
    # Test that empty string is rejected
    ok, guess_int, err = parse_guess("")
    assert ok is False
    assert guess_int is None
    assert err == "Enter a guess."
