from numbers_letters_dependent import calculate_password_score, calculate_password_strength

def test_password_strength() -> None:
    #Tests cases for different password strengths
    test_cases: dict[str, tuple[str, int]] = {
        "": ("jeez-", 0),
        "AAAAAAAAAAAAAAAAAAAAAAAAA": ("jeez-", -4),
        "AV46fssx1^^aascvbbs": ("Mid", 15),
        "awf?==^12wsas": ("Weak", 6),
        "12345655": ("Weak", 8),
        "lalalla1247fsaaaASSD1^1": ("Mid", 10),
        "adcx03ß2sasx": ("Weak", 6),
        "Dass5ist_ein_sehr_starkes_Passwort!": ("jeez-", -1),
    }

    for pwd, (expected_strength, expected_score) in test_cases.items():
        score = calculate_password_score(pwd)
        strength, message = calculate_password_strength(score)
        assert strength == expected_strength, f"'{pwd}' strength: expected {expected_strength}, got {strength}"
        assert score == expected_score, f"'{pwd}' score: expected {expected_score}, got {score}"

if __name__ == "__main__":
    test_password_strength()
    print("The microwave popcorn is popping, all tests passed!")