import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'box-20-21-team-f/services/rocket/src')))

from server.main import create_app

app = create_app()

if __name__ == '__main__':
    print("Rocket API serving ...")
    app.run(host="0.0.0.0", port=8000, debug=True)
