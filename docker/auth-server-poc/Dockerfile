FROM debian:buster

# Create directories
RUN mkdir -p /opt/auth-server-poc
#RUN mkdir -p /opt/auth-server-poc/cert
#RUN mkdir -p /opt/auth-server-poc/userdb

# Setup script
COPY setup.sh /opt/auth-server-poc/setup.sh
RUN /opt/auth-server-poc/setup.sh

# Prepare for supervisord, uwsgi, ngninx
COPY config/uwsgi.ini /opt/auth-server-poc/venv/auth-server-poc/
#COPY config/.htpasswd /opt/auth-server-poc/.htpasswd
COPY config/supervisord_app.conf /etc/supervisor/supervisord.conf
COPY config/nginx_app.conf /etc/nginx/sites-available/
COPY config/nginx.conf /etc/nginx/
COPY cert/* /etc/nginx/conf.d/
#COPY cert/private.pem /opt/auth-server-poc/cert/
#COPY cert/public.pem /opt/auth-server-poc/cert/

# Give nginx some special treatment
RUN unlink /etc/nginx/sites-enabled/default
RUN ln -s /etc/nginx/sites-available/nginx_app.conf /etc/nginx/sites-enabled/default
RUN chown www-data:www-data /var/log/nginx
RUN chown -R  www-data:www-data /var/log/nginx/
RUN chown -R www-data:www-data /var/lib/nginx
RUN chown www-data:www-data /var/lib/nginx/
RUN chown www-data:www-data /opt/auth-server-poc

# Expose HTTPS
EXPOSE 1443

ENTRYPOINT supervisord -c /etc/supervisor/supervisord.conf
