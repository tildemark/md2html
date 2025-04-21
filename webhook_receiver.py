from flask import Flask, request, jsonify
import hmac
import hashlib
import subprocess
import os

app = Flask(__name__)
GITEA_SECRET = os.environ.get('GITEA_WEBHOOK_SECRET', 'your_gitea_webhook_secret') # Get secret from environment
CONVERSION_SCRIPT_PATH = '/app/convert_manuals.py'

def verify_signature(payload_body, header_signature):
    if header_signature is None:
        return False
    sha_name, signature = header_signature.split('=')
    if sha_name != 'sha256':
        return False
    digest = hmac.new(GITEA_SECRET.encode('utf-8'), msg=payload_body, digestmod=hashlib.sha256).hexdigest()
    return hmac.compare_digest(signature, digest)

@app.route('/gitea-webhook', methods=['POST'])
def gitea_webhook_received():
    signature = request.headers.get('X-Gitea-Signature')
    if not verify_signature(request.get_data(), signature):
        return jsonify({'error': 'Invalid signature'}), 401

    if request.headers.get('X-Gitea-Event') == 'push':
        print("Push event received from Gitea. Triggering conversion...")
        try:
            subprocess.run(['python3', CONVERSION_SCRIPT_PATH], check=True)
            return jsonify({'status': 'Conversion triggered successfully'}), 200
        except subprocess.CalledProcessError as e:
            print(f"Error running conversion script: {e}")
            return jsonify({'error': 'Conversion script failed'}), 500
        except FileNotFoundError:
            print(f"Conversion script not found at: {CONVERSION_SCRIPT_PATH}")
            return jsonify({'error': 'Conversion script not found'}), 500
    else:
        print(f"Received event: {request.headers.get('X-Gitea-Event')}")
        return jsonify({'status': 'Event received'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)