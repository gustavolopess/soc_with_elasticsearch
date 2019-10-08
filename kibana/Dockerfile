FROM docker.elastic.co/kibana/kibana:7.4.0

WORKDIR /usr/share/kibana/

RUN ./bin/kibana-plugin install https://github.com/bitsensor/elastalert-kibana-plugin/releases/download/1.1.0/elastalert-kibana-plugin-1.1.0-7.4.0.zip

COPY ./elastalert/index.js /usr/share/kibana/plugins/elastalert-kibana-plugin/
