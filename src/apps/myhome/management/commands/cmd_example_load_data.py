# HOW TO

# https://docs.djangoproject.com/en/1.10/howto/custom-management-commands/



import sys
from django.utils import timezone
from django.core.management.base import BaseCommand
from django.db import DataError

# from idxchecker.models import *

from django.db.models import Max, Min
import json

def writerr(x):
    sys.stderr.write(x)


class Command(BaseCommand):
    help = 'Create JSON statistics objects and cache in database'

    def message(self, s):
        # https://docs.djangoproject.com/en/2.1/howto/custom-management-commands/
        self.stdout.write(s)


    def add_arguments(self, parser):
        parser.add_argument('title', nargs='?', default=False, help="specify which statistics to rebuild")

    def handle(self, *args, **options):

        # note: 'timeseries_bymonth' is hidden, still being tested

        VALID_OPTIONS = ['stats', 'examples', 'ontology', 'all']

        if not options['title'] or options['title'] not in VALID_OPTIONS:
            print "Please provide an argument: %s" % "|".join([x for x in VALID_OPTIONS])
            return

        if options['title'] == 'stats' or options['title'] == 'all':

            # =====
            # table Stats
            # =====
            try:
                table_stats_obj = Stats.objects.get(title="table_stats")
            except:
                table_stats_obj = Stats(title="table_stats")
            print "==> Calculating and caching data for table_stats.."
            table_stats_obj.datatext = _doCacheTableStats()
            table_stats_obj.save()

        if options['title'] == 'ontology' or options['title'] == 'all':

            # =====
            # ontology info
            # =====
            try:
                ontology_obj = Stats.objects.get(title="ontology")
            except:
                ontology_obj = Stats(title="ontology")
            print "==> Calculating and caching data for the ontology.."
            ontology_obj.datatext = _doCacheOntology()
            ontology_obj.save()


        if options['title'] == 'examples' or options['title'] == 'all':

            pass


        self.message("Done - JSON objects created!")





def _doCacheOntology():

    o = ontospy.Ontospy(sparql_endpoint=SPARQL_ENDPOINT, credentials=CREDENTIALS)

    printDebug("Updating namespaces")
    for k,v in NAMESPACES.items():
        o.rdfgraph.bind(k, rdflib.Namespace(v))
    o.namespaces = sorted(o.rdfgraph.namespaces())

    printDebug("Extracting classes info")
    o.extract_classes()
    printDebug("..done")
    printDebug("Extracting properties info")
    o.extract_properties()
    printDebug("..done")
    return cPickle.dumps(o)




def _doCacheTableStats():
    """
    """
    # global var
    ENDPOINT = SparqlHelper(SPARQL_ENDPOINT, NAMESPACES, CREDENTIALS)
    res = ENDPOINT.class_stats("json")

    # One Will Have to do this later....
    # res = res['results'].get('bindings', None)

    return json.dumps(res)





def OLD_getTableStats():
    out = {}
    out['articles_tot'] = Document.objects.all().count()
    out['scopus_indexed'] = Document.objects.filter(scopusChecked=True).filter(scopusCheckedTime__isnull=False).count()
    out['scopus_unindexed'] = Document.objects.filter(scopusChecked=False).filter(scopusCheckedTime__isnull=False).count()
    out['scopus_unchecked'] = Document.objects.filter(scopusCheckedTime__isnull=True).count()

    out['wos_indexed'] = Document.objects.filter(wosChecked=True).filter(wosCheckedTime__isnull=False).count()
    out['wos_unindexed'] = Document.objects.filter(wosChecked=False).filter(wosCheckedTime__isnull=False).count()
    out['wos_unchecked'] = Document.objects.filter(wosCheckedTime__isnull=True).count()

    out['books'] = Container.objects.filter(container_type="book", scopusChecked=True).count()

    return json.dumps(out)



def _getTimeseriesByMonth():
    """
    JSON timeseries data for metrograph.js viz

    for one line:
    [{"value": 6, "date": "1870-12-01"}, {"value": 14, "date": "1871-12-02"}]

    Note: missing years are ignored, but there's a sharp drop in the chart line so
    it's better to set them to 0
    """
    max_date = Document.objects.all().aggregate(Max('pubdate'))['pubdate__max']
    min_date = Document.objects.all().aggregate(Min('pubdate'))['pubdate__min']

    print "Stats for date range: %s to %s" % (str(min_date), str(max_date))
    date_range =  build_time_delta_by_month(min_date, max_date)

    wos_tot = []
    wos_indexed = []
    scopus_indexed = []

    for d in date_range:

        print "Checking date: %s" % str(d)

        year, month = d.split("-")[0], d.split("-")[1]
        q = Document.objects.filter(pubdate__year=year, pubdate__month=month)
        wos_tot.append({"date": d, "value" : q.count()})
        wos_indexed.append({"date": d, "value": q.filter(wosChecked=True).count()})
        scopus_indexed.append({"date": d, "value": q.filter(scopusChecked=True).count()})

    tot_res = [wos_tot, wos_indexed, scopus_indexed]
    return json.dumps(tot_res)



def _getTimeseriesByYear():
    """
    JSON timeseries data for metrograph.js viz

    for one line:
    [{"value": 6, "date": "2015"}, {"value": 14, "date": "2016"}]

    Note: missing years are ignored, but there's a sharp drop in the chart line so
    it's better to set them to 0
    """

    if False:
        # =====
        # better approach than above, but seems to fail with sqllite!
        # http://stackoverflow.com/questions/8746014/django-group-by-date-day-month-year
        # =====
        from django.db.models.functions import TruncYear
        from django.db.models import Count
        data = Document.objects.annotate(year=TruncYear('pubdate')).values('year').annotate(c=Count('id')).values('year', 'c')
        print data

    max_date = Document.objects.all().aggregate(Max('pubdate'))['pubdate__max']
    min_date = Document.objects.all().aggregate(Min('pubdate'))['pubdate__min']

    print "Stats for date range: %s to %s" % (str(min_date), str(max_date))
    if not min_date or not max_date:
        print "Unable to find min or/and max year"
        exit

    date_range = range(min_date.year, max_date.year)

    wos_tot = []
    wos_indexed = []
    scopus_indexed = []

    for d in date_range:

        print "Checking date: %s" % str(d)

        q = Document.objects.filter(pubdate__year=d)
        year = str(d)
        wos_tot.append({"date": year, "value" : q.count()})
        wos_indexed.append({"date": year, "value": q.filter(wosChecked=True).count()})
        scopus_indexed.append({"date": year, "value": q.filter(scopusChecked=True).count()})

    tot_res = [wos_tot, wos_indexed, scopus_indexed]
    return json.dumps(tot_res)



from datetime import datetime, timedelta

def build_time_delta_by_month(min_date, max_date):
    """
    from two dates, returns a list containing all months in range
    """

    start = datetime(1900, 1, 1)
    # start = datetime(2016, 10, 1)
    end = datetime(max_date.year, max_date.month, 1)
    # end = datetime(2015, 01, 1)

    result = [start.strftime('%Y-%m-%d')]

    while start <= end:
        start += timedelta(days=32)
        result.append( datetime(start.year, start.month, 1).strftime('%Y-%m-%d') )

    return result
