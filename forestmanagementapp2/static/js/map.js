document.addEventListener("DOMContentLoaded", function() {
            var mapOptions = {
                center:  { lat: latitude, lng: longitude },
                zoom: 12,
            };
            var map = new google.maps.Map(document.getElementById("map"), mapOptions);


               var marker = new google.maps.Marker({
            position: map.getCenter(),
            map: map,
            icon: 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'
        });
        });