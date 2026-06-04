import sys
import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    try:
        import tensorflow as tf
        import keras
        tf_version    = tf.__version__
        keras_version = keras.__version__
    except Exception as e:
        tf_version    = f"error: {str(e)}"
        keras_version = "no disponible"

    return jsonify({
        'python':     sys.version,
        'tensorflow': tf_version,
        'keras':      keras_version
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)