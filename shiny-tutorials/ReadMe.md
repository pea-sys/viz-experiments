Shiny を使用すると、Streamlit よりもはるかにパフォーマンスが高く、拡張性の高いアプリケーションを構築できます。

https://github.com/posit-dev/py-shiny/

ちょっとだけテンプレートを触ってみた感じでは良さそう。

```
mkdir shiny-tutorials
cd shiny-tutorials
poetry init
poetry shell
poetry add shiny
shiny create --template dashboard-tips
cd dashboard-tips
poetry add $( cat requirements.txt )
shiny run
```

template は現段階で次の種類が提供されている

```
(shiny-tutorials-py3.12) PS C:\Users\masami\source\repos\shiny-tutorials> shiny create --help
Usage: shiny create [OPTIONS]

  Create a Shiny application from a template.

  Create an app based on a template. You will be prompted with a number of
  application types, as well as the destination folder. If you don't provide a
  destination folder, it will be created in the current working directory
  based on the template name.

  After creating the application, you use `shiny run`:

      shiny run APPDIR/app.py --reload

Options:
  -t, --template [basic-app|basic-sidebar|dashboard|dashboard-tips|basic-navigation|js-component|external-gallery|js-input|js-output|js-react]
                                  Choose a template for your new application.
  -m, --mode [core|express]       Do you want to use a Shiny Express template
                                  or a Shiny Core template?
  -g, --github TEXT               The GitHub URL of the template sub-
                                  directory. For example
                                  https://github.com/posit-dev/py-shiny-
                                  templates/tree/main/dashboard
  -d, --dir TEXT                  The destination directory, you will be
                                  prompted if this is not provided.
  --package-name TEXT             If you are using one of the JavaScript
                                  component templates, you can use this flag
                                  to specify the name of the resulting package
                                  without being prompted.
  --help                          Show this message and exit.
```

その他、インターネット経由でテンプレートの適用も可能  
 https://shiny.posit.co/py/templates/

```
shiny create -m express  -g https://github.com/posit-dev/py-shiny-templates/tree/main/map-distance
```
