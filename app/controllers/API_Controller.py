from scripts.blockchain import BlockchainConcept
from scripts.unit_testing import Test
from flask.globals import request
from hashlib import sha256, md5
from flask.json import jsonify

import json
import sys

blockchain = BlockchainConcept()
file = open('scripts/_genesis.json')
GENESIS = json.load(file)
file.close()

class API_Controller(object):
    def __init__(self) -> None:
        pass

# TODO Get all chain ---
    def all_chain():
        response = {"chain": blockchain.chain, "length": len(blockchain.chain)}
        return jsonify(response), 200

# TODO Get all current transactions ---
    def get_transaction():
        return jsonify(blockchain.current_body_data)

# TODO Create a new transaction list ---
    def new_transaction():
        body = request.get_json()
        body['_id'] = md5(json.dumps(request.get_json(), sort_keys=True).encode()).hexdigest()
        body['merkle_leaf'] = f'0x{sha256(json.dumps(request.get_json(), sort_keys=True).encode()).hexdigest()}'

        block_height = blockchain.add_body_data(body)
        response = {"message": f"Transaction successful. Block {hex(block_height)}"}
        return jsonify(response), 201

# TODO Start mining to register transactions into the blockchain ---
    def block_mine():
        if blockchain.current_body_data:
            last_block = blockchain.last_block
            new_block = {
                "header": {
                    "height": hex(int(last_block['header']['height'], 16) + 1)
                },
                "body": {
                    "data": blockchain.current_body_data
                }
            }
            generate = blockchain.proof_of_work(previous_hash=last_block['header']['block_hash'], block=new_block)

            new_block['header']['block_hash'] = generate['block_hash']
            new_block['header']['size'] = hex(sys.getsizeof(new_block) * len(blockchain.current_body_data))
            new_block['header']['difficulty'] = len(GENESIS['difficulty'])
            new_block['header']['nonce'] = generate['nonce']

            blockchain.append_block(generate['content'])
            return jsonify({
                "_message": f"Hashed successfully and the block has entered the blockchain network.",
                "block_hash": last_block['header']['block_hash'],
                "previous_hash": last_block['header']['previous_hash']
            }), 200
        else:
            return jsonify({"message": "No transactions in progress"}), 200

# TODO Looping one by one and verifying each hash block in the chain ---
    def verify_chain():
        unit_test = Test()
        result = unit_test.valid_chain(blockchain.chain)
        if result['status']:
            return jsonify(result), 200
        return jsonify(result), 401

# TODO Verify single block_hash with previous_hash + block_data ---
    def verify_block():
        body = request.get_json()
        test_block = body['block']
        unit_test = Test()

        result = unit_test.Validate(test_block)
        if result['status']:
            return jsonify(result), 200
        return jsonify(result), 401
