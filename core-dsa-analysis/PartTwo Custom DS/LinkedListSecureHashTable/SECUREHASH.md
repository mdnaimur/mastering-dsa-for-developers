# Secure Hash Table:
* Prime bucket sizing with auto-resizing.
* Ordered key tracking.
* Optional TTL (time-to-live) support for entries.

---


## Setup Instruction
1. **clone the repository**
   ``` bash
   git clone https://github.com/mdnaimur/mastering-dsa-for-developers.git

   ```
   ``` bash
   git checkout ds-complexity

   ```
    ``` bash
        inside PartTwo Custom DS
        cd LinkedListSecureHashTable
    ```

2. **Run App**
   
   ``` bash
   docker-compose up --build

   ```
3. **Without Docker** 
    On Windows:
    ```bash
    python -m venv venv
    venv\Scripts\activate 
    ```


    **On macOS/Linux:**
    ``` bash
    source venv/bin/activate
    ```
    ```bash
    pip install -r requirements.txt

    ```
    **Run**
    ```bahs
    python main.py

    ```

---

**Output**

``` bash
============================================================
Test 1: Basic `set()` and `get()`
============================================================

Get 'name': Naimur
Get 'city': Dhaka
Get 'country': None

============================================================
Test 2: `delete()` Key
============================================================

Before delete - email: test@example.com
Delete result: True
After delete - email: None

============================================================
Test 3: Time-To-Live (TTL) Expiry
============================================================

Immediately after set: abc123
After 3 seconds (expired): None

============================================================
Test 4: Overwriting Existing Key
============================================================

Before overwrite: old_user
After overwrite: new_user

============================================================
Test 5: `keys()`, `values()`, and `entries()`
============================================================

Keys: ['product', 'price', 'brand']
Values: ['Laptop', '$1000', 'Lenovo']
Entries: [('product', 'Laptop'), ('price', '$1000'), ('brand', 'Lenovo')]

============================================================
Test 6: `__str__()` Representation
============================================================

product: Laptop
price: $1000
brand: Lenovo

============================================================
Test 7: Automatic Resize on Load Factor
============================================================

Final size after resize: 23
Keys: ['key4', 'key5', 'key1', 'key0', 'key8', 'key3', 'key2', 'key7', 'key6', 'key9']

============================================================
Test 8: TTL Reset After Overwrite
============================================================

Get 'token' after 3s (should still exist): temp2
Get 'token' after 5s (should be expired): None

============================================================
Test 9: Multiple Keys with Different TTLs
============================================================

short_lived (should be None): None
long_lived (should still exist): 5s

============================================================
Test 10: Get and Delete Non-Existent Keys
============================================================

Get 'missing': None
Delete 'missing': False

```