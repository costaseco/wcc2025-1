import data

def get_Items():
    return data.get_Items()

def add_Item(item):
    data.add_Item(item)

def complete_item(id):
    data.delete_item(id)
