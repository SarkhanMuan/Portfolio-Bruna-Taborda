FROM nginx:alpine

COPY index.html /usr/share/nginx/html
COPY style.css /usr/share/nginx/html

# Expõe a porta padrão do servidor web.
EXPOSE 80
