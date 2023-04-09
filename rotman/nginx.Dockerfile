FROM nginx@sha256:6650513efd1d27c1f8a5351cbd33edf85cc7e0d9d0fcb4ffb23d8fa89b601ba8
COPY static /usr/share/nginx/html/static
RUN rm /usr/share/nginx/html/*.html
