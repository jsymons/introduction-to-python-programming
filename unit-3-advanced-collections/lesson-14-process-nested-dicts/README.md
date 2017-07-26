# Process nested dicts

Write a function `analyze_age_in_dicts` that receives a list of dictionaries, pulls the value associated with the key `"age"` from each dictionary, and returns a new dictionary with two keys:

* `'avg_age'`: The average age of the input dict
* `'dictionary_count'`: The number of elements processed

```python
analyze_age_in_dicts([{"name" : "Bob", "age": 22}, {"name" : "Jane", "age" : 26}])

# {"avg_age" : 24.0, "dictionary_count" : 2}
```
