from flask import Flask, render_template, request, jsonify, send_from_directory  
import qrcode  
import os  
import time  
from blockchain import Blockchain  

app = Flask(__name__)  
blockchain = Blockchain()  

# Create QR directory  
os.makedirs('frontend/static/qrcodes', exist_ok=True)  

@app.route('/')  
def home():  
    return render_template('index.html')  

@app.route('/generate_deed', methods=['POST'])  
def generate_deed():  
    text = request.json['text']  
    deed_id = f"DEED-{int(time.time())}"  
    
    deed = {  
        'id': deed_id,  
        'text': text,  
        'from': 'AADHAR-XXXX',  
        'to': 'AADHAR-YYYY',  
        'timestamp': time.strftime("%d-%m-%Y %H:%M:%S")  
    }  

    blockchain.new_transaction(deed)  
    
    # Generate QR  
    qr = qrcode.make(f"AI Patwari Deed\n{json.dumps(deed, indent=2)}")  
    qr.save(f"frontend/static/qrcodes/{deed_id}.png")  

    return jsonify({  
        'success': True,  
        'qr_url': f"/static/qrcodes/{deed_id}.png",  
        'deed': deed  
    })  

@app.route('/static/qrcodes/<path:filename>')  
def serve_qr(filename):  
    return send_from_directory('frontend/static/qrcodes', filename)  

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=5000, debug=True)  