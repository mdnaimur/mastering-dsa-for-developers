# Event-Driven Linked List
* Listens to insert/update/delete actions.
* Supports registering external listeners with callbacks.

---


## Setup Instruction
1. **clone the repository**
   ``` bash
   git clone https://github.com/mdnaimur/mastering-dsa-for-developers.git

   ```
    ``` bash
        inside PartTwo Custom DS
        cd event_driven_linked_list
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
[Event] 🟢 Inserted: 20
[Event] 🟢 Inserted: 30
[Event] 🟢 Inserted: 50
[Event] 🟢 Inserted: 36
[Event] 🟢 Inserted: 90
Current list 10--> 20--> 30--> 50--> 36--> 90-->
[Event] ❌  Delete: 10
affter normal delete 20--> 30--> 50--> 36--> 90-->
[Event] ✳️  Updated: 45
after update:  20--> 30--> 45--> 50--> 36--> 90-->
```