$(function(){

  // Esta función inicializa el mapa con los valores de Bera
  function initMap() {
    var myLatlng = new google.maps.LatLng(-34.7660894,-58.2112031); //coordenadas de Berazategui
    var mapOptions = {
      zoom: 15, //zoom de tu mapa
      center: myLatlng, //centrar tu mapa
      scrollwheel: false, //si colocas true en vez de false el usuario podrá hacer scroll dentro del mapa
      draggable: true, //esta opción es la manito que aparece y es usado para desplazarse en el mapa
      mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    // Me guardo el mapa
    var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
    // Acá voy a mantener el último marker agregado, para solo tener uno
    var lastMarker = null;

    // Agregar una escucha al click sobre el mapa
    google.maps.event.addListener(map, 'click', function(event) {
      placeMarker(event.latLng,map);
    });

    function placeMarker(location,map) {
      // Borrar el marker anterior si lo hubiera
      if (lastMarker) {
        lastMarker.setMap(null);
      }
      // Colocar un nuevo marker en donde se dio click
      lastMarker = new google.maps.Marker({
        position: location,
        animation:google.maps.Animation.DROP,
        icon:'../static/imagenes/icono-mapa.png', //icono de mapa
        map: map });
      // Guardar las coordenadas del marker en los campos ocultos del formulario
      $('#reclamo_alta input[name=latitud]').val(lastMarker.position.lat());
      $('#reclamo_alta input[name=longitud]').val(lastMarker.position.lng());
    }
  }
  
  // Cuando se carga el sitio completamente, entonces se inicializa el mapa
  google.maps.event.addDomListener(window, 'load', initMap);
});
