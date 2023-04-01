
import streamlit as st
from flask import Flask, jsonify, request,render_template
# from pymongo import MongoClient
# from bson.objectid import ObjectId
app = Flask(__name__)
html = """
<div class="container">
  <div class="row">
    <div class="col-sm-4">
      <h3>Column 1</h3>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    </div>
    <div class="col-sm-4">
      <h3>Column 2</h3>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    </div>
    <div class="col-sm-4">
      <h3>Column 3</h3>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    </div>
  </div>
</div>
"""

@app.route('/')
def index():
    st.write(html, unsafe_allow_html=True)

if __name__ == '__main__':
    app.run()
