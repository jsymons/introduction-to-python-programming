# Get element number

Define a function `get_element_number` that receives a list of strings and a 
term. Use a loop to go through the list of strings and find the search term. 
Return the element number of the first match and 'no match' if there is no
match. 

Examples:

```python
>>> get_element_number(['a', 'b', 'c'], 'c')
2
>>> get_element_number(['a', 'a', 'a'], 'a')
0
>>> get_element_number(['a', 'b', 'c'], 's')
'no match'
```
