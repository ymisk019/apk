from kivy.app import App
from kivy.uix.modalview import ModalView
from android.runnable import run_on_ui_thread
from jnius import autoclass

Activity = autoclass('org.kivy.android.PythonActivity').mActivity
WebViewNative = autoclass('android.webkit.WebView')
WebViewClient = autoclass('android.webkit.WebViewClient')

class WebApp(App):
    def build(self):
        self.create_webview()
        return ModalView()

    @run_on_ui_thread
    def create_webview(self):
        webview = WebViewNative(Activity)
        webview.getSettings().setJavaScriptEnabled(True)
        webview.getSettings().setDomStorageEnabled(True)
        webview.getSettings().setAllowFileAccessFromFileURLs(True)
        webview.getSettings().setAllowUniversalAccessFromFileURLs(True)
        webview.setWebViewClient(WebViewClient())
        webview.loadUrl("file:///android_asset/index.html")
        Activity.setContentView(webview)

if __name__ == '__main__':
    WebApp().run()
