FROM certbot/certbot:v1.22.0

RUN apk add --no-cache bash

COPY certbot.sh /opt/

RUN chmod +x /opt/certbot.sh

ENTRYPOINT ["/opt/certbot.sh"]
