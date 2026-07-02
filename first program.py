def backpack_adventure():
    # 1. You start your adventure with an empty backpack.
    backpack = []
    print(f"Starting backpack: {backpack}")
    # 1. You found two items a torch and rope add them to your backpack
    backpack.append('rope')

    backpack.append('torch')

    print(f"After finding items: {backpack}")  

    # 2. You find a rare "gold_key", and you want to keep it safe at the very front of your backpack (index 0).
    backpack.insert(0,"gold key")

    print(f"After finding key: {backpack}")  

    # 3. You find a small pouch with extra supplies: ["rations", "water"]
    pouch = ["rations", "water"]
    backpack.extend(pouch)

    print(f"After merging pouch: {backpack}")  # Should show: ['gold_key', 'rope', 'torch', 'rations', 'water']

    # 4. A monkey steals the LAST item in your backpack!
    stolen_item= backpack.pop()
    
    print(f"The monkey stole: {stolen_item}")  # Should show: water
    print(f"Backpack now: {backpack}")

    # 5. You decide you don't need the "rope" anymore and want to remove it by name.
    backpack.remove('rope')
    print(f"After dropping rope: {backpack}") 

    # 6. You want to organize your backpack alphabetically so its neat.

    backpack.sort()
    print(f"Sorted backpack: {backpack}")  # Should show: ['gold_key', 'rations', 'torch']
    # 7. check how many items are left.
    item_count = len(backpack)
    print(f"You finished the adventure with {item_count} items!")

backpack_adventure()