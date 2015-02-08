/*global SocialMap2, Backbone*/

SocialMap2.Models = SocialMap2.Models || {};

(function () {
    'use strict';

    SocialMap2.Models.UserInfomation = Backbone.Model.extend({
        url: '/api/user/info/',

        initialize: function() {
        },

        defaults: {
        },

        validate: function(attrs, options) {
        },

        parse: function(response,  options)  {
            this.set(response);
            return response;
        }
    });

})();
