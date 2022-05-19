# import Flask class and create an instance for this class
from flask import Flask, render_template, request, send_file, url_for
from test_451_szw import figure_4_1_test_baseline_requirements, figure_4_2_test_baseline_requirements, figure_4_3_test_baseline_requirements, figure_4_4_test_baseline_requirements, figure_4_5_test_baseline_requirements, figure_4_6_test_baseline_requirements, figure_4_7_test_baseline_requirements, figure_4_8_test_baseline_requirements
import os
# define the name of the application's module - app
app = Flask(__name__)
# make app know where to connect to the database
imageResult = []

# Obtain the test result(Image)


def testResult():
    section = request.form["section"]
    imageName = ""
    sectionName = ""
    if section == '4':
        sectionName = '4.0 Temperature and Altitude'
        test = request.form["test"]
        # category = request.form["category"]
        # test pass: operatelow, operatehigh, groundlow, gorundhigh, decompression, overpressure
        # test fail: altitude, in-flight
        testOutput = {
            "Ground Survival Low Temperature and Short Time Operating Low Temp Test": 'groundandoperatinglow.jpg',
            "Ground Survival High Temperature and Short Time Operating High Temp Test": 'groundandoperatinghigh.jpg',
            "In-Flight Loss of Cooling Test": 'LoC.jpg',
            "Operating Low Temperature Test": 'operatinglow.jpg',
            "Operating High Temperature Test": 'operatinghigh.jpg',
            "Altitude Test": 'Alt.jpg',
            "Decompression Test": 'decomp.jpg',
            "Overpressure Test": 'overpressure.jpg'
        }

        if test in testOutput:
            imageName = testOutput[test]
    return (imageName, sectionName)


# perform test
def tester():
    image, section = testResult()
    dir_path = 'static'
    if image in os.listdir(dir_path):
        path = os.path.join(dir_path, image)
        os.remove(path)

    section = request.form["section"]
    if section == '4':
        test = request.form["test"]
        category = request.form["category"]
        if test == "Ground Survival Low Temperature and Short Time Operating Low Temp Test":
            input1 = request.form["input1"]
            input2 = request.form["input2"]
            figure_4_1_test_baseline_requirements(
                category=category, input1=input1, input2=input2)
        elif test == "Ground Survival High Temperature and Short Time Operating High Temp Test":
            input1 = request.form["input1"]
            input2 = request.form["input2"]
            figure_4_3_test_baseline_requirements(
                category=category, input1=input1, input2=input2)
        elif test == "In-Flight Loss of Cooling Test":
            input1 = request.form["input1"]
            input2 = request.form["input2"]
            figure_4_5_test_baseline_requirements(
                category=category, cooling_category=input1, input=input2)
        else:
            input = request.form["input1"]
            if test == "Operating Low Temperature Test":
                figure_4_2_test_baseline_requirements(
                    category=category, input=input)
            elif test == "Operating High Temperature Test":
                figure_4_4_test_baseline_requirements(
                    category=category, input=input)
            elif test == "Altitude Test":
                figure_4_6_test_baseline_requirements(
                    category=category, input=input)
            elif test == "Decompression Test":
                figure_4_7_test_baseline_requirements(
                    category=category, input=input)
            elif test == "Overpressure Test":
                figure_4_8_test_baseline_requirements(
                    category=category, input=input)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # obtain the test result and delete the previous test result.
        # image, Section = testResult()
        # dir_path = 'static'
        # if image in os.listdir(dir_path):
        #     path = os.path.join(dir_path, image)
        #     os.remove(path)
        # do test
        tester()
        Image, Section = testResult()
        path = os.path.join('static', Image)
        imageResult.append(path)
        return render_template("success.html", name=Image, section=Section)
    else:
        return render_template("newIndex.html")


@app.route('/downloadNew', methods=['GET', 'POST'])
def download_image():
    if request.method == 'GET':
        path = imageResult[-1]
        print(path)
        return send_file(path, as_attachment=True)


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
    app.debug = True
    # app.run(debug=True, port=8080)
    app.run()
