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
Examples of valid and correct block formats include header and body. You can validate the block format in the API I have created or you can also use the 'unit_testing.py' file.

### GENESIS_BLOCK
This is an example of a genesis block. If you want to hash or store data whatever data it is, You can store in 'body'. Also can pass data with array type, string, integer, float, etc.
```json
{
    "header": {
        "height": "0x0",
        "size": "0xe8",
        "merkle_root": "0x285b57d81686ccfe2b5d46f94fd7c655720e79bdb28fe399ef87fdd05d2aa8c6",
        "difficulty": 7,
        "previous_hash": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "nonce": "0x196b75",
        "time": "2022-02-10 03:11:51.954498",
        "block_hash": "0x0000065ce41fe4705c744553a7fba40c5772fb9054447a9287a4541e3fe47351"
    },
    "body": {
        "number_of_data": 3,
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
        "height": "0x1",
        "merkle_root": "0x674113e591897fd0488cc72dd5564ffaccff809e661df0ba8cae00db633f16e1",
        "size": "0x1d0",
        "difficulty": 7,
        "previous_hash": "0x0000065ce41fe4705c744553a7fba40c5772fb9054447a9287a4541e3fe47351",
        "nonce": "0x7142",
        "time": "2022-02-10 03:15:08.260755",
        "block_hash": "0x00000e0954dc62f132c09a509a2eef9ca07a3c6bbfc507951f4cdccd87cb455e"
    },
    "body": {
        "number_of_data": 2,
        "data": [
            {
                "_id": "7db42396e945064d40d51f1feb9a8096",
                "from": "Me",
                "to": "You",
                "amount": 5.7,
                "message": "haveaniceday!",
                "merkle_leaf": "0xd835a680324d678da9aa91fd18084239a798addba74bbf4ab998f1e3bbc83207"
            },
            {
                "_id": "2b36645a9bf35f6cfde8b9541ff21c29",
                "from": "0x4c4b18A646da4f8a3e402139b13d3EB73c43515co",
                "to": "0x71faFcc3997c14025fdC70a1EB5a9E7b6888F64d",
                "amount": 7.2,
                "message": "how are you today?",
                "merkle_leaf": "0x7104ae98bf2ffa137cdf7c24c49dd101a129d1a47f5a9d60196b140e86679591"
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
| ../new_data | Creating new datas/data into the chain | POST |
| ../current_data | Get a list of current data | GET |
| ../mine | Mining, generating hashes for block candidates, it takes between 1-3 minutes | GET |
| ../verify_chain | Validate every block in the chain one by one | GET |
| ../verify_block | Validate single block with previous_hash + block_data = next_hash  | POST |


**This project has met the minimum blockchain requirements.**

## License

MIT
