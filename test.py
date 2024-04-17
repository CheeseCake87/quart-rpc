import click
import requests

from quart_rpc.latest import RPCRequest


@click.group()
def run():
    pass


@run.command("add-numbers")
def add_numbers():
    response = requests.post(
        "http://127.0.0.1:5000/rpc",
        json=RPCRequest.build(
            function="add_numbers",
            data=[1, 2, 3]
        )
    )
    print(response.json())


if __name__ == '__main__':
    run()
