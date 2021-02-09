function labelStyle(){

  $('.label-styled').each(function(){
        var value = $(this).data("vll");
        var x = []
        x.push(value);
        if ( value == '1') {
            $(this).addClass('label-light-success');
        }else if ( value == '2') {
            $(this).addClass('label-light-danger');
        }else if ( value == '3') {
            $(this).addClass('label-light-warning');
        }else if ( value == '4') {
            $(this).addClass('label-light-primary');
        }else if ( value == '5') {
            $(this).addClass('label-dark');
        }else{
            $(this).addClass(' ');
        }
   });

};



jQuery(document).ready(function () {
	labelStyle();
});