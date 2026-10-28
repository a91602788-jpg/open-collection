import copy
import unittest
from check_research import queue_errors


class UncountedQueueContracts(unittest.TestCase):
    def setUp(self):
        self.index={'unique_candidates':1,'topics':[{'id':'38-skills','status':'proposed','candidate_count':1}]}
        self.row={'id':101,'repo':'example/tool','url':'https://github.com/example/tool',
                  'review_status':'pending-editorial-review','license_spdx':'CHECK-LICENSE',
                  'archived':False,'fork':False,'primary_topic_id':'38-skills','matched_topic_ids':['38-skills'],
                  'discovery_sources':[{'topic_id':'38-skills','query':'skills','url':'https://github.com/search?q=skills'}]}
        self.shards={'38-skills':{'candidates':[self.row]}}

    def test_pending_unknown_license_is_explicit(self):
        self.assertEqual(queue_errors(self.index,self.shards,set()),[])

    def test_already_counted_resource_cannot_inflate_candidate_totals(self):
        self.assertTrue(any('already counted' in e for e in queue_errors(self.index,self.shards,{101})))

    def test_cross_topic_duplicates_are_rejected(self):
        self.index['topics'].append({'id':'39-architecture','status':'proposed','candidate_count':1})
        self.shards['39-architecture']={'candidates':[copy.deepcopy(self.row)]}
        self.assertTrue(any('duplicate candidate ID' in e for e in queue_errors(self.index,self.shards,set())))

    def test_discovery_cannot_present_itself_as_editorial_acceptance(self):
        self.row['review_status']='accepted'
        self.assertTrue(any('cannot claim' in e for e in queue_errors(self.index,self.shards,set())))

    def test_reclassification_keeps_original_search_provenance(self):
        self.index['topics'][0]['candidate_count']=0
        self.index['topics'].append({'id':'39-architecture','status':'proposed','candidate_count':1})
        self.row.update(primary_topic_id='39-architecture',matched_topic_ids=['38-skills','39-architecture'])
        self.shards={'38-skills':{'candidates':[]},'39-architecture':{'candidates':[self.row]}}
        self.assertEqual(queue_errors(self.index,self.shards,set()),[])
        self.row.pop('discovery_sources')
        self.assertTrue(any('provenance' in e for e in queue_errors(self.index,self.shards,set())))


if __name__=='__main__':unittest.main()
