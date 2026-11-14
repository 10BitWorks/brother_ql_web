## brother\_ql\_web

This is a web service to print labels on Brother QL label printers.

You need Python 3 for this software to work.

![Screenshot](./screenshots/Label-Designer_Desktop.png)

The web interface is [responsive](https://en.wikipedia.org/wiki/Responsive_web_design).
There's also a screenshot showing [how it looks on a smartphone](./screenshots/Label-Designer_Phone.png)

### Additional Features
* Print text as QR Code
    * Add text to QR Code
    * Change size of QR Code
* Upload files to print
    * .pdf, .png and .jpg files
    * automatically convertion to black/white image
* Change print color for black/white/red labels
* Print lables multiple times
    * Cut every label
    * Cut only after the last label
* Migrated GUI to Bootstrap 4
* Make preview for round labels.. round

### Installation

This installation manual requires only a default installation of Debian 10 (Buster).
Install prerequisites:

    apt install fontconfig python3-venv python3-pip git poppler-utils

Get the code:

    cd /opt
    git clone https://github.com/tbnobody/brother_ql_web.git

Build the venv and install the requirements:

    cd /opt/brother_ql_web
    python3 -m venv .venv
    source /opt/brother_ql_web/.venv/bin/activate
    pip install -r requirements.txt

### Configuration file

Create a directory called 'instance', a file called 'application.py' and adjust the values to match your needs.

    mkdir /opt/brother_ql_web/instance
    touch /opt/brother_ql_web/instance/application.py

E.g.
    """
    User specific application settings
    """
    import logging
    PRINTER_MODEL = 'QL-820NWB'
    PRINTER_PRINTER = 'tcp://192.168.1.33:9100'

### Brand fonts

The 10BitWorks brand typefaces are bundled in `app/static/fonts/brand/`:

* `BarlowCondensed-Regular.ttf`, `BarlowCondensed-Bold.ttf`
* `Barlow-Regular.ttf`, `Barlow-Medium.ttf`, `Barlow-SemiBold.ttf`
* `JetBrainsMono-Regular.ttf`

They are registered at startup from `BRAND_FONT_FOLDER` by reading each font's
own metadata (via Pillow), so no fontconfig installation of the fonts is
required. Bundled files take precedence over any system-installed copies of
the same family/style. `BRAND_FONT_FAMILIES` controls which families are
listed first (as the "10BitWorks brand" group) in the font pickers, and
`LABEL_DEFAULT_FONT_FAMILY` / `LABEL_DEFAULT_FONT_STYLE` set the default font.
To override the default, set these keys in `instance/application.py`.

### Startup

To start the server, run `./run.py`.

### Automatic startup using systemd service

Copy service file, reload system, enable and start the service

    cp /opt/brother_ql_web/systemd/brother_ql_web.service /etc/systemd/system
    systemctl daemon-reload
    systemctl enable brother_ql_web
    systemctl start brother_ql_web

### Usage

Once it's running, access the web interface by opening the page with your browser.
If you run it on your local machine, go to <http://localhost:8013>.
You will then be forwarded by default to the interactive web gui located at `/labeldesigner`.

All in all, the web server offers:

* a Web GUI allowing you to print your labels at `/labeldesigner`,
* an API at `/api/print/text?text=Your_Text&font_size=100&font_family=Minion%20Pro%20(%20Semibold%20)`
  to print a label containing 'Your Text' with the specified font properties.

### License

This software is published under the terms of the GPLv3, see the LICENSE file in the repository.

Parts of this package are redistributed software products from 3rd parties. They are subject to different licenses:

* [Bootstrap](https://github.com/twbs/bootstrap), MIT License
* [Font Awesome](https://github.com/FortAwesome/Font-Awesome), CC BY 4.0 License
* [jQuery](https://github.com/jquery/jquery), MIT License
