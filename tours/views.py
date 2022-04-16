from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError
import random

title = "Stepik Travel"
subtitle = "Для тех, кого отвлекают дома"
description = """Лучшие направления, где никто не будет вам мешать сидеть на берегу и изучать программирование, дизайн,
разработку игр и управление продуктами"""
departures = {"msk": "Из Москвы", "spb": "Из Петербурга", "nsk": "Из Новосибирска", "ekb": "Из Екатеринбурга",
              "kazan": "Из Казани"}
departures_2 = {"msk": "msk", "spb": "spb", "nsk": "nsk", "ekb": "ekb", "kazan": "kazan"}
tours = {
    1: {
        "title": "Marina Lake Hotel & Spa",
        "description": "Отель выглядит уютно. Он был построен из красного соснового дерева и украшен синими камнями.  "
                       "Высокие округлые окна добавляют дому оригинальный стиль и создают атмосферу праздника.",
        "departure": "nsk",
        "picture": "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?ixlib=rb-1.2.1&ixid"
                   "=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 62000,
        "stars": "4",
        "country": "Куба",
        "nights": 6,
        "date": "2 марта",
    },
    2: {
        "title": "Baroque Hotel",
        "description": "Здание отеля имеет форму буквы U. Два расширенных блока здания связаны стеклянными нависающими "
                       "панелями. Два этажа здания имеют одинаковый размер. Второй этаж имеет совершенно другой стиль, "
                       "в отличие от первого.",
        "departure": "ekb",
        "picture": "https://images.unsplash.com/photo-1445019980597-93fa8acb246c?ixlib=rb-1.2.1&ixid"
                   "=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 85000,
        "stars": "5",
        "country": "Вьетнам",
        "nights": 8,
        "date": "12 января",
    },
    3: {
        "title": "Voyager Resort",
        "description": "Снаружи отель выглядит красиво и традиционно. Он был построен из белых камней и имеет еловые "
                       "деревянные украшения. Высокие, большие окна добавляют футуристичность стилю дома. Они были "
                       "добавлены в дом симметричным способом.",
        "departure": "nsk",
        "picture": "https://images.unsplash.com/photo-1569660072562-48a035e65c30?ixlib=rb-1.2.1&ixid"
                   "=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 63000,
        "stars": "3",
        "country": "Пакистан",
        "nights": 11,
        "date": "7 февраля",
    },
    4: {
        "title": "Orbit Hotel",
        "description": "Каждый домик оборудован средней кухней и одной небольшой ванной комнатой, в нем также есть "
                       "уютная гостиная, две спальни, скромная столовая и большой подвал. Небольшие треугольные окна "
                       "добавляют уют к общему стилю дома. Они были добавлены в дом симметричным способом.",
        "departure": "msk",
        "picture": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?ixlib=rb-1.2.1&ixid"
                   "=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 62000,
        "stars": "4",
        "country": "Индия",
        "nights": 9,
        "date": "22 января",
    },
    5: {
        "title": "Atlantis Cabin Hotel",
        "description": "Этот дом среднего размера имеет футуристический вид и находится в хорошем состоянии. Интерьер "
                       "выполнен в насыщенных тонах. Двор небольшой и выглядит очень аккуратно. Кроме того, "
                       "теплые огни в доме ночью создают неповторимую атмосферу праздника.",
        "departure": "msk",
        "picture": "https://images.unsplash.com/photo-1566073771259-6a8506099945?ixlib=rb-1.2.1&ixid"
                   "=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 68000,
        "stars": "4",
        "country": "Доминикана",
        "nights": 8,
        "date": "18 января",
    },
    6: {
        "title": "Light Renaissance Hotel",
        "description": "Этот небольшой дом выглядит довольно современно и находится в прекрасном состоянии. Интерьер "
                       "выполнен в цветах, которые напоминают вам тропический лес. Двор небольшой и заполнен "
                       "дикими растениями. Этот двор был однажды показан в телесериале, демонстрирующем "
                       "его необычный дизайн.",
        "departure": "spb",
        "picture": "https://images.unsplash.com/photo-1571896349842-33c89424de2d?ixlib=rb-1.2.1&ixid"
                   "=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 53000,
        "stars": "3",
        "country": "Пакистан",
        "nights": 13,
        "date": "15 февраля",
    },
    7: {
        "title": "King's Majesty Hotel",
        "description": "Этот дом средних размеров выглядит немного старомодно, но находится в прекрасном состоянии. "
                       "Интерьер выполнен в цветах, которые напоминают о весеннем цветнике. Двор среднего размера и "
                       "напоминает луг. Кроме того, он был построен над остатками дома, который был разрушен в "
                       "результате пожара.",
        "departure": "ekb",
        "picture": "https://images.unsplash.com/photo-1468824357306-a439d58ccb1c?ixlib=rb-1.2.1&ixid"
                   "=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 72000,
        "stars": "5",
        "country": "Мексика",
        "nights": 9,
        "date": "22 января",
    },
    8: {
        "title": "Crown Hotel",
        "description": "Этот огромный дом почти выглядит инопланетянином и находится в прекрасном состоянии. Интерьер "
                       "выполнен в цветах, напоминающих апельсиновое дерево. Двор среднего размера и напоминает луг. "
                       "Кроме того, это место известно тем, что на нем произошло убийство.",
        "departure": "kazan",
        "picture": "https://images.unsplash.com/photo-1549109786-eb80da56e693?ixlib=rb-1.2.1&ixid"
                   "=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 44000,
        "stars": "4",
        "country": "Тайланд",
        "nights": 7,
        "date": "3 февраля",
    },
    9: {
        "title": "Seascape Resort",
        "description": "Этот большой дом имеет сказочный вид и находится в отличном состоянии. Интерьер выполнен в "
                       "ярких цветах. Двор маленький и аккуратно подстрижен. На заднем дворе есть большой земельный "
                       "участок , а периметр дома имеет большой решетчатый забор. На заднем дворе "
                       "живут различные животные. Многие владельцы приложили совместные усилия для поддержания "
                       "этого объекта недвижимости.",
        "departure": "nsk",
        "picture": "https://images.unsplash.com/photo-1570214476695-19bd467e6f7a?ixlib=rb-1.2.1&ixid"
                   "=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 39000,
        "stars": "3",
        "country": "Индия",
        "nights": 10,
        "date": "1 февраля",
    },
    10: {
        "title": "Rose Sanctum Hotel",
        "description": "Снаружи этот дом выглядит старым, но чудесным. Он был построен из желтого соснового дерева и "
                       "украшен белым кирпичом. Короткие, широкие окна пропускают много света и были добавлены в дом "
                       "для создания уютной обстановки.",
        "departure": "msk",
        "picture": "https://images.unsplash.com/photo-1560200353-ce0a76b1d438?ixlib=rb-1.2.1&ixid"
                   "=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 52000,
        "stars": "4",
        "country": "Куба",
        "nights": 10,
        "date": "30 января",
    },
    11: {
        "title": "Viridian Obelisk Hotel & Spa",
        "description": "В доме очень хороший двор с большими камнями и озером. В задней части дома окна "
                       "просторные, с большими окнами, они светлые. Снаружи есть пять "
                       "маленьких деревьев. Двор в очень хорошем состоянии и очень живописный. Есть пруд для "
                       "развлечения",
        "departure": "spb",
        "picture": "https://images.unsplash.com/photo-1477120128765-a0528148fed2?ixlib=rb-1.2.1&ixid"
                   "=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 68000,
        "stars": "5",
        "country": "Индия",
        "nights": 9,
        "date": "1 марта",
    },
    12: {
        "title": "Saffron Tundra Hotel & Spa",
        "description": "Дом оборудован огромной кухней и одной современной ванной комнатой, а также имеет огромную "
                       "гостиную, две спальни, небольшую столовую, гостиную и скромную кладовую.  Дом чистый, "
                       "хорошо построенный и в хорошем состоянии.",
        "departure": "kazan",
        "picture": "https://images.unsplash.com/photo-1440151050977-247552660a3b?ixlib=rb-1.2.1&ixid"
                   "=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 72000,
        "stars": "4",
        "country": "Мексика",
        "nights": 12,
        "date": "17 февраля",
    },
    13: {
        "title": "Traveller Resort",
        "description": "Снаружи этот дом выглядит очень элегантно. Он был построен из коричневого кирпича и имеет "
                       "коричневые кирпичные украшения. Высокие, большие окна добавляют к общему стилю дома. "
                       "Крыша высокая, наклонена в одну сторону и "
                       "покрыта коричневой черепицей. Один большой дымоход высовывает центр крыши. На крыше нет окон. "
                       "Сам дом окружен великолепным садом с виноградными лозами, пагодой, прудом и множеством разных "
                       "цветов.",
        "departure": "ekb",
        "picture": "https://images.unsplash.com/photo-1553653924-39b70295f8da?ixlib=rb-1.2.1&auto=format&fit=crop&w"
                   "=800&q=60",
        "price": 49000,
        "stars": "3",
        "country": "Куба",
        "nights": 8,
        "date": "26 января"
    },
    14: {
        "title": "History Hotel & Spa",
        "description": "Крыша высокая, треугольная, многослойная, покрыта пшеничной соломой. Две большие трубы "
                       "находятся по обе стороны от дома. Многие окна пропускают много света в комнаты под "
                       "крышей. Сам дом окружен асфальтированной землей, с местом для еды и отдыха на открытом воздухе "
                       "и различными горшечными растениями.",
        "departure": "kazan",
        "picture": "https://images.unsplash.com/photo-1509600110300-21b9d5fedeb7?ixlib=rb-1.2.1&ixid"
                   "=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 91000,
        "stars": "5",
        "country": "Вьетнам",
        "nights": 9,
        "date": "3 февраля",
    },
    15: {
        "title": "Riverside Lagoon Hotel & Spa",
        "description": "Здание имеет форму круга. Дом частично окружен деревянными нависающими панелями с двух "
                       "сторон. Второй этаж меньше первого, что позволило создать несколько балконов по бокам дома. "
                       "Второй этаж следует тому же стилю, что и этаж ниже.",
        "departure": "spb",
        "picture": "https://images.unsplash.com/photo-1568084680786-a84f91d1153c?ixlib=rb-1.2.1&ixid"
                   "=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 82000,
        "stars": "4",
        "country": "Доминикана",
        "nights": 8,
        "date": "5 февраля",
    },
    16: {
        "title": "History Hotel & Spa",
        "description": "Это высокое здание из старого кирпича. Крыша высокая, треугольная, многослойная, "
                       "покрыта пшеничной соломой. В тесной квадратной спальне установлена деревянная и стеклянная "
                       "мебель. Пол деревянный, а стены текстурированы и окрашены.Настенные и напольные светильники "
                       "обеспечивают свет. Комната оформлена в цветах, напоминающих облачное небо, и в целом выглядит "
                       "очень старомодно.",
        "departure": "spb",
        "picture": "https://images.unsplash.com/photo-1564056095795-4d63b6463dbf?ixlib=rb-1.2.1&ixid"
                   "=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 74000,
        "stars": "5",
        "country": "Вьетнам",
        "nights": 12,
        "date": "24 января",
    }

}


def generation_dict():
    dict_tours = {}
    count = 0
    while count != 6:
        el = random.choice(list(tours.keys()))
        if el not in dict_tours:
            dict_tours[el] = tours[el]
            count += 1
    return dict_tours


def custom_handler404(request, exception):
    # Call when Http404 raised
    return HttpResponseNotFound('Ресурс не найден!')


def custom_handler500(request):
    # Call when raised some python exception
    return HttpResponseServerError('Ошибка сервера!')


def main_view(request):
    dict_tours = generation_dict()
    dict_central_image = {}
    element = random.choice(list(tours.keys()))
    if element not in dict_central_image:
        dict_central_image[element] = tours[element]
    return render(request, 'tours/index.html', {'title': title, 'description': description, 'subtitle': subtitle,
                                                'departures': departures, 'dict_tours': dict_tours,
                                                'dict_central_image': dict_central_image, 'departures_2': departures_2})


def departure_view(request, departure: str):
    dict_departure = {}
    count = 0
    min_price = 0
    max_price = 0
    min_nights = 0
    max_nights = 0
    for key in tours.keys():
        if tours[key]['price'] > min_price:
            min_price = tours[key]['price']
        if tours[key]['nights'] > min_nights:
            min_nights = tours[key]['nights']
    for key in tours.keys():
        if tours[key]['departure'] == departure:
            if key not in dict_departure:
                dict_departure[key] = tours[key]
                count += 1
                if min_price > tours[key]['price']:
                    min_price = tours[key]['price']
                if max_price < tours[key]['price']:
                    max_price = tours[key]['price']
                if min_nights > tours[key]['nights']:
                    min_nights = tours[key]['nights']
                if max_nights < tours[key]['nights']:
                    max_nights = tours[key]['nights']
    return render(request, 'tours/departure.html', {'departure': departures[departure], 'title': title,
                                                    'dict_departure': dict_departure, 'departures': departures,
                                                    'count': count, 'min_price': min_price, 'max_price': max_price,
                                                    'min_nights': min_nights, 'max_nights': max_nights,
                                                    'departures_2': departures_2})


def tour_view(request, id: int):
    return render(request, 'tours/tour.html', {'tour': tours[id], 'title': title,
                                               'stars': int(tours[id]['stars']) * '★', 'departures': departures,
                                               'departures_2': departures_2})
