from hashlib import sha256
from blockchain import BlockchainConcept
from flask import Flask
from flask.globals import request
from flask.json import jsonify
from cli import arguments
from validblock import Test
import secrets

'''
|--------------------------------------------------------------------------
| Blockchain Concept Copyright © 2021 rvnrstnsyh All Rights Reserved
|--------------------------------------------------------------------------
|
| Author    : rvnrstnsyh
| Website   : https://rvnrstnsyh.dev
| Github    : https://github.com/rvnrstnsyh
|
'''
args = arguments()

App = Flask(__name__)
node_identifier = f"0x{secrets.token_hex(20)}"
blockchain = BlockchainConcept()


@App.route("/", methods=["GET"])
def all_chain():
    response = {"chain": blockchain.chain, "length": len(blockchain.chain)}
    return jsonify(response), 200


@App.route("/new-transaction", methods=["POST"])
def new_transaction():
    body = request.get_json()
    required_fields = ["from", "to", "amount"]

    if not all(k in body for k in required_fields):
        return ("Missing fields", 401)
    for i in range(len(blockchain.current_transactions)):
        if body['from'] == blockchain.current_transactions[i]['from']:
            return ("Your previous transaction is still pending, please wait for it to complete.", 403)

    index = blockchain.add_transaction(
        body['from'], body['to'], body['amount'], type="consumer")
    response = {"message": f"Transaction successful. Block {hex(index)}"}
    return jsonify(response), 201


@App.route('/current-transaction', methods=["GET"])
def get_transaction():
    return jsonify(blockchain.current_transactions)


@App.route("/mine", methods=["GET"])
def block_mining():
    if blockchain.current_transactions:
        _fee = 0.5 * len(blockchain.current_transactions)
        blockchain.add_transaction(
            _from=blockchain.current_transactions[0]['from'], to=node_identifier, amount=_fee, type="miner")

        last_block = blockchain.last_block
        new_block = {
            "_id": hex(int(last_block['_id'], 16) + 1),
            "index": hex(int(last_block['index'], 16) + 1),
            "data": {"transaction": blockchain.current_transactions, "transaction_hash": f"0x{sha256(f'{blockchain.current_transactions}'.encode()).hexdigest()}"},
        }
        new_block['data']['transaction_hash'] = f"0x{sha256(f'{blockchain.current_transactions}'.encode()).hexdigest()}"

        generate = blockchain.proof_of_work(
            previous_hash=last_block['block_hash'], data=new_block)

        new_block['block_hash'] = generate['block_hash']
        new_block['nonce'] = generate['nonce']

        blockchain.append_block(generate['content'])
        return jsonify({
            "_message": f"Hashed successfully and the block has entered the blockchain network, congratulations you are rewarded with {_fee} coins.",
            "block_hash": last_block['block_hash'],
            "previous_hash": last_block['data']['previous_hash']
        }), 200
    else:
        return jsonify({"message": "No transactions in progress"}), 200


@App.route('/verify-block', methods=["POST"])
def verify_block():
    body = request.get_json()
    test_block = body['block']
    unit_test = Test()

    return jsonify(unit_test.valid_proof(test_block)), 200


if __name__ == "__main__":
    App.run(host=args.hostname, port=int(args.port))
else:
    print("python index.py -h for help.")
