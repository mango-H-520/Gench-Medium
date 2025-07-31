import mysql.connector
from mysql.connector import Error
import bcrypt  # 用于密码加密

class MySQLConnector:
    def __init__(self):
        # 数据库配置（请替换为你的MySQL信息）
        self.db_config = {
            'host': 'localhost',
            'database': 'user_db',
            'user': 'root',
            'password': '你的MySQL密码',  # 替换为你的密码
            'port': '3306'
        }
        self.connection = None

    def connect(self):
        """建立数据库连接"""
        try:
            if self.connection is None or not self.connection.is_connected():
                self.connection = mysql.connector.connect(**self.db_config)
                return True
            return True
        except Error as e:
            print(f"❌ 数据库连接失败: {e}")
            return False

    def save_user(self, username, password):
        """保存新用户到数据库（密码加密存储）"""
        try:
            cursor = self.connection.cursor()
            
            # 检查用户名是否已存在
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            if cursor.fetchone():
                cursor.close()
                return False, "用户名已存在"
            
            # 密码加密处理
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            
            # 插入新用户
            query = "INSERT INTO users (username, password) VALUES (%s, %s)"
            cursor.execute(query, (username, hashed_password.decode('utf-8')))
            self.connection.commit()
            cursor.close()
            return True, "注册成功"
        except Error as e:
            print(f"❌ 保存用户失败: {e}")
            return False, f"注册失败: {str(e)}"

    def verify_user(self, username, password):
        """验证用户登录信息"""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
            result = cursor.fetchone()
            cursor.close()
            
            if not result:
                return False, "用户名不存在"
            
            # 验证密码
            stored_password = result[0].encode('utf-8')
            if bcrypt.checkpw(password.encode('utf-8'), stored_password):
                return True, "登录成功"
            else:
                return False, "密码错误"
        except Error as e:
            print(f"❌ 验证用户失败: {e}")
            return False, f"登录失败: {str(e)}"

    def __del__(self):
        """关闭数据库连接"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
