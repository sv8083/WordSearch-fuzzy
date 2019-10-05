from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .services import search_query, sort_query
import json
from django.views import View
from django.views.generic import FormView


class SearchView(View):
    template_name= 'search.html'
    
    def get(self, request,  *args, **kwargs):

        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        return redirect('/')

class AutcompleteSearchResults(FormView):
    
    def get(self, request,  *args, **kwargs):
        if request.is_ajax():
            query = request.GET.get('term','')
            print("AJAX sending word", query)
            results = sort_query(search_query(query.lower()), query.lower())
            data = json.dumps(results)
        else:
            data = 'HTTP: 404'
        type = 'application/json'
        return HttpResponse(data, type)

class FinalSearchResults(View):
    
    def get(self, request,  *args, **kwargs):
        query = request.GET.get('auto')
        if query:
            word_list= sort_query(search_query(query.lower()), query.lower())
            if len(word_list) == 0:
                return JsonResponse({'Search_Result': "Unable to find word "})
            else:
                return JsonResponse({'Search_Result': word_list})
        else:
            return redirect('/')





