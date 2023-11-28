import sys

import anyio

import os

async def main():
    print("failed")
    raise Exception("failed")
    return 1

anyio.run(main)
