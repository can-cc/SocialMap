/*global SocialMap2, Backbone, JST*/

SocialMap2.Views = SocialMap2.Views || {};

(function () {
    'use strict';

    SocialMap2.Views.UserShow = Backbone.View.extend({
        el: '#ModalPanelBody',

        template: JST['app/scripts/templates/UserShow.ejs'],

        tagName: 'div',

        id: '',

        className: '',

        events: {
            'click .follow': 'follow',
            'click .notsee': 'notsee'
        },

        follow: function(event) {
            var id = event.target.id;

        },

        notsee: function() {

        },

        initialize: function () {
            _.bindAll(this, 'cleanup');
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
