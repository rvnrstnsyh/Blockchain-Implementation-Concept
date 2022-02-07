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
    "_id": "0x1",
    "block_hash": "0x000009fb0a6c3bb0b17d57320c4a50733d059dc2830cc2caa203fef133218f47",
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
    "nonce": "0x258ff5",
    "timestamp": "0x17ed16d9c05"
}
```

### Other block
This is an example of a block that stores simple transaction data.
```json
{
    "_id": "0x2",
    "block_hash": "0x000002486705922055a864d39b47d5a2a3bd1c93be070c03f6740ea017f8159c",
    "data": {
        "previous_hash": "0x000000c7b1c96e8fd82e833ca9531903ddcf70be302f689116cfbb0c70ffebd0",
        "transaction": [
            {
                "amount": 1.0017,
                "from": "0x4c4b18A646da4f8a3e402139b13d3EB73c43515co",
                "to": "0x71faFcc3997c14025fdC70a1EB5a9E7b6888F64d"
            },
            {
                "_fee": 0.5,
                "from": "0x4c4b18A646da4f8a3e402139b13d3EB73c43515co",
                "to": "0x5cc77be92190604789f08a2fc2079f84359cebff"
            }
        ],
        "transaction_hash": "0x00dd65477414b7cbc9707889b818980703ba7e1bb5b9835b333a93a9ffda4b2f"
    },
    "index": "0x1",
    "nonce": "0x856d",
    "timestamp": "0x17ecff5eea4"
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
