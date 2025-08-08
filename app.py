import chainlit as cl

@cl.on_chat_start
async def main():
    await cl.Message(
        content="Hello World! This is a Chainlit app.",
    ).send()