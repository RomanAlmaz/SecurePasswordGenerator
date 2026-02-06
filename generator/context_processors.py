def language(request):
    """Текущий язык из сессии (ru / en)."""
    return {'current_lang': request.session.get('lang', 'ru')}
