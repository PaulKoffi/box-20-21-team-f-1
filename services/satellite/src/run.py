from server.main import create_app

app = create_app()

if __name__ == '__main__':
    print("Satellite API serving ...")
    app.run(host="0.0.0.0", port=3550, debug=True)
