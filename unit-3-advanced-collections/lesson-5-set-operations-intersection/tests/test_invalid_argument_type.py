def test_invalid_argument_type():
    assert  common_values([1, 2, 3, 4], (1, 2, 3, 4)) == "Params not of type 'list'"
