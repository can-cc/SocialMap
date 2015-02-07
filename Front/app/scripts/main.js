/*global SocialMap2, $*/


window.SocialMap2 = {
    Models: {},
    Collections: {},
    Views: {},
    Routers: {},
    init: function () {
        'use strict';
        Backbone.emulateJSON = true;
        console.log('Hello from Backbone!');
        SocialMap2.baseDomain = '/api'


        var mapView = new SocialMap2.Views.MapView();
        mapView.render();
        var navigation = new SocialMap2.Views.Navigation();
        navigation.render();
        SocialMap2.Views.Navigation.checkLogin();
        SocialMap2.profile = new SocialMap2.Views.Profile();

        var router = new SocialMap2.Routers.MainRouter();
        Backbone.history.start();
    }
};

$(document).ready(function () {
    'use strict';
    SocialMap2.init();

    var xhr = (
        (
        window.XMLHttpRequest &&
        (window.location.protocol !== "file:" || !window.ActiveXObject)
        ) ?
            function () {
                return new window.XMLHttpRequest();
            } :
            function () {
                try {
                    return new window.ActiveXObject("Microsoft.XMLHTTP");
                } catch (e) {
                }
            }
    );
    function getCookies() {
        var request = xhr();
        request.open(
            "GET",
            (SocialMap2.baseDomain + '/hello')
        );
        request.send();
        //var data = request.responseText;
        //console.log(data);
        //if (data == 0) {
        //    location.href = "#signin";
        //} else {
        //    SocialMap2.profile.render('showProfile');
        //}
    }
    getCookies();



    function sayHello(){
        $.ajax({
            url: (SocialMap2.baseDomain + '/hello'),
            type: "GET",
            success: function(data){
            },
            error: function(){
                alert('Can not connect to the server,  Please check your network connection!\n' +
                'But you can use the map function!');
            },
            xhrFields: {
                withCredentials: true
            },
            crossDomain: true
        });
    }

    //var files;
    //
    //// Add events
    //$('#picFile').on('change', prepareUpload);
    //
    //// Grab the files and set them to our variable
    //function prepareUpload(event)
    //{
    //    files = event.target.files;
    //}
    //
    //$('#markPostCloseButton').on('click', function (){
    //    alert('fuckyou');
    //});
    //
    //$('#markPostButton2').on(
    //    'click',
    //    function(event)
    //    {
    //        event.stopPropagation(); // Stop stuff happening
    //        event.preventDefault(); // Totally stop stuff happening
    //
    //        var Picdata = new FormData();
    //        $.each(files, function(key, value)
    //        {
    //            Picdata.append(key, value);
    //        });
    //
    //        var POINT = SocialMap2.position.get('longitude') + ' ' + SocialMap2.position.get('latitude');
    //        var accuracy = SocialMap2.position.get('accuracy');
    //        var title = $('#markPostTitle').val();
    //        var text = $('#markPostText').val();
    //        $.ajax({
    //            url: (SocialMap2.baseDomain + '/markpost/'),
    //            type: "POST",
    //            data: {
    //                csrfmiddlewaretoken: $.cookie('csrftoken'),
    //                point: POINT,
    //                accuracy: accuracy,
    //                title: title,
    //                text: text,
    //                picture: Picdata
    //            },
    //            success: function(data){
    //            },
    //            error: function(data){
    //                alert('Certification may have problems, please log in again!');
    //            }
    //        });
    //    }
    //);

    $('#testb').on('click', function(){
        //var POINT = '113.494844 22.552605';
        //var mps = new SocialMap2.Models.MarkPostsCollection(POINT);
        //mps.fetch().success(function(collection, response, options){
        //    console.log(JSON.stringify(this));
        //    console.log(JSON.stringify(collection));
        //});
        //console.log(JSON.stringify(mps)+' ff');

    });


});
