function showPage() {
  document.getElementById("loader").style.display = "none";
  document.getElementById("game").style.display = "block";
}

window.onload = setTimeout(showPage, 1000)