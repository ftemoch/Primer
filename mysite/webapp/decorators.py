from django.http import HttpResponse
from django.shortcuts import redirect

def usuario_noautenticado(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('inicio')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func



def usuario_permitido(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            #Funcionalidad
            group = None
            #Si el usaurio es parte del grupo
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            # Si es usuario esta en el grupo entonces ingresar a la funcion
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                #Sino saldra este mensaje
                return HttpResponse('No estas autorizado para esta pagina')
        return wrapper_func
    return decorator

#Solo para Admin
def solo_admin(view_func):

        def wrapper_func(request, *args, **kwargs):
            #Funcionalidad
            group = None
            #Si el usaurio es parte del grupo
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            # Si es usuario esta en el grupo entonces ingresar a la funcion
            if group == 'cliente':
                return redirect('user-page')
            if group == 'admin':
                return view_func(request, *args, **kwargs)

        return wrapper_func


