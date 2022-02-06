<a href="https://www.blockchain.com"><img alt="Blockchain" src="https://i.postimg.cc/W12crkm1/pngkit-technology-png-344121.png"></a>

A blockchain, or block chain as it was originally spelled, is an ever-expanding record, called blocks, that are linked and secured using cryptographic techniques. Each block typically contains a cryptographic hash of the previous block, a timestamp, and transaction data. [Read more](https://id.wikipedia.org/wiki/Rantai_blok)

## How to use
To run this script you just need to install python version 3, pip, flask and requests

after everything is installed:
```
~# python3 index.py
```
You can also mark options such as hostname, port, and nonce/proof of work difficulty:
```
~# python3 index.py -h 127.0.0.1 -p 3000 -d 0x00000
```

## Valid block
Examples of valid and correct block formats include _id, block hash, data, index, nonce and timestamp. You can validate the block format in the API I have created or you can also use the 'validblock.py' file.

### GENESIS_BLOCK
If you want to hash or store data whatever data it is, You can store in key 'data' object. Also can pass data with array type, string, integer, float, etc.
```json
{
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

**This project is still in the concept stage.**

## License

MIT
