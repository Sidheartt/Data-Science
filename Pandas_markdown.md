# Pandas


```python
import numpy as np
```


```python
import pandas as pd
```


```python
label = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10, 'b':20, 'c':30}
```

how to make a series ?



```python
pd.Series(data = my_data, index = label)
```




    a    10
    b    20
    c    30
    dtype: int64




```python
pd.Series(my_data, label)
```




    a    10
    b    20
    c    30
    dtype: int64




```python
pd.Series(arr, label)
```




    a    10
    b    20
    c    30
    dtype: int32




```python
pd.Series(d)
```




    a    10
    b    20
    c    30
    dtype: int64




```python

```
