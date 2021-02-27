function date_init(){
    $('#kt_datetimepicker_1').datetimepicker({
                    format: 'DD/MM/YYYY HH:mm',
                    locale: 'tr'
                });

    $('#kt_datetimepicker_2').datetimepicker({
                    format: 'DD/MM/YYYY HH:mm',
                    locale: 'tr'
                });
}

function handleClick(value) {
    document.getElementById("id_backgroundColor").setAttribute('value',value);
    document.getElementById("id_borderColor").setAttribute('value',value);
}

function radio_checked(){
    var val = document.getElementById("id_backgroundColor").value;
    console.log(val);
    if (val==='#3699ff'){
        document.getElementById("_primary").checked = true;
    }else if (val==='#ffa800'){
        console.log('warning');
        document.getElementById("_warning").checked = true;
    }else if (val==='#f64e60'){
        console.log('danger');
        document.getElementById("_danger").checked = true;
    }
}

jQuery(document).ready(function () {
	date_init();
	$('input[type=radio][name=radios2]').change(function(){
	    handleClick(this.value);
	});
	radio_checked();
    $('#kt_datetimepicker_1').on("change.datetimepicker", function(e) {
        $('#kt_datetimepicker_2').datetimepicker('date',e.date);
    });

});