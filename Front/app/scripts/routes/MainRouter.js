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
            'signin': 'SignIn'
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
            $("#Map").hide();
            $("#Panel").show();
            SocialMap2.profile.render('showProfile');
        },

        SignUp: function() {
            $("#Map").hide();
            $("#Panel").show();
            SocialMap2.profile.render('signup');
        },

        SignIn: function() {
            $("#Map").hide();
            $("#Panel").show();
            SocialMap2.profile.render('signin');
        }
    });

})();
