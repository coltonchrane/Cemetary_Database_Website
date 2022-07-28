#Creates app and runs it. Run this file when executing the program
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) #TURN OFF IN PRODUCTION, TRUE MAKES IT RERUN WEBSERVER WHEN CHANGES MADE

