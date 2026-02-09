from numbers_letters_dependent import calculate_password_score, calculate_password_strength

def test_password_strength() -> None:
    #Tests cases for different password strengths
    test_cases: dict[str, tuple[str, int]] = {
        "12345": ("Weak", 1),
        "abcde": ("Weak", 1),
        "abc123": ("Mid", 12),
        "Abc123!": ("Mid", 15),
        "aaaaaa": ("Weak", 5),
        "A1!": ("Weak", 4),
        "A1!a2@b3#": ("Mid", 15)
    }

    for pwd, (expected_strength, expected_score) in test_cases.items():
        score = calculate_password_score(pwd)
        strength, message = calculate_password_strength(score)
        assert strength == expected_strength, f"'{pwd}' strength: expected {expected_strength}, got {strength}"
        assert score == expected_score, f"'{pwd}' score: expected {expected_score}, got {score}"

if __name__ == "__main__":
    test_password_strength()
    print("All tests passed!")