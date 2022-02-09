from scripts.block_chain import BlockchainConcept
from scripts.merkle_tree import get_merkle_tree
from scripts.unit_testing import Test
from flask.globals import request
from hashlib import sha256, md5
from flask.json import jsonify
from time import sleep

import json
import sys

blockchain = BlockchainConcept()
file = open('json/genesis.json')
GENESIS = json.load(file)
file.close()

class API_Controller(object):
    def __init__(self) -> None:
        pass

# TODO Get all chain ---
    def all_chain():
        response = {"chain": blockchain.chain, "length": len(blockchain.chain)}
        return jsonify(response), 200

# TODO Get all current data's ---
    def get_data():
        return jsonify(blockchain.current_body_data)

# TODO Create a new data list ---
    def new_data():
        body = request.get_json()
        body['_id'] = md5(json.dumps(request.get_json(), sort_keys=True).encode()).hexdigest()
        body['merkle_leaf'] = f'0x{sha256(json.dumps(request.get_json(), sort_keys=True).encode()).hexdigest()}'

        block_height = blockchain.add_body_data(body=body)
        response = {"message": f"data is successfully listed, in block {hex(block_height)}."}
        return jsonify(response), 201

# TODO Start mining to register data's into the blockchain ---
    def block_mine():
        if blockchain.current_body_data:
            last_block = blockchain.last_block
            new_block = {
                "header": {"height": hex(int(last_block['header']['height'], 16) + 1)},
                "body": {
                    "number_of_data": len(blockchain.current_body_data),
                    "data": blockchain.current_body_data
                }
            }
            arr = []
            for i in range(len(blockchain.current_body_data)):
                arr.append(blockchain.current_body_data[i]['merkle_leaf'])

            new_block['header']['merkle_root'] = get_merkle_tree(hashes=arr)
            new_block['header']['size'] = hex(sys.getsizeof(new_block) * len(blockchain.current_body_data))
            new_block['header']['difficulty'] = len(GENESIS['difficulty'])

            generate = blockchain.proof_of_work(previous_hash=last_block['header']['block_hash'], block=new_block)
            new_block['header']['block_hash'] = generate['block_hash']
            new_block['header']['nonce'] = generate['nonce']

            sleep(0.5)

            blockchain.append_block(block=generate['content'])
            return jsonify({
                "_message": f"Hashed successfully, block has entered the blockchain network.",
                "block_hash": last_block['header']['block_hash'],
                "previous_hash": last_block['header']['previous_hash']
            }), 200
        else:
            return jsonify({"message": "No data's to process"}), 200

# TODO Looping one by one and verifying each hash block in the chain ---
    def verify_chain():
        unit_test = Test()
        result = unit_test.valid_chain(chain=blockchain.chain)
        if result['status']:
            return jsonify(result), 200
        return jsonify(result), 401

# TODO Verify single block_hash with previous_hash + block_data ---
    def verify_block():
        body = request.get_json()
        test_block = body['block']
        unit_test = Test()

        result = unit_test.Validate(block=test_block)
        if result['status']:
            return jsonify(result), 200
        return jsonify(result), 401
