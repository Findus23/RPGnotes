# Create your views here.
from itertools import chain

from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline, TrigramWordSimilarity
from django.views.generic import TemplateView

from campaigns.models import Campaign
from characters.models import Character
from days.models import IngameDay
from factions.models import Faction
from locations.models import Location
from loot.models import Loot
from notes.models import Note


class SearchResultsView(TemplateView):
    template_name = "search/search_results.jinja"

    def get_context_data(self, **kwargs):
        print(self.request.GET)
        if "q" not in self.request.GET:
            return ""
        query_string = self.request.GET['q']
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        campaign: Campaign = self.request.tenant
        config = campaign.language
        name_vector = SearchVector('name', weight="A", config=config)
        description_vector = SearchVector("description_html", weight="B", config=config)
        query = SearchQuery(query_string, search_type='websearch', config=config)
        models = [Location, Character, Faction, IngameDay, Note, Loot]
        all_results = []
        all_similar = []
        for m in models:
            if m == IngameDay:
                vector = description_vector
            else:
                vector = description_vector + name_vector
                similar = m.objects.annotate(
                    distance=TrigramWordSimilarity(query_string, "name")
                    # distance=TrigramDistance("name", query_string)
                ).filter(name__trigram_word_similar=query_string).order_by('distance')
                all_similar.extend(list(similar))
            results = m.objects.annotate(
                search=vector,
                rank=SearchRank(vector, query),
                headline=SearchHeadline(
                    'description_html',
                    query,
                    start_sel='<strong>',
                    stop_sel='</strong>',
                ),
            ).filter(search=query).order_by('-rank')
            all_results.append(results)

        context["results"] = chain(*all_results)
        all_similar.sort(key=lambda s: s.distance)
        all_similar = [s for s in all_similar if s.distance != 0]
        context["similars"] = all_similar
        context["query"] = query_string
        return context
