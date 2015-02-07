/*global define*/

SocialMap2.Collections = SocialMap2.Collections || {};

(function () {
    'use strict';

    SocialMap2.Collections.UserMarkPosts = Backbone.Collection.extend({
        url: '/api/user/markpost/',

        model: SocialMap2.Models.MarkPost,

        parse: function(response) {
            for(var markPost in response){
                var markPost = new SocialMap2.Models.MarkPost(markPost);
                this.add(markPost);
            }
            return response;
        }
    });

})();
