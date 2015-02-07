/**
 * Created by tyan on 15-2-6.
 */

(function () {
    toBD09 = function (longitude, latitude) {
        var gcjloc = transformFromWGSToGCJ(longitude, latitude);
        var fedLoc = filter(gcjloc.lat, gcjloc.lng)
        return tes(fedLoc.lat, fedLoc.lng);
    };

    function filter(latitude, longitude){
        if (typeof (latitude) !== 'number') {
            var i = latitude.lastIndexOf('-');
            if (i > 0) {
                latitude = latitude.slice(0, i);
            }
        }
        if (typeof (longitude) !== 'number') {
            var j = longitude.lastIndexOf('.');
            if (j > 15) {
                longitude = longitude.slice(0, j);
            }
        }
        return {
            lng: longitude,
            lat: latitude
        }
    }

    var x_pi = Math.PI * 3000.0 / 180.0;
    function tes (latitude, longitude) {
        var x = longitude, y = latitude;
        var z = Math.sqrt(x * x + y * y) + 0.00002 * Math.sin(y * x_pi);
        var theta = Math.atan2(y, x) + 0.000003 * Math.cos(x * x_pi);
        return {
            lng: z * Math.cos(theta) + 0.0065,
            lat: z * Math.sin(theta) + 0.006
        }
    }

    function tesb (latitude, longitude) {
        var x = longitude, y = latitude;
        var z = Math.sqrt(x * x + y * y) + 0.00002 * Math.sin(y * x_pi);
        var theta = Math.atan2(y, x) + 0.000003 * Math.cos(x * x_pi);
        return {
            lng: z * Math.cos(theta) + 0.002,
            lat: z * Math.sin(theta) + 0.0085
        }
    }

    function tes2 (latitude, longitude) {
        var y = longitude - 0.0065, x = latitude - 0.006;
        var z = Math.sqrt(x * x + y * y) - 0.00002 * Math.sin(y * x_pi);
        var theta = Math.atan2(y, x) - 0.000003 * Math.cos(x * x_pi);
        return {
            lng: z * Math.cos(theta),
            lat : z * Math.sin(theta)
        }
    }

}());
