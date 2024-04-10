jQuery(document).ready(function ($) {
    $("#input-21f").rating({
        starCaptions: function (val) {
            if (val < 3) {
                return val;
            } else {
                return 'high';
            }
        },
        starCaptionClasses: function (val) {
            if (val < 3) {
                return 'label label-danger';
            } else {
                return 'label label-success';
            }
        },
        hoverOnClear: false
    });
    var $inp = $('#rating-input');

    $inp.rating({
        min: 0,
        max: 5,
        step: 1,
        size: 'md',
        showClear: false
    });

    $('#btn-rating-input').on('click', function () {
        $inp.rating('refresh', {
            showClear: true,
            disabled: !$inp.attr('disabled')
        });
    });


    $('.btn-danger').on('click', function () {
        $("#kartik").rating('destroy');
    });

    $('.btn-success').on('click', function () {
        $("#kartik").rating('create');
    });

    $inp.on('rating.change', function () {
        alert($('#rating-input').val());
    });


    $('.rb-rating').rating({
        'showCaption': true,
        'stars': '3',
        'min': '0',
        'max': '3',
        'step': '1',
        'size': 'xs',
        'starCaptions': {0: 'status:nix', 1: 'status:wackelt', 2: 'status:geht', 3: 'status:laeuft'}
    });
    $("#input-21c").rating({
        min: 0, max: 8, step: 0.5, size: "xl", stars: "8"
    });
});

(function (factory) {
    'use strict';
    if (typeof define === 'function' && define.amd) {
        define(['jquery'], factory);
    } else if (typeof module === 'object' && typeof module.exports === 'object') { 
        factory(require('jquery'));
    } else { 
        factory(window.jQuery);
    }
}(function ($) {
    "use strict";
    $.fn.ratingLocales['ru'] = {
        defaultCaption: '{rating} Звёзды',
        starCaptions: {
            0.5: 'Половина звезды',
            1: 'Одна звезда',
            1.5: 'Полторы звезды',
            2: 'Две звезды',
            2.5: 'Две с половиной звезды',
            3: 'Три звезды',
            3.5: 'Три с половиной звезды',
            4: 'Четыре звезды',
            4.5: 'Четыре с половиной звезды',
            5: 'Пять звёзд'
        },
        clearButtonTitle: 'Очистить',
        clearCaption: 'Без рейтинга'
    };
}));