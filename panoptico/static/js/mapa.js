var layer;

var fromProjection = new OpenLayers.Projection("EPSG:4326");   // Transform from WGS 1984
var toProjection   = new OpenLayers.Projection("EPSG:900913"); // to Spherical Mercator Projection

/* inicializa o mapa */
function initMapa(mapa) {   
		
	layer = new OpenLayers.Layer.OSM();
	
	mapa.addLayer(layer);
	
	mapa.setCenter(
	    new OpenLayers.LonLat(-8.429311180114722, 40.21088161169315).transform(
	        new OpenLayers.Projection("EPSG:4326"),
	        mapa.getProjectionObject()
	    ), 15
	); 
	 
}