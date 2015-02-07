/*global SocialMap2, Backbone, JST*/

SocialMap2.Views = SocialMap2.Views || {};

(function () {
    'use strict';

    SocialMap2.Views.Navigation = Backbone.View.extend({
        el: '#navigation',

        template: JST['app/scripts/templates/Navigation.ejs'],

        tagName: '',

        id: '',

        className: '',

        events: {
            //'click #profileNav': 'toProfile'
        },

        initialize: function () {
            //this.listenTo(this.model, 'change', this.render);
        },

        render: function () {
            this.$el.html(this.template());
            $('#profileNav').hide();
        }


    });

    SocialMap2.Views.Navigation.profileChange = function(i, username){
        if(i==1){
            $('#signNav').hide();
            $('#profileNav').text(username);
            $('#profileNav').show();
        }else{
            $('#profileNav').hide();
            $('#signNav').show();
        }
    };

    SocialMap2.Views.Navigation.checkLogin = function(callback){
        $.ajax({
            url: (SocialMap2.baseDomain + '/hello'),
            type: "GET",
            dataType: 'text',
            beforeSend: function(xhr) {
                xhr.getResponseHeader('Set-Cookie');
            },
            success: function(data){
                if (data == 0) {
                    if(callback)
                        callback(true);
                    //$('#alert').show();
                }else{
                    SocialMap2.loginError = false;
                    data = eval( '(' + data + ')' );
                    SocialMap2.Views.Navigation.profileChange(1, data.username);
                    if(callback)
                        callback(false);
                    //window.location.href = "#profile";
                }
            },
            error: function(data){
            },
            xhrFields: {
                withCredentials: true
            }
        });
    }
})();
