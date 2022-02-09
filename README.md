<a href="https://www.blockchain.com"><img alt="Blockchain" src="https://i.postimg.cc/W12crkm1/pngkit-technology-png-344121.png"></a>

A blockchain, or block chain as it was originally spelled, is an ever-expanding record, called blocks, that are linked and secured using cryptographic techniques. Each block typically contains a cryptographic hash of the previous block, a timestamp, and transaction data. [Read more](https://id.wikipedia.org/wiki/Rantai_blok)

## How to use
To run this script you just need to install python version 3, pip, flask and requests. I myself use python version 3.10.x to make this blockchain script. I assume you have installed all the dependencies needed to run this script.

after everything is installed:
```
~# python3 index.py
```
You can also give flags like hostname, port, and nonce/proof of work difficulty:
```
~# python3 index.py -h 127.0.0.1 -p 3000 -d 0x00000
```

## Valid block
Examples of valid and correct block formats include _id, block hash, data, index, nonce and timestamp. You can validate the block format in the API I have created or you can also use the 'unit_testing.py' file.

### GENESIS_BLOCK
This is an example of a genesis block. If you want to hash or store data whatever data it is, You can store in key 'data' object. Also can pass data with array type, string, integer, float, etc.
```json
{
    "header": {
        "height": "0x0",
        "size": "0xe8",
        "merkle_root": "0x285b57d81686ccfe2b5d46f94fd7c655720e79bdb28fe399ef87fdd05d2aa8c6",
        "difficulty": 7,
        "previous_hash": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "nonce": "0x531ea",
        "time": "2022-02-09 20:36:33.851480",
        "block_hash": "0x00000f05122fc7f3faddfd94fe5a7ee7e4f95d9ae99b5b76991cd72b4c6c6b6c"
    },
    "body": {
        "data": {
            "_id": "5ff99958d5df522a8542111293bde6f7",
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
            "merkle_leaf": "0x0000000000000000000000000000000000000000000000000000000000000000"
        }
    }
}
```

### Other block
This is an example of a block that stores simple transaction data.
```json
{
    "header": {
        "height": "0x2",
        "previous_hash": "0x000004ab099cee88821c621ba5c46db9143b16874521f519f1104c1a2dd03b5f",
        "nonce": "0x129f5",
        "time": "2022-02-09 20:42:09.255626",
        "block_hash": "0x000004d2dfa77ae2151c57792c04db5eba1e2abc1339eddb3bd37552f1f7ec13",
        "size": "0x1d0",
        "difficulty": 7
    },
    "body": {
        "data": [
            {
                "from": "0x4c4b18A646da4f8a3e402139b13d3EB73c43515co",
                "to": "0x71faFcc3997c14025fdC70a1EB5a9E7b6888F64d",
                "amount": 1.0872,
                "_id": "d6a2d23109508e295788f1132e3b8ee4",
                "merkle_leaf": "0x2e0fcc55bff7fd24660c818398d3f7af3a5f68b844560b3058433042066ebd59"
            },
            {
                "from": "0x4c4b18A646da4f8a3e402139b13d3EB73c43515co",
                "to": "0x71faFcc3997c14025fdC70a1EB5a9E7b6888F64d",
                "amount": 2.97,
                "_id": "6b13055ed3e1cc24bc511e486e83eab5",
                "merkle_leaf": "0x4146ea93ea4b2968b7fd1c7b506e68c28bdc11be78d225d7f71788378cc0df84"
            }
        ]
    }
}
```
Always use the block format above to validate blocks.

## RESTful API
I have created an API in such a way to access this blockchain from retrieving all blockchain data, to validating the chain by looping through the blocks one by one and matching the before and after hashes.


| Endpoint | Function | HTTP Method |
| ------ | ------ | ------ |
| http://hostname:port | as root ../ | - |
| ../ | Get all blockchain data | GET |
| ../new-transaction | Creating new transactions/data into the chain | POST |
| ../current-transaction | Get a list of current transactions | GET |
| ../mine | Mining, generating hashes for block candidates, it takes between 1-3 minutes | GET |
| ../verify-chain | Validate every block in the chain one by one | GET |
| ../verify-block | Validate single block with previous_hash + block_data = next_hash  | POST |


**This project is still in the concept stage.**

## License

MIT
