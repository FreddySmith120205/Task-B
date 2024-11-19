def restock_inventory(available_items, inventory_records, current_day):
    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the stock/restock for a given day.
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


The function will also update the inventory_records (For restocking) for a  given current day. It will also return "available_items".
    '''

    if current_day % 7 == 0:
        restocked_units = 2000 - available_items         #Restocks the difference between max items (2000) and the current amount of items (available_items)
        available_items += restocked_units         #Updates available items
        inventory_records.append([current_day, 0, restocked_units, available_items])

    elif current_day == 0:     #if current day = 0, function returns restocked units
        restocked_units = available_items       #restocked_units is set to available_items
        inventory_records.append([current_day, 0, restocked_units, available_items])        #edits the inventory_records with restocked units
    
    else:
        pass
        



    #returns available items
    return available_items
