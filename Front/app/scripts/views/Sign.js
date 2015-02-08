/*global SocialMap2, Backbone, JST*/

SocialMap2.Views = SocialMap2.Views || {};

(function () {
    'use strict';

    SocialMap2.Views.Sign = Backbone.View.extend({
        el: '#Panel',

        signUpTemp: JST['app/scripts/templates/signUp.ejs'],
        signInTemp: JST['app/scripts/templates/signIn.ejs'],

        tagName: 'div',

        id: '',

        className: '',

        events: {
            'click #signin': 'SignIn',
            'click #signup': 'SignUp'
        },

        initialize: function () {
            //Todo _BinAll
        },

        render: function (what) {
            if(what == 'signup'){
                this.ShowSignUp();
            }else if(what == 'signin'){
                this.ShowSignIn();
            }
        },

        ShowSignIn: function () {
            this.$el.html(this.signInTemp());
            $('#alert').hide();
        },

        ShowSignUp: function () {
            this.$el.html(this.signUpTemp());
        },

        SignIn: function () {
            $.ajax({
                url: (SocialMap2.baseDomain + '/api-auth/login/'),
                type: "POST",
                data: {
                    csrfmiddlewaretoken: $.cookie('csrftoken'),
                    username: $('#siUsername').val(),
                    password: $('#siPasswd').val(),
                    next: '/#profile',
                    submit: 'Log+in'
                },
                beforeSend: function(xhr) {
                    xhr.getResponseHeader('Set-Cookie');
                    xhr.setRequestHeader('X-CSRFToken', $.cookie('csrftoken'));
                },
                success: function(data){
                    SocialMap2.Views.Navigation.checkLogin(function(hasError){
                        if(hasError){
                            $('#alert').show();
                        }else{
                            window.location.href = "#profile"
                        }

                    });

                },
                error: function(){
                },
                xhrFields: {
                    withCredentials: true
                }
                //crossDomain: true
            });
        },

        SignUP: function () {
            $.ajax({
                url: (SocialMap2.baseDomain + '/user/info/'),
                type: "POST",
                data: {
                    csrfmiddlewaretoken: $.cookie('csrftoken'),
                    username: $('#suUsername').val(),
                    password: $('#suPasswd').val()
                },
                beforeSend: function (xhr) {
                    xhr.getResponseHeader('Set-Cookie');
                    xhr.setRequestHeader('X-CSRFToken', $.cookie('csrftoken'));
                },
                success: function (data) {
                    window.location.href = '#infoInit';
                },
                error: function () {
                    //Todo
                    //Todo
                    //Todo
                    //Todo
                    //Todo: Friendly Message!

                    alert('Sign Up Error!')
                },
                xhrFields: {
                    withCredentials: true
                }
            });
        }

    });

})();
/**
 * Created by tyan on 15-2-8.
 */
