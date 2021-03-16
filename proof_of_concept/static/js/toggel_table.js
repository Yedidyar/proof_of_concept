$(document).ready(function () {
  $("form").on("submit", function (event) {
    $.ajax({
      data: {
        velocity: $("#velocity").val(),
        angle: $("#angle").val(),
      },
      type: "POST",
      url: "/process",
    }).done(function (data) {
      if (data.error) {
        $("#error").text(data.error).show();
        $("#result").hide();
      } else {
        $("#h").text(data.h).show();
        $("#total_length").text(data.total_length).show();
        $("#total_time").text(data.total_time).show();
        $("#result").show();
        $("#error").hide();
      }
    });
    event.preventDefault();
  });
});
