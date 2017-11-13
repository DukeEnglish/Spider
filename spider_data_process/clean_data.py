# coding: utf-8
import re
import sys

g_attri_pattern_cfg = {
    'p': re.compile('(?<=<p>).*(?=<\/p>)', re.U | re.M | re.S),
    'a': re.compile('<a.*?>', re.U | re.M | re.S),
    'strong': re.compile('(?<=<strong>).*(?=<\/strong>)', re.U | re.M | re.S),
}

for line in sys.stdin:
      line = line.strip()
      # line1 = line1[:-1].strip()
      # print line1
      if line.split():
            for k, re_obj in g_attri_pattern_cfg.items():
                if 'a' == k:
                    line = re_obj.sub('', line)
                    line = line.replace('</a>', '')
                else:
                    res = re_obj.search(line)
                    if res:
                        line = res.group()
            if u'广告' or u'优惠' not in line:
                  line = re.sub("|","",line)
                  line = re.sub(" ","",line)
                  line = re.sub(" ","",line)
                  line = re.sub("■","",line)
                  line = re.sub("　　","",line)
                  line = re.sub("","",line)
                  line = re.sub(" ","",line)
                  line = re.sub("　　","",line)
                  if line:
                        print line