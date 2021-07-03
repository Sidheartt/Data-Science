# Pandas-DataFrame


```python
import numpy as np
import pandas as pd
```


```python
from numpy.random import randn
```


```python
np.random.seed(101)
```


```python
df = pd.DataFrame(randn(5,4), ['A','B','C','D','E'],['W','X','Y','Z'])
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>0.302665</td>
      <td>1.693723</td>
      <td>-1.706086</td>
      <td>-1.159119</td>
    </tr>
    <tr>
      <th>B</th>
      <td>-0.134841</td>
      <td>0.390528</td>
      <td>0.166905</td>
      <td>0.184502</td>
    </tr>
    <tr>
      <th>C</th>
      <td>0.807706</td>
      <td>0.072960</td>
      <td>0.638787</td>
      <td>0.329646</td>
    </tr>
    <tr>
      <th>D</th>
      <td>-0.497104</td>
      <td>-0.754070</td>
      <td>-0.943406</td>
      <td>0.484752</td>
    </tr>
    <tr>
      <th>E</th>
      <td>-0.116773</td>
      <td>1.901755</td>
      <td>0.238127</td>
      <td>1.996652</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['W']
```




    A    0.302665
    B   -0.134841
    C    0.807706
    D   -0.497104
    E   -0.116773
    Name: W, dtype: float64




```python
df[['W','Y']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>W</th>
      <th>Y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>0.302665</td>
      <td>-1.706086</td>
    </tr>
    <tr>
      <th>B</th>
      <td>-0.134841</td>
      <td>0.166905</td>
    </tr>
    <tr>
      <th>C</th>
      <td>0.807706</td>
      <td>0.638787</td>
    </tr>
    <tr>
      <th>D</th>
      <td>-0.497104</td>
      <td>-0.943406</td>
    </tr>
    <tr>
      <th>E</th>
      <td>-0.116773</td>
      <td>0.238127</td>
    </tr>
  </tbody>
</table>
</div>



How to add to existing dataframe (Column)



```python
df['new'] = df['W'] + df['Y']
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
      <th>new</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>0.302665</td>
      <td>1.693723</td>
      <td>-1.706086</td>
      <td>-1.159119</td>
      <td>-1.403420</td>
    </tr>
    <tr>
      <th>B</th>
      <td>-0.134841</td>
      <td>0.390528</td>
      <td>0.166905</td>
      <td>0.184502</td>
      <td>0.032064</td>
    </tr>
    <tr>
      <th>C</th>
      <td>0.807706</td>
      <td>0.072960</td>
      <td>0.638787</td>
      <td>0.329646</td>
      <td>1.446493</td>
    </tr>
    <tr>
      <th>D</th>
      <td>-0.497104</td>
      <td>-0.754070</td>
      <td>-0.943406</td>
      <td>0.484752</td>
      <td>-1.440510</td>
    </tr>
    <tr>
      <th>E</th>
      <td>-0.116773</td>
      <td>1.901755</td>
      <td>0.238127</td>
      <td>1.996652</td>
      <td>0.121354</td>
    </tr>
  </tbody>
</table>
</div>



how to delete a column(just the show)


```python
df.drop('new', axis=1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>0.302665</td>
      <td>1.693723</td>
      <td>-1.706086</td>
      <td>-1.159119</td>
    </tr>
    <tr>
      <th>B</th>
      <td>-0.134841</td>
      <td>0.390528</td>
      <td>0.166905</td>
      <td>0.184502</td>
    </tr>
    <tr>
      <th>C</th>
      <td>0.807706</td>
      <td>0.072960</td>
      <td>0.638787</td>
      <td>0.329646</td>
    </tr>
    <tr>
      <th>D</th>
      <td>-0.497104</td>
      <td>-0.754070</td>
      <td>-0.943406</td>
      <td>0.484752</td>
    </tr>
    <tr>
      <th>E</th>
      <td>-0.116773</td>
      <td>1.901755</td>
      <td>0.238127</td>
      <td>1.996652</td>
    </tr>
  </tbody>
</table>
</div>



how to delete a column(Actually,permanently remove it)


```python
df.drop('new', axis=1, inplace=True)
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>0.302665</td>
      <td>1.693723</td>
      <td>-1.706086</td>
      <td>-1.159119</td>
    </tr>
    <tr>
      <th>B</th>
      <td>-0.134841</td>
      <td>0.390528</td>
      <td>0.166905</td>
      <td>0.184502</td>
    </tr>
    <tr>
      <th>C</th>
      <td>0.807706</td>
      <td>0.072960</td>
      <td>0.638787</td>
      <td>0.329646</td>
    </tr>
    <tr>
      <th>D</th>
      <td>-0.497104</td>
      <td>-0.754070</td>
      <td>-0.943406</td>
      <td>0.484752</td>
    </tr>
    <tr>
      <th>E</th>
      <td>-0.116773</td>
      <td>1.901755</td>
      <td>0.238127</td>
      <td>1.996652</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.drop('E',axis=0)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>W</th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>0.302665</td>
      <td>1.693723</td>
      <td>-1.706086</td>
      <td>-1.159119</td>
    </tr>
    <tr>
      <th>B</th>
      <td>-0.134841</td>
      <td>0.390528</td>
      <td>0.166905</td>
      <td>0.184502</td>
    </tr>
    <tr>
      <th>C</th>
      <td>0.807706</td>
      <td>0.072960</td>
      <td>0.638787</td>
      <td>0.329646</td>
    </tr>
    <tr>
      <th>D</th>
      <td>-0.497104</td>
      <td>-0.754070</td>
      <td>-0.943406</td>
      <td>0.484752</td>
    </tr>
  </tbody>
</table>
</div>



how to grab a row


```python
df.loc['C']
```




    W    0.807706
    X    0.072960
    Y    0.638787
    Z    0.329646
    Name: C, dtype: float64




```python
df.iloc[2]
```




    W    0.807706
    X    0.072960
    Y    0.638787
    Z    0.329646
    Name: C, dtype: float64



To grab a single Value


```python
df.loc['B','Y']
```




    0.16690463609281317




```python
df.loc[['A','B'],['W','Y']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>W</th>
      <th>Y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>0.302665</td>
      <td>-1.706086</td>
    </tr>
    <tr>
      <th>B</th>
      <td>-0.134841</td>
      <td>0.166905</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
