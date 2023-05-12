function addNewsLetter() {
const csrftoken = $("[name=csrfmiddlewaretoken]").val();
  $.ajax({
    type: "POST",
    url: "/news-letter/create",
    headers:{"X-CSRFToken": csrftoken},
    data: { 
        'name': $('#id_name').val(),
        'email': $('#id_email').val(),
        'course': $('#id_course').val() 
    },
    success: function (response) {
        Swal.fire({
            icon: 'success',
            title: 'Success',
            text: 'News letter subscribed successfully!',
          })
        $('#id_name').val("");
        $('#id_email').val("");
        $('#id_course').val("");
    },
    error: function () {
      alert("No Data Found to delete");
    },
  });
}