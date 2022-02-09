from scripts.block_chain import BlockchainConcept
from cli import arguments
from flask import Flask

# ? Controllers
from app.controllers.API_Controller import API_Controller as API

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
args = arguments()

App = Flask(__name__)
blockchain = BlockchainConcept()


# TODO Get all chain ---
@App.route("/", methods=["GET"])
def HOME():
    return API.all_chain()


# TODO Get all current data's ---
@App.route('/current_data', methods=["GET"])
def GET_DATA():
    return API.get_data()


# TODO Create a new data list ---
@App.route("/new_data", methods=["POST"])
def DATA():
    return API.new_data()


# TODO Start mining to register data's into the blockchain ---
@App.route("/mine", methods=["GET"])
def MINE():
    return API.block_mine()


# TODO Looping one by one and verifying each hash block in the chain ---
@App.route('/verify_chain', methods=["GET"])
def VERIFY_CHAIN():
    return API.verify_chain()


# TODO Verify single block_hash with previous_hash + block_data ---
@App.route('/verify_block', methods=["POST"])
def VERIFY_BLOCK():
    return API.verify_block()


if __name__ == "__main__":
    App.run(host=args.hostname, port=int(args.port))
else:
    print("python index.py -h for help.")
