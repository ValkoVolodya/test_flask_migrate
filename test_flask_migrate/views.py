import socket
from datetime import datetime

from test_flask_migrate import app


@app.route('/healthcheck')
def healthcheck():
    data = {
        'hostname': socket.gethostname(),
        'status': 'success',
        'timestamp': str(datetime.utcnow()),
    }
    return data
