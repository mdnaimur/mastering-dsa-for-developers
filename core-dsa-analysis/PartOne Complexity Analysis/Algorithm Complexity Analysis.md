# Part 1: Algorithm Complexity Analysis

#### Analyze time and Space Complexity 

---

## 1. Insert all the beginneing of a dynamic array

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
## 2. Insert at the end of a linked list

### Code: 

```python
def append(self, data):
        new_node = Node(data)
        self.size += 1

        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node
```


**Input output**
---
**Input:**
Let's Input numer: `75`

**Output:**
``` 
75 -->
```
**Input**
Let's Input numer: `105`

**Output:**

```
75 --> 105 -->
```

**Input**
Let's Input numer: `115`

**Output:**

```
75 --> 105 --> 115 -->
```
**Input**
Let's Input numer: `135`

**Output:**

```
75 --> 105 --> 115 --> 135 -->
```

### Time Complexity
- Best Case (O(1))   
- Average Case (O(1)
- Worst Case (O(1)


| Scenario      | Complexity    |
|:--------------|:--------------|
|Best Case      | O(1)          |
|Average Case   | O(1)          |
|Worst Case     | O(1)          |
|Space          | O(1)          |

* Space complexity O(1) array hold index element once
  
##### Suggest optimizations
* For insertion end of list this approch provide best result

---
## 3. Search for an element in a Hash set

```python
def has(self, value):
        return bool(self.data.get(str(value)))

```
 
**Input output**
Let's Input numer:
```
setA = [1, 2, 3]

```

**Output:**
``` 
False: If value not present setA
True: If value found

```

### Time Complexity
- Best Case (O(1))   
- Average Case (O(1))
- Worst Case (O(1))


| Scenario      | Complexity    |
|:--------------|:--------------|
|Best Case      | O(1)          |
|Average Case   | O(1)          |
|Worst Case     | O(1)          |
|Space          | O(1)          |

* Space complexity O(1) array hold index element once
---

## 4. Rehash a hash table after crossing load factor

```python
    def _resize(self, new_size):
        old_table = self.table
        self.size = new_size
        self.table = [None] * new_size
        self.count = 0

        for bucket in old_table:
            if bucket:
                for key, value in bucket.entries():
                    self.set(key, value)

```
 
**Input output**
Let's Input numer:
```
A = [1, 2, 3]
newSize = 2

```

**Output:**
``` 
A = [1, 2, 3,__,__,__]

```

### Time Complexity
- Best Case (O(1))   
- Average Case (O(n))
- Worst Case (O(n))


| Scenario      | Complexity    |
|:--------------|:--------------|
|Best Case      | O(1)          |
|Average Case   | O(n)          |
|Worst Case     | O(n)          |
|Space          | O(n)          |

* Space complexity O(n) array hold index element once


---


## 5. Delete a node from a singly linked list by value

### Code:
```python
def remove(self, data):
        if not self.head:
            return False

        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            if self.size == 0:
                self.tail = None
            return True

        current = self.head

        while current.next:
            if current.next.data == data:
                print(f"[DEBUG] inside remove : {current.next.data}")
                current.next = current.next.next
                self.size -= 1
                if not current.next:
                    self.tail = current
                return True
            current = current.next
        return False

```

**Input output**
---
Let's given Linked List Data: 
```
75 --> 105 --> 115 --> 135 -->
```
**Input:**
Let's Input numer for Delete: `115`

**Output:**
``` 
75 --> 105--> 135 -->
```

### Time Complexity
- Best Case (O(1))   
- Average Case (O(n)
- Worst Case (O(n)


| Scenario      | Complexity    |
|:--------------|:--------------|
|Best Case      | O(1)          |
|Average Case   | O(n)          |
|Worst Case     | O(n)          |
|Space          | O(1)          |

* Space complexity O(1) array hold index element once
  
##### Suggest optimizations
* For deletion nd of linked list this approch provide best result

---

## 6. Check if an array contains all unique values

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

## 7. Count common elements in two hash sets

### Code:
```python
def intersection(setA, setB):
    result = HashSet()
    for value in setA.values():
        if setB.has(value):
            result.add(value)
    return result
```
 
**Input output**
Let's Input numer:
```
setA = [1, 2, 3]
setB = [1, 2, 4, 6, 5 ]
```

**Output:**
``` 
Result: [1, 2]

```

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
*

  

---



### 8.  Convert an array into a linked list  

### Code:
```python
  def array_to_link_list(self, arr):
        if not arr:
            return None

        self.head = Node(arr[0])
        current = self.head
        self.size = 1

        for data in arr[1:]:
            new_node = Node(data)
            current.next = new_node
            current = new_node
            self.size += 1

        self.tail = current
```
 
**Input output**
Let's Input array : `arr = [3, 4, 5, 6, 7, 15]`

**Output:**
array to linkedlist 
``` 
 3 -> 4 -> 5 -> 6 -> 7 -> 15 -> None
```


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
* None

  
  
---


### 9.  Clone a hash table with chaninig

### Code:
```python
      def clone_hashtable(self):
        new_table = HashTable(self.size)
        for bucket in self.table:
            if bucket:
                for key, value in bucket.entries():
                    new_table.set(key, value)

        return new_table
```
 
**Input output**
Let's Input array : `hashTable =  [('name', 'Naimur'), ('University', 'HUB'), ('City', 'Narayanganj'), ('Country', 'Bangladesh'), ('Phone', '01736842161')] `


**Output:**
copy HashTable
``` 
Copy HashTable : 
 [('name', 'Naimur'), ('University', 'HUB'), ('City', 'Narayanganj'), ('Country', 'Bangladesh'), ('Phone', '01736842161')]

```

### Time Complexity
- Best Case (O(1))   
- Average Case (O(n))
- Worst Case (O(n))


| Scenario      | Complexity    |
|:--------------|:--------------|
|Best Case      | O(1)          |
|Average Case   | O(n)          |
|Worst Case     | O(n)          |
|Space          | O(n)          |

* Space complexity O(n) new hash table occupy space 

Complexity Breakdown:
```python

        for bucket in self.table: _________________________ O(m)
            if bucket:
                for key, value in bucket.entries(): _______ O(k)
                    new_table.set(key, value)

O(m+k) = O(n)
```
  
##### Suggest optimizations
* None

  
  
---


### 10.  Compare array vs. hash set lookup performance 

what is lookup?
--  ***searching for a specifict element on a data structure***

Now compare the array and the hashset, who give optimized performance
**Array:** 
An Array is Data Structure used programming language to store a collecion of elemets.
  1. It contains fixed size
  2. Same type of data
  3. Order sequence
  4. Each element has an index number
   

**HashSet**

*A Hashset is a data structure that stores a collection of unique elements without any particular order.*
  
 1. Unique Elemets
 2. Unordered
 3. No Indexing 


So searching specific elements in a HashSet is more optimized because it has no indexing, so it does not need to search elements index by index like an array does.
```
here
HashSet gives  an O(1) 
Array gives  an O(n)
```


|               | Array         | Hashset      |
|:--------------|:--------------|:-------------|
|Best Case      | O(1)          | O(1)
|Average Case   | O(n)          | *
|Worst Case     | O(n)          | O(n) * rearcase
|Space          | O(1)          | O(1)


  
##### Suggest optimizations
* None

  
  
---