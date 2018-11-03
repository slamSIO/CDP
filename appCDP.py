#!/usr/bin/python3
# coding: utf-8

from flask import *

app = Flask( __name__ )

@app.route( '/' , methods = [ 'GET' ] )
def index() :
	return render_template( 'vueAccueil.html' )
	
@app.route( '/producteurs' , methods = [ 'GET' ] )
def getProducteurs() :
	return render_template( 'vueListeProducteurs.html' )


if __name__ == '__main__' :
	app.run( debug = True , host = '0.0.0.0' , port = 5000 )
