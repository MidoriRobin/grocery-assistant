#! /usr/bin/env python
from app import app
from app.mlModels.CBRecomHandler import cbrec

app.run(debug=True,host="0.0.0.0",port=8080)
