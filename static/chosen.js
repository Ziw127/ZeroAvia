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
}