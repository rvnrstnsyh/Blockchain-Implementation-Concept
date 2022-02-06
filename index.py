from scripts.blockchain import BlockchainConcept
from flask.json import jsonify
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


@App.route("/", methods=["GET"])
def HOME():
    return API.all_chain()


@App.route("/new-transaction", methods=["POST"])
def TRANSACTION():
    return API.new_transaction()


@App.route('/current-transaction', methods=["GET"])
def GET_TRANSACTION():
    return API.get_transaction()


@App.route("/mine", methods=["GET"])
def MINE():
    return API.block_mine()


@App.route('/verify-block', methods=["POST"])
def VERIFY_BLOCK():
    return API.verify_block()


if __name__ == "__main__":
    App.run(host=args.hostname, port=int(args.port))
else:
    print("python index.py -h for help.")
