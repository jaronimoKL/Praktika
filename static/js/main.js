//Фильтр
$(document).ready(function () {
    $(".filter__item").click(function () {
        let value = $(this).attr("data-filter");
        let elem = $(".elem");
        $(elem).not("." + value).hide();
        $(elem).filter("." + value).show();
    });
})
// Слайдер
$(document).ready(function () {
    $('.recently-slider-main').slick({
        infinite: true,
        slidesToShow: 5,
        slidesToScroll: 5
    });
});
// Поиск
let inp = $('.input-search');
inp.focusin(function () {
    $('.btn-search').delay(5000).attr('type', 'submit');
});
inp.focusout(function () {
    $('.btn-search').attr('type', 'button');
});