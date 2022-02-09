import json
from pymerkle import MerkleTree


def get_merkle_tree(hashes):
    dumper = {
        "header": {
            "encoding": "utf_8",
            "hash_type": "sha256",
            "raw_bytes": True,
            "security": False
        },
        "hashes": []
    }

    arr = []
    for i in range(len(hashes)):
        arr.append(hashes[i])
    dumper["hashes"] = arr

    with open('json/merkle_tree.json', 'w') as outfile:
        json.dump(dumper, outfile)
    load_tree = MerkleTree.loadFromFile('json/merkle_tree.json')
    return f'0x{load_tree.rootHash.decode("utf-8")}'
