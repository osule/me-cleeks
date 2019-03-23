import enum


class Item(enum.Enum):
  butter = 'BUTTER'
  bread = 'BREAD'


def pass_butter(receiver):
  receiver.collection.append(Item.butter)


def pass_bread(receiver):
  receiver.collection.append(Item.bread)
