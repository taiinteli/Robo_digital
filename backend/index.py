from flask import Flask, render_template, redirect, request

import asyncio
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from models.init import Base
from models.position import Position

app = Flask(__name__)
engine = create_engine("sqlite+pysqlite:///coordenates.db", echo=True)
Session = sessionmaker(bind = engine)
session = Session()

@app.route('/post', methods=["POST"])
def postForm():
    print(request.form)
    c1 = Position(x=request.form['x'], y=request.form['y'], z=request.form['z'])

    session.add(c1)
    session.commit()
    return { x: request.form['x'], y: request.form['y'], z: request.form['z'] }

@app.route('/move', methods=["GET", "POST"])
def godot_coords():
    positions = session.query(Position).all()
    if positions:
        x = positions[-1].x
        y = positions[-1].y
        z = positions[-1].z
    godotstring = f"{x}/{y}/{z}"
    return godotstring