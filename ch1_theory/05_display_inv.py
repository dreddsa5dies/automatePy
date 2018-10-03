# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'gold coin', 'ruby']

def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + '\t' + k)
        item_total += v
    print("Total number of items: " + str(item_total))

def addToInv(inv, items):
    for k in items:
        inv.setdefault(k, 0)
        inv[k] = inv[k] + 1
        
addToInv(stuff, dragonLoot)
display_inventory(stuff)