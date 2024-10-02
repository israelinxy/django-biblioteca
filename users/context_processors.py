def user_context(request):
    return {"usuario_logeado": request.user if request.user.is_authenticated else None}
