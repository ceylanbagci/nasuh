function deleteConfirmationInit() {
  $(".btn-delete-confirmation").click(function() {
    event.preventDefault(); // prevent form submit
    var link = $(this).attr("href");
    Swal.fire({
      title: 'Bu kaydı silmek istediğinizden emin misiniz?',
      text: "",
      type: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Evet',
      cancelButtonText: "Hayır",
    }).then((result) => {
      if (result.value) {
        window.location.href = link;
      }
    })
  });
}

function successMessage(message) {
  Swal.fire({
  icon: 'success',
    title:"İşlem başarılı",
    text: message,
    type: 'success',
    // timer: 1500,
  });
}

function successMessageWithReload(message) {
  Swal.fire({
  icon: 'success',
    title:"İşlem başarılı",
    text: message,
    type: 'success',
    // timer: 1500,
  }).then((result) => {
      if (result.value) {
        location.reload();
      }
    });
}

function errorMessage(message){
  Swal.fire({
    icon: 'error',
    title: "Hatalı işlem",
    text: message,
    type: 'error',
    // timer: 1500,
  });
}

function errorMessageWithReload(message){
  Swal.fire({
    icon: 'error',
    title: "Hatalı işlem",
    text: message,
    type: 'error',
    // timer: 1500,
  }).then((result) => {
      if (result.value) {
        location.reload();
      }
    });
}

$(document).ready(function() {
    deleteConfirmationInit();
});