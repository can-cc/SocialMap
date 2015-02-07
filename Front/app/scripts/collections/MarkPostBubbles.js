/*global define*/

SocialMap2.Collections = SocialMap2.Collections || {};

(function () {
    'use strict';

    SocialMap2.Models.MarkPostsCollection = Backbone.Collection.extend({
        initialize: function(POINT) {
            this.url = SocialMap2.baseDomain + '/markpost/' + POINT;
        },
        model: SocialMap2.Models.MPBubble,
        parse: function(response) {
            for(var bubble in response){
                var mpb = new SocialMap2.Models.MPBubble(bubble);
                this.add(mpb);
            }
            return response;
        }
    });

})();
