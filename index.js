// Note: This example requires that you consent to location sharing when
// prompted by your browser. If you see the error "The Geolocation service
// failed.", it means you probably did not give permission for the browser to
// locate you.
let map;
let pos;
let marker;

function initMap() {
    const image = {
      url: "https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png",
      // This marker is 20 pixels wide by 32 pixels high.
      size: new google.maps.Size(20, 32),
      // The origin for this image is (0, 0).
      origin: new google.maps.Point(0, 0),
      // The anchor for this image is the base of the flagpole at (0, 32).
      anchor: new google.maps.Point(0, 32),
    };
    const shape = {
      coords: [1, 1, 1, 20, 18, 20, 18, 1],
      type: "poly"
    };
    // Try HTML5 geolocation.
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          pos = {lat: position.coords.latitude, lng: position.coords.longitude};
          map = new google.maps.Map(document.getElementById("map"), {
            center: pos,
            zoom: 14,
          });
          marker = new google.maps.Marker({
            position: pos,
            map: map, 
            icon: image, 
            shape: shape,
          });
            $.ajax({
                    url: "/function_url",
                    type: 'POST',
                    data: JSON.stringify(pos),   // converts js value to JSON string
                    })
                    .done(function(result){     // on success get the return object from server
                        console.log(result)     // do whatever with it. In this case see it in console
                    })
        });
    } else {
      // Browser doesn't support Geolocation
      alert("Browser doesn't support!");
    }
}
