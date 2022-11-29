import hashlib

file_name = input("Enter the filename: ")
hash_original = input("Enter the original hash: ")
algo = input("Enter the algorithm (sha256/md5): ")

# Open,close, read file and calculate hash on its contents 
with open(file_name, 'rb') as file_to_check:
  data = file_to_check.read()
  # Set the algorithm:
  if algo == 'sha256':
    hash_returned = hashlib.sha256(data).hexdigest()
  if algo == 'md5':
    hash_returned = hashlib.md5(data).hexdigest()

# Compare the hash
if hash_original == hash_returned:
  print("Checksum verified.")
else:
  print("Checksum failed.")