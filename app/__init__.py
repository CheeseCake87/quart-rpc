from quart import Quart, session, render_template

from quart_rpc.latest import RPC, RPCResponse, RPCAuthSessionKey


def add_numbers(data: list) -> int:
    return RPCResponse.success(
        sum(data)
    )


def create_app():
    app = Quart(__name__)
    app.secret_key = "secret"

    RPC(
        app,
        url_prefix="/rpc",
        # session_auth=RPCAuthSessionKey("logged_in", [True]),
        host_auth=["127.0.0.1:5001"],
        functions={
            "add_numbers": add_numbers
        }
    )

    @app.before_request
    async def before_request():
        if "logged_in" not in session:
            session["logged_in"] = False

    @app.get("/")
    async def index():
        return await render_template("index.html")

    @app.get("/true")
    async def _true():
        session["logged_in"] = True
        return "Session set to true, close tab."

    @app.get("/false")
    async def _false():
        session["logged_in"] = False
        return "Session set to false, close tab."

    return app
