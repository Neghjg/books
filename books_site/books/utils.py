from django.db.models import Q
from books.models import Book
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline

def q_search(query):
    vector = SearchVector(
            "title",
            "author",
#            "description"
            )
    query = SearchQuery(query)
    result = Book.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")
    
    result = result.annotate(headline=SearchHeadline(
        "title",
        query,
        start_sel="<span style='background-color: #aaffff;'>",
        stop_sel="</span>"
        )
    )
    
    result = result.annotate(authorline=SearchHeadline(
        "author",
        query,
        start_sel="<span style='background-color: #aaffff;'>",
        stop_sel="</span>"
        )
    )
    
    #result = result.annotate(descriptionline=SearchHeadline(
    #    "description",
    #    query,
    #    start_sel="<span style='background-color: yellow;'>",
    #    stop_sel="</span>"
    #    )
    #)
    return result

    #keywords = [word for word in query.split() if len(word) > 2]
    
    #q_objects = Q()
    
    #for token in keywords:
    #    q_objects |= Q(title__icontains=token)
    #    q_objects |= Q(description__icontains=token)
    #    q_objects |= Q(author__icontains=token)
        
    #return Book.objects.filter(q_objects)