from typing import List


class ShoppingCart:
    def __init__ (self,max_items:int) -> None:
        self.items : List[str] = []
        self.max_Size = max_items

    def add(self, item: str):
        if self.size() == self.max_Size:
            raise OverflowError("cannot add more items")
        self.items.append(item)

    def size(self) -> int:
        return len(self.items)
    
    def get_items (self) -> List[str]:
        return self.items
    
    def get_total_price (self, price_map) :
        total_price = 0
        for item in self.items:
            total_price += price_map.get(item)
        return total_price
