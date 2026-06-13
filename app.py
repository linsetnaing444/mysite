from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # ဒီနေရာမှာ သင့် HTML ဖိုင်ကို ခေါ်လိုက်တာပါ
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

