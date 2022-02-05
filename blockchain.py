from hashlib import sha256
from cli import arguments, start_genesis
from time import time
import json

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


class BlockchainConcept(object):
    file = open('_genesis.json')
    GENESIS = json.load(file)
    file.close()

    difficulty = args.difficulty

    def __init__(self):
        self.current_transactions = []
        self.chain = []

        GENESIS_BLOCK = {
            "_id": "0x1",
            "index": "0x0",
            "data": {
                "transaction": [],
                "transaction_hash": self.GENESIS['parentHash']
            },
        }
        if start_genesis(args.hostname, args.port):
            generate = self.proof_of_work("GENESIS_BLOCK", GENESIS_BLOCK)
            GENESIS_BLOCK['block_hash'] = generate['block_hash']
            GENESIS_BLOCK['nonce'] = generate['nonce']
            self.append_block(generate['content'])

    def proof_of_work(self, previous_hash, data):
        proof_status = False
        nonce = 0

        while (proof_status is False):
            result = self.valid_proof(previous_hash, data, nonce)
            final_hash = result['block_hash']
            proof_status = result['status']
            nonce += 1
        return {"content": result['content'], "block_hash": final_hash, "nonce": hex(nonce)}

    def valid_proof(self, previous_hash, data, nonce):
        content = data
        content['data']['previous_hash'] = previous_hash
        content['nonce'] = hex(nonce)
        content['timestamp'] = time()

        content_hash = f"0x{sha256(json.dumps(content, sort_keys=True).encode()).hexdigest()}"

        # ? Uncomment if you want to mine faster
        print(f'{nonce}: {content_hash}')
        return {"content": content, "block_hash": content_hash, "status": content_hash[:len(self.difficulty)] == self.difficulty}

    def append_block(self, block):
        self.current_transactions = []
        self.chain.append(block)
        with open('_consensus.json', 'w') as outfile:
            json.dump(self.chain, outfile)
        return block

    def add_transaction(self, _from, to, amount, type):
        if type != "miner":
            self.current_transactions.append(
                {"from": _from, "to": to, "amount": amount})
        else:
            self.current_transactions.append(
                {"from": _from, "to": to, "_fee": amount})
        return int(self.last_block["index"], 16) + 1

    @property
    def last_block(self):
        return self.chain[-1]
