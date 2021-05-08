
$.getJSON('https://mindicador.cl/api', function (data) {
    var dailyIndicators = data;
    $("<p/>", {
        html: 'UF $' + dailyIndicators.uf.valor + "<br>Dólar $" + dailyIndicators.dolar.valor
    }).appendTo("#apisValores");
}).fail(function () {
    console.log('Error al consumir la API!');
});

$('.bxslider').bxSlider({
  auto: true,
  autoControls: true,
  stopAutoOnClick: true,
  pager: true,
  slideWidth: 600,
  mode: 'fade',
  captions: true,
});