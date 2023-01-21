import hashlib

# hex tx
raw_tx1 = '010000000186170477aa4e3c7e1b344e0ad6277a4a5aa07a09405ce54831af87f1d772e708010000006b483045022100e0d08a61f906ac98e1d1ee2f56edaf8bbbc8e38480fc2285a23f28ce6a06270e0220431364f2e946fa8b1f6bf732d97e81349f352694017acaa4584a2de6f3cc3e77012103a0e2a3a31ab76280504d6c9338961bec25eb7a3e0e638fc4f6de03bf8f6b6caaffffffff01986e1d01000000001976a914b49d851dd96160dc86aa726e123b76f601b9c73688ac00000000'
raw_tx2 = '0100000003e4d7be4314204a239d8e00691128dca7927e19a7339c7948bde56f669d27d797010000006b483045022100b988a858e2982e2daaf0755b37ad46775d6132057934877a5badc91dee2f66ff022020b967c1a2f0916007662ec609987e951baafa6d4fda23faaad70715611d6a2501210254a2dccd8c8832d4677dc6f0e562eaaa5d11feb9f1de2c50a33832e7c6190796ffffffff9e22eb1b3f24c260187d716a8a6c2a7efb5af14a30a4792a6eeac3643172379c000000006a47304402207df07f0cd30dca2cf7bed7686fa78d8a37fe9c2254dfdca2befed54e06b779790220684417b8ff9f0f6b480546a9e90ecee86a625b3ea1e4ca29b080da6bd6c5f67e01210254a2dccd8c8832d4677dc6f0e562eaaa5d11feb9f1de2c50a33832e7c6190796ffffffff1123df3bfb503b59769731da103d4371bc029f57979ebce68067768b958091a1000000006a47304402207a016023c2b0c4db9a7d4f9232fcec2193c2f119a69125ad5bcedcba56dd525e02206a734b3a321286c896759ac98ebfd9d808df47f1ce1fbfbe949891cc3134294701210254a2dccd8c8832d4677dc6f0e562eaaa5d11feb9f1de2c50a33832e7c6190796ffffffff0200c2eb0b000000001976a914e5eb3e05efad136b1405f5c2f9adb14e15a35bb488ac88cfff1b000000001976a9144846db516db3130b7a3c92253599edec6bc9630b88ac00000000'


def hash256(raw_data_hex):
    raw_data_bytes = bytes.fromhex(raw_data_hex) # convert to bytes
    txid = hashlib.sha256(hashlib.sha256(raw_data_bytes).digest()).hexdigest()
    
    # Return as big endian hex
    hash256_data_hex = bytes.fromhex(txid)[::-1].hex()
    return hash256_data_hex
    
txid1 = hash256(raw_tx1)
txid2 = hash256(raw_tx2)
print('tx1', txid1)
print('tx2', txid2)