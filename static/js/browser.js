$(document).ready(() => {
      $("tr").click(function(){
          attr_name = $(this).attr("name");
          name_parts = attr_name.split("|")
  
          $("#full_path").val(name_parts[0]);
          $("#click_type").val(name_parts[1]);
  
          $("#frmDirectory").trigger("submit");
      }); 
});