/*global SocialMap2, Backbone, JST*/

SocialMap2.Views = SocialMap2.Views || {};

(function () {
    'use strict';

    SocialMap2.Views.MPShow = Backbone.View.extend({
        el: '#ModalPanelBody',

        template: JST['app/scripts/templates/MPShow.ejs'],

        tagName: 'div',

        id: '',

        className: '',

        events: {
            'click .user': 'showUserInfo'
        },

        initialize: function () {
            _.bindAll(this, 'cleanup');
        },

        showUserInfo: function(event) {
            var user = new SocialMap2.Models.User(event.target.id);
            user.fetch().success(function (user, response, options) {
                if(SocialMap2.us){SocialMap2.us.cleanup();}
                SocialMap2.us = new SocialMap2.Views.UserShow({model: user});
                SocialMap2.us.render();
            });
        },

        render: function () {
            this.$el.html(this.template(this.model));
        },

        cleanup: function() {
            this.undelegateEvents();
            $(this.el).empty();
        }

    });

})();
