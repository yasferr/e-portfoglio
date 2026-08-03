# clean_names.py

def process_names(names):
    seen = set()           # Stores normalized names to track duplicates efficiently
    unique_names = []     # Preserves insertion order for output consistency

    for name in names:
        normalized = name.lower()  # Convert to lowercase for case-insensitive comparison

        # Check if the normalized name has already been encountered
        if normalized not in seen:
            seen.add(normalized)  # Mark name as seen
            unique_names.append(name.capitalize())  
            # Capitalize to standardize formatting in output

    unique_names.sort()  # Sort alphabetically for clean presentation
    return unique_names


# Test list with duplicates and inconsistent capitalisation
test_names = ["Alice", "bob", "alice", "Charlie", "BOB", "dave", "Eve", "charlie"]

print("Original list:", test_names)
print("Processed list:", process_names(test_names))
