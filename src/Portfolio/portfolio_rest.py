import os
os.environ['DB_NAME_PORTFOLIO'] = 'Portfolio'

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask import Blueprint
from Portfolio.portfolio import Portfolio
from Portfolio.portfolio_db import PortfolioDB

bp_portfolio = Blueprint('portfolio', 'portfolio', url_prefix='/portfolio')

db_uri = 'localhost:27017'

@bp_portfolio.route("/", methods=['GET'])
def portfolio_inicio():
    return jsonify({'Microservicio': 'Portfolio'})


@bp_portfolio.route("/<dni>", methods=['GET'])
def consultar_info_usuario(dni):
    portfolio_db = PortfolioDB(os.environ['DB_NAME_PORTFOLIO'], db_uri)
    user_portfolio = Portfolio(portfolio_db, dni)
    return jsonify(user_portfolio.consultar_datos_usuario())


@bp_portfolio.route("/<dni>/saldo", methods=['GET'])
def consultar_saldo(dni):
    portfolio_db = PortfolioDB(os.environ['DB_NAME_PORTFOLIO'], db_uri)
    user_portfolio = Portfolio(portfolio_db, dni)
    return jsonify(user_portfolio.consultar_saldo())


@bp_portfolio.route("/<dni>/acciones", methods=['GET'])
def consultar_acciones(dni):
    portfolio_db = PortfolioDB(os.environ['DB_NAME_PORTFOLIO'], db_uri)
    user_portfolio = Portfolio(portfolio_db, dni)
    return jsonify(user_portfolio.consultar_acciones())


@bp_portfolio.route("/<dni>/acciones/<mercado>", methods=['GET'])
def consultar_acciones_mercado(dni, mercado):
    portfolio_db = PortfolioDB(os.environ['DB_NAME_PORTFOLIO'], db_uri)
    user_portfolio = Portfolio(portfolio_db, dni)
    return jsonify(user_portfolio.consultar_acciones_mercado(mercado))


@bp_portfolio.route('/<dni>/ingresar-saldo', methods=['POST'])
def ingresar_saldo(dni):
    portfolio_db = PortfolioDB(os.environ['DB_NAME_PORTFOLIO'], db_uri)
    user_portfolio = Portfolio(portfolio_db, dni)
    content = request.json
    user_portfolio.incrementar_saldo(content['cantidad'])
    return jsonify(user_portfolio.consultar_saldo())


@bp_portfolio.route('/<dni>/retirar-saldo', methods=['POST'])
def retirar_saldo(dni):
    portfolio_db = PortfolioDB(os.environ['DB_NAME_PORTFOLIO'], db_uri)
    user_portfolio = Portfolio(portfolio_db, dni)
    content = request.json
    user_portfolio.decrementar_saldo(content['cantidad'])
    return jsonify(user_portfolio.consultar_saldo())


@bp_portfolio.route('/<dni>/comprar-acciones', methods=['POST'])
def comprar_acciones(dni):
    portfolio_db = PortfolioDB(os.environ['DB_NAME_PORTFOLIO'], db_uri)
    user_portfolio = Portfolio(portfolio_db, dni)
    content = request.json
    user_portfolio.comprar_acciones_mercado(content['symbol'], content['cantidad'])
    return jsonify(user_portfolio.consultar_acciones())


@bp_portfolio.route('/<dni>/vender-acciones', methods=['POST'])
def vender_acciones(dni):
    portfolio_db = PortfolioDB(os.environ['DB_NAME_PORTFOLIO'], db_uri)
    user_portfolio = Portfolio(portfolio_db, dni)
    content = request.json
    user_portfolio.vender_acciones_mercado(content['symbol'], content['cantidad'])
    return jsonify(user_portfolio.consultar_acciones())
