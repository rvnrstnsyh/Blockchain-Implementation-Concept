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

    def __init__(self) -> None:
        pass

    def re_valid_proof(self, block_test):
        try:
            block_content = {
                "header": {
                    "height": block_test['header']['height'],
                    "block_hash": block_test['header']['block_hash'],
                    "previous_hash": block_test['header']['previous_hash'],
                    "merkle_root": block_test['header']['merkle_root'],
                    "size": block_test['header']['size'],
                    "nonce": hex(int(block_test['header']['nonce'], 16) - 1),
                    "difficulty": block_test['header']['difficulty'],
                    "time": block_test['header']['time'],
                },
                "body": block_test['body'],
            }

            del block_content['header']['block_hash']
            content_hash = f"0x{sha256(json.dumps(block_content, sort_keys=True).encode()).hexdigest()}"
            difficulty = self.GENESIS['difficulty']

            proof_of_work = content_hash[:len(difficulty)] == difficulty
            hash_match = content_hash == block_test['header']['block_hash']
            final_result = proof_of_work and hash_match

            if final_result:
                return {
                    "message": "Block valid and correct.",
                    "nonce": int(block_test['header']['nonce'], 16),
                    "status": final_result,
                    "sha256(previous_hash + this_block)": content_hash,
                    "previous_hash": block_test['header']['previous_hash'],
                }
            return {
                "message": f"Block does not match and is invalid, please make sure to enter the data block correctly. If possible the chain is broken at block {int(block_test['header']['height'], 16)}.",
                "nonce": int(block_test['header']['nonce'], 16),
                "status": final_result,
                "sha256(previous_hash + this_block)": content_hash,
                "previous_hash": block_test['header']['previous_hash'],
            }

        except Exception as error:
            return {
                "status": False,
                "message": f'Block requires a {error} value, assign the key {error} to the request body.'
            }

    def valid_chain(self, chain):
        last_block = chain[0]
        current_index = 1
        total_block = 1

        while current_index < len(chain):
            block = chain[current_index]
            if block['header']['previous_hash'] != self.re_valid_proof(last_block)['sha256(previous_hash + this_block)'] and block['block_hash'][:len(self.GENESIS['difficulty'])] == self.GENESIS['difficulty']:
                return {
                    "status": False,
                    "message": f"Block does not match and is invalid. If possible the chain is broken at block {int(block['header']['height'], 16)}."
                }
            last_block = block
            current_index += 1
            total_block += 1
        return {
            "status": True,
            "message": f"There are a total of {total_block} blocks in the chain and all hashes are validly verified, blockchain is secure."
        }

    def Validate(self, block):
        return self.re_valid_proof(block)
