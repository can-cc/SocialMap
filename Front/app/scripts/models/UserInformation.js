/*global SocialMap2, Backbone*/

SocialMap2.Models = SocialMap2.Models || {};

(function () {
    'use strict';

    SocialMap2.Models.UserInfomation = Backbone.Model.extend({
        url: SocialMap2.baseDomain + '/user/info/',

        initialize: function() {
        },

        defaults: {
            "nickName": null,
            "portrait": null,
            "personalDescription": null,
            "phoneNumber": null,
            "country": null,
            "province": null,
            "city": null,
            "birthday": null,
            "school": null,
            "schoolId": null,
            "interest": null,
            "cardId": null,
            "nowCity": null,
            "publicMail": null,
            "publicPhoneNumber": null,
            "QQ": null,
            "userType": null,
            "loginTimes": null,
            "hitTimes": null,
            "friendCount": null
        },

        validate: function(attrs, options) {
        },

        parse: function(response,  options)  {
            return response;
        }
    });

})();
