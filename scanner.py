from engine import hash
import os
def scan_file(file_path,signature):
  file_name = os.path.basename(file_path)
  try:
    hash_value = hash(file_path) # Sending the file path to the engine 
    if not hash_value : # if hash file is empty or have no hash data then this part runs
      return f"File Not Found: File Name -: {file_name}"
    for sign_type,sign_value in signature : #created 2 new varible signatue type and signature value 
       if sign_type == 'hash' and hash_value == sign_value : #this part runs when the signature and the value of the signature is matched with the database
         return f"!!INFECTED FILE -: The file {file_name} is Infected\n hash = {hash_value}\n|| The file {file_name} is removed" #if the signature(MD5 HASH) is matched with he database signature values and type then it runs this part
    # --- STRING SIGNATURE DETECTION ---
    with open(file_path, "rb") as f:     # IMPORTANT: read as binary
      content = f.read()

      for sign_type, sign_value in signature:
         if sign_type == "string":
             if isinstance(sign_value, str):
               sign_value = sign_value.encode()
             if sign_value in content:
                 return f"[INFECTED] (STRING MATCH)\nFile: {file_name}\nSignature: {sign_value}"

    return f"{file_name} is safe"
  except Exception as ER:
     return f"Error in scanning {file_path} or in Database {ER}"