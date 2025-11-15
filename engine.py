import hashlib
from db_connect import get_signatures
import scanner
def hash(file_path):
 try :
  md5 = hashlib.md5()
  with open(file_path,'rb') as f :

      chunk = f.read(4096)
      while chunk:
         md5.update(chunk)
         chunk = f.read(4096)
      
      return md5.hexdigest()
 except:
   print("Error in hash converion")
