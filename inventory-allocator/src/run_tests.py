import unittest
import allocator

class TestAllocator(unittest.TestCase):
    
    def test_0_warehouse(self):
        self.assertEqual(allocator.allocate_inventory({"apple": 1}, []), [])

    def test_1_warehouse(self):
        self.assertEqual(allocator.allocate_inventory({"apple": 1}, [{"name": "owd", "inventory": {"apple": 1}}]),
                        [{"name": "owd", "inventory": {"apple": 1}}])

    def test_2_warehouse(self):
        self.assertEqual(allocator.allocate_inventory({"apple": 10}, [{"name" : "owd", "inventory": {"apple": 5}}, {"name": "dm", "inventory": {"apple": 5}}]),
                        [{"name" : "owd", "inventory": {"apple": 5}}, {"name": "dm", "inventory": {"apple": 5}}])

    def test_not_enough_inventory(self):
        self.assertEqual(allocator.allocate_inventory({"apple": 1}, [{"name": "owd", "inventory": {"apple": 0}}]), [])

    def test_not_enough_inventory_2(self):
        self.assertEqual(allocator.allocate_inventory({"apple": 2}, [{"name": "owd", "inventory": {"apple": 1}}]), [])

    def test_not_enough_inventory_3(self):
        self.assertEqual(allocator.allocate_inventory({"apple": 2}, [{"name": "owd", "inventory": {"apple": 1}}, {"name": "dm", "inventory": {"banana": 1}}]), [])

    def test_single_shipment_over_cheapest(self):
        self.assertEqual(allocator.allocate_inventory({"apple": 2}, [{"name": "owd", "inventory": {"apple": 1}}, {"name": "dm", "inventory": {"apple": 1}}, {"name": "ad", "inventory": {"apple": 2}}]),
                        [{"name": "ad", "inventory": {"apple": 2}}])

    def test_multiple_item_shipment_from_single_item_warehouses(self):
        self.assertEqual(allocator.allocate_inventory({"apple": 5, "banana": 5}, [{"name" : "owd", "inventory": {"apple": 5}}, {"name": "dm", "inventory": {"banana": 5}}]),
                        [{"name" : "owd", "inventory": {"apple": 5, "banana": 0}}, {"name": "dm", "inventory": {"apple": 0, "banana": 5}}])

    def test_multiple_item_shipment_from_multiple_item_warehouses(self):
        self.assertEqual(allocator.allocate_inventory({"apple": 5, "banana": 5}, [{"name" : "owd", "inventory": {"apple": 2, "banana": 3}}, {"name": "dm", "inventory": {"apple": 3, "banana": 2}}]),
                        [{"name" : "owd", "inventory": {"apple": 2, "banana": 3}}, {"name": "dm", "inventory": {"apple": 3, "banana": 2}}])
        

unittest.main()
        