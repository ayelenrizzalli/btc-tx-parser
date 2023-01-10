# This was the first ever bitcoin transaction where Satoshi Nakamoto sent Hal Finney 10 BTC
txid_original = 'f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16'
raw_hex = '0100000001c997a5e56e104102fa209c6a852dd90660a20b2d9c352423edce25857fcd3704000000004847304402204e45e16932b8af514961a1d3a1a25fdf3f4f7732e9d624c6c61548ab5fb8cd410220181522ec8eca07de4860a4acdd12909d831cc56cbbac4622082221a8768d1d0901ffffffff0200ca9a3b00000000434104ae1a62fe09c5f51b13905f07f06b99a2f7159b2225f374cd378d71302fa28414e7aab37397f554a7df5f142c21c1b7303b8a0626f1baded5c72a704f7e6cd84cac00286bee0000000043410411db93e1dcdb8a016b49840f8c53bc1eb68a382e97b1482ecad7b148a6909a5cb2e0eaddfb84ccf9744464f82e160bfa9b8b64f9d4c03f999b8643f656b412a3ac00000000'

# Convert from hexa to int
def convert_raw_amount_to_int(amount):
    amount_decoded_hex = bytes.fromhex(amount)[::-1].hex()
    int_amount = int(amount_decoded_hex,16)
    return(int_amount)

def convert_raw_txid(txid):
    amount_decoded_txid = bytes.fromhex(txid)[::-1].hex()
    return(amount_decoded_txid)

# Parsing tx
version = raw_hex[0:8]
print('version', version)
input_count = int(raw_hex[8:10],16)
print('input_count', input_count)
position = 10
inputs = []
outputs = []
# Parsing inputs dinamically based on input_count
for i in range(input_count):
    txid = convert_raw_txid(raw_hex[position:position+64])
    position += 64
    vout = raw_hex[position:position+8]
    position +=8
    scriptSig_len = int(raw_hex[position:position+2],16)
    position +=2
    scriptSig = raw_hex[position:position+scriptSig_len*2]
    position +=scriptSig_len*2
    sequence = convert_raw_amount_to_int(raw_hex[position:position+8])
    position +=8

    inputs.append([txid,vout,scriptSig_len,scriptSig,sequence])

print('inputs', inputs)

output_count = int(raw_hex[position:position+2],16)
position +=2
print('output_count', output_count)

# Parsing outputs dinamically based on output_count
for i in range(output_count):
    amount = convert_raw_amount_to_int(raw_hex[position:position+16]) #sats
    position += 16
    scriptPubKey_len = int(raw_hex[position:position+2],16)
    position +=2
    scriptPubKey = raw_hex[position: position+scriptPubKey_len*2]
    position +=scriptPubKey_len*2
    outputs.append([amount,scriptPubKey_len,scriptPubKey])



print('outputs', outputs)
locktime = raw_hex[position:position+8]
print('locktime', locktime)

