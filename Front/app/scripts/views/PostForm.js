/*global SocialMap2, Backbone, JST*/

SocialMap2.Views = SocialMap2.Views || {};

(function () {
    'use strict';

    SocialMap2.Views.PostForm = Backbone.View.extend({
        el: '#ModalPanelBody',

        template: JST['app/scripts/templates/PostForm.ejs'],

        tagName: 'div',

        id: '',

        className: '',

        events: {
            //'change #picFile': 'prepareUpload',
            'click #markPostButton2': 'upLoad'
        },

        prepareUpload: function(event){
            this.files = event.target.files;
        },

        upLoad: function(event){
            event.stopPropagation(); // Stop stuff happening
            event.preventDefault(); // Totally stop stuff happening

            var POINT = SocialMap2.position.get('longitude') + ' ' + SocialMap2.position.get('latitude');
            var accuracy = SocialMap2.position.get('accuracy');
            var title = $('#markPostTitle').val();
            var text = $('#markPostText').val();
            var files = $('#picFile')[0].files[0];
            var data = new FormData();

            data.append('picture', files);
            data.append('point', POINT);
            data.append('accuracy', accuracy);
            data.append('title', title);
            data.append('text', text);
            data.append('csrfmiddlewaretoken', $.cookie('csrftoken'));


            $.ajax({
                url: (SocialMap2.baseDomain + '/markpost/'),
                type: "POST",
                processData: false, // Don't process the files
                contentType: false,
                data: data,
                //{
                //    csrfmiddlewaretoken: $.cookie('csrftoken'),
                //    point: POINT,
                //    accuracy: accuracy,
                //    title: title,
                //    text: text,
                //    picture: Picdata
                //},
                success: function(data){
                    alert('succe');
                },
                error: function(data){
                    //!!!!!!!!!!!!!!!!!!!
                    alert('Certification may have problems, please log in again!');
                }
            });
        },

        initialize: function () {
            _.bindAll(this, 'cleanup');
            this.cleanup();
        },

        render: function () {
            this.$el.html(this.template());
        },

        cleanup: function() {
            this.undelegateEvents();
            $(this.el).empty();
        }

    });

})();
