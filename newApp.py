# import Flask class and create an instance for this class
from flask import Flask, render_template, request, url_for
from test_451_szw import figure_4_1_test_baseline_requirements, figure_4_2_test_baseline_requirements, figure_4_3_test_baseline_requirements, figure_4_4_test_baseline_requirements, figure_4_5_test_baseline_requirements, figure_4_6_test_baseline_requirements, figure_4_7_test_baseline_requirements, figure_4_8_test_baseline_requirements

# define the name of the application's module - app
app = Flask(__name__)
# make app know where to connect to the database

### perform test
def tester():
    section = request.form["section"]
    if section == '4':
        test = request.form["test"]
        category = request.form["category"]
        if test == "Ground Survival Low Temperature and Short Time Operating Low Temp Test":
            input1 = request.form["input1"]
            input2 = request.form["input2"]
            figure_4_1_test_baseline_requirements(category= category, input1=input1, input2=input2)
        elif test == "Ground Survival High Temperature and Short Time Operating High Temp Test":
            input1 = request.form["input1"]
            input2 = request.form["input2"]
            figure_4_3_test_baseline_requirements(category= category, input1=input1, input2=input2)
        elif test == "In-Flight Loss of Cooling Test":
            input1 = request.form["input1"]
            input2 = request.form["input2"]
            figure_4_5_test_baseline_requirements(category= category, cooling_category=input1, input=input2)
        else:
            input = request.form["input1"]
            if test == "Operating Low Temperature Test":
                figure_4_2_test_baseline_requirements(category= category, input=input)
            elif test == "Operating High Temperature Test":
                figure_4_4_test_baseline_requirements(category= category, input=input)
            elif test == "Altitude Test":
                figure_4_6_test_baseline_requirements(category= category, input=input)
            elif test == "Decompression Test":
                figure_4_7_test_baseline_requirements(category= category, input=input)
            elif test == "Overpressure Test":
                figure_4_8_test_baseline_requirements(category= category, input=input)

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        tester()
        return render_template("newIndex.html")
    else:
        return render_template("newIndex.html")

@app.route('/section', methods=['POST', 'GET'])
def process_section():
  if request.method == "POST":
    section = request.get_json()
    print(section[0]['section'])
    return section[0]['section']

@app.route('/category', methods=['POST', 'GET'])
def process_category():
  if request.method == "POST":
    category = request.get_json()
    print(category[0]['category'])
    if category[0]['category'] == 'A1':
        print('A1')
    return category[0]['category']

@app.route('/test', methods=['POST', 'GET'])
def process_test():
  if request.method == "POST":
    test = request.get_json()
    print(test[0]['test'])
    return test[0]['test']


if __name__ == '__main__':
    app.debug=True
    # app.run(debug=True, port=8080)
    app.run()
