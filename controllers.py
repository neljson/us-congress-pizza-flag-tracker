from flask import render_template, redirect, request, session, send_file
from config import db, qrcode
from models import OrderModel
import cv2
import qrcode

import random
import json

from OrderActions import OrderActions 
import io


# https://flask-session.readthedocs.io/en/latest/
# https://github.com/marcoagner/Flask-QRcode

def index():
    return render_template('index.html')

def create_order():
    request_json = request.get_json()
    print(request_json, type(request_json))
    # for x in request_json.keys():
    #     print(x,request_json[x])

    usa_state = request_json[u'usa_state']
    idbased_order_number = request_json[u'order_number']
    coffice = request_json[u'coffice']
    order = OrderActions.create( usa_state,  idbased_order_number , coffice)
    return f'Created one'

def get_orders():
    orders=OrderActions.get()
    return orders

#generate qr code 
def get_qrcode():
    data = request.args.get("value", None)
    img = qrcode.make(data)
    buf = io.BytesIO()
    img.save(buf)
    buf.seek(0)
    return buf

def send_file_qrcode():
    q = get_qrcode()
    return send_file(q, mimetype="image/jpeg")