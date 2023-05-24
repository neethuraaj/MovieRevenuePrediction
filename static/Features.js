document.addEventListener("DOMContentLoaded", function() {
  var currentYear = new Date().getFullYear();
  var yearSelect = document.getElementById("year");

  for (var year = 2023; year <= 2050; year++) {
    var option = document.createElement("option");
    option.value = year;
    option.text = year;
    yearSelect.appendChild(option);
  }
});