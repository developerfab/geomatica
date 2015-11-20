$(function () {
  $('body').on('click','#mi_ubicacion', function(e) {
    obtenerUbicacion();
  });

});

function obtenerUbicacion() { 
  if (navigator.geolocation) {     
    navigator.geolocation.getCurrentPosition(mostrarUbicacion);
  } else { 
    alert("Error! El navegador no soporta Geolocalizacion.");//3 
  } 
}
function mostrarUbicacion(posicion){ 
  var latitud = posicion.coords.latitude; 
  var longitud = posicion.coords.longitude;
  var div = document.getElementById("ubicacion"); 

  $('#id_latitud').val(latitud);
  $('#id_longitud').val(longitud);
}