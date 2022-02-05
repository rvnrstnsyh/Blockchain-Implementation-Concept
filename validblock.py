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
        content = {
            "_id": block_test['_id'],
            "index": block_test['index'],
            "data": {
                "transaction": block_test['data']['transaction'],
                "transaction_hash": block_test['data']['transaction_hash'],
                "previous_hash": block_test['data']['previous_hash']
            },
            "nonce": hex(int(block_test['nonce'], 16) - 1),
            "timestamp": block_test['timestamp']
        }
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
        "_id": "0x3",
        "index": "0x2",
        "data": {
            "transaction": [
                {
                    "from": "0x4c4b18A646da4f8a3e402139b13d3EB73c43515c",
                    "to": "0x71faFcc3997c14025fdC70a1EB5a9E7b6888F64d",
                    "amount": 2.5
                },
                {
                    "from": "0x4c4b18A646da4f8a3e402139b13d3EB73c43515c",
                    "to": "0xa323ae33c6af839a9bb66d059cd83359c9a1ea77",
                    "_fee": 0.5
                }
            ],
            "transaction_hash": "0x8a9132b8da9ff4fb473028ab4c6c6b69431b5bb00e35020520baa8491c557b51",
            "previous_hash": "0x1007a36eb4c80fcab2b44bee718dcc13b988c2bb0257fb203cc3e2f5d8ee98e4"
        },
        "nonce": "0xbc1",
        "timestamp": 1644088686.7929134,
        "block_hash": "0x1007d16f2b6c239ef20d156fefe09325401cafb3ae06ba6704a81090f94604f0"
    }
    return unit_testing.valid_proof(test_block)


print(Validate())
