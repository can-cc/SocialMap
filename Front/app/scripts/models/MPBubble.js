/*global SocialMap2, Backbone*/

SocialMap2.Models = SocialMap2.Models || {};

(function () {
    'use strict';

    SocialMap2.Models.MPBubble = Backbone.Model.extend({

        url: '',

        initialize: function() {
        },

        defaults: {
        },

        validate: function(attrs, options) {
        },

        parse: function(response, options)  {
            return response;
        }
    });

})();
