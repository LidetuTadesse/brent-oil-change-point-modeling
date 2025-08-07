from flask import Blueprint, jsonify
import pandas as pd
import json
import os

api_bp = Blueprint('api', __name__)

# Set paths
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
MODELS_DIR = os.path.join(os.path.dirname(__file__), 'models')

@api_bp.route('/api/prices', methods=['GET'])
def get_prices():
    df = pd.read_csv(os.path.join(DATA_DIR, 'brent_log_features.csv'))
    return df.to_json(orient='records')

@api_bp.route('/api/change-points', methods=['GET'])
def get_change_points():
    df = pd.read_csv(os.path.join(MODELS_DIR, 'change_points.csv'))
    return df.to_json(orient='records')

@api_bp.route('/api/events', methods=['GET'])
def get_events():
    df = pd.read_csv(os.path.join(DATA_DIR, 'key_events.csv'))
    return df.to_json(orient='records')

@api_bp.route('/api/indicators', methods=['GET'])
def get_indicators():
    df = pd.read_csv(os.path.join(DATA_DIR, 'brent_log_features.csv'))
    volatility = df['Log_Return'].std()
    avg_return = df['Log_Return'].mean()
    return jsonify({
        'volatility': round(volatility, 4),
        'average_log_return': round(avg_return, 4)
    })
