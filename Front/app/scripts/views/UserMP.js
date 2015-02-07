/*global SocialMap2, Backbone, JST*/

SocialMap2.Views = SocialMap2.Views || {};

(function () {
    'use strict';

    SocialMap2.Views.UserMP = Backbone.View.extend({
        el: '#Panel',

        template: JST['app/scripts/templates/UserMP.ejs'],

        tagName: 'div',

        id: '',

        className: '',

        //show markpost detail
        events: {
            'click .userMP': 'MPclick'
        },

        MPclick: function(event) {
            var markpost = new SocialMap2.Models.MarkPost(event.target.id);
            markpost.fetch().success(function (markpost, response, options) {
                if(SocialMap2.mpshow){SocialMap2.mpshow.cleanup();}
                SocialMap2.mpshow = new SocialMap2.Views.MPShow({model: markpost});
                SocialMap2.mpshow.render();
            });
            $('#ModalPanel').modal();
        },

        initialize: function () {
            _.bindAll(this, 'cleanup');
            this.cleanup();
        },

        render: function () {
            var mps  = JSON.stringify(this.collection);
            this.$el.html(this.template({data:this.collection}));
        },

        cleanup: function() {
            this.undelegateEvents();
            $(this.el).empty();
        }

    });

})();
