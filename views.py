__author__ = 'hhuang'


def displayPairStair(request):
    return render_to_response('templates/index.html', {'projects': project_list, 'disable_link_class': disable_link_class},
                              context_instance=RequestContext(request))