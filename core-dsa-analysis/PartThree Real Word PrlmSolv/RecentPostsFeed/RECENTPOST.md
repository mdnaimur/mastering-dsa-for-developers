# Recent Posts Feed

* Maintain the 10 most recent user posts.
* Support constant-time insertion/removal.
* Preserve chronological order.
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
        cd RecentPostsFeed
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
Explaination
Solution need to use DoubleLinkedList where Inseration and Deletion in constant time 

some key code :
for maintain 10 most recent user post.
 * This new 10 will be displyed and other delete from lsit
  ``` python
    def add_post(self, post):
        '''
        if add size > maxSize 
        then preRemove 
        '''
        self.posts.append(post)
        self.size += 1
        if self.size > self.maxsize:
            self.posts.pop_front()
            self.size -= 1
```

**Example:**

``` bash
0:  [Insert = 11] Software Developer Imran2 got promoted  Meta.
1:  [Insert = 10] Umran got promoted at Google .
2:  [Insert = 9]  Farzana just landed in Dubai 🇦🇪
3:  [Insert = 8] Tanvir watched 'The Dark Knight' again! #classic
4:  [Insert = 7] Eid Mubarak from the Rahman family 🌙
5:  [Insert = 6] New baby picture uploaded by Mahi and Sara!
6:  [Insert = 5] Arif completed a 20km ride today #fitness
7:  [Insert = 4] Nafis shared a photo from his study desk #BCSPrep
8:  [Insert = 3]  Alex just posted a food review at Burger King
9:  [Insert = 2] Sarah checked in at Saint Martin's Island
```