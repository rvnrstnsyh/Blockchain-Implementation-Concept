from sys import platform
from time import sleep
import subprocess as sp
import argparse
import json

'''
|--------------------------------------------------------------------------
| Blockchain Concept Copyright © 2022 rvnrstnsyh All Rights Reserved
|--------------------------------------------------------------------------
|
| Author    : rvnrstnsyh
| Website   : https://rvnrstnsyh.dev
| Github    : https://github.com/rvnrstnsyh
|
'''

file = open('json/genesis.json')
genesis = json.load(file)
file.close()


def arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("-host", "--hostname", dest="hostname", default=genesis['config']['hostname'], help="Server name")
    parser.add_argument("-p", "--port", dest="port", default=genesis['config']['port'], help="Server port")
    parser.add_argument("-d", "--difficulty", dest="difficulty", default=genesis['difficulty'], help="Difficulty")
    args = parser.parse_args()
    
    return args


def start_genesis(hostname, port):
    arg = arguments()
    for i in range(4):
        if platform == "linux" or platform == "linux2":
            # linux
            sp.call('clear', shell=True)
        elif platform == "darwin" or platform == "win32":
            # OS X or Windows
            sp.call('cls', shell=True)

        print(
            "Reduce the difficulty/nonce if the genesis block generation or mining process takes too long."
            f"\nhostname: {arg.hostname if arg.hostname else genesis['config']['hostname']}",
            f"\nport: {arg.port if arg.port else genesis['config']['port']}",
            f"\nparent hash: {genesis['parentHash']}",
            f"\ndifficulty: {len(arg.difficulty) if arg.difficulty else len(genesis['difficulty'])}",
            f"\nnonce: {arg.difficulty if arg.difficulty else genesis['difficulty']}\n---",
        )

        if 4-i > 1:
            print(f'on http://{hostname}:{port} regenerates genesis block in {3-i}s')
        else:
            print(f'on http://{hostname}:{port} looking for the right nonce, please wait...')
            break
        sleep(1)
