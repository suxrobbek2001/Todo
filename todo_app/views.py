from django.shortcuts import render, redirect

from .models import Todo


def todo(request):
    if request.method == 'POST':
        Todo.objects.create(
            nom=request.POST.get('n'),
            batafsil=request.POST.get('b'),
            status=request.POST.get('s'),
            vaqt=request.POST.get('v')
        )
        return redirect('/')
    t = Todo.objects.all()
    return render(request, 'todo.html', {"todo": t})
def todo1(request,son):
    t = Todo.objects.get(id=son)
    t.delete()
    return redirect('/')

