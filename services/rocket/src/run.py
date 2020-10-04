import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'src')))

from server.main import create_app

app = create_app()

if __name__ == '__main__':
    print(sys.path)
    print("Rocket API serving ...")
    app.run(host="0.0.0.0", port=8000, debug=True)
