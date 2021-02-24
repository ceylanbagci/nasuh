function districtInit(){
  $("#id_city").change(function() {
    $.ajax({
        type:"GET",
        url:"/core/get_districts_from_city/".concat($(this).val()),
        success:function(data) {
            console.log(data);
          var district_list = $.parseJSON(data.district_list);
            console.log(district_list);
          $("#id_district").empty();
          for (var i = 0; i < district_list.length; i++) {
            $("#id_district").append(new Option(district_list[i].name, district_list[i].id));
          }
          console.log($("#id_district"));
        }
    });
  });
}

$(document).ready(function() {
    districtInit();
});