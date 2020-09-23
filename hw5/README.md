# HW5

[Скриншот с визуализацией открытых и закрытых ssh сессий в кибане](screen0.png)


* [конфиг rsyslog сервера по интеграции с logstash](01-json-template.conf)
* [конфиг rsyslog сервера](99-output.conf) 
* [конфиг rsyslog клинета](99-client-output.conf)
* [конфиг logstash](logstash.conf)
* [elastic_index.json](elastic_index.json) - результат вывода комманды ```curl -XGET 'http://localhost:9200/rsyslog-*/_search?q=sshd&pretty' ```
