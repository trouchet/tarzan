from src.forms import label_input


def test_label_input():
    # Test when is_required is True
    result = label_input("Username", is_required=True)
    expected_result = "Username*"
    assert result == expected_result

    # Test when is_required is False
    result = label_input("Email", is_required=False)
    expected_result = "Email"
    assert result == expected_result
