from _discord import *
from utils import *
from Log import *
import websockets
import asyncio
from functools import wraps
import tls_client

platform = "app"
session = tls_client.Session(client_identifier="chrome_120", random_tls_extension_order=True)
session.headers = { "Authorization": private_config.get("token")}

commands = {}
def command(name=None, aliases=None):
    if aliases is None:
        aliases = []
    def decorator(func):
        command_name = name or func.__name__
        commands[command_name] = func
        
        for alias in aliases:
            commands[alias] = func

        @wraps(func)
        async def wrapper(ws, ctx, *args):
            return await func(ws, ctx, *args)
        
        return wrapper
    return decorator

async def send_ws_req(ws, req):
    await ws.send(json.dumps(req))






async def on_ready(ws, data, *args):
    Clear()
    Title("Client")
    Menu(get_state("connect"), acc=f"{data['user']['username']}#{data['user']['discriminator']}", prefix=config.get('prefix'))
    Log().info("Selfbot connected")

async def on_message(ws, message):
    content = message.get("content", "")

    if content.startswith(prefix()):
        content = content[len(prefix()):]
        command, *args = content.split()
        
        if command in commands:
            message = Message(session, message)
            channel = await Serenitty(session).get_channel(message.channel_id)
            guild = await Serenitty(session).get_guild(channel.guild_id)
            author = message.author
            ctx = Context(session, command, args, channel, guild, message, author)
            await commands[command](ws, ctx, *args)
            Log().info(f"Executed command: {command}")
        else:
            Log().err("Command not found")


@command(name="ping", aliases=["p"])
async def ping(ws, ctx, *args):
    print("Ping")

@command(name="echo", aliases=["say", "repeat"])
async def echo(ws, ctx, *text):
    await ctx.send(text)
























async def recv_json_res(ws):
    res = await ws.recv()
    if res:
        return json.loads(res)

async def heartbeat(interval, ws):
    Log().dbg("Heartbeat begin")
    while True:
        await asyncio.sleep(interval)
        heartbeatJSON = { "op": 1, "d": "null" }
        await send_ws_req(ws, heartbeatJSON)
        Log().dbg("Heartbeat sent")

async def handle_events(ws, event):
    data = event['d']
    op = event["op"]
    event_type = event["t"]

    if op == 10:
        heartbeat_interval = data['heartbeat_interval'] / 1000
        asyncio.create_task(heartbeat(heartbeat_interval, ws))

        dic = {
            "pc": ["linux", "chrome", "pc"],
            "app": ["linux", "Discord Client", "Discord"],
            "mobile": ["iOS", "Discord iOS", "Discord iOS"]
        }
        identify_payload = {
            "op": 2,
            "d": {
                "token": private_config.get('token'),
                "properties": {
                    "$os": dic[platform][0],
                    "$browser": dic[platform][1],
                    "$device": dic[platform][2]
                }
            }
        }
        await send_ws_req(ws, identify_payload)
        Log().info("Token Authentificated")
    elif op == 11:
        Log().dbg("Heartbeat received")
    
    elif event_type == "READY":
        await on_ready(ws, data)
    elif event_type == "MESSAGE_CREATE":
        await on_message(ws, data)


async def main():
    Clear()
    Title("Connecting")
    Menu(get_state("connecting"))
    res = Serenitty(session).check_token()
    if not res['valid']:
        SleepLog().err(res['message'])
        os._exit(0)
    try:
        async with websockets.connect(DISCORD_GATEWAY_URL) as ws:
            Log().dbg("Websocket connection opened")
            while True:
                try:
                    event = await recv_json_res(ws)
                    await handle_events(ws, event)
                except Exception as e:
                    print(e)
                    pass
    except TimeoutError:
        SleepLog(5).err("Connection lost, check your internet connection.")
        os._exit(0)

asyncio.run(main())