#encoding: utf-8
import sys
from collections import deque
from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from ...models import Person, Organisation

ENTITIES = {
	'FE':Person,
	'FF':Organisation
}

class Command(BaseCommand):

    args = u'<filename>'
    help = u'Imports entities from þjóðskrá'

    def handle(self, *args, **options):

		fname = args[0]
		f = open( fname, 'r' )
		count = 1
		ttime = 0
		lines = [ l for l in f.readlines() ]
		total = len( lines )
		sys.stdout.write( '%i lines to process\n'%total )
		
		f.seek( 0 )
		buff = deque()

		for l in lines:
			s = datetime.now()
			
			t = l[:2]
			klass = ENTITIES.get( t, None )

			if klass is not None:
				p, fresh = klass.from_string( l )
				if p is not None and fresh:
					buff.append( p )
					count += 1
			
				if len(buff) >= 250:
					klass.objects.bulk_create( buff )
					buff = deque()
				
				d = datetime.now() - s
				ttime += d.total_seconds()
				avg = ttime/count
			
				sys.stdout.write( '\r Saved %7i people. Remain: %.2fs. Per second: %.1f' % ( count, avg*(total-count), 1/avg ) )
				sys.stdout.flush()

		if len(buff)>0:
			Person.objects.bulk_create(buff)
			
 		sys.stdout.write( '\nDone' )