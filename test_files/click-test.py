import click

@click.command()
@click.option("--state", "-s", help='Instance State. Alternatives: Launch|Start|Stop|Restart|Terminate')
def change_state(state):
    print(state)

if __name__ == '__main__':
    change_state()