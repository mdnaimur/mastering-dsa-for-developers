# Part 1: Algorithm Complexity Analysis

#### Analyze time and Space Complexity 

---

### 1. Insert all the beginneing of a dynamic array

### Code:

```python
  def push_front(self, element):
        index = 0
        if self.length == index: 
            self.array[index] = element
            self.length += 1
            return

        for i in range(self.length, index, -1):
            self.array[i] = self.array[i - 1]

        self.array[index] = element
        self.length += 1
```

**Input output**
Let's Input numer: `39,12,87,99,56`

#### **Steps:** 
`array: []`
length = 5
input: push_front(39)

    - length == index
    - array[index] = element(=39)
  
output:
`array:[39]`

input: push_front(12)

    - length(5) -> i
    - array[_,39,_,_,_] = array[i - 1]
    - array[index] = element(=12)
  
output:
`array:[12,39]`

input: push_front(87)

    - length(5) -> i
    - array[_,12,39,_,_] = array[i - 1]
    - array[index] = element(=87)
    - 
output:
`array:[87,12,39]`

input: push_front(99)

    - length(5) -> i
    - array[_,87,12,39,_] = array[i - 1]
    - array[index] = element(=99)
  
output:
`array:[99,87,12,39]`

input: push_front(56)

    - length(5) -> i
    - array[_,99,87,12,39] = array[i - 1]
    - array[index] = element(=56)

output:
`array:[56,99,87,12,39]`

**Final Output:** `[56,99,87,12,39]`


### Time Complexity
- Best Case (O(1))   
- Average Case (O(n))
- Worst Case (O(n))

| Scenario      | Complexity    |
|:--------------|:--------------|
|Best Case      | O(1)          |
|Average Case   | O(n)          |
|Worst Case     | O(n)          |
|Space          | O(1)          |

* Space complexity O(1) array hold index element once
  
##### Suggest optimizations
* LinkList best performace
  1. Time Complexity O(1) [It inseration in Head ]
  2. Space Comlexity O(1)

---

### 6. Check if an array contains all unique values

### Code:
```python
    def is_all_unique_value(self):
        for i in range(self.length):
            for j in range(i + 1, self.length):
                if self.array[i] == self.array[j]:
                    return False
        return True
```
 
**Input output**
Let's Input numer: `39,12,87,99,56`

**Output:**
``` 
Result: True 
The array All values are unique
```
**Input output**
Let's Input numer: `39,12,87,99,56,12`

**Output:**

```
Result: False
Message: The array All values are not unique
```

### Time Complexity
- Best Case (O(1))   
- Average Case (O(n^2))
- Worst Case (O(n^2))


| Scenario      | Complexity    |
|:--------------|:--------------|
|Best Case      | O(1)          |
|Average Case   | O(n^2)          |
|Worst Case     | O(n^2)          |
|Space          | O(1)          |

* Space complexity O(1) array hold index element once
  
##### Suggest optimizations
* Binary search algorihm best performace
  1. Time Complexity O(n) 
  2. Space Comlexity O(1)

  
  N:B: But Need sort this array first
---


### 8.  Convert an array into a linked list  