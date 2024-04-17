# 📢 Quart-RPC

```bash
pip install quart-rpc
```

---

The Quart implementation of [Flask-RPC](https://github.com/CheeseCake87/flask-rpc)

The typical request/response cycle is as follows:

**Request**

```json
{
  "frpc": 1.0,
  "function": "add_numbers",
  "data": [
    1,
    2,
    3
  ]
}
```

**Response**

```json
{
  "frpc": 1.0,
  "ok": true,
  "message": "Function 'add_numbers' executed successfully",
  "data": 6
}
```

## Usage

[This repo](https://github.com/CheeseCake87/quart-rpc) contains a working example of Quart-RPC.

It also includes an example of using the [JS library](https://github.com/CheeseCake87/flask-rpc-js) that helps
in making requests via fetch to Quart-RPC.

### Simplest example

```python
from quart import Quart

from quart_rpc.latest import RPC, RPCResponse


def add_numbers(data):
    if isinstance(data, list):
        return RPCResponse.success(
            sum(data),
            "Function 'add_numbers' executed successfully"
        )


app = Quart(__name__)
rpc = RPC(app, url_prefix="/rpc")  # or RPC(blueprint, ...)
rpc.functions(
    add_numbers=add_numbers
)
```

or 

```python
...
rpc = RPC(
    app,   # or RPC(blueprint, ...)
    url_prefix="/rpc", 
    functions={
        "add_numbers": add_numbers
    }
)
...
```

`RPC(...)`

Will register a POST route with the app or blueprint that you pass in.

`rpc.functions(...)`

Will register the functions that you pass in to be called remotely.
The argument names used will be the name of the function you will call remotely, for example:

```python
rpc.functions(
    add_numbers=add_numbers,
    subtract=subtract_numbers
)
```

Calling `subtract` remotely will call the `subtract_numbers` function.

A request to the `/rpc` endpoint with the following JSON payload:

```python
import requests
from quart_rpc import RPCRequest

response = requests.post(
    "http://localhost:5000/rpc",
    json=RPCRequest.build(
        function="add_numbers",
        data=[1, 2, 3]
    )
)
```

or, if you're using the [JS library](https://github.com/CheeseCake87/flask-rpc-js):

```js
fetch("/rpc", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: frpc(
        function_ = "add_numbers",
        data = [1, 2, 3]
    )
})
```

Will return:

```json
{
  "frpc": 1.0,
  "ok": true,
  "message": "Function 'add_numbers' executed successfully",
  "data": 6
}
```
