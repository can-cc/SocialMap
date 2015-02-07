/*global SocialMap2, Backbone, JST*/

SocialMap2.Views = SocialMap2.Views || {};

(function () {
    'use strict';

    SocialMap2.Views.MapView = Backbone.View.extend({
        //events: {
        //    'getPosition': 'getPosition'
        //},

        initialize: function () {
            SocialMap2.baiduMap = new BMap.Map('Map');
            this.moveCenter = function(position) {
                var latitude = position.coords.latitude;
                var longitude = position.coords.longitude;
                var accuracy = position.coords.accuracy;
                var timestamp = position.coords.timestamp;

                SocialMap2.position = new SocialMap2.Models.PositionModel({
                    latitude:  latitude,
                    longitude: longitude,
                    accuracy:  accuracy,
                    timestamp: timestamp
                });

                var POINT = longitude + ' ' + latitude;
                console.log(POINT);
                $.ajax({
                    url: (SocialMap2.baseDomain + '/track/'),
                    type: "POST",
                    data: {
                        footPoint: POINT,
                        accuracy: accuracy
                    },
                    beforeSend: function(xhr) {
                        xhr.setRequestHeader('X-CSRFToken', $.cookie('csrftoken'));
                    },
                    success: function(data){
                    },
                    error: function(data){
                    },
                    xhrFields: {
                        withCredentials: true
                    }
                });

                var bd09 = toBD09(longitude, latitude);
                console.log(bd09.lng + ' ' + bd09.lat);
                var point = new BMap.Point(bd09.lng, bd09.lat);
                SocialMap2.baiduMap.centerAndZoom(point, 15);
                SocialMap2.baiduMap.addControl(new BMap.ZoomControl());
                SocialMap2.baiduMap.addControl(new BMap.ScaleControl());
                //SocialMap2.baiduMap.setCurrentCity("中山");
                var marker = new BMap.Marker(point);  // 创建标注
                SocialMap2.baiduMap.addOverlay(marker);               // 将标注添加到地图中
            };
            this.getPositionError = function() {
                alert('can\'t get position, please check setting!')
            };
            this.getPosition = function() {
                navigator.geolocation.getCurrentPosition(this.moveCenter, this.getPositionError, {enableHighAccuracy: true});
            };
            //SocialMap2.baiduMap.addEventListener('dragend', function () {
            //    //alert(SocialMap2.baiduMap.getCenter().lng + '\n' + SocialMap2.baiduMap.getCenter().lat);
            //    var POINT = SocialMap2.position.get('longitude') + ' ' + SocialMap2.position.get('latitude');
            //    var accuracy = SocialMap2.position.get('accuracy');
            //    $.ajax({
            //        url: ('/markpost/' + POINT),
            //        type: "GET",
            //        success: function(data){
            //            var openInfoWindow = function(infoWin) {
            //                return function() {
            //                    this.openInfoWindow(infoWin);
            //                };
            //            };
            //            for(var i=0; i<data.length; i++){
            //                var mark = data[i];
            //                var pointString = mark['point'];
            //                var start = pointString.indexOf('(');
            //                var end = pointString.indexOf(')');
            //                var points = pointString.slice(start+1, end-1);
            //                points = points.split(' ');
            //                var longitude = points[0];
            //                var latitude = points[1];
            //                var point = new BMap.Point(longitude, latitude);
            //                var icon = new BMap.Icon('images/msgMark.png', new BMap.Size(25, 45));
            //                var marker = new BMap.Marker(point, {
            //                    icon: icon
            //                });
            //                SocialMap2.baiduMap.addOverlay(marker);
            //                var infoWindow = new BMap.InfoWindow("<p>" + mark['title'] + "</p><p>" + mark['text'] + "</p>", {
            //                    enableMessage: true
            //                });
            //                marker.addEventListener("click", openInfoWindow(infoWindow));
            //            }
            //        },
            //        error: function(){
            //            alert('Please check your network connection!');
            //        }
            //    });
            //});


            function markPostControl(){
                this.defaultAnchor = BMAP_ANCHOR_TOP_LEFT;
                this.defaultOffset = new BMap.Size(20, 20);
            }
            function getPostControl(){
                this.defaultAnchor = BMAP_ANCHOR_TOP_RIGHT;
                this.defaultOffset = new BMap.Size(20, 20);
            }

            markPostControl.prototype = new BMap.Control();
            markPostControl.prototype.initialize = function(map){
                var postButton = document.createElement('button');
                postButton.innerHTML = 'Post';
                postButton.setAttribute(['type'], ['button']);
                postButton.setAttribute(['class'], ['btn btn-primary']);
                postButton.setAttribute(['data-toggle'], ['modal']);
                //postButton.setAttribute(['data-target'], ['#ModalPanel2']);
                postButton.addEventListener('click', function(){
                    $('#ModalPanel').modal();
                   var pfView = new SocialMap2.Views.PostForm();
                   pfView.render();
                });
                var div = document.createElement('div');
                div.appendChild(postButton);
                map.getContainer().appendChild(div);
                return div;
            }
            getPostControl.prototype = new BMap.Control();
            getPostControl.prototype.initialize = function(map){
                var getpostButton = document.createElement('button');
                getpostButton.innerHTML = 'Get';
                getpostButton.setAttribute(['type'], ['button']);
                getpostButton.setAttribute(['class'], ['btn btn-primary']);
                getpostButton.onclick = function(e){
                    var POINT = SocialMap2.position.get('longitude') + ' ' + SocialMap2.position.get('latitude');
                    var accuracy = SocialMap2.position.get('accuracy');
                    //var mps = new SocialMap2.Models.MarkPostsCollection(POINT);
                    //mps.fetch().success(function(collection, response, options){
                    //
                    //    var openInfoWindow = function(infoWin) {
                    //        return function() {
                    //            this.openInfoWindow(infoWin);
                    //        };
                    //    }
                    //    console.log(typeof(collection));
                    //    var bubbles = collection.toJSON();
                    //    for(var bi=0; bi<bubbles.length; bi++){
                    //        var bubble = bubbles[bi];
                    //        var id = bubble['id'];
                    //        var portrait = bubble['userInfo']['portrait'];
                    //        var i = portrait.lastIndexOf('.');
                    //        var portraitBubble = portrait.slice(0, i-1) + '_MB.jpg';
                    //        var pointString = bubble['point'];
                    //        var start = pointString.indexOf('(');
                    //        var end = pointString.indexOf(')');
                    //        var points = pointString.slice(start+1, end-1);
                    //        points = points.split(' ');
                    //        var longitude = points[0];
                    //        var latitude = points[1];
                    //        var point = new BMap.Point(longitude, latitude);
                    //        var icon = new BMap.Icon(portraitBubble, new BMap.Size(40, 40));
                    //        var marker = new BMap.Marker(point, {
                    //            icon: icon
                    //        });
                    //        marker.id = id;
                    //        SocialMap2.baiduMap.addOverlay(marker);
                    //        marker.addEventListener("click", function(){
                    //            alert(this.id);
                    //        });
                    //    }
                    //});

                    $.ajax({
                        url: (SocialMap2.baseDomain + '/markpost/' + POINT),
                        type: "GET",
                        success: function(data){
                            var openInfoWindow = function(infoWin) {
                                return function() {
                                    this.openInfoWindow(infoWin);
                                };
                            };

                            for(var ii=0; ii<data.length; ii++){
                                var bubble = data[ii];
                                var id = bubble['id'];
                                console.log(id);
                                var portrait = bubble['userInfo']['portrait'];
                                var i = portrait.lastIndexOf('.');
                                var portraitBubble = portrait.slice(0, i) + '_MB.png';
                                var pointString = bubble['point'];
                                var start = pointString.indexOf('(');
                                var end = pointString.indexOf(')');
                                var points = pointString.slice(start+1, end-1);
                                points = points.split(' ');
                                var longitude = points[0];
                                var latitude = points[1];
                                var bd09 = toBD09(longitude, latitude);
                                var point = new BMap.Point(bd09.lng, bd09.lat);
                                var icon = new BMap.Icon(portraitBubble, new BMap.Size(40, 40));
                                var marker = new BMap.Marker(point, {
                                    icon: icon
                                });
                                marker.id = id;
                                SocialMap2.baiduMap.addOverlay(marker);
                                marker.addEventListener('click', function(){
                                    var markpost = new SocialMap2.Models.MarkPost(this.id);
                                    markpost.fetch().success(function (markpost, response, options) {
                                        console.log(markpost.title);
                                        var mpshow = new SocialMap2.Views.MPShow({model: markpost});
                                        mpshow.render();
                                    });
                                    $('#ModalPanel').modal();

                                });
                            }
                        },
                        error: function(){
                            alert('Please check your network connection!');
                        }
                    });
                }
                var div = document.createElement('div');
                div.appendChild(getpostButton);
                map.getContainer().appendChild(div);
                return div;
            }
            var markCtrl = new markPostControl();
            SocialMap2.baiduMap.addControl(markCtrl);

            var getmarkCtrl = new getPostControl();
            SocialMap2.baiduMap.addControl(getmarkCtrl);
        },

        render: function () {
            this.getPosition();
        }

    });

})();
