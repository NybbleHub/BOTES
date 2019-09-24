# Boss of the Elastic SOC (BOTES) Dataset Version 1

BOTES is a security dataset adapted and modified for Elastic Stack from the original Splunk BOTS dataset ([Information about Splunk BOTS](https://github.com/splunk/botsv1))
Splunk specific, duplicated and bad parsed fields have been removed from the dataset to make it cleaner and lighter.

BOTES Python script can be used along with ECS Python script to automatically generate files needed to setup Elastic environement (Elasticsearch Index Mapping, Logstash configuration, ...) and use ECS (Elastic Common Schema) format.

# Documentation

Dataset cleaning process is fully documented here : [BOTES GitBook documentation](https://app.gitbook.com/@botes/s/botes-dataset/)

Documentation provide details about each step of cleaning, about matching between original and ECS fields and how to use BOTES and ECS Python scripts.  

# Download

Compressed version of cleaned Dataset can be downloaded on the following locations, and are ready to be ingested with Logstash by using configurations provided in the documentation :

| Data Sourcetype | Download links |
| --------------- | -------------- |
| WinEventLog:Application ||
| WinEventLog:Security ||
| WinEventLog:System ||
| XmlWinEventLog:Microsoft-Windows-Sysmon/Operational ||
| fgt_event ||
| fgt_traffic ||
| fgt_utm ||
| iis ||
| nessus:scan ||
| stream:dhcp ||
| stream:dns ||
| stream:http ||
| stream:icmp ||
| stream:ip ||
| stream:ldap ||
| stream:mapi ||
| stream:sip ||
| stream:smb ||
| stream:snmp ||
| stream:tcp ||
| suricata ||
| winregistry ||
