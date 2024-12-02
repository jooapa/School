function dox() {
  var el = document.getElementById("dox");
  el.innerHTML = "Locating…";
  // get local langitude and latitude
  navigator.geolocation.getCurrentPosition(
    function (position) {
      var lat = position.coords.latitude;
      var lon = position.coords.longitude;
      el.innerHTML = "Latitude: " + lat + "<br>Longitude: " + lon;
    },
    function () {
      el.innerHTML = "Unable to retrieve your location";
    }
  );
}

document.getElementById("btn").addEventListener("click", dox);