from hashlib import sha256
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


class Test(object):
    file = open('scripts/_genesis.json')
    GENESIS = json.load(file)
    file.close()

    def valid_proof(self, block_test):
        try:
            block_content = {
                "_id": block_test['_id'],
                "block_hash": block_test['block_hash'],
                "data": block_test['data'],
                "index": block_test['index'],
                "nonce": hex(int(block_test['nonce'], 16) - 1),
                "timestamp": block_test['timestamp']
            }

            del block_content['block_hash']
            content_hash = f"0x{sha256(json.dumps(block_content, sort_keys=True).encode()).hexdigest()}"

            proof_of_work = content_hash[:len(self.GENESIS['difficulty'])]
            hash_match = self.GENESIS['difficulty'] and content_hash == block_test['block_hash']
            final_result = proof_of_work and hash_match

            if final_result:
                return {
                    "message": "Block valid and correct.",
                    "nonce": int(block_test['nonce'], 16),
                    "status": final_result,
                    "block_hash": content_hash,
                    "previous_hash": block_test['data']['previous_hash'],
                }
            return {
                "message": f"Block does not match and is invalid, please make sure to enter the data block correctly. If possible the chain is broken at block {int(block_test['index'], 16)} with ID {int(block_test['_id'], 16)}.",
                "nonce": int(block_test['nonce'], 16),
                "status": final_result,
                "block_hash": content_hash,
                "previous_hash": block_test['data']['previous_hash'],
            }

        except Exception as error:
            return {
                "status": False,
                "message": f'Block requires a {error} value, assign the key {error} to the request body.'
            }

    def Validate(self, block):
        sample_block = {
            "_id": "0x1",
            "block_hash": "0x000005d2b438f23a7d13f8f41572bf7c25bf01033e3b059e755b377126389d24",
            "data": {
                "previous_hash": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "signature": [
                    {
                        "_type": "GENESIS_BLOCK",
                        "block_core": {
                            "author": "rvnrstnsyh",
                            "email": "re@rvnrstnsyh.dev",
                            "home": "https://rvnrstnsyh.dev"
                        }
                    }
                ],
                "signature_hash": "0x0000000000000000000000000000000000000000000000000000000000000000"
            },
            "index": "0x0",
            "nonce": "0x1ac42e",
            "timestamp": "0x17ecfe04f35"
        }

        return self.valid_proof(block)
