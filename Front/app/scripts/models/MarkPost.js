/*global SocialMap2, Backbone*/

SocialMap2.Models = SocialMap2.Models || {};

(function () {
    'use strict';

    SocialMap2.Models.MarkPost = Backbone.Model.extend({

        initialize: function(id) {
            this.url = SocialMap2.baseDomain + '/markpost/pk/' + id;
        },

        defaults: {
        },

        validate: function(attrs, options) {
        },

        parse: function(response, options)  {
            this.set(response);
            return response;
        }
    });

})();
