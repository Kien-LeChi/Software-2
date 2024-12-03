from flask import Flask, request
import mysql.connector

app = Flask(__name__)
@app.route('/airport/<icao_code>')
def haha(icao_code):
        
    connection = mysql.connector.connect(
        user = 'root',
        password = 'root',
        database = 'flight_game',
        # collation = 'utf8mb3_general_ci',
        autocommit = True
    )
    cursor = connection.cursor()
    query = f"SELECT ident, name, municipality FROM airport WHERE ident = '{icao_code}';"
    cursor.execute(query)
    result = cursor.fetchall()
    if len(result) == 0:
        response = {
            "Error": "There was no airports with the entered ICAO code",
        }
    else :
        response = {
            "ICAO": icao_code,
            "Name": result[0][1],
            "Location": result[0][2],
        }
    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)