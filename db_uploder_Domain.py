import mysql.connector
def upload(input):
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
        cursor.execute(input)
        data = cursor.fetchall()

        cursor.close()
        connection.close()
        print(data)
    except mysql.connector.Error as err :
        print(f"db error : {err}")
input = "SELECT * FROM signatures"
upload(input)

