ymaps.ready(init);

function init() {
    var map = new ymaps.Map('map', {
        center: [55.815493568921546,37.575396499999904],
        zoom: 16,
        controls: ['zoomControl'],
        behaviors: ['drag']
    });

    var placemark = new ymaps.Placemark([55.815493568921546,37.575396499999904], {
                hintContent: '<div class="map__hint">Фирма 1С</div>',
                balloonContent: [
                    '<div class="map__balloon">',
                    '<img class="map__img" src="./images/map/flag.svg" alt="1click"/>',
                    'Фирма 1clike',
                    '</div>'
                ].join('')
            },
            {
                iconLayout: 'default#image',
                iconImageHref: './images/map/flag.svg',
                iconImageSize: [85, 91],
                iconImageOffset: [-43, -77],
            });
    
    map.geoObjects.add(placemark);
    
}
