# Shopping Cart System 
* A user adds a product, the latest added product must be shown at the top.
* When the cart is finalized, products should be processed from oldest to newest.

---


## Setup Instruction
1. **clone the repository**
   ``` bash
   git clone https://github.com/mdnaimur/mastering-dsa-for-developers.git

   ```
      ``` bash
   git checkout real_world

   ```
    ``` bash
        inside dsa_real_life
        Part_1-Real-World/
        cd ShoppingCartSystemStack
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
Add Product Item
============================================================

['Mango', 'Orange', 'Apple', 'Dates']

============================================================
View Cart item
============================================================

Mango
Orange
Apple
Dates

============================================================
Checkout
============================================================

Processing checkout (Oldest to Newest):

Dates
Apple
Orange
Mango
None
```