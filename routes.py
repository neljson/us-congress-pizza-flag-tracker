from config import app
from controllers import info, send_file_qrcode, create_order, get_orders, index, get_order_by_uuid, update_order


# TODO: refactor out this from routes:
from flask import Flask, render_template, request, send_file

# add routes below
app.add_url_rule('/', view_func=index)
# create qr code
#app.add_url_rule('/createqrcode/<orderid>', view_func=send_file_qrcode, methods=["GET"])

app.add_url_rule('/qrcode/<uuid>', view_func=send_file_qrcode, methods=["GET"])

#initialize congress order ID as a UUID.
app.add_url_rule('/orders/create', view_func=create_order, methods=["POST"])
#list all the orders
app.add_url_rule('/orders', view_func=get_orders, methods=["GET"])
# get specific order
app.add_url_rule('/orders/<uuid>', view_func=get_order_by_uuid, methods=["GET"])

app.add_url_rule('/info', view_func=info, methods=["GET"])

app.add_url_rule('/update/<uuid>', view_func=update_order, methods=["POST"])