def test_process_two_dicts():
    original = [{
        "name": "Bob",
        "age": 22
    }, {
        "name": "Jane",
        "age": 26
    }]
    expected = {"avg_age": 24.0, "dictionary_count": 2}
    assert analyze_age_in_dicts(original) == expected
