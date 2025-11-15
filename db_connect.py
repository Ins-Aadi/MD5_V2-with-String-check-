import mysql.connector

def get_signatures():
    try:
        connection = mysql.connector.connect(
            host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",    
            port=4000,                     
            user="2kRt5fGg8iyL4hs.root",        
            password="6vwhb9RmUNggGdRc",     
            database="antivirus_db",
            ssl_disabled=False  
        )

        cursor = connection.cursor()
        cursor.execute("SELECT type, signature FROM signatures")
        data = cursor.fetchall()

        cursor.close()
        connection.close()

        return data
    except mysql.connector.Error as err :
        print(f"db error : {err}")
