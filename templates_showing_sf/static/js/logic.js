var map = L.map("map", {
  center: [37.754135, -122.447331],
  zoom: 12});

var streetMap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
	attribution: "Map data &copy; <a href='https://www.openstreetmap.org/'>OpenStreetMap</a> contributors, <a href='https://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA</a>, Imagery © <a href='https://www.mapbox.com/'>Mapbox</a>",
	maxZoom: 18,
	id: "mapbox.streets",
	accessToken: API_KEY 
})
.addTo(map);

var prevLayerClicked = null;
var destination = null;

function onEachFeature(feature, layer) {
	layer.on({
		click: function(e){
			if (prevLayerClicked !== null) {
				prevLayerClicked.setStyle({
					weight: 2,
					opacity: 1,
					color: "#2d97d4",
				});
			}

			var layer = e.target;
			layer.setStyle({
				weight: 2,
				color: '#ff2400',
				dashArray: '',
			});

			if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
				layer.bringToFront();
			}
			prevLayerClicked = layer;
			destination = feature.properties.DISPLAY_NAME;
		}
	});
	layer.bindPopup('<h5>' + feature.properties.DISPLAY_NAME +'</h5>');
	
}


L.geoJSON(SF_Grid, {onEachFeature: onEachFeature, style: {color: "#2d97d4"}})
.on("click", function (event) {
	var clickedMarker = event.layer;
	console.log('i clicked this')
})
// .bindPopup("Popup content")
.addTo(map);

function changestarting() {
	document.getElementById("starting_id").value = destination;
}

function changedestination() {
	document.getElementById("destination_id").value = destination;
}
// console.log(uniq);

// var url = '/data_json';
// var static_url = '/static/data/san_francisco_censustracts.json';
// var features;
// var a = 0;

// d3.json(static_url).then(function(results) {
//   console.log(results);
//   features = results.features;
//   console.log(features[0].geometry.coordinates[0]);

//   for (var i = 0; i < features.length; i++) {
//     L.polygon(
//       features[i].geometry.coordinates[0]
//       , {
//         color: "yellow",
//         fillColor: "yellow",
//         fillOpacity: 0.75
//       }).addTo(map);

//   }
// });

