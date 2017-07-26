def test_process_one_dict():
    original = [{
        "name": "Hermione",
        "age": 23
    }]
    expected = {"avg_age": 23.0, "dictionary_count": 1}
    assert analyze_age_in_dicts(original) == expected
