
##########################################################################
class Chest:
  def __init__(self, item_list):
    self.item_list = item_list

class normalChest(Chest):
  def __init__(self, item_list):
    Chest.__init__(self, item_list)
    self.chest_type = "normal chest"
    self.object_name = "Normal Chest"
    self.key_type = "normal key"

## Golden chest
class goldChest(Chest):
  def __init__(self, item_list): 
    Chest.__init__(self, item_list)
    self.chest_type = "golden chest"
    self.object_name = "golden Chest"
    self.key_type = "golden key"

## Mythical chest
class mythicalChest(Chest):
  def __init__(self, item_list): 
    Chest.__init__(self, item_list)
    self.chest_type = "mythical chest"
    self.object_name = "mythical Chest"
    self.key_type = "mythical key"

##########################################################################
