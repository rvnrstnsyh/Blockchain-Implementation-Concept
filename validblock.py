from hashlib import sha256
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


class Test(object):
    file = open('_genesis.json')
    GENESIS = json.load(file)
    file.close()

    def valid_proof(self, block_test):
        # ? Uncomment this for GENESIS_BLOCK
        content = {
            "_id": block_test['_id'],
            "index": block_test['index'],
            "data": {
                "signature": block_test['data']['signature'],
                "signature_hash": block_test['data']['signature_hash'],
                "previous_hash": block_test['data']['previous_hash']
            },
            "nonce": hex(int(block_test['nonce'], 16) - 1),
            "timestamp": block_test['timestamp']
        }
        # ! OR
        # ? Uncomment this for other block
        # content = {
        #     "_id": block_test['_id'],
        #     "index": block_test['index'],
        #     "data": {
        #         "transaction": block_test['data']['transaction'],
        #         "transaction_hash": block_test['data']['transaction_hash'],
        #         "previous_hash": block_test['data']['previous_hash']
        #     },
        #     "nonce": hex(int(block_test['nonce'], 16) - 1),
        #     "timestamp": block_test['timestamp']
        # }

        content_hash = f"0x{sha256(json.dumps(content, sort_keys=True).encode()).hexdigest()}"
        return {
            "nonce": int(block_test['nonce'], 16),
            "status": content_hash[:len(self.GENESIS['difficulty'])] == self.GENESIS['difficulty'] and content_hash == block_test['block_hash'],
            "block_hash": content_hash,
            "previous_hash": block_test['data']['previous_hash'],
        }


unit_testing = Test()


def Validate():
    test_block = {
        "_id": "0x1",
        "index": "0x0",
        "data": {
            "signature": [{"_type": "GENESIS_BLOCK", "author": "rvnrstnsyh", "email": "re@rvnrstnsyh.dev", "site": "https://rvnrstnsyh.dev"}],
            "signature_hash": "0x0000000000000000000000000000000000000000000000000000000000000000",
            "previous_hash": "0x0000000000000000000000000000000000000000000000000000000000000000"
        },
        "nonce": "0x643a8",
        "timestamp": "0x17eccb5a917",
        "block_hash": "0x000002577da1705ead2c169953a103713664f6b70d7329e23ea2f1be5cb3f685"
    }
    return unit_testing.valid_proof(test_block)


print(Validate())
