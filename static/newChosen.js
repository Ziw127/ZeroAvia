function chooseSection(){
    var section = document.getElementById("selectedSection");
    section = section.value;
    var server_data = [
  {"section": section}
 ];
 $.ajax({
   type: "POST",
   url: "/section",
   data: JSON.stringify(server_data),
   contentType: "application/json",
   dataType: 'json',
   success: function(result) {
     console.log(result);
   }
 });
   var category = document.getElementById("selectedCategory");
   var test = document.getElementById("selectedTest");


   if (test.classList.contains("hidden") == false){
        test.classList.add("hidden");
   }
   if (category.classList.contains("hidden") == false) {
        category.classList.add("hidden");
   }


   if (section == 4) {
    if (test.classList.contains("hidden") == true){
        test.classList.remove("hidden");
      }
    if (category.classList.contains("hidden") == true) {
        category.classList.remove("hidden");
      }
    }
   else {
      console.log("something happened")
      }
   console.log(test.value)
   console.log(category.value)
   console.log(section)
   inputs(test.value, category.value, section);

}

function inputs(test, category, section) {
    input1 = document.getElementById("input1");
    input2 = document.getElementById("input2");
    input3 = document.getElementById("input3");
    input4 = document.getElementById("input4");
    input5 = document.getElementById("input5");
    input6 = document.getElementById("input6");
    input7 = document.getElementById("input7");

    if (input1.classList.contains("hidden") == false) {
        input1.classList.add("hidden");
    }
    if (input2.classList.contains("hidden") == false) {
        input2.classList.add("hidden");
    }
    if (input3.classList.contains("hidden") == false) {
        input3.classList.add("hidden");
    }
    if (input4.classList.contains("hidden") == false){
        input4.classList.add("hidden");
    }
    if (input5.classList.contains("hidden") == false) {
        input5.classList.add("hidden");
    }
    if (input6.classList.contains("hidden") == false) {
        input6.classList.add("hidden");
    }
    if (input7.classList.contains("hidden") == false) {
        input7.classList.add("hidden");
    }
    console.log("before if")
    console.log(test)
    console.log(category)
    if (section == "4") {
        if (test == "Ground Survival Low Temperature and Short Time Operating Low Temp Test"){
            console.log("inside if")
            if (category == "A4" || category == "B3" || category == "C3"){
                document.getElementById("input1").classList.remove("hidden");
                document.getElementById("input2").classList.remove("hidden");
                console.log("A4 if statement")
            }
            if (category == "B4" || category == "C4"){
                document.getElementById("input1").classList.remove("hidden");
            }
        }
        else if (test == "Ground Survival High Temperature and Short Time Operating High Temp Test"){
            console.log("inside if")
            if (category == "A4" || category == "B3" || category == "C3" || category == "D3" || category == "E2" || category == "F3"){
                document.getElementById("input1").classList.remove("hidden");
                document.getElementById("input2").classList.remove("hidden");
                console.log("A4 if statement")
            }
            if (category == "B4" || category == "C4" || category == "E1"){
                document.getElementById("input1").classList.remove("hidden");
            }
        }

        // need to finish
        else if (test == "Operating Low Temperature Test"){
            if (category == "B4" || category == "C4") {
                document.getElementById("input1").classList.remove("hidden");
            }
        }
        else if (test == "Operating High Temperature Test"){
            if (category == "A4" || category == "B3" || category == "B4" || category == "C3" || category == "C4" || category == "D3" || category == "E1" || category == "E2" || category == "F3") {
                document.getElementById("input1").classList.remove("hidden");
            }
        }
        else if (test == "In-Flight Loss of Cooling Test"){
                document.getElementById("input1").classList.remove("hidden");
            if (category == "A4" || category == "B3" || category == "B4" || category == "C3" || category == "C4" || category == "D3" || category == "E1" || category == "E2" || category == "F3") {
                document.getElementById("input2").classList.remove("hidden");
            }
        }
        else if (test == "Decompression Test"){
            if (category == "A1" || category == "A2" || category == "A3" || category == "A4"){
                document.getElementById("input1").classList.remove("hidden");
            }
        }
        else if (test == "Overpressure Test"){
            if (category == "A1" || category == "A2" || category == "A3" || category == "A4"){
                document.getElementById("input1").classList.remove("hidden");
            }
        }
    }
    if (section == "6") {
        document.getElementById("input1").classList.remove("hidden");
    }
}



function chooseCategory(){
    var category = document.getElementById("selectedCategory");
    category = category.value;
    var server_data = [
  {"category": category}
 ];
 $.ajax({
   type: "POST",
   url: "/category",
   data: JSON.stringify(server_data),
   contentType: "application/json",
   dataType: 'json',
   success: function(result) {
     console.log(result);
   }
 });
 inputs(document.getElementById("selectedTest").value, category, document.getElementById("selectedSection").value);
}

function chooseTest(){
    var test = document.getElementById("selectedTest");
    test = test.value;
    var server_data = [
  {"test": test}
 ];
 $.ajax({
   type: "POST",
   url: "/test",
   data: JSON.stringify(server_data),
   contentType: "application/json",
   dataType: 'json',
   success: function(result) {
     console.log(result);
   }
 });

 if (test == "Decompression Test") {
    for (let i = 5; i < 21; i++) {
            document.getElementById("selectedCategory").options[i].disabled = true

    }
 }

 else if (test == "Overpressure Test") {
    for (let i = 5; i < 21; i++) {
            document.getElementById("selectedCategory").options[i].disabled = true

    }
 }

 else {
    for (let i = 5; i < 21; i++) {
            document.getElementById("selectedCategory").options[i].disabled = false

    }
 }

 inputs(test, document.getElementById("selectedCategory").value, document.getElementById("selectedSection").value);
}