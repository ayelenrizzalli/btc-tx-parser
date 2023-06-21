# Bitcoin Transaction Parser

`parse-btc-tx.py` script is designed to parse a Legacy Bitcoin transaction and extract relevant information from the transaction data.

## Prerequisites

- Python 3.x

## Usage

1. Open the script in a Python IDE or text editor.
2. Ensure that the `raw_hex` variable is correctly set with the transaction data you want to parse.
3. Run the script.

The script will output the following information:

- Transaction version: The version number of the transaction.
- Input count: The number of inputs in the transaction.
- Inputs: Information about each input, including the transaction ID (txid), output index (vout), scriptSig length, scriptSig (input script), and sequence number.
- Output count: The number of outputs in the transaction.
- Outputs: Information about each output, including the amount (in satoshis) and scriptPubKey length and scriptPubKey (output script).
- Locktime: The locktime value of the transaction.

## Functionality

The script provides the following functions:

### convert_raw_amount_to_int(amount)

This function takes a raw hex-encoded amount and converts it to an integer value. It reverses the byte order of the hex string and converts it to a decimal. (little-endian -> big-endian -> int)

### convert_raw_txid(txid)

This function takes a raw hex-encoded transaction ID (txid) and converts it to a human-readable format. It reverses the byte order of the hex string (little-endian -> big-endian)

### compact_field_size(hex_string)

This function handles parsing of the compact size format used in Bitcoin transactions (fields like the input count are variable length). It takes a hex string as input and returns the compact field size as a decimal value, along with the new position in the string after parsing.

## Limitations

- This script is specific to Legacy Bitcoin transactions.
- It assumes that the input transaction data is provided in the expected format and does not perform extensive error checking or validation.
- The script does not handle any additional transaction fields beyond the basic inputs, outputs, and locktime.

## License

This script is released under the [MIT License](https://opensource.org/licenses/MIT).
