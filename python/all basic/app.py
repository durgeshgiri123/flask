# from flask import Flask, jsonify
# import json
# import os

# app = Flask(__name__)

# @app.route('/api')
# def get_data():
#     # Get current file directory
#     base_dir = os.path.dirname(os.path.abspath(__file__))
#     file_path = os.path.join(base_dir, 'data.json')

#     print("Looking for file at:", file_path)  # DEBUG

#     try:
#         with open(file_path, 'r') as file:
#             data = json.load(file)
#         return jsonify(data)

#     except FileNotFoundError:
#         return jsonify({"error": f"File not found at {file_path}"}), 404

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# if __name__ == '__main__':
#     app.run(debug=True)
# this code for task 1 in tude assigenment 
# from flask import Flask, request
# app = Flask(__name__)
# @app.route('/')
# def home ():
#     return 'Welcome to the home page'
# @app.route('/api')
# def name ():
#     name = request.values.get('name')
#     age = request.values.get('age')
#     result = {'name':name,'age':age}
#     return result
# if __name__ == '__main__':
#     app.run(debug=True)
#this code for the serving templates
# from flask import Flask, request, render_template
# from datetime import datetime
# app = Flask(__name__)
# @app.route('/')
# def home ():
#     day_of_week = datetime.today().strftime('%A')
#     return render_template('index.html', day_of_week=day_of_week)
# @app.route('/api')
# def name ():
#     name = request.values.get('name')
#     age = request.values.get('age')
#     result = {'name':name,'age':age}
#     return result
# if __name__ == '__main__':
#     app.run(debug=True)
#this code for the Dynamic serving templates/
from flask import Flask, request, render_template
from datetime import datetime
app = Flask(__name__)
@app.route('/')
def home ():
    day_of_week = datetime.today().strftime('%A')
    current_time = datetime.now().strftime('%H:%M:%S')
    return render_template('index.html', day_of_week=day_of_week, current_time=current_time)
if __name__ == '__main__':
    app.run(debug=True)