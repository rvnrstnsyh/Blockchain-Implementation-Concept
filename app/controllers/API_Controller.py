from scripts.blockchain import BlockchainConcept
from scripts.unit_testing import Test
from flask.globals import request
from flask.json import jsonify
from hashlib import sha256

import secrets

blockchain = BlockchainConcept()
node_identifier = f"0x{secrets.token_hex(20)}"


class API_Controller(object):
    def __init__(self) -> None:
        pass

# TODO Get all chain ---
    def all_chain():
        response = {"chain": blockchain.chain, "length": len(blockchain.chain)}
        return jsonify(response), 200

# TODO Get all current transactions ---
    def get_transaction():
        return jsonify(blockchain.current_transactions)

# TODO Create a new transaction list ---
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

# TODO Start mining to register transactions into the blockchain ---
    def block_mine():
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
