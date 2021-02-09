function changeHeaderInit() {
  // temanın css ile widgetin css birbirlerini etkiledikleri için bu düzeltmeye
  // ihtiyaç duyuldu.
  $("h2").replaceWith(function() {
    return '<h6 class="bg-light">' + $(this).text() + '</h6>';
  });
}

$(document).ready(function () {
  changeHeaderInit();
});
