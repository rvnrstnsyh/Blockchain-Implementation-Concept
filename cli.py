import json
import argparse
import subprocess as sp
from time import sleep
from sys import platform

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

file = open('scripts/_genesis.json')
genesis = json.load(file)
file.close()


def arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-host", "--hostname", dest="hostname", default=genesis['config']['hostname'], help="Server name"
    )
    parser.add_argument(
        "-p", "--port", dest="port", default=genesis['config']['port'], help="Server port"
    )
    parser.add_argument(
        "-d", "--difficulty", dest="difficulty", default=genesis['difficulty'], help="Difficulty"
    )
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
            "Reduce the difficulty if the genesis block creation or mining process takes too long."
            f"\nhostname: {arg.hostname if arg.hostname else genesis['config']['hostname']}",
            f"\nport: {arg.port if arg.port else genesis['config']['port']}",
            f"\nnonce: {arg.difficulty if arg.difficulty else genesis['difficulty']}\n---",
        )

        if 4-i > 1:
            print(
                f'on http://{hostname}:{port} regenerates genesis block in {3-i}s')
        else:
            print(
                f'on http://{hostname}:{port} Looking for the right nonce, please wait...')
        sleep(1)

    return True
