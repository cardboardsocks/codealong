from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['textinput']
        with open('user_data.txt', 'a') as f:
            f.write(user_input + '\n')
        return render_template('success.html', data=user_input)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) 
