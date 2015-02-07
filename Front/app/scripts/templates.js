this["JST"] = this["JST"] || {};

this["JST"]["app/scripts/templates/BaiduMapView.ejs"] = function(obj) {
    obj || (obj = {});
    var __t, __p = '', __e = _.escape;
    with (obj) {
        __p += '<p>Your content here.</p>\n\n';

    }
    return __p
};

this["JST"]["app/scripts/templates/Friends.ejs"] = function(obj) {
    obj || (obj = {});
    var __t, __p = '', __e = _.escape;
    with (obj) {
        __p += '<p>Your content here.</p>\n\n';

    }
    return __p
};

this["JST"]["app/scripts/templates/MPShow.ejs"] = function(obj) {
    obj || (obj = {});
    var __t, __p = '', __e = _.escape;
    with (obj) {
        __p += '<div class="modal-content">\n    <div class="modal-header">\n        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>\n        <h4 class="modal-title" id="MPShowModalLabel">Mark Post Detail</h4>\n    </div>\n    <div class="modal-body" id="MPShowBody">\n        <div class="row">\n            <div class="col-xs-6 col-md-1">\n                <a href="#" class="thumbnail user" style="width:50px;height: 50px" id="' +
        ((__t = ( userInfo.user )) == null ? '' : __t) +
        '">\n                    <img src="' +
        ((__t = ( userInfo.portrait )) == null ? '' : __t) +
        '" alt="cannot load portrait" class="img-circle" id="' +
        ((__t = ( userInfo.user )) == null ? '' : __t) +
        '">\n                </a>\n            </div>\n            <div class="col-xs-6 col-md-1">\n                <h5 class="text-primary user" id="' +
        ((__t = ( userInfo.user )) == null ? '' : __t) +
        '">' +
        ((__t = ( userInfo.nickName )) == null ? '' : __t) +
        '</h5>\n            </div>\n            <div class="col-xs-6 col-md-1">\n                <em>' +
        ((__t = ( userInfo.personalDescription )) == null ? '' : __t) +
        '</em>\n            </div>\n        </div>\n        <h4 class="bg-info">' +
        ((__t = ( title )) == null ? '' : __t) +
        '</h4>\n        <p >' +
        ((__t = ( text )) == null ? '' : __t) +
        '</p>\n        <img src="' +
        ((__t = ( picture )) == null ? '' : __t) +
        '" class="img-responsive" alt="Responsive image">\n\n    </div>\n    <div class="modal-footer">\n        <p class="text-right"><ins>Post at ' +
        ((__t = ( postTime )) == null ? '' : __t) +
        '</ins></p>\n    </div>\n</div>\n';

    }
    return __p
};

this["JST"]["app/scripts/templates/MainView.ejs"] = function(obj) {
    obj || (obj = {});
    var __t, __p = '', __e = _.escape;
    with (obj) {
        __p += '<p>Your content here.</p>\n\n';

    }
    return __p
};

this["JST"]["app/scripts/templates/MapView.ejs"] = function(obj) {
    obj || (obj = {});
    var __t, __p = '', __e = _.escape;
    with (obj) {
        __p += '<p>Your content here.</p>\n\n';

    }
    return __p
};

this["JST"]["app/scripts/templates/Navigation.ejs"] = function(obj) {
    obj || (obj = {});
    var __t, __p = '', __e = _.escape;
    with (obj) {
        __p += '<nav class="navbar navbar-default navbar-fixed-top">\n    <div class="container-fluid">\n        <div class="navbar-header">\n            <a class="navbar-brand" href="#">\n                <span class="glyphicon glyphicon-send" aria-hidden="true"></span>\n            </a>\n            <ul class="nav nav-tabs" role="tablist">\n                <li role="presentation" class="dropdown">\n                    <a class="dropdown-toggle" data-toggle="dropdown" href="#">\n                        Map <span class="caret"></span>\n                    </a>\n                    <ul class="dropdown-menu" role="menu">\n                        <li><a href="#">Map</a></li>\n                        <li class="divider"></li>\n                        <li><a href="#text">Text</a></li>\n                    </ul>\n                </li>\n                <li role="presentation" class="dropdown">\n                    <a class="dropdown-toggle" data-toggle="dropdown">\n                        Friends <span class="caret"></span>\n                    </a>\n                    <ul class="dropdown-menu" role="menu">\n                        <li><a href="#friends">Friends</a></li>\n                        <li><a href="#message">Message</a></li>\n                        <li class="divider"></li>\n                        <li><a href="#">Separated link</a></li>\n                        <li class="divider"></li>\n                    </ul>\n                </li>\n                <li role="presentation" class="dropdown" id="signNav">\n                    <a class="dropdown-toggle" data-toggle="dropdown">\n                        Sign <span class="caret"></span>\n                    </a>\n                    <ul class="dropdown-menu" role="menu">\n                        <li><a href="#signin">Sign In</a></li>\n                        <li class="divider"></li>\n                        <li><a href="#signup">Sign Up</a></li>\n                    </ul>\n                </li>\n                <li role="presentation" class="dropdown" id="signNav">\n                    <a class="dropdown-toggle" data-toggle="dropdown">\n                        <p id="profileNav">profile</p>\n                    </a>\n                    <ul class="dropdown-menu" role="menu">\n                        <li><a href="#profile">Information</a></li>\n                        <li class="divider"></li>\n                        <li><a href="#setting" id="profileNav"><span class="glyphicon glyphicon-cog" aria-hidden="true"></span></a></li>\n                        <li class="divider"></li>\n                        <li><a href="/api/api-auth/logout?next=/#" id="profileNav"><span class="glyphicon glyphicon-remove" aria-hidden="true"></span></a></li>\n                    </ul>\n                </li>\n            </ul>\n        </div>\n    </div>\n</nav>\n';

    }
    return __p
};

this["JST"]["app/scripts/templates/PostForm.ejs"] = function(obj) {
    obj || (obj = {});
    var __t, __p = '', __e = _.escape;
    with (obj) {
        __p += '<div class="modal-content">\n    <div class="modal-header">\n        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>\n        <h4 class="modal-title" id="MPModalLabel">Made something of it!</h4>\n    </div>\n    <div class="modal-body">\n        <input type="text" class="form-control" placeholder="Title" id="markPostTitle"><br>\n        <textarea class="form-control" rows="3" id="markPostText" placeholder="Text"></textarea><br>\n        <p>Picture: </p>\n        <input type="file" id="picFile" style="width: 100%">\n    </div>\n    <div class="modal-footer">\n        <button type="button" class="btn btn-default" data-dismiss="modal" id="markPostCloseButton">Close</button>\n        <button type="button" class="btn btn-primary" id="markPostButton2">Post</button>\n    </div>\n\n</div>\n\n';

    }
    return __p
};

this["JST"]["app/scripts/templates/Profile.ejs"] = function(obj) {
    obj || (obj = {});
    var __t, __p = '', __e = _.escape;
    with (obj) {
        __p += '<br>\n<div class="input-group">\n    <span class="input-group-addon">NickName:</span>\n    <input type="text" id="nickName" class="form-control">\n</div>\n<br>\n<div class="input-group">\n    <span class="input-group-addon">Personal Description</span>\n    <textarea id="description" class="form-control"></textarea>\n</div>\n<br>\n<div class="input-group">\n    <span class="input-group-addon">phoneNumber</span>\n    <input type="text" id="phoneNumber" class="form-control" >\n</div>\n<br>\n<div class="input-group">\n    <span class="input-group-addon">City</span>\n    <input type="text" id="city" class="form-control" >\n</div>\n<br>\n<div class="input-group">\n    <span class="input-group-addon">Birthday</span>\n    <input type="text" id="birthday" class="form-control" >\n</div>\n<br>\n<div class="input-group">\n    <span class="input-group-addon">School</span>\n    <input type="text" id="school" class="form-control" >\n</div>\n<br>\n<div class="input-group">\n    <span class="input-group-addon">Interest</span>\n    <input type="text" id="interest" class="form-control" >\n</div>\n<br>\n<div class="input-group">\n    <span class="input-group-addon">CardId</span>\n    <input type="text" id="cardId" class="form-control" >\n</div>\n<br>\n<div class="input-group">\n    <span class="input-group-addon">NowCity</span>\n    <input type="text" id="nowCity" class="form-control" >\n</div>\n<br>\n<div class="input-group">\n    <span class="input-group-addon">PublicMail</span>\n    <input type="text" id="publicMail" class="form-control" >\n</div>\n<br>\n<span style="text-align:center;">\n    <button type="button" id="signup" class="btn btn-info" onclick="location.href=\'#signup\'">Alter</button>\n    <button type="button" class="btn btn-danger" onclick="location.href=\'/api/api-auth/logout?next=/#\'">Sign Out</button>\n</span>\n<br>\n<br>\n';

    }
    return __p
};

this["JST"]["app/scripts/templates/TextList.ejs"] = function(obj) {
    obj || (obj = {});
    var __t, __p = '', __e = _.escape, __j = Array.prototype.join;
    function print() { __p += __j.call(arguments, '') }
    with (obj) {

        for(var i=0; i<markPosts.length; i++) {;
            __p += '\n    ';
            var markPost = markPosts[i] ;
            __p += '\n    <div class="row">\n        <div class="col-sm-9">\n            markPost.title\n            <li role="presentation" class="dropdown text-right" id="UMPOperate">\n                <a class="dropdown-toggle" data-toggle="dropdown">\n                    Sign <span class="caret"></span>\n                </a>\n                <ul class="dropdown-menu" role="menu">\n                    <li><a href="#signin">Delete</a></li>\n                </ul>\n            </li>\n            <div class="row">\n                <div class="col-xs-8 col-sm-6">\n                    markPost.postTime\n                </div>\n                <div class="col-xs-4 col-sm-6">\n                    count\n                </div>\n            </div>\n        </div>\n    </div>\n';
        } ;
        __p += '\n\n';

    }
    return __p
};

this["JST"]["app/scripts/templates/UserMP.ejs"] = function(obj) {
    obj || (obj = {});
    var __t, __p = '', __e = _.escape, __j = Array.prototype.join;
    function print() { __p += __j.call(arguments, '') }
    with (obj) {
        __p += '<div class="container-fluid">\n';
        for(var i=0; i<data.length; i++){ ;
            __p += '\n';
            var markPost = data[i]; ;
            __p += '\n    <div class="row">\n        <div class="col-md-6"><a class="userMP" id="' +
            ((__t = ( markPost.id )) == null ? '' : __t) +
            '">' +
            ((__t = ( markPost.title )) == null ? '' : __t) +
            '</a></div>\n        <div class="col-md-3">\n            delete\n        </div>\n    </div>\n    <div class="row">\n        <div class="col-md-9">\n            ' +
            ((__t = ( markPost.text )) == null ? '' : __t) +
            '\n        </div>\n    </div>\n    <div class="row">\n        <div class="col-md-9">\n            ' +
            ((__t = ( markPost.postTime )) == null ? '' : __t) +
            '\n        </div>\n    </div>\n';
        };
        __p += '\n</div>\n';

    }
    return __p
};

this["JST"]["app/scripts/templates/UserShow.ejs"] = function(obj) {
    obj || (obj = {});
    var __t, __p = '', __e = _.escape;
    with (obj) {
        __p += '<div class="modal-content">\n    <div class="modal-header">\n        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>\n        <h4 class="modal-title" id="MPShowModalLabel" >' +
        ((__t = ( information.nickName )) == null ? '' : __t) +
        ' Detail</h4>\n    </div>\n    <div class="modal-body" id="MPShowBody">\n        <input class="UserShowId" id="' +
        ((__t = ( id )) == null ? '' : __t) +
        '">\n        <div class="row">\n            <div class="col-xs-6 col-md-1">\n                <a href="#" class="thumbnail" style="width:50px;height: 50px">\n                    <img src="' +
        ((__t = ( information.portrait )) == null ? '' : __t) +
        '" alt="cannot load portrait" class="img-circle">\n                </a>\n            </div>\n            <div class="col-xs-6 col-md-1">\n                <h5 class="text-primary">' +
        ((__t = ( information.nickName )) == null ? '' : __t) +
        '</h5>\n            </div>\n        </div>\n        <div class="row">\n            <div class="col-xs-6 col-md-1">\n                <em>' +
        ((__t = ( information.personalDescription )) == null ? '' : __t) +
        '</em>\n            </div>\n        </div>\n        <table class="table table-striped">\n            <tr>\n                <td>country: </td>\n                <td>' +
        ((__t = ( information.country )) == null ? '' : __t) +
        '</td>\n            </tr>\n            <tr>\n                <td>city: </td>\n                <td>' +
        ((__t = ( information.city )) == null ? '' : __t) +
        '</td>\n            </tr>\n            <tr>\n                <td>birthday: </td>\n                <td>' +
        ((__t = ( information.birthday )) == null ? '' : __t) +
        '</td>\n            </tr>\n            <tr>\n                <td>school: </td>\n                <td>' +
        ((__t = ( information.school )) == null ? '' : __t) +
        '</td>\n            </tr>\n            <tr>\n                <td>nowCity: </td>\n                <td>' +
        ((__t = ( information.nowCity )) == null ? '' : __t) +
        '</td>\n            </tr>\n            <tr>\n                <td>publicMail: </td>\n                <td>' +
        ((__t = ( information.publicMail )) == null ? '' : __t) +
        '</td>\n            </tr>\n            <tr>\n                <td>publicPhoneNumber: </td>\n                <td>' +
        ((__t = ( information.publicPhoneNumber )) == null ? '' : __t) +
        '</td>\n            </tr>\n            <tr>\n                <td>QQ: </td>\n                <td>' +
        ((__t = ( information.QQ )) == null ? '' : __t) +
        '</td>\n            </tr>\n        </table>\n\n\n    </div>\n    <div class="modal-footer">\n        <p class="text-right"><ins>----</ins></p>\n    </div>\n</div>\n';

    }
    return __p
};

this["JST"]["app/scripts/templates/signIn.ejs"] = function(obj) {
    obj || (obj = {});
    var __t, __p = '', __e = _.escape;
    with (obj) {
        __p += '<br>\n<div class="input-group">\n    <span class="input-group-addon"><span class="glyphicon glyphicon-user"></span></span>\n    <input type="text" id="siUsername" class="form-control" placeholder="Username">\n</div>\n<br>\n<div class="input-group">\n    <span class="input-group-addon"><span class="glyphicon glyphicon-leaf"></span></span>\n    <input type="password" id="siPasswd" class="form-control" placeholder="Password">\n</div>\n<br>\n<div class="input-group">\n    <span class="input-group-addon"><span class="glyphicon glyphicon-eye-close"></span></span>\n    <input type="text" id="verification" class="form-control" placeholder="Verification">\n</div>\n<br>\n<span style="text-align:center;">\n    <button type="button" id="signin" class="btn btn-primary">Sign In</button>\n    <button type="button" class="btn btn-info" onclick="location.href=\'#signup\'">Sign up</button>\n</span>\n<br>\n<br>\n<div class="alert alert-danger" role="alert" id="alert">Password Error or Verification Error!</div>\n';

    }
    return __p
};

this["JST"]["app/scripts/templates/signUp.ejs"] = function(obj) {
    obj || (obj = {});
    var __t, __p = '', __e = _.escape;
    with (obj) {
        __p += '<br>\n<div class="input-group">\n    <span class="input-group-addon"><span class="glyphicon glyphicon-user"></span></span>\n    <input type="text" id="suUserName" class="form-control" placeholder="Username">\n</div>\n<br>\n<div class="input-group">\n    <span class="input-group-addon"><span class="glyphicon glyphicon-leaf"></span></span>\n    <input type="text" id="suPasswd" class="form-control" placeholder="Password">\n</div>\n<br>\n<div class="input-group">\n    <span class="input-group-addon"><span class="glyphicon glyphicon-leaf"></span></span>\n    <input type="text" class="form-control" placeholder="Password Verification">\n</div>\n<br>\n<div class="input-group">\n    <span class="input-group-addon"><span class="glyphicon glyphicon-eye-close"></span></span>\n    <input type="text" id="verification" class="form-control" placeholder="Verification">\n</div>\n<br>\n<span style="text-align:center;">\n    <button type="button" id="signup" class="btn btn-info" onclick="location.href=\'#signup\'">Sign up</button>\n    <button type="button" class="btn btn-primary" onclick="location.href=\'#signin\'">Sign In</button>\n</span>\n<br>\n<br>\n';

    }
    return __p
};
