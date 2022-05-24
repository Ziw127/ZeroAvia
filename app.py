# import Flask class and create an instance for this class
from flask import Flask, render_template, request, send_file, url_for
from test_451_szw import figure_4_1_test_baseline_requirements, figure_4_2_test_baseline_requirements, figure_4_3_test_baseline_requirements, figure_4_4_test_baseline_requirements, figure_4_5_test_baseline_requirements, figure_4_6_test_baseline_requirements, figure_4_7_test_baseline_requirements, figure_4_8_test_baseline_requirements
from section6 import humidity_test
import os
import time
# define the name of the application's module - app
app = Flask(__name__)
# collect all the image paths
imagePath = []

# Obtain the test result(Image)

def testResult():
    section = request.form["section"]
    imageName = ""
    sectionName = ""
    if section == '4':
        sectionName = '4 Temperature and Altitude'
        test = request.form["test"]
        # category = request.form["category"]
        # test pass: operatelow, operatehigh, groundlow, gorundhigh, decompression, overpressure
        # test fail: altitude, in-flight
        testOutput = {
            "Ground Survival Low Temperature and Short Time Operating Low Temp Test": 'groundandoperatinglow',
            "Ground Survival High Temperature and Short Time Operating High Temp Test": 'groundandoperatinghigh',
            "In-Flight Loss of Cooling Test": 'LoC',
            "Operating Low Temperature Test": 'operatinglow',
            "Operating High Temperature Test": 'operatinghigh',
            "Altitude Test": 'Alt',
            "Decompression Test": 'decomp',
            "Overpressure Test": 'overpressure'
        }
        if test in testOutput:
            imageName = testOutput[test]
    # elif section == '6':
    #     sectionName = '6 Humidity'
    #     imageName = 'humidity'
    return (imageName, sectionName)


# perform test
def tester():
    image, sectionName = testResult()
    print("image" + image)
    print("sectionName" + sectionName)
    dir_path = 'static'
    for filename in os.listdir(dir_path):
        if filename.startswith(image):
            path = os.path.join(dir_path, filename)
            print("path" + path)
            os.remove(path)
    realTime = str(time.time()).split('.')[1]
    newImage = image + realTime + ".jpg"
    path = os.path.join(dir_path, newImage)
    print(path)
    imagePath.append(path)

    testName = "No Test for this part"
    section = request.form["section"]
    # print(section)
    if section == '4':
        test = request.form["test"]
        testName = test
        category = request.form["category"]
        if test == "Ground Survival Low Temperature and Short Time Operating Low Temp Test":
            input1 = request.form["input1"]
            input2 = request.form["input2"]
            figure_4_1_test_baseline_requirements(
                category=category, input1=input1, input2=input2, path=path)
        elif test == "Ground Survival High Temperature and Short Time Operating High Temp Test":
            input1 = request.form["input1"]
            input2 = request.form["input2"]
            figure_4_3_test_baseline_requirements(
                category=category, input1=input1, input2=input2, path=path)
        elif test == "In-Flight Loss of Cooling Test":
            input1 = request.form["input1"]
            input2 = request.form["input2"]
            figure_4_5_test_baseline_requirements(
                category=category, cooling_category=input1, input=input2, path=path)
        else:
            input = request.form["input1"]
            if test == "Operating Low Temperature Test":
                figure_4_2_test_baseline_requirements(
                    category=category, input=input, path=path)
            elif test == "Operating High Temperature Test":
                figure_4_4_test_baseline_requirements(
                    category=category, input=input, path=path)
            elif test == "Altitude Test":
                figure_4_6_test_baseline_requirements(
                    category=category, input=input, path=path)
            elif test == "Decompression Test":
                figure_4_7_test_baseline_requirements(
                    category=category, input=input, path=path)
            elif test == "Overpressure Test":
                figure_4_8_test_baseline_requirements(
                    category=category, input=input, path=path)

    elif section == '6':
        input = request.form['input1']
        humidity = humidity_test(input)
        humidity.set_category_variables()
        humidity.plot_equipment_category(path=path)

    return (newImage, sectionName, testName)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        Image, Section, Test = tester()
        return render_template("success.html", name=Image, section=Section, test=Test)
    else:
        return render_template("newIndex.html")

# only works when disabling cache


@app.route('/downloadNew', methods=['GET', 'POST'])
def download_image():
    if request.method == 'GET':
        path = imagePath[-1]
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
