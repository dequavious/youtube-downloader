import os
import sys

# from waitress import serve

from app import app


if __name__ == "__main__":
    if len(sys.argv) > 1:
        app.run(host='0.0.0.0', port=os.environ.get('PORT', f'{sys.argv[1]}'))
        # serve(app, host='0.0.0.0', port=os.environ.get('PORT', 'sys.argv[1]'))
    else:
        app.run(host='0.0.0.0', port=os.environ.get('PORT', '5000'))
        # serve(app, host='0.0.0.0', port=os.environ.get('PORT', '5000'))

