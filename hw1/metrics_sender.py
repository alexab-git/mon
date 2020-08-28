#!/usr/bin/env python3

import subprocess, re, json, socket, os
from runpy import run_path

#---setup---
metrics_script_path = '/tmp/metrics.py'
tmp_file_path =  "/tmp/metrics.txt"
host = socket.gethostname()
zbx_key = 'otus_important_metrics[{#METRICNAME}]'
key_val_separator = '='
#-----------


output = (subprocess.check_output(metrics_script_path,universal_newlines=True)).split()

#get the key, value pair and compile json
packet = []
regex_macros = '\{.*\}'
regex_metric = '\[(.*)\]'

lld_data = {'data': []}
zbx_key_macros_val = re.search(regex_macros, zbx_key).group(0)

metrics = open( tmp_file_path ,"w")

for obj in output:
    key, val = obj.split(key_val_separator,1)
    zbx_key_metric = re.search(regex_metric, key).group(1)
    lld_data['data'].append({ zbx_key_macros_val: zbx_key_metric })
    metrics.write("%s %s %s\n" % (host, key, val))

metrics.close()
print(json.dumps(lld_data))

os.popen("zabbix_sender -c /etc/zabbix/zabbix_agentd.conf -i %s" % ( tmp_file_path))


