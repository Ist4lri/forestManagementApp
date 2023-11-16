document.addEventListener("DOMContentLoaded", function() {
            var mapOptions = {
                center: { lat: 43.072880123964794, lng: 5.851873641406551  },
                zoom: 12,
            };
            var map = new google.maps.Map(document.getElementById("map"), mapOptions);


               var marker = new google.maps.Marker({
            position: map.getCenter(),
            map: map,
            icon: 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'
        });
        });