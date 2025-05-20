# Inventory Lookup System

* Maintain a product catalog
* Allow quick availability checks and frequent insertions/removals
* Ensure scalability as inventory grows
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
        inside the PartThree Real wold PrlmSolv
        cd InventoryLookUpSystem
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
Inventory Manager
============================================================


============================================================
Test 1: Add Products
============================================================

['p10', 'p30', 'p20']

============================================================
All values
============================================================

VALUEs  Product(name = Notebook, price = 250, stock = 15, category = Stationary)
VALUEs  Product(name = Backpack, price = 800, stock = 5, category = Bags)
VALUEs  Product(name = Pen, price = 100, stock = 10, category = Stationary)
Added products:
Product(name = Pen, price = 100, stock = 10, category = Stationary)
Product(name = Backpack, price = 800, stock = 5, category = Bags)
Product(name = Notebook, price = 250, stock = 15, category = Stationary)

============================================================
Test 2: Get Product Price
============================================================

Price of p10: 100
Price of p20: 250
Price of p30: 800
Price of p30: None

============================================================
 Get Product name
============================================================

name of p10: Pen
name of p20: Notebook
name of p30: Backpack

============================================================
category  2: Get Product category
============================================================

category of p10: Stationary
category of p20: Stationary
Price of p30: Bags

============================================================
Stock  : Get Product stock
============================================================

stock of p10: 10
stock of p20: 15
stock of p30: 5

============================================================
Test 3: Update Stock
============================================================

Before update: 5
After update: 12

============================================================
Test 4: Delete Product
============================================================

Deleted p20: True
Trying to get p20: None

============================================================
Test 5: Non-existent SKU Operations
============================================================

Get price of p999: None
Update stock of p999: False
Delete p999: False

============================================================
Test 6: Add Duplicate SKU (Overwrite)
============================================================

Updated p10: Product(name = Pen Pro, price = 150, stock = 25, category = Stationary)
New Price of p10: 150

```

``` bash


Bucket (index 4):
    ┌──────────────┐     ┌──────────────┐
    │ key1, value1 │ →   │ key2, value2 │ → None
    └──────────────┘     └──────────────┘
self.table[4] --> LinkedList:
    ┌──────────────────────────────────────────────┐
    │ key: "P100"                                  │
    │ value: {"name": "Tablet", "quantity": 15,    │
    │         "price": 200.00}                     │
    └──────────────────────────────────────────────┘
             ↓
    ┌──────────────────────────────────────────────┐
    │ key: "X999"                                  │
    │ value: {"name": "Speaker", "quantity": 10,   │
    │         "price": 80.00}                      │
    └──────────────────────────────────────────────┘
             ↓
           None
```