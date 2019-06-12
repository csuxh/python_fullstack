from flask import Flask, views, url_for

app = Flask(import_name=__name__)
app.config['SERVER_NAME'] = 'wupeiqi.com:5000'
"""
127.0.0.1   wupeiqi.com
127.0.0.1   web.wupeiqi.com
127.0.0.1   admin.wupeiqi.com

"""

# http://admin.wupeiqi.com:5000/
@app.route("/", subdomain="admin")
def admin_index():
    return "admin.your-domain.tld"


# http://web.wupeiqi.com:5000/
@app.route("/", subdomain="web")
def web_index():
    return "web.your-domain.tld"


# http://sdsdf.wupeiqi.com:5000/
# http://sdfsdf.wupeiqi.com:5000/
# http://asdf.wupeiqi.com:5000/

@app.route("/dynamic", subdomain="<username>")
def username_index(username):
    """Dynamic subdomains are also supported
    Try going to user1.your-domain.tld/dynamic"""
    return username + ".your-domain.tld"


if __name__ == '__main__':
    app.run()