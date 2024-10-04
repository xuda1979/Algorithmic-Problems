import heapq
from collections import defaultdict

# Class to represent a node in the Huffman Tree
class HuffmanNode:
    def __init__(self, char, freq):
        # Initialize node with character and frequency
        self.char = char
        self.freq = freq
        self.left = None  # Left child
        self.right = None  # Right child

    # Define comparison operators for the priority queue
    def __lt__(self, other):
        # Comparison is based on frequency, used by the heapq to sort nodes
        return self.freq < other.freq

# Function to build the Huffman Tree
def build_huffman_tree(frequency):
    # Create a priority queue using a min-heap with all characters and their frequencies
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)  # Convert list into a heap (min-heap)

    # Iterate until there is only one node left in the heap (root of the Huffman Tree)
    while len(heap) > 1:
        # Extract the two nodes with the lowest frequency
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Create a new internal node with these two nodes as children
        # The frequency of the new node is the sum of the frequencies of the two nodes
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        # Add the new node back into the heap
        heapq.heappush(heap, merged)

    # The remaining node is the root of the Huffman Tree
    return heap[0]

# Function to generate Huffman Codes from the Huffman Tree
def generate_codes(root, current_code, codes):
    if root is None:
        return

    # If this is a leaf node, save the current code for the character
    if root.char is not None:
        codes[root.char] = current_code
        return

    # Recur for left and right subtrees, adding "0" for left and "1" for right
    generate_codes(root.left, current_code + "0", codes)
    generate_codes(root.right, current_code + "1", codes)

# Function to compress data using Huffman Coding
def huffman_encoding(data):
    # Calculate frequency of each character in the data
    frequency = defaultdict(int)
    for char in data:
        frequency[char] += 1

    # Build the Huffman Tree from the frequency data
    root = build_huffman_tree(frequency)

    # Generate Huffman Codes by traversing the Huffman Tree
    codes = {}
    generate_codes(root, "", codes)

    # Encode the data using the generated codes
    encoded_data = "".join([codes[char] for char in data])
    return encoded_data, root

# Function to decompress data using Huffman Coding
def huffman_decoding(encoded_data, root):
    decoded_data = []
    current = root

    # Traverse the Huffman Tree based on the bits in the encoded data
    for bit in encoded_data:
        # Move to the left child if the bit is '0', otherwise move to the right child
        if bit == '0':
            current = current.left
        else:
            current = current.right

        # If we reach a leaf node, append the character to the result
        if current.char is not None:
            decoded_data.append(current.char)
            current = root  # Go back to the root for the next character

    return "".join(decoded_data)

# Example usage
if __name__ == "__main__":
    data = "huffman coding in python"
    print(f"Original data: {data}")

    # Encode the data using Huffman Coding
    encoded_data, tree_root = huffman_encoding(data)
    print(f"Encoded data: {encoded_data}")

    # Decode the encoded data back to the original message
    decoded_data = huffman_decoding(encoded_data, tree_root)
    print(f"Decoded data: {decoded_data}")

    # Additional examples
    data2 = "example text for huffman coding"
    print(f"\nOriginal data: {data2}")

    # Encode the new data
    encoded_data2, tree_root2 = huffman_encoding(data2)
    print(f"Encoded data: {encoded_data2}")

    # Decode the encoded data back to the original message
    decoded_data2 = huffman_decoding(encoded_data2, tree_root2)
    print(f"Decoded data: {decoded_data2}")

    data3 = "aaaaabbbbcccdde"
    print(f"\nOriginal data: {data3}")

    # Encode the new data
    encoded_data3, tree_root3 = huffman_encoding(data3)
    print(f"Encoded data: {encoded_data3}")

    # Decode the encoded data back to the original message
    decoded_data3 = huffman_decoding(encoded_data3, tree_root3)
    print(f"Decoded data: {decoded_data3}")