from commands import pass_bread, pass_butter, Item


class FakeReceiver:
  name = 'Birdman'
  collection = []


fake_receiver = FakeReceiver()


def test_pass_bread():
  pass_bread(fake_receiver)

  assert Item.bread in fake_receiver.collection


def test_pass_butter():
  pass_butter(fake_receiver)

  assert Item.butter in fake_receiver.collection
