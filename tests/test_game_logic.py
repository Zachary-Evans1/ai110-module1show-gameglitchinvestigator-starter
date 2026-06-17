from logic_utils import check_guess, update_score

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
