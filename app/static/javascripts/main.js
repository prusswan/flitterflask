$( document ).ready(function() {

  $("form textarea.input-xlarge").keyup(function(){
    if($(this).val().length > 200){
      $(this).val($(this).val().substr(0, 200));
    }
  });

});
