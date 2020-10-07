from server.main import create_app

app = create_app()

if __name__ == '__main__':
    print("Rocket API serving ...")
    app.run(host="localhost", port=8000, debug=True)
