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

function save_cunselling_user() {
  const csrftoken = $("[name=csrfmiddlewaretoken]").val();
    $.ajax({
      type: "POST",
      url: "/counselling/create",
      headers:{"X-CSRFToken": csrftoken},
      data: { 
          'name': $('#name').val(),
          'email': $('#email').val(),
          'number': $('#number').val(),
          'message': $('#message').val(),
      },
      success: function (response) {
        $('#exampleModal').modal('toggle')
          Swal.fire({
              icon: 'success',
              title: 'Success',
              text: `${response.data.name} our mentor will get in touch with you as soon as possible`,
            })
          $('#name').val("");
          $('#email').val("");
          $('#number').val("");
          $('#message').val("");
      },
      error: function () {
        alert("Something went wrong");
      },
    });
  }