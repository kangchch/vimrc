Vim�UnDo� $�kڱ�/����/��`@鈼,a�E.jVŒ��   #                                   ]�    _�                             ����                                                                                                                                                                                                                                                                                                                                                             ]�     �              !   import json   	import os   import pymongo as mongo   
import pdb   class DetailClient(object):   2    def retrieve_detail_data(self,indexes,**args):           pass       &class LocalDetailClient(DetailClient):       def __init__(self,datafn):           self.datafn=datafn   6        self.items=LocalDetailClient.load_data(datafn)           @staticmethod       def load_data(fn):   ,        with open(fn,encoding='utf-8') as f:               return json.load(f)          2    def retrieve_detail_data(self,indexes,**args):   #        fields = args.get('fields')           results=[]           for index in indexes:   &            pi = str(index.get('_id'))   #            item=self.items.get(pi)               if item != None:   "                if fields == None:   (                    results.append(item)                   else:   E                    result={ f:item[f] for f in fields if f in item }   ;                    result['items'] = index.get('items',{})   *                    results.append(result)           return results    �   !            5�_�                             ����                                                                                                                                                                                                                                                                                                                                                             ]�    �              #   import json   	import os   import pymongo as mongo   
import pdb           class DetailClient(object):   4    def retrieve_detail_data(self, indexes, **args):           pass           &class LocalDetailClient(DetailClient):       def __init__(self, datafn):           self.datafn = datafn   8        self.items = LocalDetailClient.load_data(datafn)           @staticmethod       def load_data(fn):   -        with open(fn, encoding='utf-8') as f:               return json.load(f)       4    def retrieve_detail_data(self, indexes, **args):   #        fields = args.get('fields')           results = []           for index in indexes:   &            pi = str(index.get('_id'))   %            item = self.items.get(pi)               if item != None:   "                if fields == None:   (                    results.append(item)                   else:   F                    result = {f: item[f] for f in fields if f in item}   <                    result['items'] = index.get('items', {})   *                    results.append(result)           return results�   #            5��