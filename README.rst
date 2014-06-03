Collect common CDNs especially blocked by GFW

So people can download all cdn files to a nearest VPS or localhost, and redirect CDN files to these files with faster speed

Maybe we can offer these files just like opensource mirrors

Offer a sample *hosts* file

=================
 How to use this
=================

1. Download all google cdn files: ``python download.py``

2. Using nginx to serve these static files

   .. code-block:: conf

      location /ajax/ {
		   alias /path/to/downloadFiles/ajax/;
		   # eg: alias /home/dengshuan/cdn-mirror/ajax.googleapis.com/ajax/;
      }

3. Add following line to your *hosts* file

   .. code-block:: conf

      127.0.0.1    ajax.googleapis.com
