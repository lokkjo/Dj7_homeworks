from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся

counter_show = Counter()
counter_click = Counter()


# Реализуйте логику подсчета количества переходов с лендига
# по GET параметру from-landing

def index(request):
    from_landing = request.GET.get('from-landing')
    if from_landing == 'original':
        counter_click.update('o')
    if from_landing == 'test':
        counter_click.update('t')
    return render_to_response('index.html')


    # Реализуйте дополнительное отображение по шаблону
    # app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    # return render_to_response('landing.html')

def landing(request):
    ab_test_arg = request.GET.get('ab-test-arg')
    if ab_test_arg == 'original':
        counter_show.update('o')
        return render_to_response('landing.html')
    if ab_test_arg == 'test':
        counter_show.update('t')
        return render_to_response('landing_alternate.html')


    # Реализуйте логику подсчета отношения количества переходов
    # к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать
    # значения test и original
    # Для вывода результат передайте в следующем формате:

def stats(request):
    if counter_show['t'] >= 1:
        test_conv = counter_click['t']/counter_show['t']
    else:
        test_conv = 0
    if counter_show['o'] >= 1:
        orig_conv = counter_click['o']/counter_show['o']
    else:
        orig_conv = 0
    return render_to_response('stats.html', context={
        'test_conversion': round(test_conv, 1),
        'original_conversion': round(orig_conv, 1),
    })
