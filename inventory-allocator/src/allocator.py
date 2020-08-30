
def allocate_inventory(shipment: dict, warehouses: list) -> list:
    """Finds cheapest shipment of items from warehouses
    Prioritizes less warehouses over cheaper warehouses"""

    high_warehouse_score = 0.0       # percentage of shipment fulfilled
    high_warehouse_index = 0         # index of highest score warehouse
    high_warehouse_shipment = None   # items fulfilled in shipment

    # find either a warehouse that can ship all items 
    # or the warehouse that can ship the most items
    for warehouse_index in range(len(warehouses)):
        warehouse_shipment, warehouse_score = contains_shipment(shipment, warehouses[warehouse_index])
        if warehouse_score == 1.0: # if warehouse contains all items
            return [{"name": warehouses[warehouse_index]["name"], "inventory": shipment}]
        elif warehouse_score > high_warehouse_score:
            high_warehouse_index = warehouse_index
            high_warehouse_score = warehouse_score
            high_warehouse_shipment = warehouse_shipment
    
    if high_warehouse_score is 0.0: # items are not in warehouses at all if highest score is 0
        return []
    
    high_warehouse_name = warehouses[high_warehouse_index]["name"] # record warehouse name before removing
    del warehouses[high_warehouse_index]                           # remove high warehouse from list

    # find another warehouse to complete the order or the next best warehouse to ship from
    next_warehouse = allocate_inventory({key: shipment[key] - high_warehouse_shipment[key] for key in shipment.keys()}, warehouses)

    if next_warehouse == []: # if empty list is ever returned, shipment could not be fulfilled
        return []
    else:
        return [{"name": high_warehouse_name, "inventory": high_warehouse_shipment}] + next_warehouse


def contains_shipment(shipment: dict, warehouse: dict) -> tuple():
    """Checks what percentage of the shipment the warehouse
    can fulfill and returns a value between 0 and 1 along with fulfilled items
    0: contains no items; 1: contains all items"""
    contained = 0.0
    total = 0
    new_shipment = dict()

    for item in shipment:
        total += shipment[item]
        if item in warehouse["inventory"]:
            contained += min(warehouse["inventory"][item], shipment[item])
            new_shipment[item] = min(warehouse["inventory"][item], shipment[item])
        else:
            new_shipment[item] = 0

    return new_shipment, (contained / total)

