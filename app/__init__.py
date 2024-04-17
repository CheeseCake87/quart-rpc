from quart import Quart

from quart_rpc.latest import RPC, RPCResponse


def add_numbers(data: list) -> int:
    return RPCResponse.success(
        sum(data)
    )


def create_app():
    app = Quart(__name__)
    RPC(
        app,
        url_prefix="/rpc",
        functions={
            "add_numbers": add_numbers
        }
    )

    return app
