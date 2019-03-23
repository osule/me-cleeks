import click

from commands import pass_butter, pass_bread


class Receiver:
  def __init__(self, name):
    self.name = name
    self.collection = []


class ReceiverCommand(click.Command):
  def invoke(self, ctx):
    return ctx.invoke(
        self.callback, Receiver('Rick'), **ctx.params)


def cli():

  params = [
      click.Option(
          param_decls=('--receiver',),
          expose_value=False,
          hidden=True,
          type=Receiver),
  ]

  command_group = click.Group()

  command_group.add_command(
      ReceiverCommand('pass_bread', callback=pass_butter, params=params)
  )

  command_group.add_command(
      ReceiverCommand('pass_butter', callback=pass_bread, params=params)
  )

  command_group()


if __name__ == '__main__':
  cli()
