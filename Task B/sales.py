import random

def daily_sales(available_items, inventory_records, current_day):
    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the sales for a given day.
---------------
Function Input:
---------------
available_items: (integer) Available Tshirts from the previous day.
inventory_records: (List) A list of inventory records until the previous day. Each row contains (day, sales, restocked items, available items)
current_day: (integer) Day number which you want to add as the current day. 

----------------
Function Output:
----------------
available_items:(integer) This function returns this integer which updates the available items at the current day.

The function will also update the inventory_records (For restocking) for a  given current day. 

    '''

    
    
    if current_day % 7 == 0:        #On restock days, the if statement passes and the function does nothing
        if current_day == 0:
            pass
    else:
        sold_units = (random.randint(0, 200))       #Simulates sales with random number 1 - 200
        available_items -= sold_units       #Updates available items so that it takes into account the items sold
        inventory_records.append([current_day, sold_units, 0, available_items])         #Updates inventory records


    return available_items      #Returns the available items