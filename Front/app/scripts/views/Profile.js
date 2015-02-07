/*global SocialMap2, Backbone, JST*/

SocialMap2.Views = SocialMap2.Views || {};

(function () {
    'use strict';

    SocialMap2.Views.Profile = Backbone.View.extend({
        el: '#Panel',

        signUpTemp: JST['app/scripts/templates/signUp.ejs'],
        signInTemp: JST['app/scripts/templates/signIn.ejs'],
        profileTemp: JST['app/scripts/templates/Profile.ejs'],

        tagName: 'div',

        id: '',

        className: '',

        events: {
            'click #signin': 'SignIn',
            'click #signup': 'SignUp'
        },

        initialize: function () {

        },

        render: function (what) {
            if(what == 'signup'){
                this.ShowSignUp();
            }else if(what == 'signin'){
                this.ShowSignIn();
            }else if(what == 'showProfile'){
                this.showProfile();
            }
        },


        showProfile: function() {
            this.$el.html(this.profileTemp());
            var userInformation = new SocialMap2.Models.UserInfomation();
            userInformation.fetch({url:SocialMap2.baseDomain + '/user/info/', success: (function(model, response, options){
                $('#nickName').val(model.get('nickName'));
                $('#description').val(model.get('personalDescription'));
                $('#phoneNumber').val(model.get('phoneNumber'));
                $('#city').val(model.get('city'));
                $('#birthday').val(model.get('birthday'));
                $('#school').val(model.get('school'));
                $('#interest').val(model.get('interest'));
                $('#cardId').val(model.get('cardId'));
                $('#nowCity').val(model.get('nowCity'));
                $('#publicMail').val(model.get('publicMail'));
            })});
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

        }

    });

})();
