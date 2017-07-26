def test_dict_without_age_key():
    original = [{
        "name": "Bob",
        "age": 22
    }, {
        "name": "Jane",
        "age": 26
    }, {
        "name": "Alice",
        "last_name": "Jones"  # WARNING! No age key.
    }]
    expected = {"avg_age": 24.0, "dictionary_count": 2}
    assert analyze_age_in_dicts(original) == expected
