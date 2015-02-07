/*global SocialMap2, Backbone*/

SocialMap2.Models = SocialMap2.Models || {};

(function () {
    'use strict';

    SocialMap2.Models.PositionModel = Backbone.Model.extend({

        url: '',

        initialize: function() {
        },

        defaults: {
            latitude:  "",
            longitude: "",
            accuracy:  "",
            timestamp: ""
        },

        validate: function(attrs, options) {
        },

        parse: function(response, options)  {
            return response;
        }
    });

})();
