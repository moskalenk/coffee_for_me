### About:
You can see a smart coffee machine that can sell coffee with additional ingredients or print a common info about all sellers. Depends on you role.
 
There are 2 roles that we can use:
```
Roles:
* salesman;
* manager.
```
We check that your name really are for necessary role in our DB.
```
Default names:
* for salesman role - Alex | Bob | Liza;
* for manager role - Jeff | Scott | Garry.
```

* For 'salesman' role we have some additional questions about his order and after we save the last order data in file(if salesman want) - 'bill.txt'(in 'coffee_for_me' dir);
* For 'manager' role we just give common info about all sellers.

### Installation:
1. install python3.6+ (download [here](https://www.python.org/downloads/release/python-367/));
2. `pip install -r requirements.txt`;
3. go to `.../coffee_for_me/db` and do `python db_creation.py` for create necessary database;
4. run main script. Go to `coffee_for_me` dir and as example do `python start_script.py salesman Liza`

### Usage and start script Option:
You can see detail in help do 'python start_script.py -h'

###If you have some issues with launching script(may it helps):
  * don't forget about adding `.../coffee_for_me` path in PYTHONPATH var(if need);
  * launch script from console(not with IDE's UI)