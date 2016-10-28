$(function(){

  $(document).on('click', function(e){
        $(".lat").html(window.google.maps.lat);
        $(".lng").html(window.google.maps.lng);
  });

function initMap() {
  var myLatlng = new google.maps.LatLng(-34.7660894,-58.2112031); //coordenadas de Berazategui
  var mapOptions = {
    zoom: 15, //zoom de tu mapa
    center: myLatlng, //centrar tu mapa
    scrollwheel: false, //si colocas true en vez de false el usuario podrá hacer scroll dentro del mapa
    draggable: true, //esta opción es la manito que aparece y es usado para desplazarse en el mapa
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };
  var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

//Add listener

  google.maps.event.addListener(map, 'click', function(event) {
    placeMarker(event.latLng,map);

  });

function placeMarker(location,map) {
  var marker = new google.maps.Marker({
    position: location,
    animation:google.maps.Animation.DROP,
    icon:'../static/imagenes/icono-mapa.png', //icono de mapa
    map: map });
  //console.log();
  //infowindow.open(map,marker);
  window.google.maps.lat = marker.position.lat();
  window.google.maps.lng = marker.position.lng();
  $('#reclamo_alta input[name=latitud]').val(marker.position.lat());
  $('#reclamo_alta input[name=longitud]').val(marker.position.lng());
  }
}

google.maps.event.addDomListener(window, 'load', initMap);

$(".lat").html(window.google.maps.lat);
$(".lng").html(window.google.maps.lng);

});

//La funcion declarada en este js tiene que devolver dos valores, la longitud
//y la latitud.
