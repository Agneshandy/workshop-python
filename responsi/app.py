from flask import Flask, render_template
app = Flask("Data_Diri")

@app.route('/')
def main():
    return render_template('index.html')

if "Data Diri" == "__main__":
    app.run()