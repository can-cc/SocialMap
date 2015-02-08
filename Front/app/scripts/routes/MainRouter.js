/*global SocialMap2, Backbone*/

SocialMap2.Routers = SocialMap2.Routers || {};

(function () {
    'use strict';
    //var map = new BMap.Map("Map");

    //var mapView = new SocialMap2.Views.MapView();

    SocialMap2.Routers.MainRouter = Backbone.Router.extend({
        routes: {
            '': 'Map',
            'map': 'Map',
            'mymp': 'mymp',
            'friends': 'Friends',
            'message': 'Message',
            'profile': 'Profile',
            'signup': 'SignUp',
            'signin': 'SignIn',
            'infoInit': 'infoInit'
        },

        infoInit: function () {
            if(!SocialMap2.profile){
                SocialMap2.profile = new SocialMap2.Views.Profile();
            }
            $("#Map").hide();
            $("#Panel").show();
            SocialMap2.profile.render('infoInit');
        },

        mymp: function() {
            var umps = new SocialMap2.Collections.UserMarkPosts();
            umps.fetch().success(function(collection, response, options){
                if(SocialMap2.userMP){SocialMap2.userMP.cleanup();}
                SocialMap2.userMP = new SocialMap2.Views.UserMP({collection: collection});
                SocialMap2.userMP.render();
                $("#Map").hide();
                $("#Panel").show();
            });
        },

        Map: function() {
            if(!SocialMap2.mapView) {
                SocialMap2.mapView = new SocialMap2.Views.MapView();
            }
            SocialMap2.mapView.render();
            function AdjustSize(){
                var bodyHeight = $( window ).height();
                var bodyWidth = $( window ).width();
                $("#Map").height( (bodyHeight * 0.8) );
                $("#Map").width( (bodyWidth * 0.9) );
            }
            AdjustSize();
            $("#Map").show();
            $("#Panel").hide();
        },

        Friends: function() {

        },

        Message: function() {

        },

        Profile: function() {
            if(!SocialMap2.profile){
                SocialMap2.profile = new SocialMap2.Views.Profile();
            }
            $.ajax({
                url: (SocialMap2.baseDomain + '/hasinfo/'),
                type: "GET",
                beforeSend: function(xhr) {
                    xhr.setRequestHeader('X-CSRFToken', $.cookie('csrftoken'));
                },
                success: function(data){
                    if(data.hasInfo==1){
                        SocialMap2.profile.render('showProfile');
                    }else{
                        window.location.href = '#infoInit';
                    }
                },
                error: function(){
                },
                xhrFields: {
                    withCredentials: true
                }
            });


            $("#Map").hide();
            $("#Panel").show();
        },

        SignUp: function() {
            if(!SocialMap2.Sign){
                SocialMap2.Sign = new SocialMap2.Views.Sign();
            }
            $("#Map").hide();
            $("#Panel").show();
            SocialMap2.Sign.render('signup');
        },

        SignIn: function() {
            if(!SocialMap2.Sign){
                SocialMap2.Sign = new SocialMap2.Views.Sign();
            }
            $("#Map").hide();
            $("#Panel").show();
            SocialMap2.Sign.render('signin');
        }
    });

})();
