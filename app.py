from flask import Flask, request, jsonify
from flask_cors import CORS
from db_connector import MySQLConnector

app = Flask(__name__)
# 允许所有设备跨域访问（生产环境可指定具体域名）
CORS(app, origins="*")

# 初始化数据库连接
db = MySQLConnector()

# 注册接口
@app.route('/api/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({"success": False, "message": "用户名和密码不能为空"}), 400

        # 连接数据库并保存用户
        if not db.connect():
            return jsonify({"success": False, "message": "数据库连接失败"}), 500
        
        success, message = db.save_user(username, password)
        return jsonify({"success": success, "message": message})
    except Exception as e:
        return jsonify({"success": False, "message": f"服务器错误: {str(e)}"}), 500

# 登录接口
@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({"success": False, "message": "用户名和密码不能为空"}), 400

        # 连接数据库并验证用户
        if not db.connect():
            return jsonify({"success": False, "message": "数据库连接失败"}), 500
        
        success, message = db.verify_user(username, password)
        return jsonify({"success": success, "message": message})
    except Exception as e:
        return jsonify({"success": False, "message": f"服务器错误: {str(e)}"}), 500

# 用户列表接口（用于验证数据存储）
@app.route('/api/users', methods=['GET'])
def get_users():
    try:
        if not db.connect():
            return jsonify({"success": False, "message": "数据库连接失败"}), 500
        
        cursor = db.connection.cursor(dictionary=True)
        cursor.execute("SELECT id, username, created_at FROM users;")
        users = cursor.fetchall()
        cursor.close()
        
        return jsonify({"success": True, "users": users}), 200
    except Exception as e:
        return jsonify({"success": False, "message": f"查询失败: {str(e)}"}), 500

if __name__ == '__main__':
    # 关键：host='0.0.0.0'允许所有设备访问
    app.run(host='0.0.0.0', port=5000, debug=True)
