import sys

import anyio

import os

async def main():
    print("failed")
    archi1=open("datos.txt","w") 
    archi1.write("failed") 
    archi1.close()
    # raise Exception("failed")
    return 1

anyio.run(main)
