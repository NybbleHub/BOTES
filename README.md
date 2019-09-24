# Boss of the Elastic SOC (BOTES) Dataset Version 1

BOTES is a security dataset adapted and modified for Elastic Stack from the original Splunk BOTS dataset ([Information about Splunk BOTS](https://github.com/splunk/botsv1)).

Splunk specific, duplicated and bad parsed fields have been removed from the dataset to make it cleaner and lighter.

BOTES Python script can be used along with ECS Python script to automatically generate files needed to setup Elastic environement (Elasticsearch Index Mapping, Logstash configuration, ...) and use ECS (Elastic Common Schema) format.

# Documentation

Dataset cleaning process is fully documented here : [BOTES GitBook documentation](https://botes.gitbook.io/botes-dataset/)

Documentation provides details about each step of cleaning, about matching between original and ECS fields, how to use BOTES and ECS Python scripts and how to setup an already installed Elastic Stack.

# Download

Compressed version of cleaned Dataset can be downloaded on the following locations, and are ready to be ingested with Logstash by using configurations provided in the documentation :

| Data Sourcetype | Download links |
| --------------- | -------------- |
| fgt_event | https://botes.s3-us-west-1.amazonaws.com/botes-data/botesv1.fgt_event.json.gz |
| fgt_traffic | https://botes.s3-us-west-1.amazonaws.com/botes-data/botesv1.fgt_traffic.json.gz |
| fgt_utm | https://botes.s3-us-west-1.amazonaws.com/botes-data/botesv1.fgt_utm.json.gz |
| iis | https://botes.s3-us-west-1.amazonaws.com/botes-data/botesv1.iis.json.gz |
| nessus:scan | https://botes.s3-us-west-1.amazonaws.com/botes-data/botesv1.nessus-scan.json.gz |
| stream:dhcp | https://botes.s3-us-west-1.amazonaws.com/botes-data/botesv1.stream-dhcp.json.gz |
| stream:dns | https://botes.s3-us-west-1.amazonaws.com/botes-data/botesv1.stream-dns.json.gz |
| stream:http | https://botes.s3-us-west-1.amazonaws.com/botes-data/botesv1.stream-http.json.gz |
| stream:icmp | https://botes.s3-us-west-1.amazonaws.com/botes-data/botesv1.stream-icmp.json.gz |
| stream:ip | https://botes.s3-us-west-1.amazonaws.com/botes-data/botesv1.stream-ip.json.gz |
| stream:ldap | https://botes.s3-us-west-1.amazonaws.com/botes-data/botesv1.stream-ldap.json.gz |
| stream:mapi | https://botes.s3-us-west-1.amazonaws.com/botes-data/botesv1.stream-mapi.json.gz |
| stream:sip | https://botes.s3-us-west-1.amazonaws.com/botes-data/botesv1.stream-sip.json.gz |
| stream:smb | https://botes.s3-us-west-1.amazonaws.com/botes-data/botesv1.stream-smb.json.gz |
| stream:snmp | https://botes.s3-us-west-1.amazonaws.com/botes-data/botesv1.stream-snmp.json.gz |
| stream:tcp | https://botes.s3-us-west-1.amazonaws.com/botes-data/botesv1.stream-tcp.json.gz |
| suricata | https://botes.s3-us-west-1.amazonaws.com/botes-data/botesv1.suricata.json.gz |
| WinEventLog:Application | https://botes.s3-us-west-1.amazonaws.com/botes-data/botesv1.WinEventLog-Application.json.gz |
| WinEventLog:Security | https://botes.s3-us-west-1.amazonaws.com/botes-data/botesv1.WinEventLog-Security.json.gz  |
| WinEventLog:System | https://botes.s3-us-west-1.amazonaws.com/botes-data/botesv1.WinEventLog-System.json.gz |
| winregistry | https://botes.s3-us-west-1.amazonaws.com/botes-data/botesv1.winregistry.json.gz |
| XmlWinEventLog:Microsoft-Windows-Sysmon/Operational | https://botes.s3-us-west-1.amazonaws.com/botes-data/botesv1.XmlWinEventLog-Microsoft-Windows-Sysmon-Operational.json.gz |
