from django.shortcuts import render
from ipware import get_client_ip

from django.views.generic import TemplateView
from map.solver import *


class HomeView(TemplateView):
    template_name = 'map/home.html'

    def get(self, request, *args, **kwargs):
        ip, is_routable = get_client_ip(request)
        if ip is None:
            print('-----------------')
            print('we cant find your ip. sneaky sneaky')
        else:
            print('-----------------')
            print(ip)

        return render(request, template_name='map/home.html')


class PuzzleSolver(TemplateView):
    template_name = 'map/sudoku.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rows'] = range(1, 10)
        context['columns'] = range(1, 10)
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        s_puzzle = []
        for x in range(1,10):
            row = []
            for y in range(1,10):
                cell = ('cell:'+str(x) + ',' + str(y))
                cell_x = request.POST.get(cell)
                row.append(int(cell_x))
            s_puzzle.append(row)
        
        for x in s_puzzle:
            print(x)
            
        print('---------------------------')
        solve_puzzle(s_puzzle)

        context = {'solveable': solve_puzzle(s_puzzle)[0], 'completed_puzzle': s_puzzle, 'counter': solve_puzzle(s_puzzle)[2]}

        return render(request, template_name='map/completed_puzzle.html', context=context)
