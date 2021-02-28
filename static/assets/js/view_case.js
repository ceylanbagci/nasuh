
function labelStyle(){
var element = $('#btn-styled')
 var value = $('#btn-styled').data('id');
    if ( value == '1') {
            element.addClass('btn-light-success');
        }else if ( value == '2') {
            element.addClass('btn-light-danger');
        }else if ( value == '3') {
            element.addClass('btn-light-warning');
        }else if ( value == '4') {
            element.addClass('btn-light-primary');
        }else if ( value == '5') {
            element.addClass('btn-dark');
        }else{
            element.addClass(' btn-secondary');
        }

};



jQuery(document).ready(function () {
	labelStyle();
});