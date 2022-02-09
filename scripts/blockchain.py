from hashlib import sha256
from cli import arguments, start_genesis
import datetime as _dt
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
args = arguments()


class BlockchainConcept(object):
    file = open('scripts/_genesis.json')
    GENESIS = json.load(file)
    file.close()

    difficulty = args.difficulty

    def __init__(self):
        self.current_body_data = []
        self.chain = []

        GENESIS_BLOCK = {
            "header": {
                "height": "0x0",
                "size": hex(232),
                "merkle_root": "0x285b57d81686ccfe2b5d46f94fd7c655720e79bdb28fe399ef87fdd05d2aa8c6",
                "difficulty": len(self.GENESIS['difficulty'])
            },
            "body": {
                "data": {
                    "_id": "5ff99958d5df522a8542111293bde6f7",
                    "signature": [{
                        "_type": "GENESIS_BLOCK",
                        "block_core": {
                            "author": "rvnrstnsyh",
                            "email": "re@rvnrstnsyh.dev",
                            "home": "https://rvnrstnsyh.dev",
                        }
                    }],
                    "merkle_leaf": self.GENESIS['parentHash']
                }
            },
        }

        # start_genesis(args.hostname, args.port)
        generate = self.proof_of_work(self.GENESIS['parentHash'], GENESIS_BLOCK)
        GENESIS_BLOCK['header']['block_hash'] = generate['block_hash']
        GENESIS_BLOCK['header']['nonce'] = generate['nonce']
        self.append_block(generate['content'])

    def proof_of_work(self, previous_hash, block):
        proof_status = False
        nonce = 0

        while (proof_status is False):
            result = self.valid_proof(previous_hash, block, nonce)
            final_hash = result['block_hash']
            proof_status = result['status']
            nonce += 1
        return {"content": result['content'], "block_hash": final_hash, "nonce": hex(nonce)}

    def valid_proof(self, previous_hash, block, nonce):
        content = block
        content['header']['previous_hash'] = previous_hash
        content['header']['nonce'] = hex(nonce)
        content['header']['time'] = str(_dt.datetime.now())

        content_hash = f"0x{sha256(json.dumps(content, sort_keys=True).encode()).hexdigest()}"

        # ? Uncomment if you want to mine faster
        # print(f'{nonce}: {content_hash[:len(self.GENESIS["difficulty"])]}')
        return {"content": content, "block_hash": content_hash, "status": content_hash[:len(self.difficulty)] == self.difficulty}

    def append_block(self, block):
        self.current_body_data = []
        self.chain.append(block)
        with open('scripts/_consensus.json', 'w') as outfile:
            json.dump(self.chain, outfile)
        return block

    def add_body_data(self, body):
        self.current_body_data.append(body)
        return int(self.last_block['header']["height"], 16) + 1

    @property
    def last_block(self):
        return self.chain[-1]
