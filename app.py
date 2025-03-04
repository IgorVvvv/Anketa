from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('survey.html')

@app.route('/submit', methods=['POST'])
def submit():
   responses = request.form.to_dict()
   with open('responses.csv', mode='a', newline='', encoding='utf-8') as file:
       writer = csv.DictWriter(file, fieldnames=responses.keys())
       if file.tell() == 0:  # Проверка, если файл пустой
           writer.writeheader()
       writer.writerow(responses)
   return redirect(url_for('thank_you'))

@app.route('/thank_you')
def thank_you():
   return "Спасибо за участие в анкете!"

if __name__ == "__main__":
   app.run(debug=True)