class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        # Set to store all DNA sequences of length 10 seen so far
        seen_sequences = set()
        
        # Set to store repeated DNA sequences
        # Using a set avoids duplicate entries in the final answer
        output_sequences = set()

        # Sliding window of fixed size 10
        # We iterate until len(s) - 10 because each substring must contain 10 characters
        for i in range(0, len(s) - 10 + 1):

            # Extract current 10-letter DNA sequence
            subString = s[i: i + 10]

            # If sequence is seen for the first time,
            # add it to seen_sequences
            if subString not in seen_sequences:
                seen_sequences.add(subString)

            # If sequence already exists in seen_sequences,
            # it means we found a repeated DNA sequence
            else:
                output_sequences.add(subString)

        # Convert set to list before returning
        return list(output_sequences)
