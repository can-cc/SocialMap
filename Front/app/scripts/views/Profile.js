/*global SocialMap2, Backbone, JST*/

SocialMap2.Views = SocialMap2.Views || {};

(function () {
    'use strict';

    SocialMap2.Views.Profile = Backbone.View.extend({
        el: '#Panel',

        profileTemp: JST['app/scripts/templates/Profile.ejs'],
        infoInitTemp: JST['app/scripts/templates/InfoInitInput.ejs'],

        tagName: 'div',

        id: '',

        className: '',

        events: {
            'click #IIIsubmit': 'submitInfo'
        },

        initialize: function () {

        },

        render: function (what) {
            if(what == 'showProfile'){
                this.showProfile();
            }else if(what == 'infoInit'){
                this.showInfoInit();
            }
        },


        showProfile: function() {
            SocialMap2.userInformation = new SocialMap2.Models.UserInfomation();
            SocialMap2.userInformation.fetch().success(function(model, response, options){
                SocialMap2.profile.$el.html(SocialMap2.profile.profileTemp(model));
            });
        },



        showInfoInit: function() {
            this.$el.html(this.infoInitTemp());
        },

        submitInfo: function() {
            $.ajax({
                url: (SocialMap2.baseDomain + '/user/info/'),
                type: "POST",
                data: {
                    csrfmiddlewaretoken: $.cookie('csrftoken'),
                    nickName: $('#IIInickName').val(),
                    personalDescription: $('#IIIdescription').val(),
                    phoneNumber: $('#IIIphoneNumber').val(),
                    city: $('#IIIcity').val(),
                    birthday: $('#IIIbirthday').val(),
                    school: $('#IIIschool').val(),
                    interest: $('#IIIinterest').val(),
                    cardId: $('#IIIcardId').val(),
                    nowCity: $('#IIInowCity').val(),
                    publicMail: $('#IIIpublicMail').val()
                },
                beforeSend: function(xhr) {
                    xhr.setRequestHeader('X-CSRFToken', $.cookie('csrftoken'));
                },
                success: function(data){
                    window.location.href = '/#profile';
                },
                error: function(){
                    //Todo change this
                    alert('submit Info Error!')
                },
                xhrFields: {
                    withCredentials: true
                }
                //crossDomain: true
            });
        }

    });

})();
