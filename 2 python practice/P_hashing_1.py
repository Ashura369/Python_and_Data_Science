
hash_table_size = 10
hash_table = [None] * hash_table_size

print(hash_table)
print("--------------------------------------------------------------")

# def hash_function(key):
    # return key % hash_table_size

def insert(index, value):
    hash_table[index] = value
    print(f"INSERTED {value} AT INDEX {index}")


# -----------------------------------------------------------------

print("--- Inserting Data ---")
insert(4, "Alice")   # 104 % 10 = 4
insert(7, "Bob")     # 207 % 10 = 7
insert(2, "Charlie") # 902 % 10 = 2

print("\n--- Hash Table State ---")
print(hash_table)
print(hash_table[2])
print(hash_table[4])
print("--------------------------------------------------------------")

nums_list = [1,1,3,35,46,5,3,1,454,93,3,33,5,5,3,3,6,5,3,46,3,1,3,126,36,5]
hash_list = [None] * 20

def count_frequencies(lst):
    for i in lst:
        index = i % len(hash_list)
        start_index = index
        
        # Probe until we find an empty slot or the same number
        while hash_list[index] is not None and hash_list[index][0] != i:
            index = (index + 1) % len(hash_list)
            
            # Prevent infinite loop if the hash list is full
            if index == start_index:
                print("Hash list is full!")
                return
        
        # If the slot is empty, insert the number with a count of 1
        if hash_list[index] is None:
            hash_list[index] = [i, 1]
        # If the number is already present, increment its count
        else:
            hash_list[index][1] += 1


count_frequencies(nums_list)



